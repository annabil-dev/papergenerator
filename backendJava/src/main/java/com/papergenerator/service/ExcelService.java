package com.papergenerator.service;

import com.papergenerator.dto.ExcelRequest;
import lombok.extern.slf4j.Slf4j;
import org.apache.poi.common.usermodel.HyperlinkType;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.ss.util.CellRangeAddress;
import org.apache.poi.xssf.streaming.SXSSFWorkbook;
import org.apache.poi.xssf.usermodel.*;
import org.apache.poi.hssf.util.HSSFColor;
import org.springframework.stereotype.Service;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.List;
import java.util.Map;

/**
 * Excel workbook generation service covering all POI modules:
 *  - HSSF (.xls - legacy format)
 *  - XSSF (.xlsx - modern format)
 *  - SXSSF (streaming .xlsx for large datasets)
 *
 * Features:
 *  - Multiple sheets, rows, cells
 *  - Cell types: string, number, boolean, formula, date, blank
 *  - Full cell styling: font (bold, italic, underline, size, color),
 *    background fill, alignment, borders, data format, word wrap
 *  - Merge regions
 *  - Column widths auto-sizing
 *  - Comments/hyperlinks
 *  - Sheet protection
 *  - Auto-filter
 *  - Freeze pane
 *  - Streaming mode for large data
 */
@Slf4j
@Service
public class ExcelService {

    // ── Public API ────────────────────────────────────────────────────────────

    /**
     * Generate an Excel workbook from an ExcelRequest.
     * Format: xlsx (XSSF), xls (HSSF), or streaming-xlsx (SXSSF).
     */
    public byte[] generateExcel(ExcelRequest req) throws IOException {
        String format = req.getFormat() != null ? req.getFormat().toLowerCase() : "xlsx";
        return switch (format) {
            case "xls" -> generateHssf(req);
            case "streaming-xlsx", "sxssf" -> generateSxssf(req);
            default -> generateXssf(req);
        };
    }

    // ── XSSF (.xlsx) ─────────────────────────────────────────────────────────

    public byte[] generateXssf(ExcelRequest req) throws IOException {
        try (XSSFWorkbook wb = new XSSFWorkbook()) {
            buildWorkbook(wb, req);
            ByteArrayOutputStream out = new ByteArrayOutputStream();
            wb.write(out);
            return out.toByteArray();
        }
    }

    // ── HSSF (.xls) ──────────────────────────────────────────────────────────

    public byte[] generateHssf(ExcelRequest req) throws IOException {
        try (HSSFWorkbook wb = new HSSFWorkbook()) {
            buildWorkbook(wb, req);
            ByteArrayOutputStream out = new ByteArrayOutputStream();
            wb.write(out);
            return out.toByteArray();
        }
    }

    // ── SXSSF (streaming .xlsx) ───────────────────────────────────────────────

    public byte[] generateSxssf(ExcelRequest req) throws IOException {
        try (XSSFWorkbook xwb = new XSSFWorkbook();
             SXSSFWorkbook wb = new SXSSFWorkbook(xwb, 100)) {
            wb.setCompressTempFiles(true);
            buildWorkbook(wb, req);
            ByteArrayOutputStream out = new ByteArrayOutputStream();
            wb.write(out);
            wb.dispose();
            return out.toByteArray();
        }
    }

    // ── Extract from existing workbook ────────────────────────────────────────

    /**
     * Extract all data from a workbook as a list of sheets → rows → cells.
     */
    public List<List<List<String>>> extractData(Workbook workbook) {
        List<List<List<String>>> result = new java.util.ArrayList<>();
        for (int si = 0; si < workbook.getNumberOfSheets(); si++) {
            Sheet sheet = workbook.getSheetAt(si);
            List<List<String>> sheetData = new java.util.ArrayList<>();
            for (Row row : sheet) {
                List<String> rowData = new java.util.ArrayList<>();
                for (Cell cell : row) {
                    rowData.add(getCellValueAsString(cell));
                }
                sheetData.add(rowData);
            }
            result.add(sheetData);
        }
        return result;
    }

    // ── Private builder ───────────────────────────────────────────────────────

    private void buildWorkbook(Workbook wb, ExcelRequest req) {
        if (req.getSheets() == null || req.getSheets().isEmpty()) {
            wb.createSheet("Sheet1");
            return;
        }
        for (ExcelRequest.SheetRequest sheetReq : req.getSheets()) {
            Sheet sheet = wb.createSheet(sheetReq.getName() != null ? sheetReq.getName() : "Sheet");
            buildSheet(wb, sheet, sheetReq);
        }
    }

    private void buildSheet(Workbook wb, Sheet sheet, ExcelRequest.SheetRequest sheetReq) {
        if (sheetReq.getRows() == null) return;
        int maxRow = 0;
        for (ExcelRequest.RowRequest rowReq : sheetReq.getRows()) {
            int rowIdx = rowReq.getRowIndex() != null ? rowReq.getRowIndex() : 0;
            if (rowIdx > maxRow) maxRow = rowIdx;
            Row row = sheet.createRow(rowIdx);
            if (rowReq.getHeight() != null) row.setHeight(rowReq.getHeight().shortValue());
            if (rowReq.getCells() != null) {
                for (ExcelRequest.CellRequest cellReq : rowReq.getCells()) {
                    int colIdx = cellReq.getColIndex() != null ? cellReq.getColIndex() : 0;
                    Cell cell = row.createCell(colIdx);
                    setCellValue(wb, cell, cellReq);
                    if (cellReq.getStyle() != null) {
                        CellStyle style = buildCellStyle(wb, cellReq.getStyle());
                        cell.setCellStyle(style);
                    }
                    // Add comment
                    if (cellReq.getComment() != null && sheet instanceof XSSFSheet xSheet) {
                        addCellComment(xSheet, cell, cellReq.getComment());
                    }
                    // Add hyperlink
                    if (cellReq.getHyperlink() != null) {
                        addCellHyperlink(wb, cell, cellReq.getHyperlink());
                    }
                }
            }
        }

        // Column widths
        if (sheetReq.getColumnWidths() != null) {
            for (Map.Entry<Integer, Integer> e : sheetReq.getColumnWidths().entrySet()) {
                sheet.setColumnWidth(e.getKey(), e.getValue() * 256);
            }
        }

        // Auto-filter
        if (Boolean.TRUE.equals(sheetReq.getAutoFilter()) && sheetReq.getAutoFilterRow() != null) {
            int filterRow = sheetReq.getAutoFilterRow();
            Row fr = sheet.getRow(filterRow);
            if (fr != null) {
                sheet.setAutoFilter(new CellRangeAddress(filterRow, filterRow,
                        fr.getFirstCellNum(), fr.getLastCellNum() - 1));
            }
        }

        // Merge regions
        if (sheetReq.getMergeRegions() != null) {
            for (ExcelRequest.MergeRegion mr : sheetReq.getMergeRegions()) {
                sheet.addMergedRegion(new CellRangeAddress(
                        mr.getFirstRow(), mr.getLastRow(), mr.getFirstCol(), mr.getLastCol()));
            }
        }

        // Sheet protection
        if (Boolean.TRUE.equals(sheetReq.getProtectSheet()) && sheet instanceof XSSFSheet xSheet) {
            if (sheetReq.getSheetPassword() != null) {
                xSheet.protectSheet(sheetReq.getSheetPassword());
            } else {
                xSheet.enableLocking();
            }
        }
    }

    private void setCellValue(Workbook wb, Cell cell, ExcelRequest.CellRequest req) {
        String type = req.getType() != null ? req.getType().toLowerCase() : "string";
        String value = req.getValue();
        switch (type) {
            case "number" -> {
                try { cell.setCellValue(Double.parseDouble(value != null ? value : "0")); }
                catch (NumberFormatException e) { cell.setCellValue(0); }
            }
            case "boolean" -> cell.setCellValue(Boolean.parseBoolean(value));
            case "formula" -> cell.setCellFormula(value != null ? value : "");
            case "blank" -> cell.setBlank();
            case "date" -> {
                try {
                    java.time.LocalDate date = java.time.LocalDate.parse(value);
                    cell.setCellValue(java.util.Date.from(date.atStartOfDay(java.time.ZoneId.systemDefault()).toInstant()));
                } catch (Exception e) {
                    cell.setCellValue(value != null ? value : "");
                }
            }
            default -> cell.setCellValue(value != null ? value : "");
        }
    }

    private CellStyle buildCellStyle(Workbook wb, ExcelRequest.CellStyleRequest req) {
        CellStyle style = wb.createCellStyle();
        Font font = wb.createFont();

        if (Boolean.TRUE.equals(req.getBold())) font.setBold(true);
        if (Boolean.TRUE.equals(req.getItalic())) font.setItalic(true);
        if (Boolean.TRUE.equals(req.getUnderline())) font.setUnderline(Font.U_SINGLE);
        if (req.getFontSize() != null) font.setFontHeightInPoints(req.getFontSize().shortValue());
        if (req.getFontColor() != null && wb instanceof XSSFWorkbook) {
            ((XSSFFont) font).setColor(new XSSFColor(hexToRgb(req.getFontColor()), null));
        }

        style.setFont(font);

        // Background
        if (req.getBgColor() != null) {
            if (wb instanceof XSSFWorkbook) {
                ((XSSFCellStyle) style).setFillForegroundColor(new XSSFColor(hexToRgb(req.getBgColor()), null));
            }
            style.setFillPattern(FillPatternType.SOLID_FOREGROUND);
        }

        // Alignment
        if (req.getAlignment() != null) {
            style.setAlignment(switch (req.getAlignment().toUpperCase()) {
                case "CENTER" -> HorizontalAlignment.CENTER;
                case "RIGHT" -> HorizontalAlignment.RIGHT;
                case "FILL" -> HorizontalAlignment.FILL;
                case "JUSTIFY" -> HorizontalAlignment.JUSTIFY;
                default -> HorizontalAlignment.LEFT;
            });
        }
        if (req.getVertAlignment() != null) {
            style.setVerticalAlignment(switch (req.getVertAlignment().toUpperCase()) {
                case "CENTER" -> VerticalAlignment.CENTER;
                case "BOTTOM" -> VerticalAlignment.BOTTOM;
                default -> VerticalAlignment.TOP;
            });
        }
        if (Boolean.TRUE.equals(req.getWrapText())) style.setWrapText(true);

        // Borders
        if (req.getBorderTop() != null) style.setBorderTop(mapBorderStyle(req.getBorderTop()));
        if (req.getBorderBottom() != null) style.setBorderBottom(mapBorderStyle(req.getBorderBottom()));
        if (req.getBorderLeft() != null) style.setBorderLeft(mapBorderStyle(req.getBorderLeft()));
        if (req.getBorderRight() != null) style.setBorderRight(mapBorderStyle(req.getBorderRight()));

        // Data format
        if (req.getDataFormat() != null) {
            DataFormat fmt = wb.createDataFormat();
            style.setDataFormat(fmt.getFormat(req.getDataFormat()));
        }

        return style;
    }

    private void addCellComment(XSSFSheet sheet, Cell cell, String commentText) {
        try {
            XSSFDrawing drawing = sheet.createDrawingPatriarch();
            XSSFClientAnchor anchor = drawing.createAnchor(0, 0, 0, 0,
                    cell.getColumnIndex(), cell.getRowIndex(),
                    cell.getColumnIndex() + 2, cell.getRowIndex() + 3);
            XSSFComment comment = drawing.createCellComment(anchor);
            XSSFRichTextString str = new XSSFRichTextString(commentText);
            comment.setString(str);
            cell.setCellComment(comment);
        } catch (Exception e) {
            log.warn("Could not add cell comment: {}", e.getMessage());
        }
    }

    private void addCellHyperlink(Workbook wb, Cell cell, String url) {
        CreationHelper helper = wb.getCreationHelper();
        Hyperlink link = helper.createHyperlink(HyperlinkType.URL);
        link.setAddress(url);
        cell.setHyperlink(link);
    }

    private BorderStyle mapBorderStyle(String s) {
        return switch (s.toUpperCase()) {
            case "THIN" -> BorderStyle.THIN;
            case "MEDIUM" -> BorderStyle.MEDIUM;
            case "THICK" -> BorderStyle.THICK;
            case "DASHED" -> BorderStyle.DASHED;
            case "DOTTED" -> BorderStyle.DOTTED;
            case "DOUBLE" -> BorderStyle.DOUBLE;
            case "NONE" -> BorderStyle.NONE;
            default -> BorderStyle.THIN;
        };
    }

    private byte[] hexToRgb(String hex) {
        if (hex == null) return new byte[]{0,0,0};
        hex = hex.replace("#", "");
        if (hex.length() == 6) {
            return new byte[]{
                (byte) Integer.parseInt(hex.substring(0, 2), 16),
                (byte) Integer.parseInt(hex.substring(2, 4), 16),
                (byte) Integer.parseInt(hex.substring(4, 6), 16)
            };
        }
        return new byte[]{0, 0, 0};
    }

    private String getCellValueAsString(Cell cell) {
        if (cell == null) return "";
        return switch (cell.getCellType()) {
            case STRING -> cell.getStringCellValue();
            case NUMERIC -> DateUtil.isCellDateFormatted(cell)
                    ? cell.getLocalDateTimeCellValue().toString()
                    : String.valueOf(cell.getNumericCellValue());
            case BOOLEAN -> String.valueOf(cell.getBooleanCellValue());
            case FORMULA -> cell.getCellFormula();
            default -> "";
        };
    }
}

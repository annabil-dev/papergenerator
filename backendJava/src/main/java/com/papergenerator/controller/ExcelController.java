package com.papergenerator.controller;

import com.papergenerator.dto.ExcelRequest;
import com.papergenerator.service.ExcelService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.ByteArrayInputStream;
import java.util.Map;

/**
 * Excel generation and extraction API.
 * Supports HSSF (.xls), XSSF (.xlsx), SXSSF (streaming).
 */
@Slf4j
@RestController
@RequestMapping("/api/excel")
@RequiredArgsConstructor
public class ExcelController {

    private final ExcelService excelService;

    /**
     * Generate an Excel workbook.
     * POST /api/excel/generate
     * Body: ExcelRequest JSON
     */
    @PostMapping("/generate")
    public ResponseEntity<byte[]> generate(@RequestBody ExcelRequest req) {
        try {
            String format = req.getFormat() != null ? req.getFormat() : "xlsx";
            byte[] bytes = excelService.generateExcel(req);
            String ext = format.equals("xls") ? ".xls" : ".xlsx";
            String filename = (req.getFilename() != null ? req.getFilename() : "workbook") + ext;
            String ct = format.equals("xls")
                    ? "application/vnd.ms-excel"
                    : "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";
            return ResponseEntity.ok()
                    .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + filename + "\"")
                    .contentType(MediaType.parseMediaType(ct))
                    .body(bytes);
        } catch (Exception e) {
            log.error("Excel generate error", e);
            return ResponseEntity.status(500).build();
        }
    }

    /**
     * Extract data from an uploaded Excel file.
     * POST /api/excel/extract
     */
    @PostMapping("/extract")
    public ResponseEntity<Map<String, Object>> extract(@RequestParam("file") MultipartFile file) {
        try {
            String name = file.getOriginalFilename();
            boolean isXls = name != null && name.endsWith(".xls");
            try (var is = new ByteArrayInputStream(file.getBytes());
                 Workbook wb = isXls ? new HSSFWorkbook(is) : new XSSFWorkbook(is)) {
                var data = excelService.extractData(wb);
                return ResponseEntity.ok(Map.of("success", true, "data", data));
            }
        } catch (Exception e) {
            log.error("Excel extract error", e);
            return ResponseEntity.status(500).body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    /**
     * Generate a demo Excel workbook showing all format features.
     * GET /api/excel/demo
     */
    @GetMapping("/demo")
    public ResponseEntity<byte[]> demo() {
        try {
            ExcelRequest req = ExcelRequest.builder()
                    .format("xlsx").filename("demo")
                    .sheets(java.util.List.of(buildDemoSheet()))
                    .build();
            byte[] bytes = excelService.generateExcel(req);
            return ResponseEntity.ok()
                    .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"demo.xlsx\"")
                    .contentType(MediaType.parseMediaType(
                            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"))
                    .body(bytes);
        } catch (Exception e) {
            return ResponseEntity.status(500).build();
        }
    }

    private ExcelRequest.SheetRequest buildDemoSheet() {
        // Build a demo sheet with various cell types and styles
        var headerStyle = ExcelRequest.CellStyleRequest.builder()
                .bold(true).fontSize(12).bgColor("4472C4").fontColor("FFFFFF")
                .alignment("CENTER").build();

        var cells1 = java.util.List.of(
                ExcelRequest.CellRequest.builder().colIndex(0).value("Name").type("string").style(headerStyle).build(),
                ExcelRequest.CellRequest.builder().colIndex(1).value("Value").type("string").style(headerStyle).build(),
                ExcelRequest.CellRequest.builder().colIndex(2).value("Formula").type("string").style(headerStyle).build()
        );
        var cells2 = java.util.List.of(
                ExcelRequest.CellRequest.builder().colIndex(0).value("Alpha").type("string").build(),
                ExcelRequest.CellRequest.builder().colIndex(1).value("42").type("number").build(),
                ExcelRequest.CellRequest.builder().colIndex(2).value("=B2*2").type("formula").build()
        );
        var cells3 = java.util.List.of(
                ExcelRequest.CellRequest.builder().colIndex(0).value("Beta").type("string").build(),
                ExcelRequest.CellRequest.builder().colIndex(1).value("100").type("number").build(),
                ExcelRequest.CellRequest.builder().colIndex(2).value("=B3+B2").type("formula").build()
        );

        return ExcelRequest.SheetRequest.builder()
                .name("Demo")
                .rows(java.util.List.of(
                        ExcelRequest.RowRequest.builder().rowIndex(0).cells(cells1).build(),
                        ExcelRequest.RowRequest.builder().rowIndex(1).cells(cells2).build(),
                        ExcelRequest.RowRequest.builder().rowIndex(2).cells(cells3).build()
                ))
                .autoFilter(true)
                .columnWidths(java.util.Map.of(0, 20, 1, 15, 2, 20))
                .build();
    }
}

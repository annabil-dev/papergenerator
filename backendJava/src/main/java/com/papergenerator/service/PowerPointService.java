package com.papergenerator.service;

import com.papergenerator.dto.PptxRequest;
import lombok.extern.slf4j.Slf4j;
import org.apache.poi.sl.usermodel.TableCell;
import org.apache.poi.xslf.usermodel.*;
import org.springframework.stereotype.Service;

import java.awt.*;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.Base64;
import java.util.List;

/**
 * PowerPoint presentation generation service.
 *
 * Covers:
 *  - XSLF (.pptx) - modern format
 *  - Multiple slides with various layouts
 *  - Text boxes, images, tables, shapes
 *  - Font styling (bold, italic, size, color)
 *  - Fill colors, line colors
 *  - Text alignment
 *  - Slide notes
 *  - Background color / image
 */
@Slf4j
@Service
public class PowerPointService {

    // ── Public API ────────────────────────────────────────────────────────────

    /**
     * Generate a PPTX presentation from a PptxRequest.
     */
    public byte[] generatePptx(PptxRequest req) throws IOException {
        try (XMLSlideShow pptx = new XMLSlideShow()) {
            pptx.setPageSize(new java.awt.Dimension(9144000 / 914400 * 914400, 6858000 / 914400 * 914400));
            if (req.getSlides() != null) {
                for (PptxRequest.SlideRequest slideReq : req.getSlides()) {
                    buildSlide(pptx, slideReq);
                }
            }
            ByteArrayOutputStream out = new ByteArrayOutputStream();
            pptx.write(out);
            return out.toByteArray();
        }
    }

    // ── Private builders ──────────────────────────────────────────────────────

    private void buildSlide(XMLSlideShow pptx, PptxRequest.SlideRequest req) {
        XSLFSlideLayout layout = getLayout(pptx, req.getLayout());
        XSLFSlide slide = pptx.createSlide(layout);

        // Apply background color
        if (req.getBgColor() != null) {
            try {
                XSLFBackground bg = slide.getBackground();
                if (bg != null) bg.setFillColor(hexToColor(req.getBgColor()));
            } catch (Exception e) {
                log.warn("Could not set slide background: {}", e.getMessage());
            }
        }

        // Apply title from layout placeholder if available
        if (req.getTitle() != null) {
            for (XSLFShape shape : slide.getShapes()) {
                if (shape instanceof XSLFTextShape ts) {
                    if (ts.getTextType() == org.apache.poi.sl.usermodel.Placeholder.TITLE
                            || ts.getTextType() == org.apache.poi.sl.usermodel.Placeholder.CENTERED_TITLE) {
                        ts.setText(req.getTitle());
                    }
                }
            }
        }

        // Apply subtitle / content
        if (req.getSubtitle() != null) {
            for (XSLFShape shape : slide.getShapes()) {
                if (shape instanceof XSLFTextShape ts) {
                    if (ts.getTextType() == org.apache.poi.sl.usermodel.Placeholder.SUBTITLE
                            || ts.getTextType() == org.apache.poi.sl.usermodel.Placeholder.BODY) {
                        ts.setText(req.getSubtitle());
                    }
                }
            }
        }

        // Custom shapes
        if (req.getShapes() != null) {
            for (PptxRequest.ShapeRequest shapeReq : req.getShapes()) {
                addShape(slide, shapeReq);
            }
        }

        // Slide notes
        if (req.getNotes() != null && !req.getNotes().isBlank()) {
            XSLFNotes notes = pptx.getNotesSlide(slide);
            if (notes != null) {
                for (XSLFShape shape : notes.getShapes()) {
                    if (shape instanceof XSLFTextShape ts) {
                        if (ts.getTextType() == org.apache.poi.sl.usermodel.Placeholder.BODY) {
                            ts.setText(req.getNotes());
                        }
                    }
                }
            }
        }
    }

    private void addShape(XSLFSlide slide, PptxRequest.ShapeRequest req) {
        if (req.getType() == null) return;
        java.awt.geom.Rectangle2D anchor = new java.awt.geom.Rectangle2D.Double(
                req.getX() * 914400, req.getY() * 914400,
                req.getWidth() * 914400, req.getHeight() * 914400);

        switch (req.getType().toLowerCase()) {
            case "textbox" -> addTextBox(slide, req, anchor);
            case "image" -> addImage(slide, req, anchor);
            case "table" -> addTable(slide, req, anchor);
            case "rectangle" -> addRectangle(slide, req, anchor);
            case "oval", "ellipse" -> addOval(slide, req, anchor);
            case "line" -> addLine(slide, req, anchor);
            default -> addTextBox(slide, req, anchor);
        }
    }

    private void addTextBox(XSLFSlide slide, PptxRequest.ShapeRequest req, java.awt.geom.Rectangle2D anchor) {
        XSLFTextBox textBox = slide.createTextBox();
        textBox.setAnchor(anchor);
        if (req.getFillColor() != null) textBox.setFillColor(hexToColor(req.getFillColor()));
        if (req.getLineColor() != null) textBox.setLineColor(hexToColor(req.getLineColor()));
        if (req.getLineWidth() != null) textBox.setLineWidth(req.getLineWidth());

        if (req.getText() != null && !req.getText().isBlank()) {
            XSLFTextParagraph para = textBox.addNewTextParagraph();
            if (req.getAlignment() != null) {
                para.setTextAlign(mapTextAlign(req.getAlignment()));
            }
            XSLFTextRun run = para.addNewTextRun();
            run.setText(req.getText());
            if (Boolean.TRUE.equals(req.getBold())) run.setBold(true);
            if (Boolean.TRUE.equals(req.getItalic())) run.setItalic(true);
            if (req.getFontSize() != null) run.setFontSize((double) req.getFontSize());
            if (req.getFontColor() != null) run.setFontColor(hexToColor(req.getFontColor()));
        }
    }

    private void addImage(XSLFSlide slide, PptxRequest.ShapeRequest req, java.awt.geom.Rectangle2D anchor) {
        if (req.getImageData() == null) return;
        try {
            byte[] imgBytes;
            if (req.getImageData().contains(",")) {
                imgBytes = Base64.getDecoder().decode(req.getImageData().substring(req.getImageData().indexOf(',') + 1));
            } else {
                imgBytes = Base64.getDecoder().decode(req.getImageData());
            }
            XMLSlideShow pptx = (XMLSlideShow) slide.getSlideShow();
            XSLFPictureData picData = pptx.addPicture(imgBytes,
                    org.apache.poi.sl.usermodel.PictureData.PictureType.PNG);
            XSLFPictureShape pic = slide.createPicture(picData);
            pic.setAnchor(anchor);
        } catch (Exception e) {
            log.warn("Could not add slide image: {}", e.getMessage());
        }
    }

    private void addTable(XSLFSlide slide, PptxRequest.ShapeRequest req, java.awt.geom.Rectangle2D anchor) {
        if (req.getTable() == null) return;
        PptxRequest.TableShape tbl = req.getTable();
        List<List<String>> data = tbl.getData();
        List<String> headers = tbl.getHeaders();
        int rows = (data != null ? data.size() : 0) + (headers != null ? 1 : 0);
        int cols = headers != null ? headers.size() : (data != null && !data.isEmpty() ? data.get(0).size() : 1);
        if (rows == 0 || cols == 0) return;

        XSLFTable table = slide.createTable(rows, cols);
        table.setAnchor(anchor);

        int rowOffset = 0;
        if (headers != null) {
            for (int c = 0; c < headers.size(); c++) {
                XSLFTableCell cell = table.getCell(0, c);
                cell.setText(headers.get(c));
                if (tbl.getHeaderBgColor() != null) cell.setFillColor(hexToColor(tbl.getHeaderBgColor()));
                XSLFTextParagraph para = cell.getTextParagraphs().get(0);
                if (!para.getTextRuns().isEmpty()) {
                    XSLFTextRun run = para.getTextRuns().get(0);
                    run.setBold(true);
                    if (tbl.getHeaderFontColor() != null) run.setFontColor(hexToColor(tbl.getHeaderFontColor()));
                }
            }
            rowOffset = 1;
        }

        if (data != null) {
            for (int r = 0; r < data.size(); r++) {
                List<String> rowData = data.get(r);
                for (int c = 0; c < cols && c < rowData.size(); c++) {
                    table.getCell(r + rowOffset, c).setText(rowData.get(c));
                }
            }
        }
    }

    private void addRectangle(XSLFSlide slide, PptxRequest.ShapeRequest req, java.awt.geom.Rectangle2D anchor) {
        XSLFAutoShape shape = slide.createAutoShape();
        shape.setShapeType(org.apache.poi.sl.usermodel.ShapeType.RECT);
        shape.setAnchor(anchor);
        if (req.getFillColor() != null) shape.setFillColor(hexToColor(req.getFillColor()));
        if (req.getLineColor() != null) shape.setLineColor(hexToColor(req.getLineColor()));
        if (req.getLineWidth() != null) shape.setLineWidth(req.getLineWidth());
        if (req.getText() != null) shape.setText(req.getText());
    }

    private void addOval(XSLFSlide slide, PptxRequest.ShapeRequest req, java.awt.geom.Rectangle2D anchor) {
        XSLFAutoShape shape = slide.createAutoShape();
        shape.setShapeType(org.apache.poi.sl.usermodel.ShapeType.ELLIPSE);
        shape.setAnchor(anchor);
        if (req.getFillColor() != null) shape.setFillColor(hexToColor(req.getFillColor()));
        if (req.getLineColor() != null) shape.setLineColor(hexToColor(req.getLineColor()));
        if (req.getText() != null) shape.setText(req.getText());
    }

    private void addLine(XSLFSlide slide, PptxRequest.ShapeRequest req, java.awt.geom.Rectangle2D anchor) {
        XSLFConnectorShape connector = slide.createConnector();
        connector.setAnchor(anchor);
        if (req.getLineColor() != null) connector.setLineColor(hexToColor(req.getLineColor()));
        if (req.getLineWidth() != null) connector.setLineWidth(req.getLineWidth());
    }

    // ── Utilities ─────────────────────────────────────────────────────────────

    private XSLFSlideLayout getLayout(XMLSlideShow pptx, String layoutName) {
        for (XSLFSlideMaster master : pptx.getSlideMasters()) {
            for (XSLFSlideLayout layout : master.getSlideLayouts()) {
                if (layout.getName() != null &&
                        (layoutName == null || layout.getName().equalsIgnoreCase(layoutName))) {
                    return layout;
                }
            }
            // Return BLANK as fallback
            for (XSLFSlideLayout layout : master.getSlideLayouts()) {
                if ("BLANK".equalsIgnoreCase(layout.getName()) || layout.getName() == null)
                    return layout;
            }
            return master.getSlideLayouts()[0];
        }
        return null;
    }

    private Color hexToColor(String hex) {
        if (hex == null) return Color.BLACK;
        hex = hex.replace("#", "");
        try {
            int r = Integer.parseInt(hex.substring(0, 2), 16);
            int g = Integer.parseInt(hex.substring(2, 4), 16);
            int b = Integer.parseInt(hex.substring(4, 6), 16);
            return new Color(r, g, b);
        } catch (Exception e) {
            return Color.BLACK;
        }
    }

    private org.apache.poi.sl.usermodel.TextParagraph.TextAlign mapTextAlign(String align) {
        return switch (align.toUpperCase()) {
            case "CENTER" -> org.apache.poi.sl.usermodel.TextParagraph.TextAlign.CENTER;
            case "RIGHT" -> org.apache.poi.sl.usermodel.TextParagraph.TextAlign.RIGHT;
            case "JUSTIFY" -> org.apache.poi.sl.usermodel.TextParagraph.TextAlign.JUSTIFY;
            default -> org.apache.poi.sl.usermodel.TextParagraph.TextAlign.LEFT;
        };
    }
}

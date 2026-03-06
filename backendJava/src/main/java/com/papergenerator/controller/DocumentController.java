package com.papergenerator.controller;

import com.papergenerator.dto.DocxRequest;
import com.papergenerator.service.DocxService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.apache.poi.xwpf.usermodel.XWPFDocument;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.ByteArrayInputStream;
import java.util.Map;

/**
 * Document controller — full DOCX generation and manipulation API.
 */
@Slf4j
@RestController
@RequestMapping("/api/docx")
@RequiredArgsConstructor
public class DocumentController {

    private final DocxService docxService;

    /**
     * Generate a DOCX document from a comprehensive request.
     * POST /api/docx/generate
     */
    @PostMapping("/generate")
    public ResponseEntity<byte[]> generate(@RequestBody DocxRequest req) {
        try {
            XWPFDocument doc = docxService.createDocument();
            // Apply page setup if provided
            if (req.getPageSetup() != null) {
                var ps = req.getPageSetup();
                if (ps.getOrientation() != null) {
                    docxService.setPageOrientation(doc, "landscape".equalsIgnoreCase(ps.getOrientation()));
                }
                if (ps.getTopMargin() != null && (ps.getTopMargin() > 0 || (ps.getBottomMargin() != null && ps.getBottomMargin() > 0))) {
                    docxService.setPageMargins(doc, ps.getTopMargin(), ps.getBottomMargin() != null ? ps.getBottomMargin() : 0,
                            ps.getLeftMargin() != null ? ps.getLeftMargin() : 0, ps.getRightMargin() != null ? ps.getRightMargin() : 0);
                }
                if (ps.getColumns() != null && ps.getColumns() > 1) {
                    docxService.setPageColumns(doc, ps.getColumns(), ps.getColumnSpacing() != null ? ps.getColumnSpacing().doubleValue() : 720);
                }
            }
            // Apply metadata
            if (req.getMetadata() != null) {
                var meta = req.getMetadata();
                var props = doc.getProperties().getCoreProperties();
                if (meta.getTitle() != null) props.setTitle(meta.getTitle());
                if (meta.getSubject() != null) props.setSubjectProperty(meta.getSubject());
                if (meta.getAuthor() != null) props.setCreator(meta.getAuthor());
                if (meta.getDescription() != null) props.setDescription(meta.getDescription());
                if (meta.getKeywords() != null) props.setKeywords(meta.getKeywords());
            }
            // Add header/footer
              if (req.getHeaderText() != null) docxService.addHeader(doc, req.getHeaderText());
              if (req.getFooterText() != null) docxService.addFooter(doc, req.getFooterText());
              if (req.getPassword() != null) docxService.protectDocument(doc, req.getPassword());
              // Apply content elements
              if (req.getElements() != null) {
                  for (DocxRequest.ContentElement el : req.getElements()) {
                    docxService.applyElement(doc, el);
                }
            }
            byte[] bytes = docxService.saveToBytes(doc);
            String filename = req.getFilename() != null ? req.getFilename() : "document.docx";
            return ResponseEntity.ok()
                    .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + filename + "\"")
                    .contentType(MediaType.parseMediaType(
                            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"))
                    .body(bytes);
        } catch (Exception e) {
            log.error("DOCX generate error", e);
            return ResponseEntity.status(500).build();
        }
    }

    /**
     * Extract text content from an uploaded DOCX.
     * POST /api/docx/extract/text
     */
    @PostMapping("/extract/text")
    public ResponseEntity<Map<String, Object>> extractText(@RequestParam("file") MultipartFile file) {
        try {
            XWPFDocument doc = new XWPFDocument(new ByteArrayInputStream(file.getBytes()));
            String text = docxService.extractText(doc);
            return ResponseEntity.ok(Map.of("success", true, "text", text));
        } catch (Exception e) {
            return ResponseEntity.status(500).body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    /**
     * Extract tables from an uploaded DOCX.
     * POST /api/docx/extract/tables
     */
    @PostMapping("/extract/tables")
    public ResponseEntity<Map<String, Object>> extractTables(@RequestParam("file") MultipartFile file) {
        try {
            XWPFDocument doc = new XWPFDocument(new ByteArrayInputStream(file.getBytes()));
            var tables = docxService.extractTables(doc);
            return ResponseEntity.ok(Map.of("success", true, "tables", tables));
        } catch (Exception e) {
            return ResponseEntity.status(500).body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    /**
     * Extract document structure (headings, paragraphs, tables summary).
     * POST /api/docx/extract/structure
     */
    @PostMapping("/extract/structure")
    public ResponseEntity<Map<String, Object>> extractStructure(@RequestParam("file") MultipartFile file) {
        try {
            XWPFDocument doc = new XWPFDocument(new ByteArrayInputStream(file.getBytes()));
            var structure = docxService.extractStructure(doc);
            return ResponseEntity.ok(Map.of("success", true, "structure", structure));
        } catch (Exception e) {
            return ResponseEntity.status(500).body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    /**
     * Get raw XML body of an uploaded DOCX.
     * POST /api/docx/xml
     */
    @PostMapping("/xml")
    public ResponseEntity<Map<String, Object>> getXml(@RequestParam("file") MultipartFile file) {
        try {
            XWPFDocument doc = new XWPFDocument(new ByteArrayInputStream(file.getBytes()));
            String xml = docxService.getBodyXml(doc);
            return ResponseEntity.ok(Map.of("success", true, "xml", xml));
        } catch (Exception e) {
            return ResponseEntity.status(500).body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    /**
     * List available built-in styles.
     * GET /api/docx/styles
     */
    @GetMapping("/styles")
    public ResponseEntity<Map<String, Object>> listStyles() {
        try {
            XWPFDocument doc = docxService.createDocument();
            var styles = docxService.listStyles(doc);
            return ResponseEntity.ok(Map.of("success", true, "styles", styles));
        } catch (Exception e) {
            return ResponseEntity.status(500).body(Map.of("success", false, "error", e.getMessage()));
        }
    }
}

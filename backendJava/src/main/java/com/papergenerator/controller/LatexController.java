package com.papergenerator.controller;

import com.papergenerator.service.LatexService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

/**
 * LaTeX conversion and validation API.
 */
@Slf4j
@RestController
@RequestMapping("/api/latex")
@RequiredArgsConstructor
public class LatexController {

    private final LatexService latexService;

    /**
     * Convert LaTeX math to MathML.
     * POST /api/latex/to-mathml
     * Body: { "latex": "\\frac{a}{b}" }
     */
    @PostMapping("/to-mathml")
    public ResponseEntity<Map<String, Object>> toMathml(@RequestBody Map<String, String> body) {
        String latex = body.get("latex");
        if (latex == null || latex.isBlank()) {
            return ResponseEntity.badRequest()
                    .body(Map.of("success", false, "error", "Missing 'latex' field"));
        }
        try {
            String mathml = latexService.latexToMathml(latex);
            return ResponseEntity.ok(Map.of("success", true, "mathml", mathml));
        } catch (Exception e) {
            log.error("LaTeX→MathML error for: {}", latex, e);
            return ResponseEntity.status(500)
                    .body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    /**
     * Convert LaTeX math to OMML (Word-native math XML string).
     * POST /api/latex/to-omml
     * Body: { "latex": "\\frac{a}{b}" }
     */
    @PostMapping("/to-omml")
    public ResponseEntity<Map<String, Object>> toOmml(@RequestBody Map<String, String> body) {
        String latex = body.get("latex");
        if (latex == null || latex.isBlank()) {
            return ResponseEntity.badRequest()
                    .body(Map.of("success", false, "error", "Missing 'latex' field"));
        }
        try {
            String omml = latexService.latexToOmmlString(latex);
            return ResponseEntity.ok(Map.of("success", true, "omml", omml));
        } catch (Exception e) {
            log.error("LaTeX→OMML error for: {}", latex, e);
            return ResponseEntity.status(500)
                    .body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    /**
     * Validate LaTeX syntax.
     * POST /api/latex/validate
     * Body: { "latex": "..." }
     */
    @PostMapping("/validate")
    public ResponseEntity<Map<String, Object>> validate(@RequestBody Map<String, String> body) {
        String latex = body.get("latex");
        if (latex == null) {
            return ResponseEntity.badRequest()
                    .body(Map.of("success", false, "error", "Missing 'latex' field"));
        }
        boolean valid = latexService.validateLatex(latex);
        return ResponseEntity.ok(Map.of("success", true, "valid", valid,
                "normalized", latexService.normalizeLatex(latex)));
    }

    /**
     * Batch convert multiple LaTeX expressions.
     * POST /api/latex/batch
     * Body: { "expressions": ["expr1", "expr2", ...], "format": "mathml"|"omml" }
     */
    @PostMapping("/batch")
    public ResponseEntity<Map<String, Object>> batchConvert(@RequestBody Map<String, Object> body) {
        @SuppressWarnings("unchecked")
        var expressions = (java.util.List<String>) body.get("expressions");
        String format = (String) body.getOrDefault("format", "mathml");
        if (expressions == null || expressions.isEmpty()) {
            return ResponseEntity.badRequest()
                    .body(Map.of("success", false, "error", "Missing 'expressions' field"));
        }
        java.util.List<Map<String, Object>> results = new java.util.ArrayList<>();
        for (String expr : expressions) {
            try {
                String converted = "omml".equalsIgnoreCase(format)
                        ? latexService.latexToOmmlString(expr)
                        : latexService.latexToMathml(expr);
                results.add(Map.of("input", expr, "output", converted, "success", true));
            } catch (Exception e) {
                results.add(Map.of("input", expr, "error", e.getMessage(), "success", false));
            }
        }
        return ResponseEntity.ok(Map.of("success", true, "results", results));
    }

    /**
     * Normalize LaTeX expression.
     * GET /api/latex/normalize?expr=...
     */
    @GetMapping("/normalize")
    public ResponseEntity<Map<String, Object>> normalize(@RequestParam String expr) {
        String normalized = latexService.normalizeLatex(expr);
        return ResponseEntity.ok(Map.of("success", true, "input", expr, "normalized", normalized));
    }
}

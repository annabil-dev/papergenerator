package com.papergenerator.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.papergenerator.config.AppConfig;
import com.papergenerator.dto.GenerateFullRequest;
import com.papergenerator.dto.GenerateRequest;
import com.papergenerator.dto.PaperDto;
import com.papergenerator.service.*;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

/**
 * Main paper API controller.
 * Mirrosrs all /api/* endpoints from the Python Flask backend plus extras.
 */
@Slf4j
@RestController
@RequestMapping("/api")
@RequiredArgsConstructor
public class PaperController {

    private final IeeePaperService ieeePaperService;
    private final OpenAIService openAIService;
    private final PaperStorageService paperStorageService;
    private final JobService jobService;
    private final AppConfig.AppDirectories dirs;
    private final ObjectMapper mapper;

    // ──────────────────── Health ────────────────────

    @GetMapping("/health")
    public Map<String, Object> health() {
        return Map.of(
                "status", "ok",
                "service", "Paper Generator Java",
                "version", "2.0.0",
                "timestamp", System.currentTimeMillis()
        );
    }

    // ──────────────────── AI Generation ────────────────────

    /**
     * Generate text for one paper section using AI.
     * POST /api/generate
     */
    @PostMapping("/generate")
    public ResponseEntity<Map<String, Object>> generateSection(@RequestBody GenerateRequest req) {
        try {
            // convert PaperDto to Map for context
            @SuppressWarnings("unchecked")
            java.util.Map<String, Object> ctx = req.getPaperContext() != null
                    ? mapper.convertValue(req.getPaperContext(), java.util.Map.class)
                    : null;
            String text = openAIService.generateSectionText(
                    req.getPrompt(), req.getSection(), req.getLastText(), ctx);
            return ResponseEntity.ok(Map.of("success", true, "text", text));
        } catch (Exception e) {
            log.error("Generate section error", e);
            return ResponseEntity.status(500).body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    /**
     * Generate a full paper JSON using AI (async).
     * POST /api/generate-full  → { job_id }
     */
    @PostMapping("/generate-full")
    public ResponseEntity<Map<String, Object>> generateFull(@RequestBody GenerateFullRequest req) {
        String jobId = jobService.submit(() -> {
            try {
                String json = openAIService.generateFullPaperJson(req.getPrompt(), req.getModel());
                PaperDto paper = paperStorageService.parsePaperJson(json);
                String id = paperStorageService.savePaper(paper);
                return Map.of("paper_id", id, "paper", paper);
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        });
        return ResponseEntity.ok(Map.of("success", true, "job_id", jobId));
    }

    /**
     * Poll an async job.
     * GET /api/job/{jobId}
     */
    @GetMapping("/job/{jobId}")
    public ResponseEntity<Map<String, Object>> getJob(@PathVariable String jobId) {
        JobService.JobStatus status = jobService.getJob(jobId);
        if (status == null) {
            return ResponseEntity.status(404).body(Map.of("error", "Job not found: " + jobId));
        }
        return ResponseEntity.ok(status.toMap());
    }

    // ──────────────────── Export / DOCX ────────────────────

    /**
     * Export a paper to IEEE-format DOCX.
     * POST /api/export  body: PaperDto JSON
     */
    @PostMapping("/export")
    public ResponseEntity<byte[]> exportPaper(@RequestBody PaperDto paper) {
        try {
            byte[] bytes = ieeePaperService.generateIeeeDocx(paper);
            String filename = sanitizeFilename(paper.getTitle()) + ".docx";
            return ResponseEntity.ok()
                    .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + filename + "\"")
                    .contentType(MediaType.parseMediaType(
                            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"))
                    .body(bytes);
        } catch (Exception e) {
            log.error("Export paper error", e);
            return ResponseEntity.status(500).build();
        }
    }

    // ──────────────────── Image Upload ────────────────────

    /**
     * Upload an image for use in papers.
     * POST /api/upload-image
     */
    @PostMapping("/upload-image")
    public ResponseEntity<Map<String, Object>> uploadImage(@RequestParam("file") MultipartFile file) {
        try {
            String ext = getExtension(Objects.requireNonNull(file.getOriginalFilename()));
            String filename = UUID.randomUUID().toString().substring(0, 8) + ext;
            Path dest = dirs.getUploadsDir().resolve(filename);
            Files.write(dest, file.getBytes());
            return ResponseEntity.ok(Map.of("success", true, "filename", filename,
                    "url", "/api/images/" + filename));
        } catch (Exception e) {
            return ResponseEntity.status(500).body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    /**
     * Serve uploaded images.
     * GET /api/images/{filename}
     */
    @GetMapping("/images/{filename}")
    public ResponseEntity<byte[]> getImage(@PathVariable String filename) {
        // Sanitize - prevent path traversal
        if (filename.contains("..") || filename.contains("/")) {
            return ResponseEntity.badRequest().build();
        }
        try {
            Path file = dirs.getUploadsDir().resolve(filename);
            if (!file.toAbsolutePath().startsWith(dirs.getUploadsDir().toAbsolutePath())) {
                return ResponseEntity.status(HttpStatus.FORBIDDEN).build();
            }
            if (!Files.exists(file)) return ResponseEntity.notFound().build();
            byte[] bytes = Files.readAllBytes(file);
            String ct = Files.probeContentType(file);
            return ResponseEntity.ok()
                    .contentType(MediaType.parseMediaType(ct != null ? ct : "application/octet-stream"))
                    .body(bytes);
        } catch (Exception e) {
            return ResponseEntity.status(500).build();
        }
    }

    // ──────────────────── Papers CRUD ────────────────────

    @GetMapping("/papers")
    public ResponseEntity<Map<String, Object>> listPapers() {
        try {
            return ResponseEntity.ok(Map.of("success", true, "papers", paperStorageService.listPapers()));
        } catch (Exception e) {
            return ResponseEntity.status(500).body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    @PostMapping("/papers")
    public ResponseEntity<Map<String, Object>> savePaper(@RequestBody PaperDto paper) {
        try {
            String id = paperStorageService.savePaper(paper);
            return ResponseEntity.ok(Map.of("success", true, "id", id));
        } catch (Exception e) {
            return ResponseEntity.status(500).body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    @GetMapping("/papers/{id}")
    public ResponseEntity<?> getPaper(@PathVariable String id) {
        try {
            PaperDto paper = paperStorageService.loadPaper(id);
            return ResponseEntity.ok(Map.of("success", true, "paper", paper));
        } catch (NoSuchElementException e) {
            return ResponseEntity.status(404).body(Map.of("success", false, "error", e.getMessage()));
        } catch (Exception e) {
            return ResponseEntity.status(500).body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    @DeleteMapping("/papers/{id}")
    public ResponseEntity<Map<String, Object>> deletePaper(@PathVariable String id) {
        try {
            boolean deleted = paperStorageService.deletePaper(id);
            return ResponseEntity.ok(Map.of("success", deleted));
        } catch (Exception e) {
            return ResponseEntity.status(500).body(Map.of("success", false, "error", e.getMessage()));
        }
    }

    // ──────────────────── Helpers ────────────────────

    private String sanitizeFilename(String title) {
        if (title == null || title.isBlank()) return "paper";
        return title.replaceAll("[^a-zA-Z0-9._\\- ]", "_")
                    .replaceAll("\\s+", "_")
                    .substring(0, Math.min(80, title.length()));
    }

    private String getExtension(String filename) {
        int dot = filename.lastIndexOf('.');
        return dot >= 0 ? filename.substring(dot) : ".bin";
    }
}

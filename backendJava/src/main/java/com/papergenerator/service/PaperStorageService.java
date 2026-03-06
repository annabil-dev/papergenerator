package com.papergenerator.service;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.papergenerator.config.AppConfig;
import com.papergenerator.dto.PaperDto;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.*;

/**
 * Paper CRUD service — save, load, list, delete paper JSON files.
 * Mirrors the Python /api/papers endpoints.
 */
@Slf4j
@Service
@RequiredArgsConstructor
public class PaperStorageService {

    private final AppConfig.AppDirectories dirs;
    private final ObjectMapper mapper;

    public String savePaper(PaperDto paper) throws IOException {
        String id = paper.getId() != null ? paper.getId() : UUID.randomUUID().toString().substring(0, 8);
        paper = PaperDto.builder()
                .id(id).title(paper.getTitle()).authors(paper.getAuthors())
                .abstractText(paper.getAbstractText()).keywords(paper.getKeywords())
                .sections(paper.getSections()).acknowledgment(paper.getAcknowledgment())
                .references(paper.getReferences()).figures(paper.getFigures())
                .tables(paper.getTables()).equations(paper.getEquations())
                .metadata(paper.getMetadata())
                .build();
        Path file = dirs.getPapersDir().resolve(id + ".json");
        mapper.writerWithDefaultPrettyPrinter().writeValue(file.toFile(), paper);
        return id;
    }

    public PaperDto loadPaper(String id) throws IOException {
        Path file = dirs.getPapersDir().resolve(id + ".json");
        if (!Files.exists(file)) throw new NoSuchElementException("Paper not found: " + id);
        return mapper.readValue(file.toFile(), PaperDto.class);
    }

    public List<Map<String, String>> listPapers() throws IOException {
        List<Map<String, String>> papers = new ArrayList<>();
        try (var stream = Files.list(dirs.getPapersDir())) {
            stream.filter(p -> p.toString().endsWith(".json")).forEach(p -> {
                try {
                    JsonNode node = mapper.readTree(p.toFile());
                    Map<String, String> m = new HashMap<>();
                    m.put("id", p.getFileName().toString().replace(".json", ""));
                    m.put("title", node.path("title").asText("Untitled"));
                    m.put("modified", LocalDateTime.ofInstant(
                            Instant.ofEpochMilli(p.toFile().lastModified()), ZoneId.systemDefault()).toString());
                    papers.add(m);
                } catch (Exception ignored) {}
            });
        }
        papers.sort((a, b) -> b.get("modified").compareTo(a.get("modified")));
        return papers;
    }

    public boolean deletePaper(String id) throws IOException {
        Path file = dirs.getPapersDir().resolve(id + ".json");
        return Files.deleteIfExists(file);
    }

    /**
     * Parse a paper from raw JSON string (for generated papers from AI).
     */
    public PaperDto parsePaperJson(String json) throws IOException {
        return mapper.readValue(json, PaperDto.class);
    }

    /**
     * Normalize a paper DTO - fill defaults for missing fields.
     */
    public PaperDto normalizePaper(PaperDto paper) {
        if (paper.getAuthors() == null || paper.getAuthors().isEmpty()) {
            paper = PaperDto.builder()
                    .id(paper.getId()).title(paper.getTitle())
                    .authors(List.of(PaperDto.AuthorDto.builder()
                            .name("Author Name").affiliation("Department, University")
                            .location("City, Country").email("author@example.com").build()))
                    .abstractText(paper.getAbstractText())
                    .keywords(paper.getKeywords() != null ? paper.getKeywords() : new ArrayList<>())
                    .sections(paper.getSections() != null ? paper.getSections() : new ArrayList<>())
                    .acknowledgment(paper.getAcknowledgment())
                    .references(paper.getReferences() != null ? paper.getReferences() : new ArrayList<>())
                    .figures(paper.getFigures() != null ? paper.getFigures() : new ArrayList<>())
                    .tables(paper.getTables() != null ? paper.getTables() : new ArrayList<>())
                    .equations(paper.getEquations() != null ? paper.getEquations() : new ArrayList<>())
                    .build();
        }
        // Normalize sections
        if (paper.getSections() != null) {
            for (int i = 0; i < paper.getSections().size(); i++) {
                PaperDto.SectionDto sec = paper.getSections().get(i);
                if (sec.getId() == null) {
                    // Can't mutate directly since inner classes may not be builder-equipped
                    // The Jackson deserialization should handle defaults
                }
            }
        }
        return paper;
    }
}

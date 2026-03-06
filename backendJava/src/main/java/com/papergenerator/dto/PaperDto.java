package com.papergenerator.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.Builder;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Full IEEE paper data transfer object.
 * Maps 1:1 with the Python backend paper JSON schema.
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@JsonIgnoreProperties(ignoreUnknown = true)
public class PaperDto {

    private String id;
    private String title;

    @Builder.Default
    private List<AuthorDto> authors = new ArrayList<>();

    private String abstractText;  // mapped from "abstract"

    @Builder.Default
    private List<String> keywords = new ArrayList<>();

    @Builder.Default
    private List<SectionDto> sections = new ArrayList<>();

    private String acknowledgment;

    @Builder.Default
    private List<ReferenceDto> references = new ArrayList<>();

    @Builder.Default
    private List<FigureDto> figures = new ArrayList<>();

    @Builder.Default
    private List<TableDto> tables = new ArrayList<>();

    @Builder.Default
    private List<EquationDto> equations = new ArrayList<>();

    private Map<String, Object> metadata;

    // ── Nested DTOs ──────────────────────────────────────────────────────────

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class AuthorDto {
        private String name;
        private String affiliation;
        private String location;
        private String email;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class SectionDto {
        private String id;
        private String number;
        private String title;
        private String content;

        @Builder.Default
        private List<SubsectionDto> subsections = new ArrayList<>();
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class SubsectionDto {
        private String id;
        private String letter;
        private String title;
        private String content;

        @Builder.Default
        private List<NumberedItemDto> numberedItems = new ArrayList<>();
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class NumberedItemDto {
        private String number;
        private String title;
        private String content;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class ReferenceDto {
        private String id;
        private String text;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class FigureDto {
        private String id;
        private String caption;
        private String filename;
        private String url;
        private Double widthInches;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class TableDto {
        private String id;
        private String caption;

        @Builder.Default
        private List<String> headers = new ArrayList<>();

        @Builder.Default
        private List<List<String>> rows = new ArrayList<>();
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class EquationDto {
        private String id;
        private String latex;
        private int number;
    }
}

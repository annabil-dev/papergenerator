package com.papergenerator.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.Builder;

import java.util.List;
import java.util.Map;

/**
 * Request DTO for arbitrary DOCX generation with all POI features.
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@JsonIgnoreProperties(ignoreUnknown = true)
public class DocxRequest {

    private String filename;

    // Page setup
    private PageSetup pageSetup;

    // Metadata
    private DocMetadata metadata;

    // Content elements
    private List<ContentElement> elements;

    // Headers / footers
    private String headerText;
    private String footerText;

    // Password protection
    private String password;

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class PageSetup {
        private String size;           // A4, Letter, Legal
        private String orientation;    // portrait, landscape
        private Double topMargin;      // inches
        private Double bottomMargin;
        private Double leftMargin;
        private Double rightMargin;
        private Integer columns;       // 1 or 2
        private Integer columnSpacing; // twips
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class DocMetadata {
        private String author;
        private String title;
        private String subject;
        private String keywords;
        private String description;
        private Map<String, String> customProperties;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class ContentElement {
        private String type;   // paragraph, table, image, pageBreak, sectionBreak, toc, field, numbering, latex

        // Paragraph
        private String text;
        private String style;
        private String alignment;  // LEFT, CENTER, RIGHT, BOTH
        private Boolean bold;
        private Boolean italic;
        private Boolean underline;
        private Boolean strike;
        private Boolean subscript;
        private Boolean superscript;
        private String fontFamily;
        private Integer fontSize;
        private String fontColor;
        private String highlight;
        private Double spaceBefore;
        private Double spaceAfter;
        private Double lineSpacing;
        private String lineSpacingRule;  // SINGLE, DOUBLE, EXACTLY, AT_LEAST, MULTIPLE
        private Double leftIndent;
        private Double rightIndent;
        private Double firstLineIndent;
        private ParagraphBorder border;
        private List<RunSegment> runs;
        private String bookmarkName;
        private String hyperlinkUrl;

        // Numbering
        private String listType;   // bullet, number
        private Integer listLevel;
        private String numFormat;  // DECIMAL, BULLET, LOWER_LETTER, UPPER_LETTER, LOWER_ROMAN, UPPER_ROMAN

        // Table
        private TableData table;

        // Image
        private ImageData image;

        // LaTeX
        private String latex;
        private Boolean displayEquation;
        private String equationNumber;

        // Field
        private String fieldCode;

        // Section break type
        private String breakType;  // PAGE, NEXT_PAGE, CONTINUOUS, EVEN_PAGE, ODD_PAGE
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class RunSegment {
        private String text;
        private Boolean bold;
        private Boolean italic;
        private Boolean underline;
        private Boolean strike;
        private Boolean subscript;
        private Boolean superscript;
        private String fontFamily;
        private Integer fontSize;
        private String fontColor;
        private String highlight;
        private Boolean lineBreak;
        private Boolean tab;
        private String hyperlinkUrl;
        private String bookmarkStart;
        private String bookmarkEnd;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class TableData {
        private Integer rows;
        private Integer cols;
        private String alignment;    // LEFT, CENTER, RIGHT
        private Double tableWidth;   // pct 0-100 or inches
        private String widthUnit;    // PCT, DXA, NIL, AUTO
        private List<RowData> rowData;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class RowData {
        private List<CellData> cells;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class CellData {
        private String text;
        private String verticalAlignment;  // TOP, CENTER, BOTTOM
        private String bgColor;
        private Boolean bold;
        private Integer fontSize;
        private String alignment;
        private Integer colSpan;
        private Integer rowSpan;
        private BorderSpec borders;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class ImageData {
        private String filename;
        private String base64;
        private Double widthInches;
        private Double heightInches;
        private String position;  // inline, floating
        private Integer posX;
        private Integer posY;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class ParagraphBorder {
        private String top;
        private String bottom;
        private String left;
        private String right;
        private String color;
        private Integer size;
        private Integer space;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class BorderSpec {
        private String top;
        private String bottom;
        private String left;
        private String right;
        private String color;
        private Integer sz;
    }
}

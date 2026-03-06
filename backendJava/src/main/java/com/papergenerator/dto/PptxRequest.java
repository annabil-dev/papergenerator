package com.papergenerator.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.Builder;

import java.util.List;

/**
 * Request DTO for PowerPoint generation (XSLF/HSLF).
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@JsonIgnoreProperties(ignoreUnknown = true)
public class PptxRequest {

    private String filename;
    private String format;   // pptx, ppt
    private List<SlideRequest> slides;

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class SlideRequest {
        private String layout;     // TITLE, CONTENT, TITLE_AND_CONTENT, BLANK, TWO_CONTENT
        private String title;
        private String subtitle;
        private String notes;
        private List<ShapeRequest> shapes;
        private String bgColor;    // hex RRGGBB
        private String bgImage;    // base64 or filename
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class ShapeRequest {
        private String type;       // textbox, image, table, chart, line, rectangle, oval, connector
        private double x;          // inches
        private double y;          // inches
        private double width;      // inches
        private double height;     // inches
        private String text;
        private Boolean bold;
        private Boolean italic;
        private Integer fontSize;
        private String fontColor;
        private String fillColor;
        private String lineColor;
        private Double lineWidth;
        private String alignment;
        private String imageData;  // base64 or filename
        private TableShape table;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class TableShape {
        private List<List<String>> data;
        private List<String> headers;
        private String headerBgColor;
        private String headerFontColor;
    }
}

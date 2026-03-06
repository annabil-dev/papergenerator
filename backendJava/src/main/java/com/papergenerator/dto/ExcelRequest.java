package com.papergenerator.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.Builder;

import java.util.List;
import java.util.Map;

/**
 * Request DTO for Excel workbook generation (HSSF/XSSF/SXSSF).
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@JsonIgnoreProperties(ignoreUnknown = true)
public class ExcelRequest {

    private String filename;
    private String format;  // xlsx, xls, streaming-xlsx

    private List<SheetRequest> sheets;

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class SheetRequest {
        private String name;
        private List<RowRequest> rows;
        private Map<Integer, Integer> columnWidths;  // colIndex -> width in chars
        private Boolean autoFilter;
        private Integer autoFilterRow;
        private List<MergeRegion> mergeRegions;
        private Boolean protectSheet;
        private String sheetPassword;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class RowRequest {
        private Integer rowIndex;
        private Integer height;  // in points * 20
        private List<CellRequest> cells;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class CellRequest {
        private Integer colIndex;
        private String value;
        private String type;       // string, number, boolean, formula, date, blank
        private CellStyleRequest style;
        private String comment;
        private String hyperlink;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class CellStyleRequest {
        private Boolean bold;
        private Boolean italic;
        private Boolean underline;
        private Integer fontSize;
        private String fontColor;     // hex RRGGBB
        private String bgColor;       // hex RRGGBB
        private String alignment;     // LEFT, CENTER, RIGHT, FILL, JUSTIFY
        private String vertAlignment; // TOP, CENTER, BOTTOM
        private Boolean wrapText;
        private String borderTop;
        private String borderBottom;
        private String borderLeft;
        private String borderRight;
        private String dataFormat;    // e.g., "#,##0.00", "yyyy-mm-dd"
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class MergeRegion {
        private int firstRow;
        private int lastRow;
        private int firstCol;
        private int lastCol;
    }
}

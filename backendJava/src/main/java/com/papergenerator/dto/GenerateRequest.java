package com.papergenerator.dto;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.Builder;

/**
 * Request DTO for AI text generation.
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class GenerateRequest {
    private String prompt;
    private String lastText;
    private String section;
    private PaperDto paperContext;
}

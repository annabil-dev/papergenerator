package com.papergenerator.dto;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.Builder;

/**
 * Request DTO for full paper generation.
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class GenerateFullRequest {
    private String prompt;
    private String customPrompt;
    private String model;
}

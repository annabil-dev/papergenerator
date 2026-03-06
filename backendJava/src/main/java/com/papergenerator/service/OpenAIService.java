package com.papergenerator.service;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;

import java.time.Duration;
import java.util.List;
import java.util.Map;

/**
 * OpenAI API client service.
 * Supports: chat completions (text generation), streaming.
 */
@Slf4j
@Service
public class OpenAIService {

    private final WebClient webClient;
    private final ObjectMapper mapper;

    @Value("${openai.api-key:}")
    private String apiKey;

    @Value("${openai.model:gpt-4o-mini}")
    private String defaultModel;

    @Value("${openai.timeout:600}")
    private int timeoutSeconds;

    // Section-specific system prompts (mirrors Python backend)
    private static final Map<String, String> SECTION_PROMPTS = Map.of(
        "title", """
            You are an IEEE conference paper title writer. Generate a concise, specific paper title (max 15 words)
            that clearly indicates the research contribution. Include key technical terms and method names if relevant.
            Return ONLY the title.""",
        "abstract", """
            You are an IEEE conference paper writer. Generate a 150-200 word abstract following IEEE format.
            Start with problem statement, then propose method, then results. Include quantitative metrics if available.
            For formulas use $..$ notation. Return ONLY the abstract text.""",
        "introduction", """
            You are an IEEE conference researcher. Write an INTRODUCTION section (200-300 words) that:
            1) Motivates the problem with background
            2) Identifies the research gap
            3) States contributions clearly
            Include citations as [1], [2], etc. Use $$formula$$ for displayed equations. Write naturally, academically.""",
        "methodology", """
            You are a systems researcher. Write a METHODOLOGY/APPROACH section that describes:
            1) Problem formulation (with equations if needed)
            2) Proposed method/algorithm (with formulas: use $x$ for inline, $$formula$$ for display)
            3) Implementation details
            Use IEEE notation and cite related work as [1], [2]. Be technical and specific.""",
        "results", """
            You are a research scientist. Write EXPERIMENTAL RESULTS section:
            1) Datasets/benchmarks used
            2) Evaluation metrics with values (e.g., "achieves 92.5% accuracy")
            3) Comparison with baselines [1][2]
            4) Analysis and insights
            Include numerical results. Cite properly. Be quantitative.""",
        "conclusion", """
            You are an academic writer. Write CONCLUSION section (100-150 words):
            1) Summarize key contributions
            2) Highlight achieved metrics
            3) Mention future work
            Keep it clear and formal. No markdown.""",
        "acknowledgment", """
            You are writing paper acknowledgments. Write 2-3 sentences thanking:
            - Funding agencies
            - Collaborators/advisors
            - Data/resource providers
            Format: "We thank X for Y support. We gratefully acknowledge Z."
            Keep it professional and concise."""
    );

    public OpenAIService(WebClient openAiWebClient, ObjectMapper objectMapper) {
        this.webClient = openAiWebClient;
        this.mapper = objectMapper;
    }

    /**
     * Generate text for a specific paper section.
     */
    public String generateSectionText(String prompt, String section, String lastText,
                                       Map<String, Object> paperContext) {
        validateApiKey();
        String systemPrompt = SECTION_PROMPTS.getOrDefault(section != null ? section.toLowerCase() : "",
                "You are an expert academic writer for IEEE papers. Generate content for the specified section. " +
                "Use LaTeX notation for formulas ($..$ inline, $$...$$ display). Cite with [1], [2], etc format. " +
                "Write formally and technically. Return ONLY the content.");

        List<Map<String, String>> messages = buildMessages(systemPrompt, prompt, lastText, section, paperContext);

        return callChatCompletions(messages, defaultModel);
    }

    /**
     * Generate a full IEEE paper JSON from a topic prompt.
     */
    public String generateFullPaperJson(String prompt, String model) {
        validateApiKey();
        String effectiveModel = model != null && !model.isBlank() ? model : defaultModel;

        List<Map<String, String>> messages = List.of(
            Map.of("role", "system", "content", FULL_PAPER_SYSTEM_PROMPT),
            Map.of("role", "user", "content",
                "Generate a complete IEEE conference paper about: " + prompt + "\n\n" +
                "Return ONLY valid JSON matching the schema above.")
        );

        return callChatCompletions(messages, effectiveModel);
    }

    /**
     * Generic chat completion call.
     */
    public String callChatCompletions(List<Map<String, String>> messages, String model) {
        validateApiKey();
        try {
            Map<String, Object> body = Map.of(
                "model", model != null ? model : defaultModel,
                "messages", messages,
                "temperature", 0.7
            );

            String responseJson = webClient.post()
                .uri("/chat/completions")
                .header("Authorization", "Bearer " + apiKey)
                .header("Content-Type", "application/json")
                .bodyValue(body)
                .retrieve()
                .bodyToMono(String.class)
                .timeout(Duration.ofSeconds(timeoutSeconds))
                .block();

            if (responseJson == null) throw new RuntimeException("Empty response from OpenAI");
            JsonNode root = mapper.readTree(responseJson);
            if (root.has("error")) throw new RuntimeException("OpenAI error: " + root.get("error").get("message").asText());
            return root.path("choices").path(0).path("message").path("content").asText();
        } catch (Exception e) {
            throw new RuntimeException("OpenAI API error: " + e.getMessage(), e);
        }
    }

    public boolean isConfigured() {
        return apiKey != null && !apiKey.isBlank() && !apiKey.equals("sk-your-actual-api-key");
    }

    public String getModel() { return defaultModel; }

    private void validateApiKey() {
        if (!isConfigured()) {
            throw new RuntimeException("OPENAI_API_KEY not configured. Please set it in application.properties or env.");
        }
    }

    private List<Map<String, String>> buildMessages(String systemPrompt, String prompt,
                                                      String lastText, String section,
                                                      Map<String, Object> paperContext) {
        var messages = new java.util.ArrayList<Map<String, String>>();
        messages.add(Map.of("role", "system", "content", systemPrompt));

        if (paperContext != null || lastText != null) {
            var contextParts = new java.util.ArrayList<String>();
            if (paperContext != null) {
                if (paperContext.get("title") != null) contextParts.add("Paper title: " + paperContext.get("title"));
            }
            if (lastText != null && !lastText.isBlank()) {
                contextParts.add("\n--- Current content of '" + section + "' section ---\n" + lastText + "\n--- End ---");
            }
            if (!contextParts.isEmpty()) {
                messages.add(Map.of("role", "user", "content", String.join("\n", contextParts)));
                messages.add(Map.of("role", "assistant", "content", "I understand the context. What would you like me to do?"));
            }
        }
        messages.add(Map.of("role", "user", "content", prompt));
        return messages;
    }

    // Full paper generation system prompt (mirrors Python generate_ai_josn_paper.py)
    private static final String FULL_PAPER_SYSTEM_PROMPT = """
You are a senior IEEE conference paper author with 15+ years of publication experience.
Your task is to generate a COMPLETE, PUBLICATION-READY IEEE conference paper in strict JSON format.

All formulas inside JSON string values use LaTeX delimiters:
  • $...$ for inline math
  • $$...$$ for display/block math
The "equations" array uses RAW LaTeX only (NO $ delimiters).

Return ONLY valid JSON with this exact structure:
{
  "title": "Specific technical title, max 15 words",
  "authors": [
    {
      "name": "Firstname Lastname",
      "affiliation": "Department of Computer Science, University Name",
      "location": "City, Country",
      "email": "author@university.edu"
    }
  ],
  "abstract": "150-200 words abstract here",
  "keywords": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"],
  "sections": [
    {
      "id": "sec-introduction",
      "number": "I",
      "title": "Introduction",
      "content": "Section content with citations [1], inline math $x_i$, and display equations $$E = mc^2$$.",
      "subsections": [
        {
          "id": "sec-1a",
          "letter": "A",
          "title": "Subsection Title",
          "content": "Subsection content here.",
          "numberedItems": []
        }
      ]
    },
    {
      "id": "sec-related",
      "number": "II",
      "title": "Related Work",
      "content": "Related work content here.",
      "subsections": []
    },
    {
      "id": "sec-method",
      "number": "III",
      "title": "Proposed Method",
      "content": "Method description with formulas.",
      "subsections": []
    },
    {
      "id": "sec-experiments",
      "number": "IV",
      "title": "Experimental Results",
      "content": "Results with [TABLE:table-1] and [FIGURE:figure-1].",
      "subsections": []
    },
    {
      "id": "sec-conclusion",
      "number": "V",
      "title": "Conclusion",
      "content": "Conclusion content.",
      "subsections": []
    }
  ],
  "acknowledgment": "Acknowledgment text here.",
  "references": [
    {"id": "1", "text": "A. Author, 'Title,' in Proc. IEEE Conf., 2023, pp. 1-5."},
    {"id": "2", "text": "B. Author, 'Title,' IEEE Trans. X, vol. 1, no. 1, pp. 1-10, 2023."}
  ],
  "figures": [
    {"id": "figure-1", "caption": "Fig. 1. Caption text.", "filename": "", "url": ""}
  ],
  "tables": [
    {
      "id": "table-1",
      "caption": "TABLE I. Comparison Results.",
      "headers": ["Method", "Metric1", "Metric2"],
      "rows": [
        ["Baseline", "85.2", "78.3"],
        ["Proposed", "92.5", "88.1"]
      ]
    }
  ],
  "equations": [
    {"id": "eq-1", "latex": "y = f(x) + \\\\epsilon", "number": 1}
  ]
}

Write with formal academic language. Include at least 5 references, 1 table, and 1 figure.
Return ONLY the JSON, no other text.
""";
}

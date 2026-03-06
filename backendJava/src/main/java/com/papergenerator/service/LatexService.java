package com.papergenerator.service;

import lombok.extern.slf4j.Slf4j;
import org.apache.poi.xwpf.usermodel.XWPFParagraph;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Service;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;

import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMResult;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.regex.Pattern;

/**
 * LaTeX ↔ MathML ↔ OMML conversion service.
 *
 * Pipeline: LaTeX → MathML (via custom parser) → OMML (via MML2OMML.XSL XSLT).
 *
 * For LaTeX → MathML we use a built-in lightweight converter that handles
 * the most common IEEE paper math patterns. For full coverage the XSLT
 * transformer (Saxon) is applied on the MathML output.
 */
@Slf4j
@Service
public class LatexService {

    private static final String OMML_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math";
    private static final String MATHML_NS = "http://www.w3.org/1998/Math/MathML";

    // Cached XSLT transformer
    private Transformer mml2ommlTransformer;
    private boolean transformerLoaded = false;

    // ── Public API ────────────────────────────────────────────────────────────

    /**
     * Convert LaTeX expression to OMML XML node suitable for embedding into DOCX.
     * Returns null on failure.
     */
    public Node latexToOmmlNode(String latex) {
        try {
            String mathml = latexToMathml(latex);
            if (mathml == null || mathml.isBlank()) return null;
            return mathmlToOmmlNode(mathml);
        } catch (Exception e) {
            log.debug("LaTeX→OMML failed for '{}': {}", latex, e.getMessage());
            return null;
        }
    }

    /**
     * Convert LaTeX to MathML string.
     */
    public String latexToMathml(String latex) {
        if (latex == null || latex.isBlank()) return null;
        latex = latex.trim();
        // Remove outer delimiters if present
        if (latex.startsWith("$$") && latex.endsWith("$$")) latex = latex.substring(2, latex.length() - 2).trim();
        if (latex.startsWith("$") && latex.endsWith("$")) latex = latex.substring(1, latex.length() - 1).trim();

        try {
            return convertLatexToMathml(latex);
        } catch (Exception e) {
            log.warn("LaTeX→MathML error: {}", e.getMessage());
            return null;
        }
    }

    /**
     * Convert MathML string to OMML DOM Node using MML2OMML.XSL.
     */
    public Node mathmlToOmmlNode(String mathml) {
        Transformer t = getTransformer();
        if (t == null) return null;
        try {
            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            dbf.setNamespaceAware(true);
            Document mathmlDoc = dbf.newDocumentBuilder()
                    .parse(new java.io.ByteArrayInputStream(mathml.getBytes(StandardCharsets.UTF_8)));
            DOMResult result = new DOMResult();
            t.transform(new DOMSource(mathmlDoc), result);
            Document ommlDoc = (Document) result.getNode();
            return ommlDoc != null ? ommlDoc.getDocumentElement() : null;
        } catch (Exception e) {
            log.warn("MathML→OMML error: {}", e.getMessage());
            return null;
        }
    }

    /**
     * Render LaTeX as OMML XML string (for embedding into DOCX XML directly).
     */
    public String latexToOmmlString(String latex) {
        try {
            Node omml = latexToOmmlNode(latex);
            if (omml == null) return null;
            ByteArrayOutputStream out = new ByteArrayOutputStream();
            TransformerFactory.newInstance().newTransformer()
                    .transform(new DOMSource(omml), new StreamResult(out));
            return out.toString(StandardCharsets.UTF_8);
        } catch (Exception e) {
            log.warn("OMML→string error: {}", e.getMessage());
            return null;
        }
    }

    /**
     * Validate LaTeX expression (basic syntax check).
     */
    public boolean validateLatex(String latex) {
        if (latex == null || latex.isBlank()) return false;
        // Check balanced braces
        int depth = 0;
        for (char c : latex.toCharArray()) {
            if (c == '{') depth++;
            else if (c == '}') depth--;
            if (depth < 0) return false;
        }
        return depth == 0;
    }

    /**
     * Normalize LaTeX: ensure proper escaping and clean up common mistakes.
     */
    public String normalizeLatex(String latex) {
        if (latex == null) return null;
        latex = latex.trim();
        // Remove outer $ delimiters
        if (latex.startsWith("$$") && latex.endsWith("$$"))
            latex = latex.substring(2, latex.length() - 2).trim();
        else if (latex.startsWith("$") && latex.endsWith("$"))
            latex = latex.substring(1, latex.length() - 1).trim();

        // Common normalizations
        latex = latex.replace("\\\\", "\\");
        return latex;
    }

    // ── Private: XSLT Transformer ─────────────────────────────────────────────

    private synchronized Transformer getTransformer() {
        if (transformerLoaded) return mml2ommlTransformer;
        transformerLoaded = true;
        try {
            // Try Saxon-HE for full XSLT 2.0 support
            TransformerFactory factory = new net.sf.saxon.TransformerFactoryImpl();
            ClassPathResource xslResource = new ClassPathResource("MML2OMML.XSL");
            try (InputStream is = xslResource.getInputStream()) {
                Source xslSource = new StreamSource(is);
                mml2ommlTransformer = factory.newTransformer(xslSource);
                log.info("MML2OMML.XSL transformer loaded successfully (Saxon)");
            }
        } catch (Exception e) {
            log.warn("Could not load MML2OMML.XSL transformer: {}. Math will render as plain text.", e.getMessage());
            mml2ommlTransformer = null;
        }
        return mml2ommlTransformer;
    }

    // ── Private: LaTeX → MathML lightweight converter ─────────────────────────

    /**
     * Lightweight LaTeX → MathML converter handling common IEEE math patterns.
     * Uses pattern-based token parsing to produce W3C MathML 3.
     */
    private String convertLatexToMathml(String latex) {
        StringBuilder sb = new StringBuilder();
        sb.append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
        sb.append("<math xmlns=\"").append(MATHML_NS).append("\" display=\"block\">");
        sb.append("<mrow>");
        sb.append(tokenizeLatex(latex));
        sb.append("</mrow></math>");
        return sb.toString();
    }

    /**
     * Recursive LaTeX tokenizer → MathML fragment.
     */
    private String tokenizeLatex(String latex) {
        if (latex == null || latex.isBlank()) return "";
        StringBuilder out = new StringBuilder();
        int i = 0;
        int len = latex.length();

        while (i < len) {
            char c = latex.charAt(i);

            // Skip whitespace
            if (Character.isWhitespace(c)) { i++; continue; }

            // Backslash command
            if (c == '\\') {
                int[] end = {i + 1};
                String cmd = readCommand(latex, i + 1, end);
                i = end[0];
                out.append(handleCommand(cmd, latex, end));
                i = end[0];
                continue;
            }

            // Group { ... }
            if (c == '{') {
                int close = findMatchingBrace(latex, i);
                if (close > i) {
                    String inner = latex.substring(i + 1, close);
                    out.append("<mrow>").append(tokenizeLatex(inner)).append("</mrow>");
                    i = close + 1;
                } else {
                    i++;
                }
                continue;
            }

            // Superscript ^
            if (c == '^') {
                i++;
                String arg = readArg(latex, i);
                i += getArgLen(latex, i);
                out.append("<msup><mi/><mrow>").append(tokenizeLatex(arg)).append("</mrow></msup>");
                continue;
            }

            // Subscript _
            if (c == '_') {
                i++;
                String arg = readArg(latex, i);
                i += getArgLen(latex, i);
                out.append("<msub><mi/><mrow>").append(tokenizeLatex(arg)).append("</mrow></msub>");
                continue;
            }

            // Digit or decimal
            if (Character.isDigit(c) || (c == '.' && i + 1 < len && Character.isDigit(latex.charAt(i + 1)))) {
                int j = i;
                while (j < len && (Character.isDigit(latex.charAt(j)) || latex.charAt(j) == '.')) j++;
                out.append("<mn>").append(escapeXml(latex.substring(i, j))).append("</mn>");
                i = j;
                continue;
            }

            // Letter → identifier
            if (Character.isLetter(c)) {
                out.append("<mi>").append(c).append("</mi>");
                i++;
                continue;
            }

            // Operators and symbols
            out.append(charToMathml(c));
            i++;
        }
        return out.toString();
    }

    private String handleCommand(String cmd, String latex, int[] pos) {
        return switch (cmd) {
            case "frac" -> {
                String num = readArgAt(latex, pos);
                String den = readArgAt(latex, pos);
                yield "<mfrac><mrow>" + tokenizeLatex(num) + "</mrow><mrow>" + tokenizeLatex(den) + "</mrow></mfrac>";
            }
            case "sqrt" -> {
                String inner = readArgAt(latex, pos);
                yield "<msqrt><mrow>" + tokenizeLatex(inner) + "</mrow></msqrt>";
            }
            case "sum" -> "<mo>&#x2211;</mo>";
            case "prod" -> "<mo>&#x220F;</mo>";
            case "int" -> "<mo>&#x222B;</mo>";
            case "oint" -> "<mo>&#x222E;</mo>";
            case "infty" -> "<mn>&#x221E;</mn>";
            case "partial" -> "<mo>&#x2202;</mo>";
            case "nabla" -> "<mo>&#x2207;</mo>";
            case "alpha" -> "<mi>&#x03B1;</mi>";
            case "beta" -> "<mi>&#x03B2;</mi>";
            case "gamma" -> "<mi>&#x03B3;</mi>";
            case "delta" -> "<mi>&#x03B4;</mi>";
            case "epsilon" -> "<mi>&#x03F5;</mi>";
            case "varepsilon" -> "<mi>&#x03B5;</mi>";
            case "zeta" -> "<mi>&#x03B6;</mi>";
            case "eta" -> "<mi>&#x03B7;</mi>";
            case "theta" -> "<mi>&#x03B8;</mi>";
            case "kappa" -> "<mi>&#x03BA;</mi>";
            case "lambda" -> "<mi>&#x03BB;</mi>";
            case "mu" -> "<mi>&#x03BC;</mi>";
            case "nu" -> "<mi>&#x03BD;</mi>";
            case "xi" -> "<mi>&#x03BE;</mi>";
            case "pi" -> "<mi>&#x03C0;</mi>";
            case "rho" -> "<mi>&#x03C1;</mi>";
            case "sigma" -> "<mi>&#x03C3;</mi>";
            case "tau" -> "<mi>&#x03C4;</mi>";
            case "phi" -> "<mi>&#x03C6;</mi>";
            case "chi" -> "<mi>&#x03C7;</mi>";
            case "psi" -> "<mi>&#x03C8;</mi>";
            case "omega" -> "<mi>&#x03C9;</mi>";
            case "Gamma" -> "<mi>&#x0393;</mi>";
            case "Delta" -> "<mi>&#x0394;</mi>";
            case "Theta" -> "<mi>&#x0398;</mi>";
            case "Lambda" -> "<mi>&#x039B;</mi>";
            case "Sigma" -> "<mi>&#x03A3;</mi>";
            case "Phi" -> "<mi>&#x03A6;</mi>";
            case "Psi" -> "<mi>&#x03A8;</mi>";
            case "Omega" -> "<mi>&#x03A9;</mi>";
            case "times" -> "<mo>&#xD7;</mo>";
            case "cdot" -> "<mo>&#xB7;</mo>";
            case "cdots" -> "<mo>&#x22EF;</mo>";
            case "ldots" -> "<mo>&#x2026;</mo>";
            case "pm" -> "<mo>&#xB1;</mo>";
            case "mp" -> "<mo>&#x2213;</mo>";
            case "leq", "le" -> "<mo>&#x2264;</mo>";
            case "geq", "ge" -> "<mo>&#x2265;</mo>";
            case "neq", "ne" -> "<mo>&#x2260;</mo>";
            case "approx" -> "<mo>&#x2248;</mo>";
            case "equiv" -> "<mo>&#x2261;</mo>";
            case "in" -> "<mo>&#x2208;</mo>";
            case "notin" -> "<mo>&#x2209;</mo>";
            case "subset" -> "<mo>&#x2282;</mo>";
            case "supset" -> "<mo>&#x2283;</mo>";
            case "cup" -> "<mo>&#x222A;</mo>";
            case "cap" -> "<mo>&#x2229;</mo>";
            case "oplus" -> "<mo>&#x2295;</mo>";
            case "otimes" -> "<mo>&#x2297;</mo>";
            case "to" -> "<mo>&#x2192;</mo>";
            case "rightarrow" -> "<mo>&#x2192;</mo>";
            case "leftarrow" -> "<mo>&#x2190;</mo>";
            case "Rightarrow" -> "<mo>&#x21D2;</mo>";
            case "Leftarrow" -> "<mo>&#x21D0;</mo>";
            case "forall" -> "<mo>&#x2200;</mo>";
            case "exists" -> "<mo>&#x2203;</mo>";
            case "langle" -> "<mo>&#x27E8;</mo>";
            case "rangle" -> "<mo>&#x27E9;</mo>";
            case "left" -> "<mo>";  // simplified
            case "right" -> "</mo>";
            case "mathbf" -> {
                String arg = readArgAt(latex, pos);
                yield "<mtext mathvariant=\"bold\">" + escapeXml(arg) + "</mtext>";
            }
            case "mathit" -> {
                String arg = readArgAt(latex, pos);
                yield "<mi>" + escapeXml(arg) + "</mi>";
            }
            case "mathrm", "textrm" -> {
                String arg = readArgAt(latex, pos);
                yield "<mi mathvariant=\"normal\">" + escapeXml(arg) + "</mi>";
            }
            case "mathcal" -> {
                String arg = readArgAt(latex, pos);
                yield "<mi mathvariant=\"script\">" + escapeXml(arg) + "</mi>";
            }
            case "mathbb" -> {
                String arg = readArgAt(latex, pos);
                yield "<mi mathvariant=\"double-struck\">" + escapeXml(arg) + "</mi>";
            }
            case "text", "operatorname" -> {
                String arg = readArgAt(latex, pos);
                yield "<mtext>" + escapeXml(arg) + "</mtext>";
            }
            case "overline" -> {
                String arg = readArgAt(latex, pos);
                yield "<mover><mrow>" + tokenizeLatex(arg) + "</mrow><mo>&#xAF;</mo></mover>";
            }
            case "hat" -> {
                String arg = readArgAt(latex, pos);
                yield "<mover><mrow>" + tokenizeLatex(arg) + "</mrow><mo>^</mo></mover>";
            }
            case "tilde" -> {
                String arg = readArgAt(latex, pos);
                yield "<mover><mrow>" + tokenizeLatex(arg) + "</mrow><mo>~</mo></mover>";
            }
            case "vec" -> {
                String arg = readArgAt(latex, pos);
                yield "<mover><mrow>" + tokenizeLatex(arg) + "</mrow><mo>&#x2192;</mo></mover>";
            }
            case "bar" -> {
                String arg = readArgAt(latex, pos);
                yield "<mover><mrow>" + tokenizeLatex(arg) + "</mrow><mo>&#xAF;</mo></mover>";
            }
            case "underbrace" -> {
                String arg = readArgAt(latex, pos);
                yield "<munder><mrow>" + tokenizeLatex(arg) + "</mrow><mo>&#x23DF;</mo></munder>";
            }
            case "overbrace" -> {
                String arg = readArgAt(latex, pos);
                yield "<mover><mrow>" + tokenizeLatex(arg) + "</mrow><mo>&#x23DE;</mo></mover>";
            }
            case "lfloor" -> "<mo>&#x230A;</mo>";
            case "rfloor" -> "<mo>&#x230B;</mo>";
            case "lceil" -> "<mo>&#x2308;</mo>";
            case "rceil" -> "<mo>&#x2309;</mo>";
            case "lvert", "|" -> "<mo>&#x7C;</mo>";
            case "rvert" -> "<mo>&#x7C;</mo>";
            case "lVert" -> "<mo>&#x2016;</mo>";
            case "rVert" -> "<mo>&#x2016;</mo>";
            case "arg" -> "<mo>arg</mo>";
            case "max" -> "<mo>max</mo>";
            case "min" -> "<mo>min</mo>";
            case "argmax" -> "<mo>arg&#x2009;max</mo>";
            case "argmin" -> "<mo>arg&#x2009;min</mo>";
            case "exp" -> "<mo>exp</mo>";
            case "log" -> "<mo>log</mo>";
            case "ln" -> "<mo>ln</mo>";
            case "sin" -> "<mo>sin</mo>";
            case "cos" -> "<mo>cos</mo>";
            case "tan" -> "<mo>tan</mo>";
            case "lim" -> "<mo>lim</mo>";
            case "det" -> "<mo>det</mo>";
            case "dim" -> "<mo>dim</mo>";
            case "ker" -> "<mo>ker</mo>";
            case "begin" -> {
                String env = readArgAt(latex, pos);
                yield "<mtable><!-- " + env + " -->";
            }
            case "end" -> {
                readArgAt(latex, pos);
                yield "</mtable>";
            }
            case "\\\\" -> "<mspace linebreak=\"newline\"/>";
            case "," -> "<mspace width=\"0.167em\"/>";
            case ";" -> "<mspace width=\"0.278em\"/>";
            case "!" -> "<mspace width=\"-0.167em\"/>";
            case " " -> "<mspace width=\"0.333em\"/>";
            case "quad" -> "<mspace width=\"1em\"/>";
            case "qquad" -> "<mspace width=\"2em\"/>";
            default -> "<mi>" + escapeXml(cmd) + "</mi>";
        };
    }

    // ── Parsing utilities ─────────────────────────────────────────────────────

    private String readCommand(String latex, int start, int[] endPos) {
        int i = start;
        int len = latex.length();
        if (i >= len) { endPos[0] = i; return ""; }
        if (!Character.isLetter(latex.charAt(i))) {
            endPos[0] = i + 1;
            return String.valueOf(latex.charAt(i));
        }
        int j = i;
        while (j < len && Character.isLetter(latex.charAt(j))) j++;
        endPos[0] = j;
        // Skip trailing spaces
        while (endPos[0] < len && latex.charAt(endPos[0]) == ' ') endPos[0]++;
        return latex.substring(i, j);
    }

    private String readArgAt(String latex, int[] pos) {
        // Skip whitespace
        while (pos[0] < latex.length() && Character.isWhitespace(latex.charAt(pos[0]))) pos[0]++;
        if (pos[0] >= latex.length()) return "";
        if (latex.charAt(pos[0]) == '{') {
            int close = findMatchingBrace(latex, pos[0]);
            if (close > pos[0]) {
                String inner = latex.substring(pos[0] + 1, close);
                pos[0] = close + 1;
                return inner;
            }
        }
        // Single char arg
        String ch = String.valueOf(latex.charAt(pos[0]));
        pos[0]++;
        return ch;
    }

    private String readArg(String latex, int start) {
        int[] pos = {start};
        return readArgAt(latex, pos);
    }

    private int getArgLen(String latex, int start) {
        if (start >= latex.length()) return 0;
        if (latex.charAt(start) == '{') {
            int close = findMatchingBrace(latex, start);
            return close >= start ? close - start + 1 : 1;
        }
        return 1;
    }

    private int findMatchingBrace(String latex, int openPos) {
        int depth = 0;
        for (int i = openPos; i < latex.length(); i++) {
            if (latex.charAt(i) == '{') depth++;
            else if (latex.charAt(i) == '}') {
                depth--;
                if (depth == 0) return i;
            }
        }
        return -1;
    }

    private String charToMathml(char c) {
        return switch (c) {
            case '+' -> "<mo>+</mo>";
            case '-' -> "<mo>-</mo>";
            case '*' -> "<mo>*</mo>";
            case '/' -> "<mo>/</mo>";
            case '=' -> "<mo>=</mo>";
            case '<' -> "<mo>&lt;</mo>";
            case '>' -> "<mo>&gt;</mo>";
            case '(' -> "<mo>(</mo>";
            case ')' -> "<mo>)</mo>";
            case '[' -> "<mo>[</mo>";
            case ']' -> "<mo>]</mo>";
            case '|' -> "<mo>|</mo>";
            case '!' -> "<mo>!</mo>";
            case ',' -> "<mo>,</mo>";
            case '.' -> "<mo>.</mo>";
            case ':' -> "<mo>:</mo>";
            case ';' -> "<mo>;</mo>";
            default -> "<mo>" + escapeXml(String.valueOf(c)) + "</mo>";
        };
    }

    private String escapeXml(String text) {
        if (text == null) return "";
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;");
    }
}

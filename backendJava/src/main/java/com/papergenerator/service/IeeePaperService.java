package com.papergenerator.service;

import com.papergenerator.config.AppConfig;
import com.papergenerator.dto.PaperDto;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.apache.poi.xwpf.usermodel.*;
import org.openxmlformats.schemas.wordprocessingml.x2006.main.*;
import org.springframework.stereotype.Service;
import org.w3c.dom.Node;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * IEEE Conference Paper DOCX Generator.
 *
 * 100% faithful port of Python generate_docx_from_json.py plus Java-native extensions:
 *  - Full OMML math via XSLT (MML2OMML.XSL) + Saxon
 *  - All inline/display LaTeX → OMML conversion
 *  - Bullet blocks, tables, figures, references
 *  - Two-column IEEE layout with 1-col title/abstract section
 *  - Native Word styles and formatting matching IEEE template
 */
@Slf4j
@Service
@RequiredArgsConstructor
public class IeeePaperService {

    private final LatexService latexService;
    private final AppConfig.AppDirectories dirs;

    // --- Constants -----------------------------------------------------------
    private static final String TIMES_NEW_ROMAN = "Times New Roman";
    private static final String MATH_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math";

    // Inline math pattern: $...$  (not $$...$$)
    private static final Pattern INLINE_MATH = Pattern.compile("(?<!\\$)\\$(?!\\$)(.+?)(?<!\\$)\\$(?!\\$)");
    // Display math pattern: $$...$$
    private static final Pattern DISPLAY_MATH = Pattern.compile("\\$\\$(.+?)\\$\\$", Pattern.DOTALL);
    // Bold: **...**
    private static final Pattern BOLD_PATTERN = Pattern.compile("\\*\\*(.+?)\\*\\*");
    // Italic: *...*
    private static final Pattern ITALIC_PATTERN = Pattern.compile("(?<!\\*)\\*(?!\\*)(.+?)(?<!\\*)\\*(?!\\*)");
    // Citation: [1], [1,2], [1-3]
    private static final Pattern CITATION = Pattern.compile("\\[[0-9][0-9,\\s\\-\u2013]*]");
    // Figure/Table reference: [FIGURE:id] [TABLE:id]
    private static final Pattern FIGURE_REF = Pattern.compile("\\[FIGURE:([^]]+)]");
    private static final Pattern TABLE_REF = Pattern.compile("\\[TABLE:([^]]+)]");

    // ── Public API ────────────────────────────────────────────────────────────

    /**
     * Generate IEEE DOCX from a PaperDto.
     * @return DOCX bytes
     */
    public byte[] generateIeeeDocx(PaperDto paper) throws IOException {
        XWPFDocument doc = new XWPFDocument();

        setupPageLayout(doc);
        setupDefaultStyle(doc);

        addTitle(doc, paper);
        addAuthors(doc, paper);
        addAbstract(doc, paper);
        addKeywords(doc, paper);
        addColumnSectionBreak(doc);  // 1-col → 2-col continuous

        for (PaperDto.SectionDto section : paper.getSections()) {
            addSection(doc, section, paper);
        }

        if (paper.getAcknowledgment() != null && !paper.getAcknowledgment().isBlank()) {
            addSectionHeading(doc, "ACKNOWLEDGMENT");
            addBodyParagraph(doc, paper.getAcknowledgment(), true);
        }

        if (paper.getReferences() != null && !paper.getReferences().isEmpty()) {
            addSectionHeading(doc, "REFERENCES");
            addReferences(doc, paper.getReferences());
        }

        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        doc.write(baos);
        return baos.toByteArray();
    }

    // ── Document setup ────────────────────────────────────────────────────────

    private void setupPageLayout(XWPFDocument doc) {
        // Body sectPr will be modified for 2-column after the 1-col intro break
        CTSectPr sectPr = doc.getDocument().getBody().isSetSectPr()
                ? doc.getDocument().getBody().getSectPr()
                : doc.getDocument().getBody().addNewSectPr();
        CTPageSz pgSz = sectPr.isSetPgSz() ? sectPr.getPgSz() : sectPr.addNewPgSz();
        pgSz.setW(BigInteger.valueOf(12240));  // Letter 8.5in
        pgSz.setH(BigInteger.valueOf(15840));  // Letter 11in
        CTPageMar pgMar = sectPr.isSetPgMar() ? sectPr.getPgMar() : sectPr.addNewPgMar();
        pgMar.setTop(BigInteger.valueOf(1080));    // 0.75in
        pgMar.setBottom(BigInteger.valueOf(1440)); // 1.0in
        pgMar.setLeft(BigInteger.valueOf(900));    // 0.625in
        pgMar.setRight(BigInteger.valueOf(900));   // 0.625in
    }

    private void setupDefaultStyle(XWPFDocument doc) {
        // Set Normal style to Times New Roman 10pt
        try {
            XWPFStyles styles = doc.createStyles();
            CTStyle ctNormal = CTStyle.Factory.newInstance();
            ctNormal.setType(STStyleType.PARAGRAPH);
            ctNormal.setStyleId("Normal");
            ctNormal.setDefault(true);
            CTString name = ctNormal.addNewName();
            name.setVal("Normal");
            var rPr = ctNormal.addNewRPr();
            CTFonts fonts = rPr.addNewRFonts();
            fonts.setAscii(TIMES_NEW_ROMAN);
            fonts.setHAnsi(TIMES_NEW_ROMAN);
            fonts.setEastAsia(TIMES_NEW_ROMAN);
            CTHpsMeasure sz = rPr.addNewSz();
            sz.setVal(BigInteger.valueOf(20)); // 10pt = 20 half-pts
            CTHpsMeasure szCs = rPr.addNewSzCs();
            szCs.setVal(BigInteger.valueOf(20));
            var pPr = ctNormal.addNewPPr();
            CTSpacing spacing = pPr.addNewSpacing();
            spacing.setBefore(BigInteger.ZERO);
            spacing.setAfter(BigInteger.ZERO);
            spacing.setLine(BigInteger.valueOf(240));
            spacing.setLineRule(STLineSpacingRule.AUTO);
            styles.addStyle(new XWPFStyle(ctNormal, styles));
        } catch (Exception e) {
            log.warn("Could not set up default style: {}", e.getMessage());
        }
    }

    // ── Title section ─────────────────────────────────────────────────────────

    private void addTitle(XWPFDocument doc, PaperDto paper) {
        String title = paper.getTitle() != null ? paper.getTitle() : "Untitled Paper";
        XWPFParagraph p = doc.createParagraph();
        p.setAlignment(ParagraphAlignment.CENTER);
        setSpacing(p, 0, 12);
        XWPFRun run = p.createRun();
        run.setText(title);
        run.setBold(true);
        run.setFontSize(24);
        run.setFontFamily(TIMES_NEW_ROMAN);
    }

    private void addAuthors(XWPFDocument doc, PaperDto paper) {
        List<PaperDto.AuthorDto> authors = paper.getAuthors();
        if (authors == null || authors.isEmpty()) return;
        XWPFParagraph p = doc.createParagraph();
        p.setAlignment(ParagraphAlignment.CENTER);
        setSpacing(p, 0, 12);
        for (int i = 0; i < authors.size(); i++) {
            PaperDto.AuthorDto author = authors.get(i);
            if (i > 0) p.createRun().addBreak();
            XWPFRun nameRun = p.createRun();
            nameRun.setText(author.getName() != null ? author.getName() : "");
            nameRun.setFontSize(11);
            nameRun.setFontFamily(TIMES_NEW_ROMAN);
            for (String field : new String[]{author.getAffiliation(), author.getLocation()}) {
                if (field != null && !field.isBlank()) {
                    p.createRun().addBreak();
                    XWPFRun fr = p.createRun();
                    fr.setText(field);
                    fr.setFontSize(10);
                    fr.setFontFamily(TIMES_NEW_ROMAN);
                    fr.setItalic(true);
                }
            }
            if (author.getEmail() != null && !author.getEmail().isBlank()) {
                p.createRun().addBreak();
                XWPFRun er = p.createRun();
                er.setText("e-mail: " + author.getEmail());
                er.setFontSize(10);
                er.setFontFamily(TIMES_NEW_ROMAN);
                er.setItalic(true);
            }
        }
    }

    private void addAbstract(XWPFDocument doc, PaperDto paper) {
        String abs = paper.getAbstractText();
        if (abs == null || abs.isBlank()) return;
        XWPFParagraph p = doc.createParagraph();
        p.setAlignment(ParagraphAlignment.BOTH);
        setSpacing(p, 6, 6);
        XWPFRun labelRun = p.createRun();
        labelRun.setText("Abstract\u2014");
        labelRun.setBold(true);
        labelRun.setItalic(true);
        labelRun.setFontSize(9);
        labelRun.setFontFamily(TIMES_NEW_ROMAN);
        XWPFRun contentRun = p.createRun();
        contentRun.setText(abs);
        contentRun.setItalic(true);
        contentRun.setFontSize(9);
        contentRun.setFontFamily(TIMES_NEW_ROMAN);
    }

    private void addKeywords(XWPFDocument doc, PaperDto paper) {
        List<String> kws = paper.getKeywords();
        if (kws == null || kws.isEmpty()) return;
        XWPFParagraph p = doc.createParagraph();
        p.setAlignment(ParagraphAlignment.BOTH);
        setSpacing(p, 2, 0);
        XWPFRun labelRun = p.createRun();
        labelRun.setText("Keywords\u2014");
        labelRun.setBold(true);
        labelRun.setItalic(true);
        labelRun.setFontSize(9);
        labelRun.setFontFamily(TIMES_NEW_ROMAN);
        XWPFRun kwRun = p.createRun();
        kwRun.setText(String.join(", ", kws));
        kwRun.setItalic(true);
        kwRun.setFontSize(9);
        kwRun.setFontFamily(TIMES_NEW_ROMAN);
    }

    /**
     * Insert an invisible separator paragraph that ends the 1-col section and
     * starts the 2-col section — exactly matching the Python implementation.
     */
    private void addColumnSectionBreak(XWPFDocument doc) {
        // Invisible separator paragraph (1pt font, exact 1pt line height)
        XWPFParagraph sep = doc.createParagraph();
        CTPPr sepPPr = sep.getCTP().addNewPPr();
        var sepRPr = sepPPr.addNewRPr();
        var sepSz = sepRPr.addNewSz();
        sepSz.setVal(BigInteger.TWO); // 1pt
        CTSpacing sp = sepPPr.addNewSpacing();
        sp.setBefore(BigInteger.ZERO);
        sp.setAfter(BigInteger.ZERO);
        sp.setLine(BigInteger.valueOf(20));
        sp.setLineRule(STLineSpacingRule.EXACT);

        // Inline sectPr: 1-col continuous break
        CTSectPr sec1 = sepPPr.addNewSectPr();
        CTSectType secType = sec1.addNewType();
        secType.setVal(STSectionMark.CONTINUOUS);
        CTPageSz pgSz = sec1.addNewPgSz();
        pgSz.setW(BigInteger.valueOf(12240));
        pgSz.setH(BigInteger.valueOf(15840));
        CTPageMar pgMar = sec1.addNewPgMar();
        pgMar.setTop(BigInteger.valueOf(1080));
        pgMar.setRight(BigInteger.valueOf(900));
        pgMar.setBottom(BigInteger.valueOf(1440));
        pgMar.setLeft(BigInteger.valueOf(900));
        CTColumns cols1 = sec1.addNewCols();
        cols1.setNum(BigInteger.ONE);
        cols1.setSpace(BigInteger.valueOf(720));

        // Body final sectPr: 2-column
        CTSectPr bodySectPr = doc.getDocument().getBody().isSetSectPr()
                ? doc.getDocument().getBody().getSectPr()
                : doc.getDocument().getBody().addNewSectPr();
        // Remove existing cols
        if (bodySectPr.isSetCols()) bodySectPr.unsetCols();
        CTColumns cols2 = bodySectPr.addNewCols();
        cols2.setNum(BigInteger.TWO);
        cols2.setSpace(BigInteger.valueOf(340));
    }

    // ── Section content ───────────────────────────────────────────────────────

    private void addSection(XWPFDocument doc, PaperDto.SectionDto section, PaperDto paper) {
        String number = section.getNumber() != null ? section.getNumber() : "";
        String title = section.getTitle() != null ? section.getTitle() : "";
        String heading = number.isBlank() ? title.toUpperCase()
                : number + ". " + title.toUpperCase();
        addSectionHeading(doc, heading);
        if (section.getContent() != null && !section.getContent().isBlank())
            addContentParagraphs(doc, section.getContent(), paper);
        if (section.getSubsections() != null) {
            for (PaperDto.SubsectionDto sub : section.getSubsections()) {
                addSubsection(doc, sub, paper);
            }
        }
    }

    private void addSubsection(XWPFDocument doc, PaperDto.SubsectionDto sub, PaperDto paper) {
        String letter = sub.getLetter() != null ? sub.getLetter() : "";
        String title = sub.getTitle() != null ? sub.getTitle() : "";
        String heading = letter.isBlank() ? title : letter + ". " + title;
        XWPFParagraph p = doc.createParagraph();
        p.setAlignment(ParagraphAlignment.LEFT);
        setSpacing(p, 6, 3);
        XWPFRun run = p.createRun();
        run.setText(heading);
        run.setBold(true);
        run.setItalic(true);
        run.setFontSize(10);
        run.setFontFamily(TIMES_NEW_ROMAN);

        if (sub.getContent() != null && !sub.getContent().isBlank())
            addContentParagraphs(doc, sub.getContent(), paper);

        if (sub.getNumberedItems() != null) {
            for (PaperDto.NumberedItemDto item : sub.getNumberedItems()) {
                String iHead = (item.getNumber() != null ? item.getNumber() + ") " : "")
                        + (item.getTitle() != null ? item.getTitle() : "");
                XWPFParagraph ip = doc.createParagraph();
                setSpacing(ip, 3, 3);
                XWPFRun ir = ip.createRun();
                ir.setText(iHead);
                ir.setBold(true);
                ir.setItalic(true);
                ir.setFontSize(10);
                ir.setFontFamily(TIMES_NEW_ROMAN);
                if (item.getContent() != null)
                    addContentParagraphs(doc, item.getContent(), paper);
            }
        }
    }

    /**
     * Parse and render content blocks: display equations, figures, tables, bullets, text.
     * Mirrors the Python _add_content_paragraphs function exactly.
     */
    private void addContentParagraphs(XWPFDocument doc, String content, PaperDto paper) {
        // Split on display equations first
        String[] blocks = DISPLAY_MATH.split(content, -1);
        Matcher displayMatcher = DISPLAY_MATH.matcher(content);
        List<String> latexBlocks = new java.util.ArrayList<>();
        while (displayMatcher.find()) latexBlocks.add(displayMatcher.group(1).trim());

        int latexIdx = 0;
        for (String block : blocks) {
            block = block.trim();
            if (!block.isEmpty()) {
                // Check if this is an equation block
            }
            // Parse paragraphs in block
            if (!block.isEmpty()) parseBlock(doc, block, paper);
            // Insert display equation if there is one
            if (latexIdx < latexBlocks.size()) {
                String latex = latexBlocks.get(latexIdx++);
                String eqNum = findEquationNumber(latex, paper);
                insertDisplayEquation(doc, latex, eqNum);
            }
        }
    }

    private void parseBlock(XWPFDocument doc, String block, PaperDto paper) {
        for (String para : block.split("\n{2,}")) {
            para = para.trim();
            if (para.isEmpty()) continue;
            if (FIGURE_REF.matcher(para).matches()) { addFigure(doc, para, paper); continue; }
            if (TABLE_REF.matcher(para).matches()) { addTableFromRef(doc, para, paper); continue; }
            if (para.contains("\u2022") || para.startsWith("•")) { addBulletBlock(doc, para); continue; }
            // Normal text - split on single newlines
            for (String line : para.split("\n")) {
                line = line.trim();
                if (line.isEmpty()) continue;
                XWPFParagraph p = doc.createParagraph();
                p.setAlignment(ParagraphAlignment.BOTH);
                setFirstLineIndent(p, 360); // 0.25in
                setSpacing(p, 0, 2);
                addFormattedText(p, line, paper);
            }
        }
    }

    /**
     * Add a centred display equation paragraph.
     * Mirrors Python _insert_display_eq.
     */
    private void insertDisplayEquation(XWPFDocument doc, String latex, String eqNum) {
        XWPFParagraph p = doc.createParagraph();
        p.setAlignment(ParagraphAlignment.CENTER);
        setSpacing(p, 6, 6);

        Node omml = latexService.latexToOmmlNode(latex);
        if (omml != null) {
            try {
                Node imported = p.getCTP().getDomNode().getOwnerDocument().importNode(omml, true);
                p.getCTP().getDomNode().appendChild(imported);
            } catch (Exception e) {
                // fallback
                XWPFRun run = p.createRun();
                run.setItalic(true);
                run.setFontSize(10);
                run.setFontFamily(TIMES_NEW_ROMAN);
                run.setText(latex);
            }
        } else {
            XWPFRun run = p.createRun();
            run.setItalic(true);
            run.setFontSize(10);
            run.setFontFamily(TIMES_NEW_ROMAN);
            run.setText(latex);
        }

        if (eqNum != null && !eqNum.isBlank()) {
            XWPFRun numRun = p.createRun();
            numRun.setFontSize(10);
            numRun.setFontFamily(TIMES_NEW_ROMAN);
            numRun.setText("    (" + eqNum + ")");
        }
    }

    /**
     * Append inline equation as OMML, or fallback to italic text.
     * Mirrors Python _append_inline_eq.
     */
    private boolean appendInlineEquation(XWPFParagraph para, String latex) {
        Node omml = latexService.latexToOmmlNode(latex);
        if (omml != null) {
            try {
                Node imported = para.getCTP().getDomNode().getOwnerDocument().importNode(omml, true);
                para.getCTP().getDomNode().appendChild(imported);
                return true;
            } catch (Exception ignored) {}
        }
        return false;
    }

    /**
     * Add mixed inline formatted text to paragraph.
     * Mirrors Python _add_formatted_text.
     */
    private void addFormattedText(XWPFParagraph para, String text, PaperDto paper) {
        // Tokenize by inline math, bold, italic, citation
        Pattern tokenRe = Pattern.compile(
                "(?<!\\$)\\$(?!\\$)(.+?)(?<!\\$)\\$(?!\\$)" + // inline math
                "|\\*\\*([^*]+)\\*\\*" +                        // **bold**
                "|(?<!\\*)\\*([^*]+)\\*" +                      // *italic*
                "|(\\[[0-9][0-9,\\s\\-\u2013]*])"               // citation
        );
        Matcher m = tokenRe.matcher(text);
        int last = 0;
        while (m.find()) {
            // Plain text before this token
            if (m.start() > last) {
                addPlainRun(para, text.substring(last, m.start()));
            }
            if (m.group(1) != null) {
                // Inline math
                String formula = m.group(1).trim();
                if (!appendInlineEquation(para, formula)) {
                    XWPFRun r = para.createRun();
                    r.setItalic(true);
                    r.setFontSize(10);
                    r.setFontFamily(TIMES_NEW_ROMAN);
                    r.setText(formula);
                }
            } else if (m.group(2) != null) {
                // Bold
                XWPFRun r = para.createRun();
                r.setBold(true);
                r.setFontSize(10);
                r.setFontFamily(TIMES_NEW_ROMAN);
                r.setText(m.group(2));
            } else if (m.group(3) != null) {
                // Italic
                XWPFRun r = para.createRun();
                r.setItalic(true);
                r.setFontSize(10);
                r.setFontFamily(TIMES_NEW_ROMAN);
                r.setText(m.group(3));
            } else if (m.group(4) != null) {
                // Citation
                addPlainRun(para, m.group(4));
            }
            last = m.end();
        }
        if (last < text.length()) addPlainRun(para, text.substring(last));
    }

    private void addPlainRun(XWPFParagraph para, String text) {
        XWPFRun run = para.createRun();
        run.setText(text);
        run.setFontSize(10);
        run.setFontFamily(TIMES_NEW_ROMAN);
    }

    private void addBulletBlock(XWPFDocument doc, String text) {
        String[] parts = text.split("(?=[\u2022•])");
        for (String part : parts) {
            part = part.trim();
            if (part.isEmpty()) continue;
            if (part.startsWith("\u2022") || part.startsWith("•")) {
                String itemText = part.substring(1).trim();
                XWPFParagraph p = doc.createParagraph();
                p.setAlignment(ParagraphAlignment.BOTH);
                setIndent(p, 360, -216); // left 0.25in, hanging 0.15in
                setSpacing(p, 1, 1);
                XWPFRun bullet = p.createRun();
                bullet.setText("\u2022 ");
                bullet.setFontSize(10);
                bullet.setFontFamily(TIMES_NEW_ROMAN);
                addFormattedText(p, itemText, null);
            } else {
                XWPFParagraph p = doc.createParagraph();
                p.setAlignment(ParagraphAlignment.BOTH);
                setFirstLineIndent(p, 360);
                setSpacing(p, 0, 2);
                addPlainRun(p, part);
            }
        }
    }

    // ── Figure / Table ────────────────────────────────────────────────────────

    private void addFigure(XWPFDocument doc, String figureRef, PaperDto paper) {
        Matcher m = FIGURE_REF.matcher(figureRef);
        if (!m.find()) return;
        String figId = m.group(1).trim();
        PaperDto.FigureDto figure = null;
        if (paper.getFigures() != null) {
            for (PaperDto.FigureDto f : paper.getFigures()) {
                if (figId.equals(f.getId())) { figure = f; break; }
            }
        }

        XWPFParagraph imgPara = doc.createParagraph();
        imgPara.setAlignment(ParagraphAlignment.CENTER);
        setSpacing(imgPara, 6, 3);

        if (figure != null && figure.getFilename() != null) {
            Path imgPath = dirs.getUploadsDir().resolve(figure.getFilename());
            if (Files.exists(imgPath)) {
                try {
                    byte[] imgBytes = Files.readAllBytes(imgPath);
                    String fn = figure.getFilename().toLowerCase();
                    int picType = fn.endsWith(".png") ? XWPFDocument.PICTURE_TYPE_PNG
                            : fn.endsWith(".gif") ? XWPFDocument.PICTURE_TYPE_GIF
                            : XWPFDocument.PICTURE_TYPE_JPEG;
                    double w = figure.getWidthInches() != null ? figure.getWidthInches() : 3.0;
                    XWPFRun imgRun = imgPara.createRun();
                    imgRun.addPicture(new java.io.ByteArrayInputStream(imgBytes), picType,
                            figure.getFilename(), (int)(w * 914400), (int)(w * 914400 * 0.75));
                } catch (Exception e) {
                    imgPara.createRun().setText("[Figure: " + (figure.getFilename()) + "]");
                }
            }
        }

        // Caption
        String caption = figure != null && figure.getCaption() != null ? figure.getCaption() : "";
        if (!caption.isBlank()) {
            XWPFParagraph capPara = doc.createParagraph();
            capPara.setAlignment(ParagraphAlignment.CENTER);
            setSpacing(capPara, 0, 6);
            XWPFRun capRun = capPara.createRun();
            capRun.setText(caption);
            capRun.setFontSize(8);
            capRun.setFontFamily(TIMES_NEW_ROMAN);
        }
    }

    private void addTableFromRef(XWPFDocument doc, String tableRef, PaperDto paper) {
        Matcher m = TABLE_REF.matcher(tableRef);
        if (!m.find()) return;
        String tblId = m.group(1).trim();
        PaperDto.TableDto tableData = null;
        if (paper.getTables() != null) {
            for (PaperDto.TableDto t : paper.getTables()) {
                if (tblId.equals(t.getId())) { tableData = t; break; }
            }
        }
        if (tableData == null) return;

        String caption = tableData.getCaption() != null ? tableData.getCaption() : "";
        if (!caption.isBlank()) {
            XWPFParagraph capPara = doc.createParagraph();
            capPara.setAlignment(ParagraphAlignment.CENTER);
            setSpacing(capPara, 6, 3);
            XWPFRun capRun = capPara.createRun();
            capRun.setText(caption);
            capRun.setBold(true);
            capRun.setFontSize(8);
            capRun.setFontFamily(TIMES_NEW_ROMAN);
        }

        List<String> headers = tableData.getHeaders();
        List<List<String>> rows = tableData.getRows();
        if (headers == null || headers.isEmpty()) return;

        XWPFTable table = doc.createTable(1 + (rows != null ? rows.size() : 0), headers.size());
        table.setTableAlignment(TableRowAlign.CENTER);
        // Set grid border style
        CTTblPr tblPr = table.getCTTbl().getTblPr();
        if (tblPr == null) tblPr = table.getCTTbl().addNewTblPr();
        CTTblBorders borders = tblPr.isSetTblBorders() ? tblPr.getTblBorders() : tblPr.addNewTblBorders();
        setBorderSingle(borders.addNewTop()); setBorderSingle(borders.addNewBottom());
        setBorderSingle(borders.addNewLeft()); setBorderSingle(borders.addNewRight());
        setBorderSingle(borders.addNewInsideH()); setBorderSingle(borders.addNewInsideV());

        // Header row
        for (int i = 0; i < headers.size(); i++) {
            XWPFTableCell cell = table.getRow(0).getCell(i);
            cell.setText("");
            XWPFParagraph cp = cell.getParagraphArray(0);
            cp.setAlignment(ParagraphAlignment.CENTER);
            XWPFRun r = cp.createRun();
            r.setText(headers.get(i));
            r.setBold(true);
            r.setFontSize(8);
            r.setFontFamily(TIMES_NEW_ROMAN);
        }

        // Data rows
        if (rows != null) {
            for (int ri = 0; ri < rows.size(); ri++) {
                List<String> row = rows.get(ri);
                for (int ci = 0; ci < headers.size() && ci < row.size(); ci++) {
                    XWPFTableCell cell = table.getRow(ri + 1).getCell(ci);
                    cell.setText("");
                    XWPFParagraph cp = cell.getParagraphArray(0);
                    cp.setAlignment(ParagraphAlignment.CENTER);
                    XWPFRun r = cp.createRun();
                    r.setText(row.get(ci));
                    r.setFontSize(8);
                    r.setFontFamily(TIMES_NEW_ROMAN);
                }
            }
        }
    }

    // ── References ────────────────────────────────────────────────────────────

    private void addReferences(XWPFDocument doc, List<PaperDto.ReferenceDto> refs) {
        for (PaperDto.ReferenceDto ref : refs) {
            XWPFParagraph p = doc.createParagraph();
            p.setAlignment(ParagraphAlignment.BOTH);
            setSpacing(p, 0, 1);
            setIndent(p, 360, -360); // left 0.25in, hanging 0.25in
            XWPFRun r1 = p.createRun();
            r1.setText("[" + (ref.getId() != null ? ref.getId() : "") + "]\t");
            r1.setFontSize(8);
            r1.setFontFamily(TIMES_NEW_ROMAN);
            XWPFRun r2 = p.createRun();
            r2.setText(ref.getText() != null ? ref.getText() : "");
            r2.setFontSize(8);
            r2.setFontFamily(TIMES_NEW_ROMAN);
        }
    }

    // ── Heading helpers ───────────────────────────────────────────────────────

    private void addSectionHeading(XWPFDocument doc, String text) {
        XWPFParagraph p = doc.createParagraph();
        p.setAlignment(ParagraphAlignment.CENTER);
        setSpacing(p, 12, 6);
        XWPFRun run = p.createRun();
        run.setText(text);
        run.setBold(true);
        run.setFontSize(10);
        run.setFontFamily(TIMES_NEW_ROMAN);
    }

    private XWPFParagraph addBodyParagraph(XWPFDocument doc, String text, boolean indent) {
        XWPFParagraph p = doc.createParagraph();
        p.setAlignment(ParagraphAlignment.BOTH);
        if (indent) setFirstLineIndent(p, 360);
        setSpacing(p, 0, 2);
        addFormattedText(p, text, null);
        return p;
    }

    // ── Spacing / Indent helpers ──────────────────────────────────────────────

    private void setSpacing(XWPFParagraph para, long beforePt, long afterPt) {
        CTPPr pPr = para.getCTP().isSetPPr() ? para.getCTP().getPPr() : para.getCTP().addNewPPr();
        CTSpacing spacing = pPr.isSetSpacing() ? pPr.getSpacing() : pPr.addNewSpacing();
        spacing.setBefore(BigInteger.valueOf(beforePt * 20));
        spacing.setAfter(BigInteger.valueOf(afterPt * 20));
    }

    private void setFirstLineIndent(XWPFParagraph para, long twips) {
        CTPPr pPr = para.getCTP().isSetPPr() ? para.getCTP().getPPr() : para.getCTP().addNewPPr();
        CTInd ind = pPr.isSetInd() ? pPr.getInd() : pPr.addNewInd();
        ind.setFirstLine(BigInteger.valueOf(twips));
    }

    private void setIndent(XWPFParagraph para, long leftTwips, long firstLineTwips) {
        CTPPr pPr = para.getCTP().isSetPPr() ? para.getCTP().getPPr() : para.getCTP().addNewPPr();
        CTInd ind = pPr.isSetInd() ? pPr.getInd() : pPr.addNewInd();
        ind.setLeft(BigInteger.valueOf(leftTwips));
        if (firstLineTwips < 0) {
            ind.setHanging(BigInteger.valueOf(-firstLineTwips));
        } else {
            ind.setFirstLine(BigInteger.valueOf(firstLineTwips));
        }
    }

    // ── Utility ───────────────────────────────────────────────────────────────

    private String findEquationNumber(String latex, PaperDto paper) {
        if (paper == null || paper.getEquations() == null) return "";
        for (PaperDto.EquationDto eq : paper.getEquations()) {
            if (latex.trim().equals(eq.getLatex() != null ? eq.getLatex().trim() : ""))
                return String.valueOf(eq.getNumber());
        }
        return "";
    }

    private void setBorderSingle(CTBorder border) {
        border.setVal(STBorder.SINGLE);
        border.setSz(BigInteger.valueOf(4));
        border.setSpace(BigInteger.ZERO);
        border.setColor("000000");
    }
}

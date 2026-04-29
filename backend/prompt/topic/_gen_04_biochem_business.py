"""Generator: Biochemistry, Genetics, Business, Management — 10 topic files"""
import os; D = os.path.dirname(os.path.abspath(__file__))

TOPICS = {

"biochemistry_metabolism": """================================================================================
TOPIC GUIDE — Biochemistry & Metabolism
================================================================================
FIELD: Biochemistry, Genetics and Molecular Biology
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Biokimia, Metabolisme, Enzimologi, Biokimia Struktural, Metabolomik

ABSTRACT CHARACTERISTICS:
  200–250 words. Reports: metabolic pathway, enzyme studied, model organism/cell line/tissue,
  assay methods, quantitative findings (enzyme activity nmol/min/mg protein, metabolite
  concentration µM/mM, IC50 µM for inhibitors), statistical analysis.

INTRODUCTION ELEMENTS:
  - Metabolic pathway importance in cellular physiology and disease.
  - Enzyme/metabolite: structure, function, role in pathway.
  - Disease connection: diabetes, cancer, neurodegenerative disease metabolic dysregulation.
  - Research gap: unstudied isoform, novel inhibitor, allosteric site, metabolic flux.
  - Objectives: characterization, inhibitor screening, pathway analysis.

LITERATURE REVIEW:
  Common section name: "Background" (part of Introduction) or "Literature Review"
  - Biochemical pathway overview: glycolysis, TCA cycle, lipid metabolism, amino acid catabolism.
  - Enzyme kinetics: Michaelis-Menten (Km, Vmax), Hill coefficient (cooperativity).
  - Metabolomics approaches: targeted vs. untargeted; NMR vs. LC-MS.
  - Structural biochemistry: X-ray crystallography, cryo-EM, NMR of proteins.
  - Disease-enzyme link: hexokinase in cancer Warburg effect; AMPK in diabetes.
  Key references: Stryer (Biochemistry textbook), BRENDA enzyme database, KEGG pathway.

METHODOLOGY:
  Common section name: "Materials and Methods"
  - Sample preparation: cell lysis, protein extraction, partial purification (ammonium sulfate fractionation).
  - Protein quantification: Bradford or Lowry assay.
  - Enzyme activity assay: substrate, product measured, detection method (UV-Vis at 340nm for NADH).
  - Kinetic parameters: Lineweaver-Burk plot for Km/Vmax; Dixon plot for Ki (inhibition constant).
  - Metabolomics: LC-MS/MS or GC-MS; untargeted (HMDB database annotation); targeted (standard curves).
  - Cell culture: HepG2, MCF-7, HEK293T; DMEM + 10% FBS; 5% CO2; passage number.
  - Statistical: ANOVA, Tukey's post-hoc; IC50 by GraphPad (4-parameter logistic curve).

TYPICAL RESULTS & DISCUSSION:
  - Enzyme specific activity: typical range 0.01–10 nmol/min/mg protein (varies widely by enzyme).
  - Km values: typical 0.1–10 mM; Vmax varies by enzyme/conditions.
  - IC50 of natural product inhibitor: 10–500 µM (lower = more potent).
  - Metabolite fold-change: 2–10× between control and treatment in metabolomics.
  - Cell viability IC50: 10–200 µM for cytotoxic compounds.
  Tables: enzyme kinetic parameters, inhibition constants, metabolite concentrations.
  Figures: Lineweaver-Burk plot, dose-response curve, metabolomics heatmap/PCA.

TYPICAL FIGURES:
  - Lineweaver-Burk plot (double reciprocal).
  - Dose-response curve (log concentration vs. activity %).
  - Metabolomics: PCA score plot, heatmap (hierarchical clustering).
  - Protein structure image (from PDB).
  - Western blot image (protein expression level).

TYPICAL TABLES:
  - Kinetic parameters: Km (mM) | Vmax | Kcat | Kcat/Km | Ki by inhibitor.
  - Metabolite concentrations: metabolite | control (µM) | treatment (µM) | FC | p-value.
  - Purification table: step | total protein | total activity | specific activity | yield %.

CONCLUSION CHARACTERISTICS:
  - Characterization of enzyme or metabolite changes summarized.
  - Inhibitor potency and selectivity conclusion.
  - Disease relevance of metabolic finding.
  - Limitations: in vitro conditions, single cell line, non-physiological concentrations.
  - Future: structural determination, in vivo validation, drug development pipeline.

COMMON REFERENCE VENUES:
  Journal of Biological Chemistry, Biochemistry, FEBS Journal, Biochemical Journal,
  Metabolomics, Journal of Proteome Research, Nature Chemical Biology, PLoS ONE

DOMAIN VOCABULARY:
  Km, Vmax, Kcat, IC50, Ki, Lineweaver-Burk, specific activity, metabolomics,
  LC-MS, GC-MS, KEGG, HMDB, NMR, Western blot, Bradford assay, NADH,
  glycolysis, TCA cycle, Warburg effect, AMPK, hexokinase, lipid oxidation

METHODOLOGY KEYWORDS:
  enzyme kinetics assay, Bradford protein assay, Western blot, LC-MS/MS, GC-MS,
  untargeted metabolomics, HPLC purification, Lineweaver-Burk analysis,
  MTT cell viability assay, molecular docking (if in silico included)
""",

"molecular_genetics": """================================================================================
TOPIC GUIDE — Molecular Genetics & Genomics
================================================================================
FIELD: Biochemistry, Genetics and Molecular Biology
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Genetika Molekuler, Genomik, Transkriptomik, SNP, Mutasi, Ekspresi Gen

ABSTRACT CHARACTERISTICS:
  200–250 words. Reports: gene/variant studied, population/sample, molecular methods
  (PCR, sequencing, microarray, RNA-seq), genetic findings (allele frequency,
  OR for disease association, fold-change of gene expression, p-value).

INTRODUCTION ELEMENTS:
  - Gene function and regulatory importance.
  - Genetic basis of the disease/trait under study.
  - Population genetics context: Hardy-Weinberg, linkage disequilibrium.
  - Research gap: unstudied variant in specific population, gene-environment interaction.
  - Objectives: association study, functional characterization, expression analysis.

LITERATURE REVIEW:
  Common section name: "Background" (in Introduction) or "Literature Review"
  - Gene structure: promoter, exons, introns, UTRs, regulatory elements.
  - Common variants: SNPs (single nucleotide polymorphisms), indels, copy number variants.
  - GWAS (genome-wide association studies) findings for the phenotype.
  - Gene expression: mRNA levels (RT-qPCR), RNA-seq (DESeq2 analysis).
  - Epigenetics: DNA methylation (bisulfite sequencing), histone modifications (ChIP-seq).
  - Bioinformatics tools: GATK, PLINK, DESeq2, Ensembl, NCBI databases.

METHODOLOGY:
  Common section name: "Materials and Methods"
  - Sample collection: blood/tissue; DNA extraction (salting-out or kit-based).
  - RNA extraction: TRIzol, quality check (RIN >7.0, A260/A280 >1.8).
  - Genotyping: PCR-RFLP, real-time PCR (TaqMan), Sanger sequencing, next-generation sequencing.
  - Gene expression: RT-qPCR (2^-ΔΔCt method); RNA-seq (HISAT2 alignment, DESeq2 normalization).
  - Statistical (genetics): Hardy-Weinberg equilibrium test; chi-square or logistic regression for association; OR with 95% CI.
  - RNA-seq: DEGs defined as |log2FC| ≥1.0, adjusted p-value (FDR) <0.05.
  - Bioinformatics: pathway enrichment (GSEA, KEGG, GO), PPI network (STRING).

TYPICAL RESULTS & DISCUSSION:
  - Allele frequency: minor allele frequency (MAF) 0.10–0.35 for common SNPs.
  - Association: OR = 1.5–3.0 (p < 0.001) for moderate genetic risk.
  - Gene expression: |log2FC| = 1–3; DEGs: 50–500 in typical transcriptomic study.
  - Hardy-Weinberg: p > 0.05 in controls (equilibrium confirmed).
  - RT-qPCR: relative expression 2–5× in disease vs. control.
  Tables: genotype frequencies, OR table, top DEGs list, enriched pathways.
  Figures: volcano plot, heatmap of DEGs, pathway enrichment dot plot, LD block diagram.

TYPICAL FIGURES:
  - Volcano plot: log2FC vs. -log10(padj) for RNA-seq.
  - Heatmap: top 50 DEGs (row: genes, column: samples).
  - KEGG/GO enrichment dot plot.
  - Sanger sequencing electropherogram.
  - LD (linkage disequilibrium) block plot.
  - UMAP/t-SNE (for single-cell RNA-seq).

TYPICAL TABLES:
  - Genotype and allele frequencies: AA | Aa | aa | MAF (patients vs. controls, p-value).
  - Logistic regression: genotype model (dominant/recessive) | OR | 95%CI | p.
  - Top 20 DEGs: gene | log2FC | baseMean | padj | function annotation.

CONCLUSION CHARACTERISTICS:
  - Genetic variant/expression associated with disease confirmed or rejected.
  - Functional relevance: variant in regulatory region, splicing effect.
  - Population-specific findings.
  - Limitations: small sample, multiple testing without full GWAS power, single population.
  - Future: GWAS, functional validation (CRISPR), larger cohort.

COMMON REFERENCE VENUES:
  Human Genetics, American Journal of Human Genetics, Genetics, Nature Genetics,
  PLOS Genetics, Molecular Biology and Evolution, Genome Biology,
  Nucleic Acids Research, BMC Genomics, Bioinformatics

DOMAIN VOCABULARY:
  SNP, indel, CNV, MAF, Hardy-Weinberg, OR, logistic regression, RNA-seq,
  DEG, log2FC, padj (FDR), GWAS, KEGG, GO, STRING, TaqMan, RFLP,
  Sanger sequencing, NGS, PCR, RIN, HISAT2, DESeq2, PLINK, GATK

METHODOLOGY KEYWORDS:
  DNA extraction, RNA extraction (TRIzol), PCR-RFLP, TaqMan genotyping,
  Sanger sequencing, RNA-seq (HISAT2/DESeq2), RT-qPCR (2^-ΔΔCt), GWAS,
  GSEA, Hardy-Weinberg test, logistic regression, bioinformatics pipeline
""",

"strategic_management": """================================================================================
TOPIC GUIDE — Strategic Management
================================================================================
FIELD: Business, Management and Accounting / Management
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Manajemen Strategik, Keunggulan Kompetitif, Formulasi Strategi, Analisis Industri

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: industry/sector context, research question (competitive advantage,
  strategic alignment, firm performance), methodology (survey n, case study, SEM),
  key findings (constructs, standardized coefficients, R², p-values), theoretical contribution.

INTRODUCTION ELEMENTS:
  - Competitive landscape changes and firm performance pressures.
  - Strategic management frameworks: RBV, dynamic capabilities, competitive strategy (Porter).
  - Research gap: moderating/mediating variable, new context (digital, post-COVID), emerging market.
  - Research questions and hypotheses (H1: "X → Y, β>0, p<0.05").
  - Theoretical and practical contributions.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Resource-Based View (RBV): VRIN resources (Barney, 1991), dynamic capabilities (Teece, 1997).
  - Porter's frameworks: Five Forces (competitive dynamics), Generic Strategies (cost/differentiation/focus), Value Chain.
  - Balanced Scorecard (BSC): Kaplan & Norton (1992) — 4 perspectives.
  - Strategic leadership: CEO characteristics, TMT composition.
  - Innovation: Schumpeterian innovation, open innovation (Chesbrough), disruptive innovation (Christensen).
  - Research model: conceptual framework with hypothesized relationships.

METHODOLOGY:
  Common section name: "Research Methodology" / "Methods"
  - Research approach: quantitative (survey-SEM), qualitative (case study), or mixed-methods.
  - Survey: self-administered questionnaire; Likert scale 1–5 or 1–7; n=100–500 firms/managers.
  - Construct measurement: established scales (e.g., competitive advantage: Bharadwaj et al., 1993).
  - Sampling: purposive/snowball sampling; managers/owners of manufacturing/service firms.
  - SEM (PLS-SEM or CB-SEM): SmartPLS or AMOS software.
  - Validity/reliability: AVE >0.5, CR >0.7, Cronbach's α >0.7; discriminant validity (HTMT <0.85).
  - Model fit (CB-SEM): CFI/TLI >0.95, RMSEA <0.08, SRMR <0.08.

TYPICAL RESULTS & DISCUSSION:
  - β (standardized path coefficient): 0.15–0.55 for significant paths.
  - R² (variance explained): 0.25–0.60 for dependent construct (adequate for management research).
  - Mediation: indirect effect with BC-CI not including zero (significant mediation).
  - Moderating: interaction term β significant, change in R².
  - f² (effect size): small 0.02, medium 0.15, large 0.35.
  Tables: outer loadings, construct reliability/validity, path coefficients.
  Figures: structural model diagram with β and p-values, radar chart (BSC perspectives).

TYPICAL FIGURES:
  - Structural equation model diagram: constructs, paths, β values.
  - Bar/radar chart: BSC performance across four perspectives.
  - Scatter plot: strategy type vs. performance indicator.
  - Moderating effect plot (2-way interaction).

TYPICAL TABLES:
  - Measurement model: construct | AVE | CR | α | items.
  - Discriminant validity: HTMT matrix.
  - Structural model: H# | path | β | SE | t-stat | p | decision.
  - Respondent profile: industry | firm size | manager tenure.

CONCLUSION CHARACTERISTICS:
  - Supported/unsupported hypotheses summary.
  - Theoretical implications: contribution to RBV, dynamic capabilities, or Porter's framework.
  - Practical implications for managers/policymakers.
  - Limitations: cross-sectional, self-reporting bias, single industry.
  - Future: longitudinal study, multi-industry, multi-country comparison.

ADDITIONAL SECTIONS:
  - "Implications for Theory and Practice"
  - "Research Limitations and Future Directions"

COMMON REFERENCE VENUES:
  Strategic Management Journal, Academy of Management Journal,
  Journal of Management, Administrative Science Quarterly,
  Long Range Planning, British Journal of Management,
  Management International Review

DOMAIN VOCABULARY:
  RBV, dynamic capabilities, Porter, competitive advantage, VRIN, differentiation,
  cost leadership, BSC, value chain, five forces, TMT, SEM, PLS-SEM, CB-SEM,
  AVE, CR, Cronbach's α, HTMT, β, R², mediation, moderation, f²

METHODOLOGY KEYWORDS:
  PLS-SEM (SmartPLS), CB-SEM (AMOS), survey research, Likert scale,
  CFA (confirmatory factor analysis), path analysis, mediation analysis,
  moderation analysis, bootstrapping, purposive sampling
""",

"human_resource_management": """================================================================================
TOPIC GUIDE — Human Resource Management (HRM)
================================================================================
FIELD: Business, Management and Accounting / Management
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Manajemen SDM, Rekrutmen, Pelatihan, Kompensasi, Keterlibatan Karyawan, HRM Strategis

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: HRM practice studied, organizational context, research method
  (survey, SEM, regression), sample (n, industry), key findings (β, R², effect size),
  practical implications.

INTRODUCTION ELEMENTS:
  - HRM importance in achieving organizational performance.
  - Specific HRM challenge: talent retention, engagement, diversity, digital HRM.
  - Research gap: HRM practice → performance link in specific context (SME, public sector, emerging market).
  - Hypotheses based on theoretical model (AMO theory, SET, JD-R).

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Conceptual Framework"
  - AMO theory (Ability, Motivation, Opportunity): Appelbaum et al. (2000).
  - Social Exchange Theory (SET): Blau (1964) — reciprocity in employer-employee relationship.
  - High-Performance Work Systems (HPWS): bundle of HR practices.
  - Job Demands-Resources (JD-R) model: burnout and engagement.
  - Organizational Commitment: Meyer & Allen (1991) — affective, continuance, normative.
  - Employee engagement: Schaufeli's UWES (vigor, dedication, absorption).
  - Compensation theory: equity theory (Adams, 1963), expectancy theory (Vroom, 1964).

METHODOLOGY:
  Common section name: "Research Methodology"
  - Design: cross-sectional survey, longitudinal panel, quasi-experimental.
  - Population: employees in specific sector; stratified/random sampling.
  - Questionnaire: validated scales (UWES-9, OCQ, PERMA-V etc.); Likert 1–5 or 1–7.
  - Variables: independent (HRM practices), mediating (engagement, commitment), dependent (performance, turnover intention).
  - SEM: PLS-SEM or CB-SEM; path analysis, mediation with bootstrapping.
  - Reliability: α >0.7; Validity: CFA, AVE >0.5.

TYPICAL RESULTS & DISCUSSION:
  - Job satisfaction mean score: 3.5–4.2/5.0 (typical satisfied employees).
  - Engagement UWES: vigor 3.8–4.5; dedication 3.9–4.6; absorption 3.5–4.3.
  - HRM → Performance: β = 0.25–0.45, p<0.001 (common finding).
  - Mediation: engagement mediates HRM → performance (indirect β=0.15, BC-CI excludes 0).
  - Turnover intention: negatively related to engagement (β = -0.35 to -0.50).
  Tables: descriptive stats, correlation matrix, path coefficients.
  Figures: SEM diagram, mediation plot, bar chart of HRM practices effectiveness.

TYPICAL FIGURES:
  - SEM/path diagram with β values and significance stars.
  - Bar chart: mean scores of HRM practices by group.
  - Mediation visualization diagram.
  - Correlation heatmap.

TYPICAL TABLES:
  - Descriptive statistics and correlation matrix (mean, SD, r).
  - SEM path coefficients: β | SE | t | p | 95%CI.
  - Mediation analysis: direct | indirect | total effect.

CONCLUSION CHARACTERISTICS:
  - Which HRM practices most significantly predict performance/engagement.
  - Practical implications for HR managers and organizations.
  - Limitations: self-report, cross-sectional, single industry.
  - Future: longitudinal study, multi-level HRM research, digital HRM.

COMMON REFERENCE VENUES:
  Human Resource Management, Journal of Applied Psychology,
  International Journal of Human Resource Management,
  Journal of Organizational Behavior, Personnel Psychology,
  Human Resource Management Review, Academy of Management Review

DOMAIN VOCABULARY:
  HRM, HPWS, AMO theory, SET, JD-R, engagement, commitment, turnover intention,
  UWES, OCQ, job satisfaction, training, compensation, recruitment, retention,
  talent management, performance appraisal, HR metrics

METHODOLOGY KEYWORDS:
  PLS-SEM, CB-SEM, CFA, Cronbach's alpha, survey research, mediation,
  moderation, UWES measurement, correlation analysis, logistic regression
""",

"operations_management": """================================================================================
TOPIC GUIDE — Operations Management & Supply Chain
================================================================================
FIELD: Business, Management and Accounting / Management
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Manajemen Operasi, Rantai Pasokan, Logistik, Lean, Six Sigma, Kualitas

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: industry/process context, operations problem studied
  (waste, delay, quality defect), methodology (lean analysis, simulation, SEM, case study),
  key findings (cycle time reduction %, defect rate ppm, OEE %, cost savings IDR/USD).

INTRODUCTION ELEMENTS:
  - Operational efficiency challenges in the industry/sector.
  - Specific problem: waste in production, supply chain disruption, quality failure.
  - Research gap: application in new industry context, lean tools not yet applied, digital SCM.
  - Objectives and expected contributions.

LITERATURE REVIEW:
  Common section name: "Literature Review"
  - Lean manufacturing: 7 wastes (TIM WOOD), value stream mapping, 5S, Kaizen.
  - Six Sigma: DMAIC methodology, process capability (Cp, Cpk), DPMO, sigma level.
  - Total Quality Management (TQM): Deming's 14 points, Juran's quality trilogy, EFQM.
  - Supply chain: SCOR model, demand forecasting (ARIMA, exponential smoothing), bullwhip effect.
  - Inventory management: EOQ model, safety stock calculation, ABC analysis.
  - Industry 4.0/5.0: IoT in production, smart supply chain, predictive maintenance.

METHODOLOGY:
  Common section name: "Research Methodology" / "Methods"
  - Case study or empirical study in specific company/industry.
  - Data collection: process observation, time study (time and motion), document analysis.
  - Tools: VSM (Value Stream Mapping), SIPOC diagram, Pareto chart, fishbone (Ishikawa).
  - Statistical process control: control charts (X̄-R, p-chart), process capability indices.
  - Simulation: Arena/Simul8/AnyLogic discrete event simulation.
  - Survey (if supply chain study): SEM, structural equation model with supply chain performance constructs.

TYPICAL RESULTS & DISCUSSION:
  - OEE (Overall Equipment Effectiveness): world class >85%; typical manufacturing 40–65%.
  - Defect rate: before lean intervention 5–15%; after 1–3%.
  - Cycle time reduction: 20–40% after VSM implementation.
  - DPMO: Six Sigma target <3.4; typical pre-improvement 5000–50000 DPMO.
  - Sigma level: 3σ = 66,807 DPMO; 4σ = 6,210; 5σ = 233; 6σ = 3.4.
  Tables: VSM current vs. future state metrics, defect classification, control chart data.
  Figures: VSM current/future state, Pareto chart, control charts, OEE trend.

TYPICAL FIGURES:
  - Value Stream Map (current and future state).
  - Pareto chart: defect types by frequency/impact.
  - Control chart: X̄-R chart or p-chart.
  - OEE trend before/after intervention.
  - Fishbone (Ishikawa) diagram.

TYPICAL TABLES:
  - Process metrics: cycle time | value-added time | takt time | WIP.
  - Quality metrics: defect rate | DPMO | sigma level | Cp | Cpk.
  - Before/after comparison: metric | before | after | improvement %.

CONCLUSION CHARACTERISTICS:
  - Operational improvements achieved with quantified results.
  - Practical contribution: lean/Six Sigma tool applicability in the context.
  - Limitations: single company, short observation period, seasonal effects.
  - Future: full supply chain implementation, digital lean, simulation-based optimization.

COMMON REFERENCE VENUES:
  International Journal of Production Economics, Journal of Operations Management,
  International Journal of Operations & Production Management,
  Supply Chain Management: An International Journal, Production Planning & Control,
  Journal of Manufacturing Systems, International Journal of Lean Six Sigma

DOMAIN VOCABULARY:
  OEE, lean, VSM, 5S, kaizen, Six Sigma, DMAIC, DPMO, Cp, Cpk, sigma level,
  TQM, SCOR, EOQ, bullwhip effect, JIT, kanban, takt time, cycle time, WIP,
  Pareto, fishbone, FMEA, SPC, control chart, supply chain

METHODOLOGY KEYWORDS:
  value stream mapping, time study, statistical process control, control charts,
  process capability analysis, discrete event simulation, ABC analysis,
  DMAIC, SIPOC, FMEA, SEM survey (supply chain performance)
""",

"digital_marketing_v2": """================================================================================
TOPIC GUIDE — Digital Marketing & Consumer Behavior (Digital)
================================================================================
FIELD: Business, Management and Accounting / Marketing
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Pemasaran Digital, Media Sosial, E-Commerce, Perilaku Konsumen Digital, SEO/SEM

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: digital platform context (Instagram, TikTok, marketplace),
  constructs studied (brand awareness, purchase intention, electronic WOM, trust),
  method (SEM, survey, experiment), sample (n, millennials/gen-Z), key findings (β, R²).

INTRODUCTION ELEMENTS:
  - Digital transformation of marketing: online consumers (5.0B+ globally).
  - Specific digital channel/behavior: social media influence, eWOM, influencer marketing.
  - Theoretical basis: TAM (Technology Acceptance Model), S-O-R framework, TRA, TPB.
  - Research gap: specific platform not studied, new construct, Indonesian/Asian market.
  - Hypotheses: "eWOM positively influences purchase intention (H1)."

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Technology Acceptance Model (TAM): Davis (1989) — perceived usefulness, ease of use.
  - Theory of Planned Behavior (TPB): Ajzen (1991).
  - S-O-R model: stimulus-organism-response.
  - eWOM (electronic word of mouth): credibility, valence, volume.
  - Social media marketing (SMM) dimensions: content, interactivity, community, entertainment.
  - Trust in e-commerce: security, privacy, reputation.
  - Influencer marketing: parasocial relationship, source credibility.

METHODOLOGY:
  Common section name: "Research Methodology"
  - Quantitative survey; online questionnaire (Google Forms/Qualtrics).
  - Sample: millennial/gen-Z consumers; purposive sampling (social media users).
  - Measurement: validated multi-item scales (3–5 items per construct), Likert 1–5.
  - SEM: PLS-SEM (SmartPLS); bootstrapping 5000 samples for significance.
  - Validity: outer loading >0.7, AVE >0.5, HTMT <0.85.
  - Reliability: CR >0.7, Cronbach's α >0.7.
  - Common method bias: Harman's single factor test.

TYPICAL RESULTS & DISCUSSION:
  - Purchase intention R² = 0.40–0.65 (well-explained by digital marketing constructs).
  - SMM → Purchase intention: β = 0.30–0.50, significant.
  - eWOM → Trust: β = 0.25–0.45.
  - Influencer credibility → Purchase intention: β = 0.20–0.40.
  - Moderating effect of brand attitude: R² change = 0.03–0.08.
  Tables: reliability/validity table, path coefficients, mediation results.
  Figures: SEM path diagram, bar chart of construct means, moderation plot.

TYPICAL FIGURES:
  - PLS-SEM path diagram.
  - Moderation effect plot (interaction effect visualization).
  - Bar chart: construct means across groups (gender, platform).
  - Importance-Performance Map Analysis (IPMA).

TYPICAL TABLES:
  - Construct reliability and validity: AVE | CR | α | items.
  - Path coefficients: β | SE | t | p | H decision.
  - Discriminant validity: HTMT matrix.

CONCLUSION CHARACTERISTICS:
  - Key digital marketing constructs driving purchase intention/brand loyalty.
  - Platform-specific implications (TikTok vs. Instagram strategies).
  - Managerial implications: digital content strategy.
  - Limitations: single platform, convenience sampling, cross-sectional.
  - Future: multi-platform, longitudinal, neuromarketing.

COMMON REFERENCE VENUES:
  Journal of Marketing, Journal of Interactive Marketing, Computers in Human Behavior,
  Journal of Business Research, Information & Management,
  Electronic Commerce Research and Applications, Internet Research

DOMAIN VOCABULARY:
  TAM, S-O-R, TPB, eWOM, influencer, SMM, brand awareness, purchase intention,
  trust, perceived usefulness, UGC, engagement rate, CTR, ROAS, SEO, SEM,
  PLS-SEM, AVE, HTMT, outer loading, bootstrapping, moderation

METHODOLOGY KEYWORDS:
  PLS-SEM (SmartPLS), online survey, CFA, bootstrapping, HTMT criterion,
  Harman's single factor, IPMA, moderation analysis, mediation analysis
""",

"financial_accounting": """================================================================================
TOPIC GUIDE — Financial Accounting
================================================================================
FIELD: Business, Management and Accounting / Accounting
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Akuntansi Keuangan, Pelaporan Keuangan, IFRS/PSAK, Audit, Konservatisme

ABSTRACT CHARACTERISTICS:
  150–200 words. Reports: accounting phenomenon (earnings management, conservatism,
  disclosure quality), sample (n firms, industry, years), empirical method (panel regression),
  key findings (coefficient, t-statistic, significance level, R²).

INTRODUCTION ELEMENTS:
  - Financial reporting quality and its role in capital markets.
  - Specific issue: earnings management (accruals), conservatism, disclosure, sustainability reporting.
  - Agency theory foundation: separation of ownership and control.
  - Research gap: IFRS adoption effect in emerging market, specific industry not studied.
  - Hypotheses (H1–H4) with theoretical basis.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Agency theory (Jensen & Meckling, 1976): information asymmetry, contracting.
  - Signaling theory (Spence, 1973): voluntary disclosure.
  - Earnings management: accrual-based (Jones, 1991; Modified Jones model), real activities (Roychowdhury, 2006).
  - Conservatism: Basu (1997) model, goodwill impairment.
  - IFRS adoption effects: comparability, relevance, timeliness.
  - Audit quality: Big 4 vs. non-Big 4, auditor independence, audit fees.
  - Corporate governance: board independence, managerial ownership, institutional ownership.

METHODOLOGY:
  Common section name: "Research Method" / "Methodology"
  - Sample: publicly listed firms (IDX / NYSE), industry, year range (3–10 years panel).
  - Data source: financial statements (annual reports), Bloomberg, COMPUSTAT, Indonesia Stock Exchange.
  - Dependent variable: discretionary accruals (Modified Jones model), earnings quality (Dechow-Dichev).
  - Independent variables: firm size (ln assets), leverage, ROA, growth, board size, audit quality.
  - Model: panel data regression (FE/RE, Hausman test); OLS with robust SE.
  - Endogeneity control: instrumental variable (IV), 2SLS, GMM if dynamic panel.

TYPICAL RESULTS & DISCUSSION:
  - Discretionary accruals: mean ~ 0.02–0.05 of total assets; range -0.20 to +0.20.
  - Audit quality (Big 4): negative association with DA, β = -0.030 to -0.060, p<0.05.
  - Firm size: negative DA association (larger firms less earnings management).
  - ROA: positive DA (income-increasing when profitable).
  - R² (within): 15–35% typical for accounting panel studies.
  Tables: descriptive stats, Pearson correlation, regression results.
  Figures: time series of mean DA, scatter plot (DA vs. leverage).

TYPICAL FIGURES:
  - Time series: mean discretionary accruals per year.
  - Scatter plot: leverage vs. discretionary accruals.
  - Box plot: DA by audit quality (Big 4 vs. non-Big 4).

TYPICAL TABLES:
  - Descriptive statistics (mean | SD | min | max | n).
  - Pearson correlation matrix.
  - Panel regression results: variable | coeff | SE | t-stat | p-value.
  - Robustness tests (alternative model specification).

CONCLUSION CHARACTERISTICS:
  - Relationship between corporate governance/audit quality and earnings quality confirmed.
  - Implications for standard setters, auditors, investors.
  - Limitations: emerging market only, accrual measure limitations.
  - Future: real activities manipulation, sustainability accounting, textual analysis.

COMMON REFERENCE VENUES:
  The Accounting Review, Journal of Accounting and Economics,
  Journal of Accounting Research, Accounting, Organizations and Society,
  European Accounting Review, Journal of Financial Reporting,
  Journal of Contemporary Accounting & Economics

DOMAIN VOCABULARY:
  discretionary accruals, Modified Jones model, Big 4, conservatism, IFRS, PSAK,
  agency theory, signaling theory, board independence, leverage, ROA, firm size,
  Hausman test, fixed effects, random effects, GMM, 2SLS, earnings quality

METHODOLOGY KEYWORDS:
  Modified Jones model, Dechow-Dichev model, panel data regression (FE/RE),
  Hausman test, GMM, 2SLS, OLS with robust SE, Pearson correlation,
  Basu asymmetric timeliness model, financial statement analysis
""",

"corporate_finance_v2": """================================================================================
TOPIC GUIDE — Corporate Finance
================================================================================
FIELD: Business, Management and Accounting / Finance
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Keuangan Korporat, Struktur Modal, Dividen, Nilai Perusahaan, Merger & Akuisisi

ABSTRACT CHARACTERISTICS:
  150–200 words. Reports: firm-level study, financial variable (capital structure, dividend policy,
  firm value Tobin's Q, ROE, ROA), sample (n firms, years), methodology (panel regression,
  event study), key coefficients and significance.

INTRODUCTION ELEMENTS:
  - Capital market efficiency and corporate financing decisions.
  - Specific finance problem: optimal capital structure, dividend signaling, M&A value creation.
  - Theoretical foundations: M&M theorem, Trade-off theory, Pecking Order theory.
  - Research gap: specific industry, market, or context not studied.
  - Hypotheses based on chosen theory.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - M&M Theorem (Modigliani & Miller, 1958): capital structure irrelevance under perfect markets.
  - Trade-Off Theory: optimal debt-equity balancing tax shield vs. financial distress costs.
  - Pecking Order Theory (Myers & Majluf, 1984): internal > debt > equity financing preference.
  - Dividend policy: signaling hypothesis (Bhattacharya, 1979), bird-in-hand.
  - Firm valuation: Tobin's Q = Market Value / Book Value of Assets; PBV, P/E ratio.
  - Agency cost theory: debt as disciplining tool; free cash flow hypothesis (Jensen, 1986).
  - M&A: synergy hypothesis, market reaction (abnormal returns from event study).

METHODOLOGY:
  Common section name: "Research Method" / "Methodology"
  - Sample: publicly listed manufacturing/banking/property firms; 5–10 year panel.
  - Data: IDX/Bloomberg/COMPUSTAT; annual reports.
  - Dependent variables: firm value (Tobin's Q, PBV), profitability (ROE, ROA), stock return.
  - Independent: leverage (DER), dividend payout ratio, firm size, growth, liquidity.
  - Model: panel data regression (FE/RE); Hausman test; OLS, 2SLS.
  - Event study (M&A): CAR = cumulative abnormal return = ΣAR around event window.
  - Event window: typically [-5, +5] or [-1, +1] days around announcement.

TYPICAL RESULTS & DISCUSSION:
  - Tobin's Q: manufacturing <1.5; banking 1.0–2.0; tech firms >2.0.
  - DER (debt-equity ratio): manufacturing 0.5–2.0; optimal level per trade-off theory.
  - Leverage → Firm value: curvilinear (inverted U-shape) or negative at high debt.
  - ROE: manufacturing 8–15%; banking 12–20%.
  - CAR in M&A announcement window: acquirer -1% to +3%; target +15 to +30%.
  Tables: descriptive stats, correlation, panel regression, event study CAR.
  Figures: leverage distribution box plot, Tobin's Q vs. DER scatter, CAR event window plot.

TYPICAL FIGURES:
  - Scatter plot: DER vs. Tobin's Q.
  - Event study: CAR cumulative abnormal return plot over event window.
  - Box plot: financial ratios by industry sector.
  - Time series: mean leverage and Tobin's Q over study period.

TYPICAL TABLES:
  - Descriptive statistics (financial ratios).
  - Hausman test result.
  - Panel regression: variable | coeff | SE | t | p (FE and RE results).

CONCLUSION CHARACTERISTICS:
  - Financial structure determinants of firm value identified.
  - Theory supported (Trade-off vs. Pecking Order).
  - Managerial implications: optimal debt level, dividend policy.
  - Limitations: single country, accounting data (not market microstructure), endogeneity.
  - Future: dynamic panel GMM, behavioral finance angle, ESG integration.

COMMON REFERENCE VENUES:
  Journal of Finance, Journal of Financial Economics,
  Review of Financial Studies, Journal of Corporate Finance,
  Financial Management, Pacific-Basin Finance Journal,
  International Review of Financial Analysis

DOMAIN VOCABULARY:
  Tobin's Q, DER, leverage, capital structure, ROE, ROA, M&M theorem, trade-off theory,
  pecking order, dividend payout, PBV, CAR, event study, abnormal return,
  agency theory, free cash flow, panel regression, FE, RE, Hausman test, GMM

METHODOLOGY KEYWORDS:
  panel data regression, Hausman test, GMM (dynamic panel), event study,
  CAR calculation (market model), Tobin's Q, Brown & Warner method,
  2SLS instrumental variable, OLS with clustered SE
""",

}

def write_topic(name, content):
    path = os.path.join(D, f"{name}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.lstrip())
    print(f"  wrote {name}.txt")

for name, content in TOPICS.items():
    write_topic(name, content)
print(f"gen_04: {len(TOPICS)} topics written.")

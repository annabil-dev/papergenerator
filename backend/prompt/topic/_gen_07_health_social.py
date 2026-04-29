"""Generator: Nursing, Pharmacology, Public Health, Psychology, Social Sciences — 10 topic files"""
import os; D = os.path.dirname(os.path.abspath(__file__))

TOPICS = {

"clinical_nursing": """================================================================================
TOPIC GUIDE — Clinical Nursing
================================================================================
FIELD: Nursing / Health Sciences
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Keperawatan Klinik, ICU, Perawatan Luka, Asuhan Keperawatan, Keperawatan Medikal Bedah

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: patient population (n, diagnosis, ward), nursing intervention or care
  practice, study design, outcome measures (pain scale NRS/VAS, wound healing rate, LOS days,
  patient satisfaction score, nursing knowledge score), statistical results.

INTRODUCTION ELEMENTS:
  - Clinical nursing problem: pain management, wound care, patient safety, infection control.
  - Patient burden and nurse-sensitive outcomes.
  - Gap in current practice: evidence-based care not implemented, inconsistent protocol.
  - Research objectives: evaluate nursing intervention effectiveness.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Nursing theoretical models: Gordon's Functional Health Patterns, Henderson's 14 needs, Orem's self-care.
  - Pain assessment tools: NRS (0–10), VAS (0–100mm), FLACC (children), BPS (ICU non-verbal).
  - Wound care: TIME framework (Tissue, Infection, Moisture, Edge), wound healing stages.
  - Patient safety: 6 National Patient Safety Goals (NPSG), falls prevention, medication errors.
  - Nursing care plan: NANDA-I diagnoses, NIC interventions, NOC outcomes.
  - Evidence-based practice: PICO framework, levels of evidence (I–VII).

METHODOLOGY:
  Common section name: "Research Method" / "Methods"
  - Design: quasi-experimental (pre-post), RCT, descriptive correlational, case study.
  - Setting: hospital ward (surgical, medical, ICU), community health center.
  - Sample: patient/nurse population; purposive/random sampling; inclusion/exclusion criteria.
  - Nursing intervention: specific protocol (wound dressing change frequency, positioning, oral care).
  - Instruments: validated pain scales, satisfaction questionnaire (KQCAH), SF-36, observation checklist.
  - Data collection: direct observation, patient interview, medical record review.
  - Statistical: paired t-test (pre-post), Mann-Whitney U, chi-square; α = 0.05.
  - Ethical: informed consent, Helsinki declaration, hospital ethics committee.

TYPICAL RESULTS & DISCUSSION:
  - Pain NRS: preintervention 7–8/10; postintervention 3–4/10 (p<0.001).
  - Wound healing: control 14–21 days; experimental 10–14 days.
  - LOS (length of stay): standard care 7–10 days; improved protocol 5–7 days.
  - Patient satisfaction: mean 3.8–4.5/5.0 (mostly satisfied).
  - Nursing knowledge pre: 60–70%; post-training: 85–95%.
  Tables: pre-post comparison table, demographic characteristics, intervention details.
  Figures: pain score change bar chart, wound healing photo series, satisfaction radar.

TYPICAL FIGURES:
  - Bar chart/box plot: pain score before and after intervention.
  - Wound healing photo series (Day 0, Day 7, Day 14).
  - Bar chart: patient satisfaction scores by dimension.
  - Nursing knowledge pre-post test score comparison.

TYPICAL TABLES:
  - Demographic characteristics: age | sex | diagnosis | LOS | comorbidities.
  - Outcome comparison: variable | pre (mean ± SD) | post | p-value.
  - Wound assessment: wound size cm² | exudate | wound edge | granulation tissue.

CONCLUSION CHARACTERISTICS:
  - Nursing intervention significantly improved clinical outcomes.
  - Practical implementation recommendation for ward protocols.
  - Limitations: single site, small sample, no control group (in some designs).
  - Future: multicenter RCT, long-term follow-up, cost-effectiveness analysis.

COMMON REFERENCE VENUES:
  Journal of Clinical Nursing, Nursing Research, International Journal of Nursing Studies,
  Wound Repair and Regeneration, American Journal of Critical Care,
  Journal of Advanced Nursing, Nurse Education Today

DOMAIN VOCABULARY:
  NRS, VAS, FLACC, BPS, NANDA-I, NIC, NOC, PICO, LOS, NPSG, KQCAH,
  wound debridement, dressing, colostomy, pressure ulcer, VAP, CAUTI,
  evidence-based practice, nursing care plan, patient-centered care, ICU

METHODOLOGY KEYWORDS:
  quasi-experimental pre-post design, RCT, pain scale assessment, wound measurement,
  PICO framework, paired t-test, Mann-Whitney U, chi-square, Wilcoxon,
  direct observation, medical record review, informed consent
""",

"pharmacology": """================================================================================
TOPIC GUIDE — Pharmacology & Drug Research
================================================================================
FIELD: Pharmacology, Toxicology and Pharmaceutics
DEFAULT CITATION STYLE: APA or Vancouver
SUBDISCIPLINE: Farmakologi, Farmakokinetik, Farmakodinamik, Farmasi Klinis, Penemuan Obat

ABSTRACT CHARACTERISTICS:
  200–250 words. Reports: drug/compound studied, biological target, study model
  (in vitro cell line, in vivo animal, clinical), endpoints (IC50 µM, ED50 mg/kg,
  LD50 mg/kg, Cmax ng/mL, t1/2 h, AUC ng·h/mL, protein binding %).

INTRODUCTION ELEMENTS:
  - Disease target and current therapeutic gap.
  - Mechanism of drug action: target receptor/enzyme, signaling pathway.
  - Pharmacological rationale for study (potency, selectivity, toxicity issues of existing drugs).
  - Research objectives: evaluate efficacy, determine mechanism, characterize PK parameters.

LITERATURE REVIEW:
  Common section name: "Background" / "Literature Review"
  - Receptor pharmacology: agonist/antagonist, dose-response relationship, therapeutic index.
  - Drug classes: antibiotics (mechanism, resistance), antihypertensives, antidiabetics, anticancer.
  - Natural products: alkaloids, flavonoids, terpenoids as lead compounds.
  - Pharmacokinetics (PK): ADME (absorption, distribution, metabolism, excretion).
  - PK parameters: Cmax, Tmax, t1/2, AUC, bioavailability (F%), volume of distribution (Vd), clearance (CL).
  - Toxicology: LD50, NOAEL, hERG channel safety, hepatotoxicity (ALT/AST elevation).

METHODOLOGY:
  Common section name: "Materials and Methods"
  In vitro:
  - Cell lines: VERO, HepG2, HeLa, MCF-7, RAW264.7 (ATCC); culture conditions.
  - MTT/MTS assay for IC50: serial dilution, 72h incubation, absorbance at 570nm.
  - Enzyme inhibition: fluorometric/colorimetric assay; IC50, Ki determination.
  - Receptor binding: radioligand binding assay, Ki (nM) calculation.
  In vivo (animal):
  - Species: Wistar rat (200–250g), BALB/c mouse; ethical approval (IACUC/ACEC).
  - Dose: ED50 estimated from dose-response; range 10–200 mg/kg oral/i.p.
  - PK study: blood sampling at 0, 0.25, 0.5, 1, 2, 4, 8, 24h post-dose.
  - Plasma analysis: LC-MS/MS quantification; PK modeling (non-compartmental: Phoenix WinNonlin).
  - Toxicology: acute LD50 (limit test 2000 mg/kg), sub-chronic 28-day; hematology, histopathology.
  - Statistical: ANOVA, Dunnett's test, GraphPad Prism; p<0.05.

TYPICAL RESULTS & DISCUSSION:
  - IC50: potent natural product 1–50 µM; drug candidate <1 µM.
  - LD50: high safety margin >2000 mg/kg (oral) in rodents.
  - PK (oral rat): Cmax 500–2000 ng/mL; t1/2 2–8h; F% 20–60%.
  - ED50: anti-inflammatory 10–50 mg/kg; analgesic 5–30 mg/kg.
  - hERG IC50: safety threshold >30µM (>30× therapeutic concentration).
  Tables: IC50 comparison by compound, PK parameter table, histopathology summary.
  Figures: dose-response curve (sigmoidal), PK time-concentration curve, histopathology images.

TYPICAL FIGURES:
  - Sigmoidal dose-response curve with IC50.
  - PK concentration-time curve (mean ± SD).
  - Histopathology images: liver, kidney (H&E stain) at treatment doses.
  - Bar chart: enzyme activity % inhibition by compound concentration.
  - Docking visualization (molecular docking of compound in binding site).

TYPICAL TABLES:
  - IC50 by compound (comparison with reference drug).
  - PK parameters: Cmax | Tmax | t1/2 | AUC0-inf | F% | Vd | CL.
  - Acute toxicity: dose | mortality | observation (LD50 estimate).
  - Hematology and clinical chemistry (mean ± SD vs. control).

CONCLUSION CHARACTERISTICS:
  - Compound showed X-fold more potent/selective than reference.
  - PK profile supports once/twice daily dosing.
  - Safety margin adequate: TI (therapeutic index) >10.
  - Limitations: in vitro to in vivo extrapolation, single animal species.
  - Future: lead optimization, formulation development, Phase I clinical trial.

COMMON REFERENCE VENUES:
  Journal of Medicinal Chemistry, European Journal of Pharmacology,
  British Journal of Pharmacology, Drug Metabolism and Pharmacokinetics,
  Pharmaceutical Research, Biochemical Pharmacology, Toxicology Letters,
  Journal of Ethnopharmacology, Natural Product Research

DOMAIN VOCABULARY:
  IC50, ED50, LD50, Cmax, Tmax, t1/2, AUC, F%, Vd, CL, ADME, hERG,
  MTT assay, dose-response, agonist, antagonist, therapeutic index, NOAEL,
  LC-MS/MS, Phoenix WinNonlin, non-compartmental PK, histopathology, IACUC

METHODOLOGY KEYWORDS:
  MTT/MTS cell viability assay, enzyme inhibition assay, radioligand binding,
  oral/intraperitoneal dosing, blood sampling PK study, LC-MS/MS quantification,
  non-compartmental analysis (NCA), ANOVA with Dunnett's, histopathology (H&E)
""",

"public_health_epidemiology": """================================================================================
TOPIC GUIDE — Public Health & Epidemiology
================================================================================
FIELD: Medicine / Public Health
DEFAULT CITATION STYLE: Vancouver or APA
SUBDISCIPLINE: Kesehatan Masyarakat, Epidemiologi, Promosi Kesehatan, Gizi Masyarakat, One Health

ABSTRACT CHARACTERISTICS:
  200–250 words (structured for epidemiological studies). Reports: study design
  (cross-sectional/cohort/case-control), population, prevalence/incidence, risk factors
  (OR or RR with 95% CI, p-value), and public health implications.

INTRODUCTION ELEMENTS:
  - Burden of disease in population (national/regional incidence/prevalence from national statistics).
  - Social determinants of health: poverty, education, access to care, environmental factors.
  - Research gap: local data lacking, risk factor profile for specific subpopulation.
  - Public health program implication.
  - Study objectives: describe, analyze, evaluate.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Epidemiological triangle: host, agent, environment.
  - Epidemiological measures: incidence rate, prevalence, AR (attack rate), CFR (case fatality rate).
  - Study designs: cross-sectional (prevalence), cohort (incidence, RR), case-control (OR).
  - Causal inference: Bradford Hill criteria, DAG (directed acyclic graph).
  - Health behavior theories: HBM (Health Belief Model), TTM (Transtheoretical Model), TPB.
  - Nutritional epidemiology: dietary assessment (24h recall, FFQ), stunting, obesity, malnutrition.
  - Vector-borne diseases: dengue, malaria, entomological surveillance.

METHODOLOGY:
  Common section name: "Materials and Methods" / "Study Design"
  - Design: cross-sectional (prevalence study), case-control, cohort.
  - Population and sampling: community/clinic-based; random sampling; sample size calculation (Lemeshow formula or Raosoft).
  - Data collection: structured questionnaire, anthropometric measurement (weight, height), blood specimen.
  - Variables: independent (risk factor), dependent (disease/outcome), confounders.
  - Laboratory: blood glucose, lipid panel, hemoglobin, urine analysis.
  - Statistical: chi-square (bivariate), logistic regression (multivariate); OR | 95% CI | p-value.
  - Confounding control: adjustment in logistic regression; stratification.

TYPICAL RESULTS & DISCUSSION:
  - Prevalence: hypertension 25–35%; diabetes 6–10%; stunting 20–37% (varies by region).
  - Risk factors with OR: smoking → hypertension OR 2.1 (1.6–2.8); obesity OR 3.5 (2.5–5.0).
  - Adjusted OR after confounder control typically lower than crude OR.
  - Coverage: immunization coverage >80% target; actual 70–90%.
  - Response rate: >80% typical for community surveys.
  Tables: demographic profile, bivariate analysis, multivariate logistic regression.
  Figures: bar chart prevalence, forest plot OR, age-sex pyramid, disease mapping.

TYPICAL FIGURES:
  - Bar chart: disease prevalence by age group / sex / area.
  - Forest plot: risk factors and their OR (95% CI).
  - Age-sex population pyramid.
  - Disease incidence map (choropleth).
  - Line graph: trend over years.

TYPICAL TABLES:
  - Demographic characteristics (n, %).
  - Bivariate analysis: variable | cases n(%) | controls n(%) | OR | 95%CI | p.
  - Multivariate logistic regression: variable | adjusted OR | 95%CI | p.

CONCLUSION CHARACTERISTICS:
  - Prevalence/incidence of condition described with context.
  - Key risk factors identified with strength of association.
  - Public health implications: targeted intervention, policy recommendation.
  - Limitations: cross-sectional causality, recall bias, single area.
  - Future: longitudinal follow-up, intervention study, multi-site.

COMMON REFERENCE VENUES:
  American Journal of Public Health, Bulletin of the World Health Organization,
  International Journal of Epidemiology, Epidemiology & Infection,
  BMC Public Health, PLoS ONE, Lancet Public Health,
  Journal of Epidemiology and Community Health, Asia Pacific Journal of Public Health

DOMAIN VOCABULARY:
  OR, RR, AR, CFR, incidence, prevalence, cohort, case-control, cross-sectional,
  logistic regression, chi-square, HBM, TTM, stunting, wasting, obesity,
  determinants, Bradford Hill, DAG, confounding, effect modification, selection bias

METHODOLOGY KEYWORDS:
  cross-sectional survey, case-control study, cohort study, sample size (Lemeshow),
  structured interview, 24h dietary recall, FFQ, anthropometric measurement,
  logistic regression, chi-square, Lemeshow goodness-of-fit, stratified analysis
""",

"clinical_psychology": """================================================================================
TOPIC GUIDE — Clinical Psychology
================================================================================
FIELD: Psychology / Clinical Psychology
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Psikologi Klinis, Intervensi, Kesehatan Mental, Terapi, Penilaian Psikologis

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: clinical condition, sample (n, diagnosis method), intervention
  (psychotherapy type, CBT/DBT/ACT, n sessions), outcome measures (BDI, BAI, DASS-21,
  PHQ-9, GAD-7, PCL-5, reduction %), pre-post comparison, effect size (Cohen's d).

INTRODUCTION ELEMENTS:
  - Prevalence and impact of the clinical condition.
  - Psychopathology: etiology, cognitive-behavioral model, neurobiological correlates.
  - Current evidence-based treatments and their limitations (access, cost, resistance).
  - Research gap: specific population, culture-adapted intervention, new delivery mode.
  - Objectives: evaluate efficacy, identify predictors of treatment response.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Introduction"
  - Theoretical model: cognitive model of depression (Beck), cognitive model of anxiety (Clark & Wells), trauma model (Foa).
  - Cognitive distortions: overgeneralization, catastrophizing, all-or-nothing thinking.
  - Evidence-based treatments: CBT, DBT, ACT, EMDR (for PTSD), IPT.
  - Assessment instruments: BDI-II, BAI, DASS-21, PHQ-9, GAD-7, PTSD Checklist (PCL-5), MMPI-2, WAIS-IV.
  - Effect size conventions: d<0.2 trivial; 0.2–0.5 small; 0.5–0.8 medium; >0.8 large.
  - Psychological first aid, crisis intervention, telepsychology.

METHODOLOGY:
  Common section name: "Method"
  - Design: RCT, quasi-experimental pre-post, single case experimental design (SCED), case series.
  - Diagnostic: structured interview (MINI, SCID-5/DSM-5 criteria), or self-report screening.
  - Sample: clinical population (outpatient/inpatient); age range; severity level.
  - Intervention: therapy type (individual/group), number of sessions (8–20 sessions), frequency.
  - Assessment: pre-treatment, mid-treatment, post-treatment, follow-up (3–6 months).
  - Measures: validated scales in local language (Indonesian BDI-II, DASS-21, PHQ-9).
  - Statistical: paired t-test, Wilcoxon, repeated measures ANOVA; effect size Cohen's d = (M1-M2)/SDpooled.
  - Multiple comparison correction: Bonferroni if multiple outcomes.

TYPICAL RESULTS & DISCUSSION:
  - BDI-II: minimal <14; mild 14–19; moderate 20–28; severe ≥29. Pre: 28–35; Post: 10–15.
  - DASS-21 total: severe range 43–63; with treatment reduction to mild (28–42).
  - PHQ-9: pre 15–20 (moderate-severe); post 5–8 (mild).
  - Effect size Cohen's d: CBT for depression d = 0.7–1.2 (medium to large).
  - Remission rate: 50–70% after 16 sessions CBT.
  - Clinically significant change: 50% or more reduction in symptom score.
  Tables: pre-post scores with SD, effect sizes, response/remission rates.
  Figures: symptom score change over sessions, individual trajectories, effect size bar chart.

TYPICAL FIGURES:
  - Line graph: mean symptom score over assessment points.
  - Bar chart: pre vs. post score with significance markers.
  - Box plot: score distribution by group or time point.
  - Effect size forest plot (if meta-analysis).
  - Individual trajectory lines (single-case design).

TYPICAL TABLES:
  - Demographic characteristics: n | sex | mean age | diagnosis | severity.
  - Pre-post scores: measure | pre (mean ± SD) | post | p | Cohen's d | 95%CI.
  - Response/remission: group | responders n(%) | remitters n(%) | chi-square.

CONCLUSION CHARACTERISTICS:
  - Intervention significantly reduced symptom severity with medium-large effect.
  - Remission/response rates comparable to or exceeding benchmarks.
  - Clinical and theoretical implications.
  - Limitations: no control group, therapist allegiance, population specificity.
  - Future: RCT with active control, digital delivery, mechanism study (mediation).

COMMON REFERENCE VENUES:
  Journal of Consulting and Clinical Psychology, Behaviour Research and Therapy,
  Cognitive Therapy and Research, Clinical Psychology Review,
  Depression and Anxiety, Journal of Traumatic Stress,
  Psychological Medicine, Journal of Abnormal Psychology

DOMAIN VOCABULARY:
  CBT, DBT, ACT, EMDR, IPT, BDI-II, BAI, DASS-21, PHQ-9, GAD-7, PCL-5,
  SCID-5, MINI, cognitive distortion, automatic thought, schema, exposure,
  behavioral activation, mindfulness, emotion regulation, effect size (d), remission

METHODOLOGY KEYWORDS:
  SCID-5 diagnostic interview, BDI-II/DASS-21 assessment, pre-post design, RCT,
  repeated measures ANOVA, Cohen's d, clinically significant change (Jacobson-Truax),
  reliable change index, Bonferroni correction, single-case experimental design
""",

"sociology_social_science": """================================================================================
TOPIC GUIDE — Sociology & Social Sciences
================================================================================
FIELD: Social Sciences / Sociology
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Sosiologi, Ilmu Sosial, Perubahan Sosial, Stratifikasi, Gender, Komunitas

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: social phenomenon studied, theoretical lens, methodology
  (qualitative/quantitative/mixed), sample/participants (n, group, region),
  key findings (emergent themes, correlations, social patterns, policy implications).

INTRODUCTION ELEMENTS:
  - Social context and relevance: rapid urbanization, inequality, demographic change, digital society.
  - Theoretical framing: conflict theory, functionalism, symbolic interactionism, structuralism.
  - Research gap: underrepresented group, new social phenomenon, specific local context.
  - Research question (qualitative) or hypotheses (quantitative).
  - Positionality (for qualitative): researcher's standpoint.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Foundational theorists: Durkheim (solidarity, suicide), Marx (class, alienation), Weber (rationalization, bureaucracy).
  - Contemporary theories: Bourdieu (capital, habitus, field), Giddens (structuration theory), Foucault (power/discourse).
  - Social stratification: class, race/ethnicity, gender, intersectionality (Crenshaw).
  - Social movements: resource mobilization theory, political opportunity structure, framing.
  - Community sociology: social capital (Putnam), collective action, civic engagement.
  - Digital sociology: social media, algorithms, digital inequality.

METHODOLOGY:
  Common section name: "Research Methodology" / "Methods"
  - Qualitative: ethnography, grounded theory, phenomenology, case study, discourse analysis.
  - Data collection: in-depth interviews (n=15–30), focus group discussions (3–6 groups, 6–10 participants each), participant observation.
  - Interview guide: semi-structured, open-ended questions.
  - Analysis: thematic analysis (Braun & Clarke 6 phases), NVivo/Atlas.ti coding.
  - Quantitative: social survey; Likert scale; n=100–500.
  - Statistical: descriptive, chi-square, regression for survey data.
  - Mixed methods: sequential or concurrent triangulation.
  - Ethical: informed consent, anonymity, power relations consideration.
  - Trustworthiness (qualitative): credibility, transferability, dependability, confirmability.

TYPICAL RESULTS & DISCUSSION:
  - Qualitative: 3–6 main themes with sub-themes and illustrative quotes.
  - Quantitative: odds ratios, regression coefficients for social determinants.
  - Social stratification: income Gini coefficient reference; gender pay gap %.
  - Social capital: Putnam's scale score ranges 10–50.
  - Community participation rate: 30–70% active in civic organizations.
  Tables: thematic structure table, demographic profile, regression summary.
  Figures: conceptual framework diagram, social network diagram, thematic mind map.

TYPICAL FIGURES:
  - Conceptual/theoretical framework diagram.
  - Social network analysis graph (nodes = actors, edges = relationships).
  - Bar chart: survey response distribution.
  - Thematic map (for thematic analysis results).

TYPICAL TABLES:
  - Participant demographic profile (qualitative).
  - Thematic structure: main theme | sub-theme | illustrative quote | frequency.
  - Regression results (quantitative component).

CONCLUSION CHARACTERISTICS:
  - Summary of findings in relation to theoretical framework.
  - Contribution to sociological theory and empirical knowledge.
  - Policy implications.
  - Limitations: positionality bias, generalizability, single context.
  - Future: comparative study, longitudinal, mixed methods expansion.

COMMON REFERENCE VENUES:
  American Sociological Review, Sociological Theory, Journal of Marriage and Family,
  Social Problems, Sociology, British Journal of Sociology,
  Gender & Society, Social Forces, International Sociology

DOMAIN VOCABULARY:
  Bourdieu, habitus, capital, field, structuration, intersectionality, social class,
  ethnography, grounded theory, phenomenology, thematic analysis, saturation,
  reflexivity, positionality, discourse analysis, social capital, collective action

METHODOLOGY KEYWORDS:
  semi-structured interview, focus group discussion, participant observation, ethnography,
  thematic analysis (Braun & Clarke), NVivo/Atlas.ti coding, survey design,
  theoretical saturation, member checking, triangulation
""",

"educational_psychology": """================================================================================
TOPIC GUIDE — Educational Psychology & Pedagogy
================================================================================
FIELD: Psychology / Education
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Psikologi Pendidikan, Motivasi Belajar, Metode Pembelajaran, Evaluasi Pendidikan

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: educational context (grade level, subject, school type),
  intervention (teaching method, ICT tool, pedagogical approach), sample (n teachers/students),
  outcomes (learning achievement score, motivation scale score, pre-post comparison,
  effect size d), statistical significance.

INTRODUCTION ELEMENTS:
  - Educational challenge: learning gap, low motivation, teacher effectiveness.
  - Learning theories: constructivism (Vygotsky, Piaget), self-determination theory (SDT), social cognitive theory (Bandura).
  - Research gap: new teaching method in local context, ICT integration effect, metacognition training.
  - Objectives: evaluate effect of intervention on learning outcomes and motivation.
  - Hypotheses: H1: "Problem-based learning significantly improves critical thinking..."

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Learning theories: Bloom's taxonomy (cognitive domain), Vygotsky ZPD, Piaget's stages.
  - Teaching methods: problem-based learning (PBL), project-based (PjBL), cooperative learning, flipped classroom.
  - ICT in education: e-learning, gamification, AR/VR, LMS (Moodle, Google Classroom).
  - Motivation: intrinsic vs. extrinsic; Self-Determination Theory (SDT): autonomy, competence, relatedness.
  - Academic achievement: cognitive test, formative vs. summative assessment.
  - 21st century skills: critical thinking, collaboration, communication, creativity (4C).
  - Self-regulated learning (SRL): planning, monitoring, evaluation.

METHODOLOGY:
  Common section name: "Research Method"
  - Design: quasi-experimental (pretest-posttest control group), RCT, or descriptive.
  - Participants: students (elementary/junior/senior high/university), teachers.
  - Sampling: intact class/cluster sampling; control vs. experimental class.
  - Intervention: new teaching method vs. conventional; duration (4–12 weeks, N sessions).
  - Instruments: learning achievement test (valid, reliable α>0.7); motivation scale (MSLQ, AMS).
  - Data: pretest | posttest scores; motivation pre/post; observation of learning process.
  - Statistical: independent samples t-test (posttest control vs. experimental), ANCOVA (controlling pretest), paired t-test, effect size Cohen's d.

TYPICAL RESULTS & DISCUSSION:
  - Learning achievement: experimental mean 78–88; control 65–72 (posttest).
  - Effect size: small d=0.3–0.5; medium d=0.5–0.8; large d>0.8 for strong teaching intervention.
  - Motivation scale: MSLQ scale mean 4.0–5.0/7.0 scale or higher in experimental.
  - N-gain score: <0.3 low; 0.3–0.7 medium; >0.7 high (learning gain indicator).
  Tables: pre-post score comparison, effect size, N-gain per group.
  Figures: pre-post score bar chart, N-gain comparison, motivation radar chart.

TYPICAL FIGURES:
  - Bar chart: pretest and posttest scores (control vs. experimental).
  - N-gain category distribution pie chart.
  - Scatter plot: motivation vs. achievement.
  - Line graph: score improvement over time.

TYPICAL TABLES:
  - Descriptive statistics: group | n | pretest (mean ± SD) | posttest | N-gain.
  - Independent t-test: t | df | p | Cohen's d.
  - Motivation scale: dimension | control (mean) | experimental | p.

CONCLUSION CHARACTERISTICS:
  - Intervention significantly improved learning outcomes and/or motivation.
  - Effect size demonstrates practical significance.
  - Implications for teachers, curriculum designers, policymakers.
  - Limitations: quasi-experimental bias, single subject, short duration, Hawthorne effect.
  - Future: longitudinal follow-up, other subject areas, mixed methods, real-world scaling.

COMMON REFERENCE VENUES:
  Educational Psychology Review, Journal of Educational Psychology,
  Learning and Instruction, Computers & Education, Teaching and Teacher Education,
  Journal of Science Education and Technology, British Educational Research Journal

DOMAIN VOCABULARY:
  constructivism, ZPD, Bloom's taxonomy, PBL, PjBL, flipped classroom, gamification,
  N-gain, MSLQ, AMS, SDT, intrinsic motivation, 21st century skills, 4C,
  formative assessment, metacognition, SRL, effect size, Cohen's d

METHODOLOGY KEYWORDS:
  quasi-experimental pretest-posttest, intact class sampling, ANCOVA,
  independent t-test, paired t-test, Cohen's d, N-gain calculation,
  MSLQ questionnaire, learning achievement test validation, Cronbach's alpha
""",

"political_science": """================================================================================
TOPIC GUIDE — Political Science & International Relations
================================================================================
FIELD: Social Sciences / Political Science
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Ilmu Politik, Hubungan Internasional, Kebijakan Publik, Pemerintahan, Demokrasi

ABSTRACT CHARACTERISTICS:
  150–200 words. Reports: political phenomenon studied (election, policy, diplomatic relations,
  governance), theoretical lens, methodology (case study, comparative analysis, qualitative,
  quantitative), unit of analysis, and key findings or arguments.

INTRODUCTION ELEMENTS:
  - Political context: democratization, regional security, governance reform, global institutions.
  - Theoretical framework: realism, liberalism, constructivism (IR), institutionalism, rational choice.
  - Research gap: understudied case, new empirical evidence, theoretical contribution.
  - Research question and argument (thesis statement).

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - IR theories: Waltz (neorealism), Keohane & Nye (liberalism/interdependence), Wendt (constructivism).
  - Democratic theory: procedural (Schumpeter), substantive democracy, democratic consolidation.
  - Public policy: policy cycle, agenda setting (Kingdon's multiple streams), implementation theory.
  - Comparative politics: electoral systems (majoritarian vs. PR), party systems, presidentialism vs. parliamentarism.
  - Political economy: varieties of capitalism, developmental state, fiscal policy.
  - Southeast Asia political context: ASEAN, Indonesia democratization, regional security.

METHODOLOGY:
  Common section name: "Research Methodology" / "Analytical Framework"
  - Qualitative: case study (Yin), process tracing, historical institutionalism, discourse analysis.
  - Comparative: most similar/most different system design (MSSD/MDSD).
  - Quantitative: cross-national datasets (V-Dem, Freedom House, World Bank governance indicators), regression.
  - Data sources: official documents, government reports, elite interviews, NGO reports.
  - Content analysis: primary sources (speeches, treaties, legislation, media).
  - Methods for IR: game theory formalization, network analysis of alliances.

TYPICAL RESULTS & DISCUSSION:
  - Democracy index: Freedom House score 1–7; V-Dem liberal democracy index 0–1.
  - Governance: World Bank CPIA; Transparency International CPI (0–100).
  - Electoral: vote share %, Gallagher disproportionality index, ENPP (effective number of parties).
  - Foreign policy: trade volume USD billion; treaty ratification rates.
  Tables: case comparison matrix, governance indicator trends.
  Figures: time series of democracy scores, coalition formation chart, network diagram.

TYPICAL FIGURES:
  - Time-series: democracy or governance score over years.
  - Comparative bar chart: country scores on governance indicators.
  - Network diagram: alliance/cooperation network.
  - Process tracing timeline diagram.

TYPICAL TABLES:
  - Case comparison matrix (country | variable | outcome).
  - V-Dem/Freedom House indicators by country and year.
  - Policy analysis: policy | actors | mechanisms | outcome.

CONCLUSION CHARACTERISTICS:
  - Theoretical argument supported/challenged by empirical evidence.
  - Contribution to comparative politics, IR theory, or policy studies.
  - Policy recommendation for practitioners.
  - Limitations: case selection bias, data availability, single period.
  - Future: comparative expansion, quantitative testing of theory, policy evaluation.

COMMON REFERENCE VENUES:
  American Political Science Review, Comparative Politics, World Politics,
  Journal of Democracy, International Organization, Foreign Affairs,
  Governance, Asian Survey, Contemporary Southeast Asia,
  Journal of Southeast Asian Studies

DOMAIN VOCABULARY:
  realism, liberalism, constructivism, neoliberal institutionalism, hegemony,
  democratization, electoral system, party system, coalition, civil society,
  V-Dem, Freedom House, ASEAN, sovereignty, norm diffusion, process tracing

METHODOLOGY KEYWORDS:
  case study (Yin), process tracing, most similar system design, comparative analysis,
  discourse analysis, elite interview, content analysis, regression (cross-national),
  V-Dem dataset, Freedom House data, Qualitative Comparative Analysis (QCA)
""",

}

def write_topic(name, content):
    path = os.path.join(D, f"{name}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.lstrip())
    print(f"  wrote {name}.txt")

for name, content in TOPICS.items():
    write_topic(name, content)
print(f"gen_07: {len(TOPICS)} topics written.")

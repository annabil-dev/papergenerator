"""Generator: Medicine (Internal), Surgery, Neurology, Psychiatry — 10 topic files"""
import os; D = os.path.dirname(os.path.abspath(__file__))

TOPICS = {

"cardiology": """================================================================================
TOPIC GUIDE — Cardiology
================================================================================
FIELD: Medicine / Internal Medicine
DEFAULT CITATION STYLE: Vancouver
SUBDISCIPLINE: Kardiologi, Penyakit Jantung Koroner, Gagal Jantung, Aritmia, Kardiologi Intervensi

ABSTRACT CHARACTERISTICS:
  200–300 words (structured: Background, Methods, Results, Conclusion).
  Reports: study design (RCT/cohort/case-control/cross-sectional), patient population
  (n, mean age ± SD, % male), intervention or exposure, primary outcomes (MACE rate %,
  LVEF %, 30-day mortality %, HR with 95% CI), p-value.
  Example: "Patients receiving SGLT2 inhibitor had significantly lower MACE rate (12.3% vs 18.7%,
  HR 0.66, 95% CI 0.52–0.84, p<0.001)."

INTRODUCTION ELEMENTS:
  - Global/national burden of cardiovascular disease (CVD): mortality rates, DALYs.
  - Specific condition: pathophysiology of CAD, HF, atrial fibrillation.
  - Current guideline-recommended therapy and its limitations.
  - Research gap: comparative effectiveness, specific patient subgroup, novel biomarker.
  - Primary and secondary study objectives.
  - Hypotheses: superiority/non-inferiority of intervention.
  Subsections: Background, Rationale, Objectives.

LITERATURE REVIEW:
  Common section name: "Background" (integrated into Introduction in Vancouver style)
  - Pathophysiology: atherosclerosis, plaque rupture, ischemia-reperfusion, cardiac remodeling.
  - Risk factors: hypertension, diabetes, dyslipidemia, smoking (Framingham Risk Score).
  - Diagnostic criteria: ESC/ACC/AHA guidelines for ACS, HF, AF.
  - Evidence from landmark trials: RALES, EMPHASIS-HF, PARADIGM-HF, CASTLE-AF.
  - Current pharmacotherapy: ACE inhibitors, ARBs, beta-blockers, statins, SGLT2i, GLP-1RA.
  - Biomarkers: troponin I/T, BNP/NT-proBNP, CRP, IL-6.
  Key frameworks: cardiovascular risk stratification, TIMI/GRACE scores, NYHA classification.

METHODOLOGY:
  Common section name: "Methods" / "Patients and Methods"
  Study designs used:
  - RCT: randomization, blinding (double-blind preferred), allocation concealment.
  - Observational: prospective cohort, retrospective cohort, case-control.
  - Cross-sectional: population survey.
  Patient selection: inclusion (age 18–75, confirmed diagnosis by ECG/Echo/angiography),
    exclusion (severe renal/hepatic impairment, pregnancy).
  Interventions: drug dosage, stent type, ablation protocol.
  Primary endpoint: MACE (CV death + MI + stroke), LVEF change, symptom score.
  Secondary endpoints: hospitalization, QoL (KCCQ score), NT-proBNP change.
  Statistical analysis: survival analysis (Kaplan-Meier, log-rank), Cox proportional hazards,
    logistic regression; sample size calculation based on expected event rate.
  Biomarker analysis: ELISA, immunoassay; echocardiography (2D, Doppler, strain imaging).

TYPICAL RESULTS & DISCUSSION:
  Section name: "Results" (separate from "Discussion")
  - LVEF: normal >55%; HFrEF <40%; HFmrEF 40–49%.
  - NT-proBNP: normal <300 pg/mL; HF >1000 pg/mL; response to treatment: 30–50% reduction.
  - MACE rate: high-risk population 15–25% per year; with optimal treatment 8–12%.
  - Typical OR for risk factor: HTN → CVD OR 2.1 (1.6–2.8); DM → OR 1.8 (1.4–2.3).
  - Kaplan-Meier curves for survival analysis with HR and 95% CI.
  - Subgroup analysis: treatment effect consistent across age, sex, diabetes subgroups.
  Tables: baseline characteristics, primary/secondary outcomes table, Cox regression.
  Figures: Kaplan-Meier survival curve, forest plot (subgroup analysis), LVEF change bar.

TYPICAL FIGURES:
  - Kaplan-Meier event-free survival curve (treatment vs. control).
  - Forest plot: subgroup analysis (interaction p-values).
  - Box plot / bar chart: echocardiographic parameters by group.
  - CONSORT flow diagram (for RCT).
  - ECG strip: arrhythmia example.

TYPICAL TABLES:
  - Baseline characteristics (mean ± SD or n (%) for each group; p-value for balance).
  - Primary outcomes (event rate %, HR, 95% CI, p-value).
  - Multivariate logistic/Cox regression (OR/HR, 95% CI, adjusted p-value).

CONCLUSION CHARACTERISTICS:
  - States whether primary endpoint was met.
  - Clinical implication: changed practice, confirmed guidelines, new treatment option.
  - Limitations: single center, short follow-up, unmeasured confounders.
  - Future: multicenter RCT, longer follow-up, mechanistic sub-study.

ADDITIONAL SECTIONS:
  - "Ethical Approval": IRB/ethics committee reference number.
  - "Clinical Trial Registration": ClinicalTrials.gov identifier.
  - "Data Availability Statement".

COMMON REFERENCE VENUES:
  New England Journal of Medicine, Lancet, JAMA, Circulation,
  European Heart Journal, Journal of the American College of Cardiology (JACC),
  Heart, JACC: Heart Failure, European Journal of Heart Failure

DOMAIN VOCABULARY:
  MACE, LVEF, NT-proBNP, troponin, STEMI, NSTEMI, ACS, HFrEF, HFpEF,
  ACE inhibitor, ARB, beta-blocker, statin, SGLT2i, PCI, CABG, ablation,
  Kaplan-Meier, Cox regression, HR, 95% CI, NNT, NYHA class, GRACE score

METHODOLOGY KEYWORDS:
  RCT, double-blind, intention-to-treat, per-protocol, Kaplan-Meier, Cox regression,
  logistic regression, ANOVA, echocardiography, cardiac MRI, coronary angiography,
  CONSORT, STROBE, propensity score matching
""",

"endocrinology_diabetes": """================================================================================
TOPIC GUIDE — Endocrinology & Diabetes
================================================================================
FIELD: Medicine / Internal Medicine
DEFAULT CITATION STYLE: Vancouver
SUBDISCIPLINE: Endokrinologi, Diabetes Melitus, Tiroid, Obesitas, Sindrom Metabolik

ABSTRACT CHARACTERISTICS:
  200–300 words (structured). Reports: diabetic population characteristics,
  intervention/exposure, primary outcomes (HbA1c %, fasting glucose mg/dL,
  BMI kg/m², HOMA-IR, lipid profile), study duration, statistical results.

INTRODUCTION ELEMENTS:
  - Global prevalence of DM (IDF statistics: ~537 million adults in 2021).
  - Pathophysiology: type 1 (autoimmune β-cell destruction) vs type 2 (insulin resistance + β-cell failure).
  - Complications: macro- (CVD, stroke) and microvascular (nephropathy, retinopathy, neuropathy).
  - Current treatment gaps: glycemic control rate (only 50% achieve HbA1c <7% globally).
  - Research gap: novel intervention, biomarker, management strategy.

LITERATURE REVIEW:
  Common section name: "Background" (in Introduction)
  - Insulin signaling pathway: IRS-1, PI3K/Akt, GLUT4 translocation.
  - Risk factors: obesity (BMI ≥30), physical inactivity, genetic predisposition (TCF7L2 polymorphism).
  - Diagnostic criteria: ADA guidelines (FPG ≥126 mg/dL; HbA1c ≥6.5%; 2h OGTT ≥200 mg/dL).
  - Pharmacotherapy: metformin, SGLT2 inhibitors, GLP-1 receptor agonists, insulin.
  - Thyroid: TSH, fT4, fT3 reference ranges; Hashimoto's, Grave's disease.
  - Metabolic syndrome criteria (IDF/WHO): waist circumference, HDL, TG, FPG, BP.

METHODOLOGY:
  Common section name: "Methods" / "Subjects and Methods"
  - Design: cross-sectional (prevalence), cohort (incidence, prognosis), RCT (intervention).
  - Patients: DM type 2 patients, age 40–70, HbA1c 7–10%, no severe renal/liver disease.
  - Anthropometric: BMI, waist circumference, waist-hip ratio.
  - Laboratory: FPG (enzymatic method), HbA1c (HPLC), HOMA-IR = (FPI × FPG)/22.5.
  - Lipid profile: total cholesterol, LDL, HDL, triglycerides (Friedewald equation).
  - Intervention: drug/dietary intervention for 12–24 weeks.
  - Statistical: paired t-test, Mann-Whitney, logistic regression, correlation.

TYPICAL RESULTS & DISCUSSION:
  - HbA1c reduction: typically 0.5–1.5% with pharmacotherapy.
  - FPG: controlled <126 mg/dL; uncontrolled 200–300 mg/dL.
  - BMI: normal 18.5–24.9; overweight 25–29.9; obese ≥30 kg/m².
  - HOMA-IR: <2.0 normal; >2.5 insulin resistant; DM type 2 often 3–6.
  - Lipid: LDL target <70 mg/dL (high CVD risk); TG high >150 mg/dL.
  Tables: baseline metabolic profile, pre-post changes ± SD with p-values.
  Figures: scatter plot (HbA1c vs. BMI), box plot (glucose by treatment), Kaplan-Meier.

TYPICAL FIGURES:
  - Scatter plot: HbA1c correlation with BMI/HOMA-IR.
  - Box plot: glucose/HbA1c before and after intervention.
  - Bar chart: prevalence of complications by glycemic control status.
  - Forest plot: meta-analysis effect sizes.

TYPICAL TABLES:
  - Metabolic characteristics: FPG | HbA1c | BMI | HOMA-IR | lipid profile (mean ± SD).
  - Treatment response: Δ HbA1c | Δ FPG | p-value (paired t-test).
  - Logistic regression: predictors of glycemic failure (OR, 95%CI, p).

CONCLUSION CHARACTERISTICS:
  - Reports efficacy of intervention in improving glycemic/metabolic outcomes.
  - Clinical implication: guideline update, therapeutic choice.
  - Limitations: short duration, selection bias, self-reported dietary data.
  - Future: long-term follow-up, mechanistic studies, genetic factors.

COMMON REFERENCE VENUES:
  Diabetes Care, Diabetologia, Lancet Diabetes & Endocrinology,
  Journal of Clinical Endocrinology & Metabolism, Diabetes,
  European Journal of Endocrinology, Obesity Reviews

DOMAIN VOCABULARY:
  HbA1c, FPG, OGTT, HOMA-IR, insulin resistance, β-cell, SGLT2 inhibitor,
  GLP-1, metformin, TSH, fT4, cortisol, adipokine, leptin, adiponectin,
  metabolic syndrome, dyslipidemia, LDL, HDL, triglyceride, BMI

METHODOLOGY KEYWORDS:
  HPLC (HbA1c), enzymatic glucose assay, ELISA (insulin/adipokines), OGTT,
  DEXA (body composition), continuous glucose monitoring, RCT,
  logistic regression, meta-analysis, systematic review
""",

"oncology_cancer": """================================================================================
TOPIC GUIDE — Oncology & Cancer Medicine
================================================================================
FIELD: Medicine / Internal Medicine
DEFAULT CITATION STYLE: Vancouver
SUBDISCIPLINE: Onkologi, Tumor Solid, Hematologi Onkologi, Kanker Paru/Payudara/Kolorektal/Serviks

ABSTRACT CHARACTERISTICS:
  200–300 words (structured). Reports: cancer type, stage (TNM), patient population,
  intervention (chemotherapy regimen/targeted therapy/immunotherapy), primary outcomes
  (ORR %, PFS months, OS months, median survival, p-value, HR).

INTRODUCTION ELEMENTS:
  - Global cancer incidence and mortality (GLOBOCAN statistics).
  - Specific cancer type: epidemiology, risk factors, molecular pathogenesis.
  - Standard of care and its limitations (response rates, resistance mechanisms).
  - Research gap: novel target, combination strategy, predictive biomarker.
  - Study objectives: efficacy and safety assessment.

LITERATURE REVIEW:
  Common section name: "Background" (in Introduction)
  - Molecular biology: driver mutations (KRAS, EGFR, BRAF, HER2, ALK), hallmarks of cancer (Hanahan & Weinberg).
  - Staging: AJCC/TNM staging system.
  - Treatment landscape: cytotoxic chemotherapy, targeted therapy (TKIs, mAbs), immunotherapy (PD-1/PD-L1).
  - Biomarkers: PD-L1 expression (IHC), MSI/MMR status, TMB.
  - Resistance mechanisms: acquired mutations, EMT, tumor microenvironment.
  Key landmark trials: KEYNOTE-189, CheckMate 067, ADAURA, FLAURA.

METHODOLOGY:
  Common section name: "Methods" / "Patients and Methods"
  - Design: Phase I/II/III RCT, cohort study.
  - Patients: histologically confirmed cancer, ECOG PS 0–2, staging by CT/PET.
  - Treatment regimen: drug names, doses, cycles.
  - Response assessment: RECIST 1.1 criteria (CR, PR, SD, PD).
  - Efficacy endpoints: ORR = (CR+PR)/N×100; PFS (time to progression/death); OS (time to death).
  - Safety: CTCAE grading of adverse events (grade 1–5).
  - Statistical: Kaplan-Meier for PFS/OS, log-rank test, Cox regression, Fisher's exact for ORR.

TYPICAL RESULTS & DISCUSSION:
  - ORR ranges: cytotoxic 20–40%; targeted therapy 40–70%; immunotherapy (selected) 30–50%.
  - PFS: median 4–12 months for standard; 12–24+ months for targeted/immunotherapy.
  - OS: median 12–24 months for most advanced solid tumors.
  - Grade 3/4 adverse events: 20–40% for standard chemo; 5–15% for immunotherapy.
  - Biomarker analysis: PD-L1+ (TPS ≥1%) ORR 40% vs PD-L1- 15%.
  Tables: patient demographics/staging, efficacy outcomes, adverse events summary.
  Figures: Kaplan-Meier PFS/OS curves, waterfall plot (tumor response), spider plot.

TYPICAL FIGURES:
  - Kaplan-Meier: PFS and OS curves (treatment vs. control).
  - Waterfall plot: best % change from baseline tumor size.
  - Spider plot: tumor size change over time per patient.
  - Bar chart: adverse event frequency by grade.
  - Forest plot: subgroup PFS/OS analysis.

TYPICAL TABLES:
  - Patient characteristics (age, sex, PS, histology, stage, prior therapy).
  - Efficacy summary: ORR | DCR | median PFS | median OS | HR (95%CI) | p-value.
  - Safety: adverse event | all grade (%) | grade ≥3 (%).

CONCLUSION CHARACTERISTICS:
  - Efficacy and safety conclusion with clinical context.
  - Comparison with existing standard of care.
  - Biomarker implications for patient selection.
  - Limitations: sample size, heterogeneous population, short follow-up.

COMMON REFERENCE VENUES:
  New England Journal of Medicine, Lancet Oncology, Journal of Clinical Oncology,
  Cancer Cell, Cancer Research, Annals of Oncology, Nature Cancer, JAMA Oncology

DOMAIN VOCABULARY:
  ORR, CR, PR, SD, PD, PFS, OS, DCR, RECIST, TMB, PD-L1, MSI-H, TMB-H,
  TKI, mAb, checkpoint inhibitor, CTCAE, ECOG PS, TNM, driver mutation,
  KRAS, EGFR, HER2, ALK, VEGF, checkpoint, cytokine, apoptosis

METHODOLOGY KEYWORDS:
  RECIST 1.1, Kaplan-Meier, log-rank test, Cox regression, IHC, PD-L1 scoring,
  NGS (next-generation sequencing), flow cytometry, FISH, immunohistochemistry,
  CTCAE grading, response assessment, Phase II/III design
""",

"pulmonology_respiratory": """================================================================================
TOPIC GUIDE — Pulmonology & Respiratory Medicine
================================================================================
FIELD: Medicine / Internal Medicine
DEFAULT CITATION STYLE: Vancouver
SUBDISCIPLINE: Pulmonologi, PPOK, Asma, TB, Pneumonia, Kanker Paru

ABSTRACT CHARACTERISTICS:
  200–300 words (structured). Reports: respiratory condition, patient characteristics,
  lung function parameters (FEV1 % predicted, FEV1/FVC ratio, PaO2 mmHg, SpO2 %),
  intervention, outcomes (exacerbation rate, hospitalization, mortality).

INTRODUCTION ELEMENTS:
  - Global burden: COPD prevalence 10–15% of adults >40; TB 10 million new cases/year.
  - Pathophysiology: airway inflammation, remodeling, gas exchange impairment.
  - Current management gaps: COPD underdiagnosis, TB drug resistance, asthma control.
  - Research objectives: new treatment, biomarker validation, management algorithm.

LITERATURE REVIEW:
  Common section name: "Background" (in Introduction)
  - Pulmonary function tests (PFTs): spirometry interpretation (GOLD criteria for COPD).
  - COPD staging: GOLD 1–4 (mild to very severe) based on FEV1% predicted.
  - Asthma: GINA guidelines, FeNO (fractional exhaled NO), bronchial provocation.
  - TB: microbiological diagnosis (AFB smear, GeneXpert, culture), drug-susceptibility testing.
  - Community-acquired pneumonia: PSI/PORT score, CURB-65 severity score.
  - COVID-19 pulmonary manifestations: ARDS, ground-glass opacities, long COVID.

METHODOLOGY:
  Common section name: "Methods" / "Subjects and Methods"
  - Diagnosis: spirometry (ATS/ERS criteria), CT chest, HRCT, bronchoscopy with BAL.
  - Spirometry: FVC, FEV1, FEV1/FVC, DLCO measurement.
  - Microbiological: sputum AFB smear, culture, GeneXpert MTB/RIF, drug sensitivity.
  - Blood gas: arterial blood gas (ABG): pH, PaO2, PaCO2, HCO3-, SpO2.
  - Patient-reported outcomes: COPD Assessment Test (CAT), mMRC dyspnea scale, ACQ for asthma.
  - Intervention: inhaled corticosteroid, bronchodilator (SABA/LABA/LAMA), anti-TB regimen.
  - Statistical: ANOVA, Kruskal-Wallis, regression, Kaplan-Meier.

TYPICAL RESULTS & DISCUSSION:
  - FEV1% predicted: GOLD 1 ≥80%; GOLD 2 50–79%; GOLD 3 30–49%; GOLD 4 <30%.
  - FEV1/FVC: <0.7 = obstructive; normal >0.7.
  - SpO2: normal >95%; mild hypoxemia 90–95%; severe <90%.
  - Exacerbation rate: COPD 1–3/year; with treatment reduction 30–50%.
  - CAT score: mild <10; moderate 10–20; severe >20.
  Tables: spirometry results, CAT/mMRC scores, exacerbation rates.
  Figures: spirometry traces, lung function change over time, CT chest image.

TYPICAL FIGURES:
  - Spirometry flow-volume loop.
  - CT chest findings (annotated with findings).
  - Kaplan-Meier: time to first exacerbation.
  - Bar chart: FEV1 change from baseline by treatment.

TYPICAL TABLES:
  - Spirometry and gas exchange: FVC | FEV1 | FEV1/FVC | DLCO (% predicted).
  - Symptom scores: CAT | mMRC | ACQ at baseline and follow-up.
  - Exacerbation data: rate per year | hospitalization % | mortality %.

CONCLUSION CHARACTERISTICS:
  - Efficacy of intervention on lung function/symptom/exacerbation outcomes.
  - Clinical guidelines implication.
  - Limitations: duration, population generalizability.
  - Future: biomarker-guided therapy, precision medicine approach.

COMMON REFERENCE VENUES:
  American Journal of Respiratory and Critical Care Medicine, Thorax, Chest,
  European Respiratory Journal, Respiratory Medicine, BMC Pulmonary Medicine,
  International Journal of Tuberculosis and Lung Disease

DOMAIN VOCABULARY:
  FEV1, FVC, FEV1/FVC, DLCO, GOLD stage, COPD, asthma, TB, AFB, GeneXpert,
  PaO2, SpO2, hypoxemia, bronchodilator, ICS, LABA, LAMA, mMRC, CAT, ACQ,
  exacerbation, HRCT, BAL, FeNO, ARDS, pulmonary hypertension

METHODOLOGY KEYWORDS:
  spirometry, plethysmography, diffusing capacity (DLCO), arterial blood gas,
  GeneXpert, sputum culture, bronchoscopy, HRCT chest, provocation test,
  FeNO measurement, 6-minute walk test
""",

"nephrology_renal": """================================================================================
TOPIC GUIDE — Nephrology & Renal Medicine
================================================================================
FIELD: Medicine / Internal Medicine
DEFAULT CITATION STYLE: Vancouver
SUBDISCIPLINE: Nefrologi, CKD, AKI, Glomerulonefritis, Hemodialisis, Transplantasi Ginjal

ABSTRACT CHARACTERISTICS:
  200–300 words (structured). Reports: renal condition, eGFR (ml/min/1.73m²), CKD stage,
  proteinuria (mg/day or mg/g creatinine), intervention, outcomes (CKD progression, CV events,
  mortality rate, change in eGFR slope).

INTRODUCTION ELEMENTS:
  - Global CKD prevalence (~13% of general population; ESRD requiring RRT: 2–3 million globally).
  - Pathophysiology: glomerular filtration, tubular function, renin-angiotensin-aldosterone system.
  - Major etiologies: diabetic nephropathy (40%), hypertensive nephrosclerosis (25%), GN (20%).
  - Current management gap: CKD progression prevention, hyperkalemia management with RAAS.
  - Research objectives: intervention on eGFR decline, proteinuria reduction, CV outcomes.

LITERATURE REVIEW:
  Common section name: "Background" (in Introduction)
  - CKD staging: KDIGO 2022 classification (G1–G5, A1–A3 albuminuria categories).
  - Biomarkers: serum creatinine, cystatin C, eGFR (CKD-EPI formula), urine ACR, UPCR.
  - Pathology: glomerulosclerosis, tubulointerstitial fibrosis, vascular changes.
  - RAAS inhibition: ACEi/ARB - cornerstone of CKD management.
  - Novel agents: SGLT2i (renoprotective CREDENCE/DAPA-CKD trials), finerenone.
  - Dialysis modalities: HD, CAPD; AV fistula for vascular access.

METHODOLOGY:
  Common section name: "Patients and Methods"
  - Diagnosis: eGFR by CKD-EPI, urine ACR (spot urine), kidney biopsy (if GN suspected).
  - Renal function: serum creatinine, BUN, cystatin C, urine protein/creatinine ratio.
  - Imaging: renal ultrasound (kidney size cm, echogenicity), Doppler RI.
  - Histopathology: PAS/Masson staining, IF, EM (Oxford classification for IgAN).
  - Intervention: SGLT2i, ACEi/ARB, dietary protein restriction, BP control target.
  - Follow-up: 6–24 months; eGFR slope (ml/min/1.73m²/year) as primary endpoint.
  - Statistical: mixed effects model for eGFR slope, Cox regression for ESRD/death.

TYPICAL RESULTS & DISCUSSION:
  - eGFR: G1 ≥90; G2 60–89; G3a 45–59; G3b 30–44; G4 15–29; G5 <15 ml/min/1.73m².
  - Proteinuria: A1 <30 mg/g; A2 30–300; A3 >300 mg/g creatinine.
  - eGFR slope: CKD progression -3 to -5 ml/min/1.73m²/year; with SGLT2i -0.5 to -1.
  - ESRD risk reduction with SGLT2i: ~30–40% in CREDENCE trial.
  Tables: renal function parameters, urinalysis, biopsy findings.
  Figures: eGFR trajectory curve, Kaplan-Meier for ESRD, biopsy micrograph.

TYPICAL FIGURES:
  - eGFR trajectory curve over time by treatment.
  - Kaplan-Meier: ESRD or doubling of creatinine.
  - Scatter plot: proteinuria vs. eGFR decline slope.
  - Kidney biopsy micrograph (PAS/Masson stain).

TYPICAL TABLES:
  - Renal function: creatinine | eGFR | BUN | cystatin C | urine ACR/UPCR.
  - Primary outcome: eGFR slope | ESRD incidence | mortality (HR, 95%CI, p).
  - Histological classification (if biopsy study).

CONCLUSION CHARACTERISTICS:
  - Effect of intervention on CKD progression/proteinuria/CV outcomes.
  - Clinical guideline implication (KDIGO).
  - Limitations: single ethnicity, non-biopsy diagnosis, limited follow-up.
  - Future: genetic determinants of CKD progression, biomarker-guided therapy.

COMMON REFERENCE VENUES:
  Journal of the American Society of Nephrology (JASN), Kidney International,
  CJASN (Clinical Journal of ASN), NDT (Nephrology, Dialysis, Transplantation),
  American Journal of Kidney Diseases, Kidney Medicine

DOMAIN VOCABULARY:
  eGFR, CKD-EPI, creatinine, cystatin C, ACR, UPCR, RAAS, ACEi, ARB, SGLT2i,
  glomerulonephritis, nephrotic syndrome, AKI (KDIGO stages), ESRD, dialysis,
  hemodialysis, peritoneal dialysis, CKD staging (G1-G5), albuminuria (A1-A3),
  KDIGO, sclerosis, fibrosis, Oxford classification, IgAN

METHODOLOGY KEYWORDS:
  CKD-EPI formula, urine ACR, kidney biopsy, eGFR slope analysis, mixed effects model,
  Kaplan-Meier, Cox regression, renal ultrasound, IF (immunofluorescence),
  EM (electron microscopy), propensity score matching
""",

"neurology": """================================================================================
TOPIC GUIDE — Neurology
================================================================================
FIELD: Medicine / Specialties
DEFAULT CITATION STYLE: Vancouver
SUBDISCIPLINE: Neurologi, Stroke, Epilepsi, Parkinson, Multiple Sclerosis, Demensia

ABSTRACT CHARACTERISTICS:
  200–300 words (structured). Reports: neurological condition, diagnostic method,
  patient population characteristics, intervention, primary outcomes
  (NIHSS score, modified Rankin Scale (mRS), UPDRS score, seizure freedom rate %,
  response time, MRI findings).

INTRODUCTION ELEMENTS:
  - Neurological disease burden: stroke (leading cause of disability), epilepsy (50 million globally), PD (10 million).
  - Pathophysiology: ischemia/hemorrhage (stroke), dopaminergic degeneration (PD), cortical excitability (epilepsy), neuroinflammation (MS).
  - Current treatment limitations: thrombolysis time window, drug-resistant epilepsy, disease modification in PD.
  - Research gap: novel treatment, biomarker, neuroprotection strategy.

LITERATURE REVIEW:
  Common section name: "Background" (in Introduction)
  - Stroke: TOAST classification (ischemic subtypes), mTICI scale for reperfusion, NIHSS for severity.
  - Epilepsy: ILAE 2017 classification, definition of drug-resistance, EEG findings.
  - Parkinson's: Braak staging, Unified Parkinson's Disease Rating Scale (UPDRS), H&Y scale.
  - MS: McDonald criteria (2017), EDSS score, MRI lesion load (T2/T1-Gd).
  - Dementia: NIA-AA criteria for AD, MMSE/MoCA cognitive assessment, CSF biomarkers (Aβ42, tau).
  Landmark trials: DAWN, DEFUSE-3 (thrombectomy); OPERA (ocrelizumab for MS); LEAP (levodopa).

METHODOLOGY:
  Common section name: "Methods" / "Patients and Methods"
  - Neurological assessment: NIHSS (stroke), UPDRS (PD), EDSS (MS), MMSE/MoCA (dementia).
  - Neuroimaging: brain MRI (T1, T2, FLAIR, DWI, SWI, perfusion), CT, PET.
  - EEG: recording, interpretation, seizure quantification.
  - Neuropsychological testing: cognitive domains, validated scales.
  - CSF analysis: Aβ42/40 ratio, phospho-tau 181, t-tau, NfL.
  - Biomarkers: blood NfL, GFAP, α-synuclein (seeding amplification assay).
  - Intervention: tPA, thrombectomy, DBS (PD), ASM (antiseizure medication), DMT (MS).
  - Statistical: logistic regression (mRS dichotomization), Wilcoxon, Mann-Whitney, ANCOVA.

TYPICAL RESULTS & DISCUSSION:
  - NIHSS: mild stroke 1–4; moderate 5–15; severe >15. Good outcome: mRS 0–2 at 90 days.
  - Thrombectomy mTICI 2b–3 reperfusion: 65–80% of treated patients.
  - Epilepsy: seizure-free rate: monotherapy 60–70%; polytherapy 50%; surgery 60–80%.
  - UPDRS motor: PD mild 10–20; moderate 20–40; with L-dopa improvement 30–50%.
  - EDSS: MS mild 0–3.5; moderate 4–6.5; severe 7–10.
  Tables: baseline characteristics, outcome scale scores, neuroimaging findings.
  Figures: MRI images with annotations, DWI lesion maps, outcome bar charts, ROC curves (biomarker).

TYPICAL FIGURES:
  - Brain MRI: DWI/ADC (stroke), T2/FLAIR (MS lesions), dopamine PET (PD).
  - Bar chart: mRS distribution (0–6) at follow-up.
  - Kaplan-Meier: time to seizure recurrence; time to disease progression.
  - ROC curve: diagnostic biomarker.

TYPICAL TABLES:
  - Clinical characteristics: age | sex | NIHSS/UPDRS/EDSS | comorbidities.
  - Outcome: scale score at baseline | 90-day | p-value.
  - MRI findings: lesion volume cm³ | lesion count | location.

CONCLUSION CHARACTERISTICS:
  - Efficacy of intervention on functional/disability outcomes.
  - Biomarker or imaging finding significance.
  - Limitations: small sample, single center, short follow-up.
  - Future: neuroprotection trials, biomarker validation, personalized medicine.

COMMON REFERENCE VENUES:
  New England Journal of Medicine, Lancet Neurology, Brain, Neurology,
  JAMA Neurology, Annals of Neurology, Journal of Neurology,
  European Journal of Neurology, Stroke, Epilepsia

DOMAIN VOCABULARY:
  NIHSS, mRS, UPDRS, EDSS, MMSE, MoCA, MRI, DWI, FLAIR, EEG, tPA, thrombectomy,
  mTICI, reperfusion, Aβ42, tau, NfL, GFAP, alpha-synuclein, dopamine, serotonin,
  dementia, epilepsy, seizure, MS, PD, ALS, Huntington, neuroinflammation

METHODOLOGY KEYWORDS:
  NIHSS assessment, MRI volumetry, EEG recording, neuropsychological testing,
  CSF biomarkers, blood NfL, CONSORT, STROBE, mRS dichotomization,
  logistic regression, propensity score, meta-analysis
""",

"psychiatry": """================================================================================
TOPIC GUIDE — Psychiatry
================================================================================
FIELD: Medicine / Specialties
DEFAULT CITATION STYLE: Vancouver or APA
SUBDISCIPLINE: Psikiatri, Depresi, Skizofrenia, Gangguan Bipolar, Anxietas, Psikosis

ABSTRACT CHARACTERISTICS:
  200–300 words (structured). Reports: psychiatric disorder (DSM-5/ICD-11 criteria),
  patient sample, assessment tools (HDRS, BPRS, PHQ-9, GAD-7, PANSS),
  intervention (medication/psychotherapy), outcomes (symptom score reduction %, remission rate %).

INTRODUCTION ELEMENTS:
  - Psychiatric disease burden: depression (280 million globally), schizophrenia (24 million), bipolar (40 million).
  - Pathophysiology: monoamine hypothesis (depression), dopamine hypothesis (schizophrenia), circadian disruption (bipolar).
  - Treatment gap: 50–75% of patients in LMICs receive no treatment.
  - Research gap: treatment-resistant depression, antipsychotic adherence, psychotherapy access.

LITERATURE REVIEW:
  Common section name: "Background" / "Literature Review"
  - Diagnostic criteria: DSM-5 categories, ICD-11 equivalents.
  - Neurobiological mechanisms: HPA axis, serotonin (5-HT), dopamine, GABA/glutamate.
  - Pharmacotherapy: SSRIs (depression), antipsychotics (1st/2nd gen - schizophrenia), mood stabilizers (bipolar - lithium, valproate).
  - Psychotherapy: CBT, DBT, IPT, ACT efficacy data.
  - Rating scales: HDRS, MADRS, PANSS, BPRS, YMRS, CGI, PHQ-9, GAD-7.
  - Neuroimaging: fMRI (prefrontal hypoactivity in depression), PET (DA binding in schizophrenia).

METHODOLOGY:
  Common section name: "Methods" / "Study Design"
  - Design: RCT (drug/psychotherapy), cohort, cross-sectional prevalence, case-control.
  - Diagnostic confirmation: structured clinical interview (SCID-5/MINI).
  - Assessment instruments: HDRS-17 (depression), PANSS (schizophrenia), YMRS (mania), GAD-7 (anxiety).
  - Intervention: specific drug (dose, duration), psychotherapy protocol (session number, modality).
  - Follow-up: baseline, week 2, week 4, week 8, week 12.
  - Statistical: t-test, Mann-Whitney, mixed ANOVA for repeated measures, logistic regression.
  - Response: ≥50% symptom score reduction; Remission: score below threshold (HDRS ≤7).

TYPICAL RESULTS & DISCUSSION:
  - HDRS-17: severe depression ≥20; mild 8–13; remission ≤7. Response rate 50–70% with SSRIs.
  - PANSS total: typical schizophrenia 60–90; with treatment reduction 20–35%.
  - PHQ-9: mild 5–9; moderate 10–14; severe 15–27.
  - Response/remission rate: antidepressants 40–60% response; psychotherapy 50–65%.
  - Typical comparative study: SSRI vs. CBT; no significant difference at 16 weeks.
  Tables: baseline scores, week 8/12 outcomes, response/remission rates.
  Figures: symptom score change over time, response rate comparison bar chart.

TYPICAL FIGURES:
  - Line graph: mean symptom score over time by treatment group.
  - Bar chart: response/remission rates at endpoint.
  - Kaplan-Meier: time to response/remission.
  - Brain imaging: fMRI activation maps (pre vs. post treatment).

TYPICAL TABLES:
  - Demographic and clinical characteristics.
  - Symptom score changes: baseline | week 4 | week 8 | week 12 (mean ± SD, p-value).
  - Response/remission rates (%, χ² test, OR with 95% CI).

CONCLUSION CHARACTERISTICS:
  - Efficacy comparison; non-inferiority or superiority findings.
  - Clinical implication: guideline update, treatment sequencing.
  - Limitations: blinding challenges in psychotherapy RCTs, placebo response.
  - Future: biomarker-guided treatment selection, transcranial stimulation.

COMMON REFERENCE VENUES:
  JAMA Psychiatry, Lancet Psychiatry, American Journal of Psychiatry,
  World Psychiatry, British Journal of Psychiatry, Psychological Medicine,
  Journal of Affective Disorders, Schizophrenia Bulletin

DOMAIN VOCABULARY:
  DSM-5, ICD-11, HDRS, PANSS, PHQ-9, GAD-7, MADRS, YMRS, SCID,
  SSRI, SNRI, antipsychotic, mood stabilizer, CBT, DBT, ECT, TMS,
  remission, response, treatment-resistance, adherence, stigma, HPA axis

METHODOLOGY KEYWORDS:
  SCID-5/MINI diagnostic interview, HDRS/PANSS rating, RCT design,
  mixed ANOVA, logistic regression, repeated measures, blinded rating,
  intention-to-treat analysis, CONSORT
""",

"orthopedic_surgery": """================================================================================
TOPIC GUIDE — Orthopedic Surgery
================================================================================
FIELD: Medicine / Surgery
DEFAULT CITATION STYLE: Vancouver
SUBDISCIPLINE: Bedah Ortopedi, Artroskopi, Penggantian Sendi, Patah Tulang, Tulang Belakang

ABSTRACT CHARACTERISTICS:
  200–300 words (structured). Reports: condition (fracture type, OA grade, ACL injury),
  surgical technique, patient characteristics, primary outcomes (functional score VAS/
  KOOS/OHS/ODI, union rate %, ROM degrees, complication rate %, follow-up duration months).

INTRODUCTION ELEMENTS:
  - Epidemiology: fracture incidence, osteoarthritis prevalence (>30% of >65 years).
  - Biomechanics and pathophysiology of the condition.
  - Current surgical approaches and their limitations.
  - Research gap: novel technique comparison, implant design, rehabilitation protocol.
  - Study objectives: functional outcome, complication profile, return to activity.

LITERATURE REVIEW:
  Common section name: "Background" / "Introduction"
  - Anatomy: relevant joint/bone structure, biomechanical considerations.
  - Fracture classification: AO/OTA (long bones), Neer (proximal humerus), Garden (femoral neck).
  - OA grading: Kellgren-Lawrence (KL) grade 1–4 on X-ray.
  - Surgical techniques: ORIF, IMN (intramedullary nail), arthroplasty (TKA/THA), ACL reconstruction graft options.
  - Implant comparisons: locked plates vs. IMN; cemented vs. cementless prosthesis.
  - Outcome scores: VAS (pain 0–10), KOOS/WOMAC (knee), Harris Hip Score, Oxford Hip/Knee Score.

METHODOLOGY:
  Common section name: "Methods" / "Patients and Methods"
  - Study design: prospective/retrospective cohort, RCT.
  - Inclusion: confirmed diagnosis by X-ray/MRI, age range, informed consent.
  - Surgical technique: detailed step-by-step description (position, approach, implant used).
  - Rehabilitation protocol: weight-bearing timeline, physiotherapy program.
  - Follow-up: 3, 6, 12 months with clinical and radiological assessment.
  - Outcome measures: VAS, functional scores, ROM (goniometry), union rate (X-ray), implant complication.
  - Statistical: t-test, Mann-Whitney, chi-square, ANOVA for repeated measures.

TYPICAL RESULTS & DISCUSSION:
  - VAS pain: preoperative 7–9/10; postoperative 6 months 1–3/10.
  - Oxford Knee Score: poor <27/48; improvement to excellent >41/48.
  - ROM: TKA flexion preop 80–90°; postop 12mo 120–130°.
  - Union rate: ORIF proximal humerus 85–95% at 3 months.
  - Complication rate: infection 1–3%; hardware failure 2–5%; revision 3–7% at 5 years.
  Tables: preop vs. postop functional scores, complication summary, implant data.
  Figures: X-ray series (preop, post-surgery, follow-up), functional score line graph.

TYPICAL FIGURES:
  - X-ray: preoperative | immediate postoperative | 6/12 month follow-up series.
  - Bar chart: functional score comparison pre vs. post at each time point.
  - Kaplan-Meier: implant survival curve.
  - Intraoperative photograph (if teaching paper).

TYPICAL TABLES:
  - Patient demographics and diagnosis.
  - Functional outcomes at each time point (mean ± SD, p-value).
  - Radiological outcomes: alignment (°), union/non-union, implant position.
  - Complication profile (type | n | %).

CONCLUSION CHARACTERISTICS:
  - Summary of functional and radiological outcomes.
  - Superiority/equivalence of technique.
  - Complication profile vs. literature.
  - Limitations: small sample, short follow-up, heterogeneous surgical experience.
  - Future: long-term RCT, patient-reported outcomes, cost-effectiveness.

COMMON REFERENCE VENUES:
  Journal of Bone and Joint Surgery (JBJS), The Bone & Joint Journal,
  Acta Orthopaedica, Injury, Knee Surgery Sports Traumatology Arthroscopy,
  Journal of Arthroplasty, Spine, World Journal of Orthopedics

DOMAIN VOCABULARY:
  ORIF, IMN, TKA, THA, ACL, KL grade, VAS, KOOS, WOMAC, Oxford Knee Score,
  Harris Hip Score, union rate, ROM, goniometry, implant, prosthesis,
  cortical screw, locking plate, intramedullary nail, arthroplasty, arthroscopy

METHODOLOGY KEYWORDS:
  prospective cohort, retrospective cohort, RCT, goniometry, VAS rating,
  functional score (KOOS/WOMAC/Harris), radiological assessment, Kaplan-Meier
  implant survival, power analysis, CONSORT
""",

"obstetrics_gynecology": """================================================================================
TOPIC GUIDE — Obstetrics & Gynecology
================================================================================
FIELD: Medicine / Obstetrics & Gynecology
DEFAULT CITATION STYLE: Vancouver
SUBDISCIPLINE: Kebidanan, Ginekologi, Kehamilan, Persalinan, Reproduksi, Kanker Ginekologi

ABSTRACT CHARACTERISTICS:
  200–300 words (structured). Reports: obstetric/gynecological condition,
  patient characteristics (gestational age, parity, BMI), intervention,
  primary outcomes (mode of delivery %, neonatal APGAR score, maternal morbidity rate %,
  complication rate %, recurrence-free survival for gynecological cancer).

INTRODUCTION ELEMENTS:
  - Maternal and neonatal morbidity/mortality statistics (WHO, UNICEF data).
  - Pathophysiology: pre-eclampsia (placental dysfunction, systemic endothelial injury),
    GDM (insulin resistance), PPH (uterine atony), cervical cancer (HPV).
  - Current management protocols and their limitations.
  - Research gap: novel intervention, early prediction biomarker, new surgical technique.

LITERATURE REVIEW:
  Common section name: "Background" / "Introduction"
  - Hypertensive disorders of pregnancy: ISSHP classification (PE, chronic HTN, GH).
  - Gestational diabetes: WHO/IADPSG criteria (OGTT 75g: FPG ≥5.1, 1h ≥10.0, 2h ≥8.5 mmol/L).
  - Fetal monitoring: CTG interpretation (FIGO guidelines), biophysical profile, Doppler.
  - Gynecological cancers: FIGO staging (cervical, endometrial, ovarian), HPV vaccination.
  - Endometriosis: revised ASRM staging, visual ENZIAN system.
  - Preterm labor prediction: cervical length (mm), fFN (fetal fibronectin), PIGF.

METHODOLOGY:
  Common section name: "Methods" / "Subjects and Methods"
  - Design: prospective cohort (obstetric prediction), RCT (intervention), retrospective case series.
  - Population: pregnant women with specific condition, gestational age, parity.
  - Diagnostic tools: ultrasound (fetal biometry, Doppler, cervical length), CTG, colposcopy.
  - Laboratory: CBC, coagulation, liver function, renal function, OGTT, HbA1c, AFP, β-HCG, CA-125.
  - Intervention: magnesium sulfate, antihypertensive, cervical cerclage, operative delivery.
  - Neonatal outcomes: birth weight (g), APGAR 1/5 min, NICU admission rate, neonatal death.
  - Statistical: Kaplan-Meier, Cox regression, logistic regression (preterm birth prediction).

TYPICAL RESULTS & DISCUSSION:
  - Pre-eclampsia rate: 3–8% of pregnancies; severe: 1–2%.
  - GDM prevalence: 6–15% of pregnancies (varies by ethnicity).
  - Preterm birth rate: <10% in high-income; 12–18% in LMIC.
  - C-section rate: global 21%, varies 15–50% by country.
  - APGAR score: normal ≥7 at 5 min; low <7 indicates neonatal distress.
  - PE prediction: cervical length <25mm → 5–6x increased preterm risk.
  Tables: obstetric outcomes, neonatal outcomes, complications.
  Figures: fetal growth chart, Kaplan-Meier (recurrence/survival), cervical length scatter.

TYPICAL FIGURES:
  - Fetal growth percentile chart.
  - Ultrasound image (fetal biometry/Doppler).
  - Kaplan-Meier: recurrence-free survival (gynecological cancer).
  - Bar chart: delivery outcomes by intervention group.

TYPICAL TABLES:
  - Obstetric characteristics: GA at delivery | parity | BMI | comorbidities.
  - Maternal outcomes: PE | GDM | PPH | C-section rate.
  - Neonatal outcomes: birth weight | APGAR | NICU admission | mortality.

CONCLUSION CHARACTERISTICS:
  - Effect of intervention on maternal/neonatal outcomes.
  - Clinical implication for obstetric management protocol.
  - Limitations: population heterogeneity, short follow-up, self-reported data.
  - Future: biomarker validation, long-term pediatric outcomes, multicenter study.

COMMON REFERENCE VENUES:
  American Journal of Obstetrics & Gynecology, BJOG (British Journal of OG),
  Obstetrics & Gynecology, Ultrasound in Obstetrics & Gynecology,
  Human Reproduction, European Journal of Obstetrics & Gynecology,
  Gynecologic Oncology, Journal of Maternal-Fetal & Neonatal Medicine

DOMAIN VOCABULARY:
  pre-eclampsia, GDM, APGAR, CTG, biophysical profile, Doppler, FIGO staging,
  cervical length, fFN, PIGF, placenta, preterm labor, PPH, C-section, LSCS,
  HPV, colposcopy, endometriosis, ASRM stage, ovarian reserve, AMH, FSH

METHODOLOGY KEYWORDS:
  obstetric ultrasound, Doppler velocimetry, OGTT, CTG monitoring, colposcopy,
  Kaplan-Meier, Cox regression, logistic regression, prospective cohort,
  CONSORT, STROBE, propensity score matching
""",

"pediatrics": """================================================================================
TOPIC GUIDE — Pediatrics & Child Health
================================================================================
FIELD: Medicine / Pediatrics
DEFAULT CITATION STYLE: Vancouver
SUBDISCIPLINE: Pediatri, Neonatologi, Nutrisi Anak, Penyakit Infeksi Anak, Tumbuh Kembang

ABSTRACT CHARACTERISTICS:
  200–300 words (structured). Reports: age group (neonate/infant/child/adolescent),
  condition, sample size, intervention, outcomes (WAZ/HAZ/WHZ z-scores,
  fever clearance time h, hospitalization days, development milestone achievement %).

INTRODUCTION ELEMENTS:
  - Child health statistics: U5MR (under-5 mortality rate per 1000 live births), stunting prevalence %.
  - Specific pediatric condition: epidemiology, pathophysiology, clinical manifestations.
  - Growth and development context: WHO growth standards.
  - Research gap: treatment effectiveness in children, dose optimization, developmental outcome.

LITERATURE REVIEW:
  Common section name: "Background" / "Introduction"
  - Growth assessment: WHO child growth standards (WAZ, HAZ, WHZ), MUAC.
  - Malnutrition: global burden (stunting 149M, wasting 47M, 2020 UNICEF data).
  - Common pediatric infections: pneumonia, diarrhea, dengue, malaria.
  - IMCI (Integrated Management of Childhood Illness) classification.
  - Vaccine-preventable diseases: coverage rates, herd immunity.
  - Developmental assessment: Denver-II, Bayley Scales, MCHAT.

METHODOLOGY:
  Common section name: "Methods" / "Patients and Methods"
  - Design: RCT, prospective cohort, cross-sectional (nutritional survey).
  - Population: age definition (neonate 0–28d, infant 0–12m, child 1–12y, adolescent 13–18y).
  - Anthropometry: weight (kg), height (cm), head circumference (cm); z-scores (WHO Anthro).
  - Laboratory: CBC, CRP, blood culture, dengue NS1/IgM-IgG, malaria RDT, stool microscopy.
  - Nutritional assessment: dietary recall, food frequency questionnaire, MUAC.
  - Development: validated tools (Denver-II, MCHAT, KPSP).
  - Statistical: t-test, Mann-Whitney, chi-square, logistic regression, growth chart analysis.

TYPICAL RESULTS & DISCUSSION:
  - Stunting (HAZ <-2): national prevalence 20–37% (Indonesia); severely stunted HAZ <-3.
  - Wasting (WHZ <-2): acute malnutrition indicator.
  - Fever clearance: pneumonia with antibiotics 48–72h; dengue resolution 5–7 days.
  - Breastfeeding: exclusive BF 0–6 months → stunting OR 0.67 (95%CI 0.55–0.82).
  Tables: growth parameter z-scores, clinical outcomes, complication rate.
  Figures: growth chart with z-score lines, fever clearance curve, bar chart of nutritional status.

TYPICAL FIGURES:
  - WHO growth chart with patient data points plotted.
  - Fever clearance curve over time.
  - Bar chart: nutritional status distribution (normal/stunted/wasted/overweight).
  - Kaplan-Meier: time to recovery/discharge.

TYPICAL TABLES:
  - Baseline characteristics: age | sex | WAZ | HAZ | WHZ | MUAC.
  - Clinical outcomes: fever clearance | hospitalization days | complication | mortality.
  - Development milestone achievement % by age group.

CONCLUSION CHARACTERISTICS:
  - Effect of intervention on growth/clinical/development outcomes.
  - Public health implication: nutrition program, vaccination, IMCI protocol.
  - Limitations: single center, short follow-up, heterogeneous age groups.
  - Future: community-based RCT, long-term developmental follow-up.

COMMON REFERENCE VENUES:
  Pediatrics (AAP), Archives of Disease in Childhood, JAMA Pediatrics,
  The Lancet Child & Adolescent Health, Pediatric Infectious Disease Journal,
  Journal of Pediatrics, Acta Paediatrica, Paediatrica Indonesiana

DOMAIN VOCABULARY:
  WAZ, HAZ, WHZ, MUAC, stunting, wasting, underweight, U5MR, APGAR,
  IMCI, EBF (exclusive breastfeeding), vaccine coverage, neonatal, NICU,
  Denver-II, MCHAT, Bayley scales, febrile convulsion, dengue shock syndrome

METHODOLOGY KEYWORDS:
  anthropometric assessment (WHO Anthro), dietary 24h recall, FFQ,
  Denver-II developmental assessment, MCHAT screening,
  blood culture, dengue serology, stool microscopy, logistic regression
""",

}

def write_topic(name, content):
    path = os.path.join(D, f"{name}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.lstrip())
    print(f"  wrote {name}.txt")

for name, content in TOPICS.items():
    write_topic(name, content)
print(f"gen_03: {len(TOPICS)} topics written.")

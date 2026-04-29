"""Generator 08: accounting, aerospace_engineering, agriculture, anthropology, architecture,
artificial_intelligence_ethics, augmented_reality, autonomous_vehicles, biology,
biomedical_engineering, blockchain, chemical_engineering"""
import os; D = os.path.dirname(os.path.abspath(__file__))

TOPICS = {

"accounting": """================================================================================
TOPIC GUIDE — Accounting
================================================================================
FIELD: Business / Accounting
DEFAULT CITATION STYLE: APA or Harvard
SUBDISCIPLINE: Akuntansi Keuangan, Akuntansi Manajemen, Audit, Perpajakan, Akuntansi Sektor Publik

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: research setting (public companies, SMEs, government entities),
  accounting phenomenon studied, methodology (archival data analysis, survey, experiment),
  sample (n firms/respondents, period), key statistical results (regression coefficients,
  R², t-stat, Cronbach's α), and contribution to accounting literature.

INTRODUCTION ELEMENTS:
  - Economic/regulatory context: financial reporting standards (IFRS, PSAK), auditing standards.
  - Problem: earnings management, audit quality decline, tax avoidance behavior, disclosure gaps.
  - Theoretical background: agency theory, stakeholder theory, institutional theory.
  - Research gap: unexplored context (emerging market, specific industry, post-IFRS adoption).
  - Hypotheses: H1–H3 typically.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Agency theory (Jensen & Meckling 1976): information asymmetry, principal-agent conflict.
  - Earnings management: accruals-based (Jones model modified, Kothari model) vs. real activities.
  - Audit quality: Big4 vs. non-Big4, auditor independence, rotation, fee pressure.
  - Corporate governance: board composition, audit committee, ownership structure.
  - Tax avoidance: book-tax difference (BTD), effective tax rate (ETR), tax planning aggressiveness.
  - Value relevance: Ohlson (1995) model; ERC (earnings response coefficient).
  - Financial distress: Altman Z-score, Piotroski F-score.

METHODOLOGY:
  Common section name: "Research Methodology" / "Methods"
  - Data: archival (financial statements from BEI/IDX, Bloomberg, DataStream); n=50–500 firms.
  - Period: 3–10 years; panel data (fixed effects, random effects; Hausman test).
  - Dependent variable: discretionary accruals (DA), ETR, audit quality proxy, ROA.
  - Independent variables: board size, ownership concentration, leverage, firm size (ln total assets).
  - Regression: OLS, logistic (for binary), tobit (for censored); robust standard errors.
  - Endogeneity: 2SLS (two-stage least squares), PSM (propensity score matching), lagged IV.
  - Survey (if primary): Likert scale (1–5); reliability (Cronbach's α >0.7); validity (CFA); SEM.
  - Ethical: data source cited; no respondent identification.

TYPICAL RESULTS & DISCUSSION:
  - Earnings management (DA): mean DA ≈ 0.02–0.06 (small but significant).
  - ETR: 22–28% (Indonesia 25% statutory); tax avoidance = statutory ETR − actual ETR.
  - Audit quality: Big4 dummy negative relation to DA: β ≈ -0.02 to -0.05, p<0.05.
  - R² (OLS): accounting studies typically 15–40%.
  - Survey: path coefficient (SEM) typically 0.3–0.7 with t-stat >1.96.
  Tables: descriptive statistics, correlation matrix, regression results (Panels A-B).
  Figures: conceptual framework, residual plot, trend of key variable over years.

TYPICAL FIGURES:
  - Conceptual/research framework diagram.
  - Trend line: mean earnings management or ETR over time.
  - Bar chart: comparison across industry or firm type.
  - Scatter plot: residuals vs. fitted (OLS diagnostics).

TYPICAL TABLES:
  - Descriptive statistics: variable | n | mean | SD | min | max.
  - Pearson/Spearman correlation matrix.
  - Regression results: variable | coefficient | SE | t-stat | p-value | VIF.
  - Robustness check (alternative measurement/sample).

CONCLUSION CHARACTERISTICS:
  - Hypotheses supported or rejected with implications for regulators, auditors, investors.
  - Contribution to agency theory/earnings management literature in emerging markets.
  - Limitations: endogeneity concerns, single country, self-selection bias.
  - Future: cross-country comparison, causal study (diff-in-diff), longitudinal analysis.

COMMON REFERENCE VENUES:
  The Accounting Review, Journal of Accounting Research,
  Contemporary Accounting Research, Accounting, Organizations and Society,
  Journal of Financial Reporting and Accounting, Asian Journal of Accounting Research,
  Journal of Accounting and Public Policy

DOMAIN VOCABULARY:
  accruals, discretionary accruals, Jones model, ETR, BTD, agency theory,
  audit quality, Big4, IFRS, PSAK, earnings response coefficient (ERC),
  Altman Z-score, Piotroski, SEM, CFA, Cronbach's alpha, panel data, VIF

METHODOLOGY KEYWORDS:
  archival data analysis, Jones modified model (accruals), ETR measurement,
  panel data regression (FE/RE), Hausman test, Propensity Score Matching (PSM),
  2SLS endogeneity, logistic regression, SEM-PLS/AMOS, reliability-validity test
""",

"aerospace_engineering": """================================================================================
TOPIC GUIDE — Aerospace Engineering
================================================================================
FIELD: Engineering / Aerospace
DEFAULT CITATION STYLE: AIAA or IEEE
SUBDISCIPLINE: Aerodinamika, Propulsi, Struktur Pesawat, Avionik, Mekanika Penerbangan, UAV

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: aerospace system or component (wing, airfoil, propulsion, UAV),
  analysis method (CFD, FEM, wind tunnel, flight test), key performance metrics
  (lift coefficient CL, drag CD, L/D ratio, thrust-to-weight ratio, structural safety factor,
  natural frequency Hz, fatigue life cycles), comparison with baseline or standard.

INTRODUCTION ELEMENTS:
  - Aviation/space industry context: fuel efficiency demands, UAV proliferation, space missions.
  - Engineering problem: aerodynamic drag, structural weight, propulsion efficiency, flight stability.
  - Existing design limitations.
  - Research objective: optimize, design, analyze aerospace system/component.
  - Contribution: novel geometry, material, control algorithm, simulation model.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Aerodynamics: Navier-Stokes equations, potential flow theory, boundary layer theory.
  - Airfoil profiles: NACA 4-series, 6-series; transonic profiles (supercritical).
  - CFD methods: RANS (k-ε, k-ω SST), LES, DNS; solvers (ANSYS Fluent, OpenFOAM, SU2).
  - Structural analysis: FEM (ANSYS Mechanical, Nastran), composite materials (CFRP), failure criteria.
  - Propulsion: turbofan (bypass ratio, thermal efficiency), rocket propulsion (Isp, thrust equation).
  - UAV: fixed-wing vs. multirotor, control systems (PID, LQR, MPC), payload/endurance.
  - Flight mechanics: 6-DOF equations, stability derivatives, trim analysis.

METHODOLOGY:
  Common section name: "Methodology" / "Numerical/Experimental Methods"
  - CFD: geometry (CAD), meshing (structured/unstructured, y+ <1 for wall-resolved), solver setup (AoA sweep 0–20°), convergence (residuals <1e-6).
  - Wind tunnel: scale model, velocity range (Re = 1e5 – 1e7), force balance, PIV.
  - FEM: mesh convergence study, boundary conditions, load cases (1g + gust + landing).
  - Material: CFRP laminate stacking sequence; composite failure (Tsai-Wu, Hashin).
  - Flight test: instrumented aircraft/UAV, GPS/IMU logging, autopilot (ArduPilot/PX4).
  - Optimization: Genetic Algorithm, gradient-based (adjoint method), surrogate model (Kriging, RBF).

TYPICAL RESULTS & DISCUSSION:
  - CL max: conventional airfoil 1.2–1.6; high-lift devices 2.0–2.8.
  - L/D ratio: glider 30–50; transport aircraft 15–20; UAV 8–15.
  - Drag reduction: blended winglet ≈ 3–5% drag reduction; winglet optimization ≈ 5–10%.
  - Structural weight saving: CFRP vs. Al alloy: 20–30% weight reduction.
  - Thrust-to-weight ratio (UAV): 1.5–3.0 for multirotor.
  - Modal analysis: first natural frequency must exceed flutter onset frequency.
  Tables: aerodynamic coefficients vs. AoA, mesh sensitivity study, structural safety factors.
  Figures: pressure contour, streamline plot, CL-CD polar, stress distribution, mode shapes.

TYPICAL FIGURES:
  - Pressure coefficient Cp distribution on wing surface.
  - CL vs. AoA and CD vs. AoA curves.
  - CL-CD polar diagram.
  - Von Mises stress contour (FEM).
  - CFD velocity/pressure contour visualization.
  - UAV flight path trajectory plot.

TYPICAL TABLES:
  - Aerodynamic coefficients: AoA | CL | CD | CM | L/D.
  - Mesh sensitivity: elements | CL | CD | % difference.
  - Material properties: material | E (GPa) | ν | ρ (kg/m³) | σult (MPa).

CONCLUSION CHARACTERISTICS:
  - Aerodynamic/structural/propulsive performance improvement quantified.
  - Validated against experimental data or published references.
  - Design recommendations for specific flight regime.
  - Limitations: CFD turbulence model limitations, scale effects in wind tunnel.
  - Future: full-scale validation, multi-disciplinary optimization (MDO), flight testing.

COMMON REFERENCE VENUES:
  AIAA Journal, Aerospace Science and Technology, Journal of Aircraft,
  Journal of Spacecraft and Rockets, Acta Astronautica, Progress in Aerospace Sciences,
  Chinese Journal of Aeronautics, International Journal of Aeronautical and Space Sciences

DOMAIN VOCABULARY:
  CL, CD, CM, L/D, AoA, NACA, CFD, RANS, k-ω SST, OpenFOAM, ANSYS Fluent,
  FEM, CFRP, Tsai-Wu, UAV, autopilot, PID, LQR, MPC, Isp, bypass ratio,
  boundary layer, turbulence, flutter, y+, mesh convergence, adjoint method

METHODOLOGY KEYWORDS:
  CFD simulation (RANS k-ω SST), wind tunnel testing, FEM structural analysis,
  mesh convergence study, composite failure criteria (Tsai-Wu, Hashin),
  genetic algorithm optimization, adjoint-based shape optimization, 6-DOF flight simulation
""",

"agriculture": """================================================================================
TOPIC GUIDE — Agriculture (General)
================================================================================
FIELD: Agricultural Sciences
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Pertanian Umum, Tanaman Pangan, Pertanian Berkelanjutan, Ketahanan Pangan, Agroteknologi

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: crop type, agricultural practice studied, experimental design
  (field trial, greenhouse, pot experiment), treatments, key results (yield kg/ha,
  growth parameters, soil properties, economic return), and statistical significance.

INTRODUCTION ELEMENTS:
  - Food security context: population growth, demand for food, climate change threats to production.
  - Specific agricultural challenge: low yield, soil degradation, pest pressure, water scarcity.
  - Research gap: new variety, fertilizer formulation, management practice in local context.
  - Objectives: evaluate treatment effects on crop growth, yield, soil health.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Food security theory: pillars (availability, access, utilization, stability) — FAO framework.
  - Crop physiology: photosynthesis, leaf area index (LAI), harvest index (HI), yield components.
  - Soil science: soil texture, pH, CEC, organic matter, macro/micronutrients.
  - Fertilization: N, P, K requirements per crop; organic vs. synthetic; slow-release fertilizer.
  - Sustainable agriculture: intercropping, cover crops, no-till, integrated crop management (ICM).
  - Irrigation: deficit irrigation, drip irrigation water use efficiency (WUE kg/m³).
  - Pesticides: IPM (Integrated Pest Management), biological control, resistance management.

METHODOLOGY:
  Common section name: "Materials and Methods"
  - Experimental design: RCBD (Randomized Complete Block Design), factorial CRD; 3–5 replicates.
  - Location: research station or farmer's field; GPS coordinates; soil classification.
  - Treatments: n=4–8 treatment levels (e.g., fertilizer doses: 0, 100, 150, 200 kg N/ha).
  - Crop management: planting date, spacing, irrigation schedule, pest/disease monitoring.
  - Measurements: plant height (cm), SPAD chlorophyll index, LAI (LAI-2000), dry weight (g), yield (kg/ha).
  - Soil analysis: pH (pH meter), organic C (Walkley-Black), N total (Kjeldahl), P available (Olsen/Bray).
  - Statistical: ANOVA (one-way or two-way); means comparison DMRT/Tukey HSD (α = 0.05); SAS/SPSS/R.

TYPICAL RESULTS & DISCUSSION:
  - Rice yield: 4–7 t/ha conventional; optimized 7–10 t/ha.
  - Maize yield: 5–8 t/ha without fertilizer; 8–12 t/ha optimized N fertilizer.
  - Soybean yield: 1.5–2.5 t/ha; improved variety 2.5–3.5 t/ha.
  - Fertilizer efficiency: agronomic efficiency (AE, kg grain per kg N) = 10–25.
  - Soil organic matter: 1.5–3.5% (medium fertility); improvement with compost +0.3–0.5% per season.
  Tables: treatment × block yield data, ANOVA table, soil analysis summary.
  Figures: bar chart yield by treatment, growth curve (plant height), soil nutrient comparison.

TYPICAL FIGURES:
  - Bar chart: yield (kg/ha) per treatment with error bars ± SD.
  - Line graph: plant height growth over time by treatment.
  - Scatter plot: yield vs. soil N or LAI correlation.
  - Photographs: field experimental plots.

TYPICAL TABLES:
  - Treatment mean comparison: treatment | plant height (cm) | yield (kg/ha) | DMRT notation.
  - ANOVA summary: source | df | SS | MS | F | p.
  - Soil properties: treatment | pH | OM% | N | P | K.

CONCLUSION CHARACTERISTICS:
  - Optimal treatment identified (e.g., 150 kg N/ha produced highest yield).
  - Yield component response to treatment explained mechanistically.
  - Economic benefit analysis (net income increase).
  - Limitations: single season/location, limited variety tested.
  - Future: multi-year multi-location, farmer participatory research, climate adaptation.

COMMON REFERENCE VENUES:
  Field Crops Research, European Journal of Agronomy, Agricultural Systems,
  Agronomy Journal, Plant and Soil, Experimental Agriculture,
  Crop Science, Indonesian Journal of Agronomy

DOMAIN VOCABULARY:
  yield, RCBD, DMRT, Tukey HSD, LAI, SPAD, harvest index, AE, WUE,
  N-P-K, CEC, organic matter, IPM, Walkley-Black, Kjeldahl, Olsen-Bray,
  food security, intercropping, deficit irrigation, GMO

METHODOLOGY KEYWORDS:
  RCBD field experiment, factorial design, ANOVA, DMRT/Tukey HSD,
  Kjeldahl N analysis, Walkley-Black C, LAI measurement (LAI-2000),
  chlorophyll index (SPAD), yield component analysis
""",

"anthropology": """================================================================================
TOPIC GUIDE — Anthropology
================================================================================
FIELD: Social Sciences / Anthropology
DEFAULT CITATION STYLE: APA or Chicago
SUBDISCIPLINE: Antropologi Budaya, Antropologi Sosial, Etnografi, Arkeologi, Antropologi Linguistik

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: community/culture/site studied, theoretical lens,
  methods (ethnographic fieldwork, survey, archaeological excavation, interview),
  key findings (cultural practices, social structures, ritual significance, artifact analysis).

INTRODUCTION ELEMENTS:
  - Cultural or social context: community profile, geographic setting, historical background.
  - Anthropological problem: cultural change, identity, globalization impact, traditional knowledge.
  - Theoretical framing: structuralism, functionalism, interpretivism, postcolonialism.
  - Research gap: understudied community, undocumented practice, reinterpretation needed.
  - Research question and positionality of researcher.

LITERATURE REVIEW:
  Common section name: "Theoretical Framework" / "Literature Review"
  - Founders: Malinowski (functionalism, fieldwork), Boas (cultural relativism), Lévi-Strauss (structuralism), Geertz (thick description, interpretive anthropology).
  - Key concepts: culture, habitus (Bourdieu), liminality (Turner), rite of passage (van Gennep).
  - Indigenous studies: UNDRIP, cultural sovereignty, epistemic justice.
  - Material culture: artifact analysis, ethnoarchaeology, museology.
  - Linguistic anthropology: Sapir-Whorf hypothesis, language endangerment, language and identity.
  - Medical anthropology: illness narratives, health-seeking behavior, traditional medicine.

METHODOLOGY:
  Common section name: "Research Methodology" / "Methods"
  - Ethnographic fieldwork: participant observation (3 months–2 years); field notes; thick description.
  - Interviews: in-depth, semi-structured, oral history (n=15–30 key informants); purposive + snowball sampling.
  - Focus group discussions (FGD): 2–4 groups of 6–10 participants.
  - Archaeological: surface survey, excavation, stratigraphy, artifact typology, C14 dating.
  - Artefact analysis: iconography, material identification (XRF, SEM).
  - Data analysis: thematic coding (NVivo/Atlas.ti), narrative analysis, discourse analysis.
  - Ethical: free prior informed consent (FPIC), community benefit sharing, anonymization.
  - Reflexivity: researcher's standpoint, positionality statement.

TYPICAL RESULTS & DISCUSSION:
  - Ethnographic themes: 3–5 major themes with rich descriptive narrative and illustrative quotes.
  - Cultural persistence/change indicators (e.g., % youth retaining traditional practice).
  - Archaeological: artifact distribution by stratigraphic layer; C14 dates (cal BP).
  - Linguistic: documentation of X endangered words/phrases; use frequency.
  Tables: informant profile, thematic structure, artifact typology table.
  Figures: kinship diagram, ritual sequence timeline, map of study area, artifact photos.

TYPICAL FIGURES:
  - Study area/community map.
  - Kinship/social structure diagram.
  - Ritual or ceremony photograph/illustration.
  - Artifact photographs with typology labels.
  - Timeline: historical sequence of cultural events.

TYPICAL TABLES:
  - Informant profile: code | gender | age | role | years in community.
  - Thematic structure: theme | sub-theme | illustrative quote | informant code.
  - Artifact typology: type | material | period | context | function.

CONCLUSION CHARACTERISTICS:
  - Cultural phenomenon interpreted within theoretical framework.
  - Contribution to anthropological knowledge of specific region/community.
  - Ethical recommendations for cultural preservation or policy.
  - Limitations: researcher positionality, community access limitations, linguistic barrier.
  - Future: longitudinal study, comparative ethnography, community-based participatory research.

COMMON REFERENCE VENUES:
  American Ethnologist, Cultural Anthropology, Journal of the Royal Anthropological Institute,
  American Anthropologist, Ethnology, Journal of Southeast Asian Studies,
  Wacana (Universitas Indonesia), Archipel (EFEO Paris)

DOMAIN VOCABULARY:
  ethnography, thick description, participant observation, emic/etic, habitus,
  liminality, rite of passage, cultural relativism, kinship, materiality,
  FPIC, reflexivity, positionality, discourse analysis, oral history, artefact

METHODOLOGY KEYWORDS:
  ethnographic fieldwork, participant observation, semi-structured interview,
  thematic analysis (NVivo/Atlas.ti), narrative analysis, C14 dating,
  FPIC consent, snowball sampling, reflexivity statement
""",

"architecture": """================================================================================
TOPIC GUIDE — Architecture & Urban Design
================================================================================
FIELD: Architecture / Built Environment
DEFAULT CITATION STYLE: APA or Chicago
SUBDISCIPLINE: Arsitektur, Desain Urban, Konservasi Bangunan, Arsitektur Vernakular, Bangunan Hijau

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: building type or urban area studied, design approach or
  analytical method (space syntax, post-occupancy evaluation, BIM, thermal simulation),
  key findings (spatial performance, thermal comfort PMV/PPD, structural efficiency,
  cultural significance), and implications for architectural practice.

INTRODUCTION ELEMENTS:
  - Architectural or urban challenge: rapid urbanization, heritage loss, energy inefficiency, thermal discomfort.
  - Cultural and contextual significance of study site.
  - Theoretical/design framework: genius loci, biophilic design, sustainable architecture.
  - Research gap: undocumented typology, unevaluated performance, new design method.
  - Research question or design objectives.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Architectural theory: Vitruvius' triad (firmitas, utilitas, venustas); Norberg-Schulz (place theory); Frampton (critical regionalism).
  - Space syntax: Hillier & Hanson (1984); integration value, connectivity, depth map.
  - Vernacular architecture: climate-responsive design, local materials, cultural expression.
  - Green architecture: LEED, GREENSHIP, passive design strategies.
  - Thermal comfort: Fanger's PMV-PPD model; ASHRAE 55; adaptive comfort model.
  - Building Information Modeling (BIM): IFC standard, parametric design, Revit, ArchiCAD.
  - Heritage conservation: Venice Charter, Burra Charter; authenticity and integrity.

METHODOLOGY:
  Common section name: "Research Method" / "Design Method"
  - Qualitative: architectural documentation (measured drawing, photography), case study analysis.
  - Space syntax: DepthMapX software; integration, connectivity, intelligibility analysis.
  - POE (Post-Occupancy Evaluation): user satisfaction survey (n=30–100), observation.
  - BIM: 3D parametric model (Revit/Grasshopper); clash detection, quantity take-off.
  - Thermal simulation: EnergyPlus, IES VE, Design Builder; EPW weather file; PMV/PPD.
  - Material testing: compression strength, thermal conductivity, moisture absorption.
  - Computational design: parametric (Grasshopper + Ladybug Tools), genetic algorithm optimization.

TYPICAL RESULTS & DISCUSSION:
  - Space syntax: mean integration value (HH) 0.8–1.5; high-activity spaces >1.2.
  - Thermal comfort: PMV optimal = 0 ± 0.5; PPD <10% for comfortable zone.
  - Energy consumption: reference building 150–250 kWh/m²/year; green design 80–120 kWh/m²/year.
  - User satisfaction (POE): mean score 3.5–4.5/5.0 (mostly satisfied).
  - BIM clash detection: typically 50–200 clashes detected in model coordination.
  Tables: space syntax metrics, thermal comfort data, energy simulation results.
  Figures: space syntax axial/visibility map, thermal comfort contour, energy profile chart.

TYPICAL FIGURES:
  - Space syntax depth map / visibility graph analysis.
  - Thermal comfort contour plot (PMV distribution).
  - 3D BIM model visualization.
  - Site plan and floor plan drawings.
  - Daylighting analysis (illuminance lux map).

TYPICAL TABLES:
  - Space syntax metrics: space | integration | connectivity | depth | intelligibility.
  - Thermal simulation: zone | PMV | PPD% | mean radiant T (°C) | cooling load kW.
  - User satisfaction: aspect | mean score | SD | rating.

CONCLUSION CHARACTERISTICS:
  - Architectural design or performance assessed with evidence-based findings.
  - Design recommendation for improving spatial quality or thermal/energy performance.
  - Cultural heritage preservation implications.
  - Limitations: simulation accuracy, POE sample size, single climate zone.
  - Future: full BIM implementation, GREENSHIP certification, community participatory design.

COMMON REFERENCE VENUES:
  Building and Environment, Energy and Buildings, Frontiers of Architectural Research,
  Journal of Architecture and Urbanism, ArchNet-IJAR,
  DIMENSI (Petra University), NALARs (UMJ),
  Habitat International, Cities

DOMAIN VOCABULARY:
  space syntax, integration value, PMV, PPD, LEED, GREENSHIP, BIM, Revit,
  Grasshopper, EnergyPlus, vernacular, genius loci, passive design, POE,
  EPW weather file, Ladybug, thermal comfort, Burra Charter, IFC standard

METHODOLOGY KEYWORDS:
  space syntax (DepthMapX), post-occupancy evaluation (survey), BIM parametric modeling,
  thermal simulation (EnergyPlus/IES VE), daylighting simulation (Radiance/Dialux),
  POE questionnaire, measured drawing, material testing
""",

"artificial_intelligence_ethics": """================================================================================
TOPIC GUIDE — AI Ethics & Responsible AI
================================================================================
FIELD: Computer Science / Ethics / Philosophy of Technology
DEFAULT CITATION STYLE: APA or IEEE
SUBDISCIPLINE: Etika AI, AI yang Dapat Dipercaya, Keadilan Algoritmik, Privasi Data, Regulasi AI

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: AI system or domain studied (facial recognition, predictive policing,
  recommendation systems, medical AI), ethical framework applied, methodology (case study,
  experimental bias measurement, survey, policy analysis), key findings (bias metrics,
  fairness gap, compliance assessment, public perception), and policy implications.

INTRODUCTION ELEMENTS:
  - AI proliferation and societal impact: automation, decision-making, surveillance.
  - Specific ethical challenge: algorithmic bias, lack of transparency, privacy violation, autonomous weapons.
  - Regulatory context: EU AI Act, UNESCO AI Ethics Recommendation, NIST AI RMF.
  - Research gap: specific stakeholder perspective, domain-specific ethics framework, emerging risk.
  - Research question: normative (what should be done) or empirical (what is happening).

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background" / "Theoretical Framework"
  - Foundational AI ethics principles: UNESCO (2021) 11 principles; OECD AI Principles (2019).
  - Algorithmic bias: training data bias, historical bias, representation bias; measurement (equalized odds, demographic parity).
  - Explainability / XAI: LIME, SHAP, Grad-CAM; model cards, datasheets for datasets.
  - Fairness definitions: individual fairness, group fairness, counterfactual fairness.
  - Privacy: differential privacy (ε-DP), federated learning, GDPR, data minimization.
  - AI governance: EU AI Act risk categories (unacceptable/high/limited/minimal), national AI policies.
  - Autonomous systems ethics: moral agency, trolley problem, Asimov's laws.

METHODOLOGY:
  Common section name: "Methodology" / "Research Methods"
  - Bias audit: dataset analysis (demographic imbalance), algorithmic fairness metrics.
  - Fairness metrics: accuracy parity, equal opportunity (TPR parity), demographic parity, disparate impact (DI = min_rate/max_rate; <0.8 = biased).
  - Experimental: deploy AI system on test datasets; measure output bias by protected attribute (gender, race, age).
  - Survey: expert opinion (Delphi method), public attitude (Likert scale, n=200–1000).
  - Policy analysis: document analysis of national AI regulations; comparative legal analysis.
  - Case study: specific AI deployment (healthcare, criminal justice, hiring); thematic analysis.
  - Tools: Fairness Indicators (TensorFlow), IBM AI Fairness 360, Aequitas.

TYPICAL RESULTS & DISCUSSION:
  - Disparate impact: face recognition error rate Black females 34.7% vs. White males 0.8% (Buolamwini & Gebru 2018 type finding).
  - Fairness gap: accuracy difference between demographic groups 5–20%.
  - Survey: 65–75% of users distrust fully automated decision-making in high-stakes contexts.
  - Policy: EU AI Act classifies X types of systems as "high risk" requiring conformity assessment.
  Tables: bias metrics comparison, policy framework comparison, fairness audit results.
  Figures: demographic bias visualization, fairness-accuracy tradeoff curve, regulatory comparison.

TYPICAL FIGURES:
  - Heatmap: error rate by demographic group.
  - Fairness-accuracy tradeoff curve.
  - Policy comparison matrix (heatmap).
  - Bar chart: public survey responses to AI trust items.

TYPICAL TABLES:
  - Fairness metrics: group | accuracy | FPR | FNR | DI score.
  - Policy comparison: country | key AI law | risk framework | enforcement.
  - Principles mapping: principle | EU AI Act | OECD | UNESCO | overlap.

CONCLUSION CHARACTERISTICS:
  - Bias or ethical risks identified and quantified.
  - Mitigation recommendations (algorithmic, organizational, regulatory).
  - Contribution to AI ethics framework or governance debate.
  - Limitations: evolving regulations, context-specificity, fairness definition controversy.
  - Future: longitudinal bias monitoring, intersectional fairness, AI ethics education.

COMMON REFERENCE VENUES:
  ACM FAccT (Fairness, Accountability, Transparency),
  IEEE Transactions on Technology and Society, AI & Society (Springer),
  Ethics and Information Technology, Big Data & Society,
  Journal of Artificial Intelligence Research (JAIR),
  Science and Engineering Ethics

DOMAIN VOCABULARY:
  algorithmic bias, disparate impact, demographic parity, equalized odds, LIME, SHAP,
  XAI, GDPR, differential privacy, federated learning, EU AI Act, OECD, UNESCO,
  AI Fairness 360, Aequitas, fairness-accuracy tradeoff, model card, datasheet

METHODOLOGY KEYWORDS:
  fairness audit (IBM AI Fairness 360/Aequitas), disparate impact analysis,
  bias metrics measurement, Delphi expert survey, policy document analysis,
  case study (thematic analysis), Grad-CAM XAI, differential privacy evaluation
""",

"augmented_reality": """================================================================================
TOPIC GUIDE — Augmented Reality & Mixed Reality
================================================================================
FIELD: Computer Science / Human-Computer Interaction
DEFAULT CITATION STYLE: IEEE or APA
SUBDISCIPLINE: Augmented Reality, Mixed Reality, XR, Marker-based AR, Markerless AR, AR in Education/Industry

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: AR application domain (education, industry, healthcare, tourism),
  system design (marker-based/markerless, device type), methodology (experimental study,
  usability evaluation, user study), metrics (task completion time, accuracy, SUS score,
  learning gain, presence score, latency ms), and comparison with non-AR baseline.

INTRODUCTION ELEMENTS:
  - Reality-virtuality continuum (Milgram 1994): VR, AR, MR, XR.
  - Application domain motivation: immersive learning, remote maintenance, surgical training.
  - Challenges: occlusion handling, tracking accuracy, user acceptance, device cost.
  - Research gap: specific application domain, population group, AR platform evaluation.
  - Objectives: design, implement, evaluate AR system for target application.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Literature Review"
  - AR technology: marker-based (Vuforia, ARToolKit), markerless (SLAM, ARCore, ARKit), GPS-based.
  - Platforms: ARCore (Android), ARKit (iOS), Vuforia, Microsoft HoloLens, Meta Quest.
  - AR in education: constructivist learning theory, spatial cognition improvement, engagement.
  - AR in industry: AR-assisted assembly, remote guidance (Microsoft Dynamics 365 Guides), maintenance.
  - AR in healthcare: surgical navigation, anatomy visualization, rehabilitation.
  - Usability: System Usability Scale (SUS ≥68 = acceptable), USE questionnaire, NASA-TLX (cognitive load).
  - Presence: Witmer & Singer (1998); Slater's presence questionnaire.

METHODOLOGY:
  Common section name: "System Design and Evaluation" / "Methodology"
  - System development: Unity 3D + ARCore/ARKit/Vuforia; 3D model creation (Blender, AutoCAD).
  - Tracking: image target (Vuforia), plane detection + object recognition (ARCore), QR codes.
  - User study: between-subjects (AR vs. non-AR) or within-subjects (counterbalanced).
  - Participants: n=20–60, age range, tech literacy level.
  - Tasks: predefined task set (assembly, quiz, navigation, visualization).
  - Measures: task time (s), accuracy (%), error count, SUS, NASA-TLX, pre-post knowledge test.
  - Statistical: independent t-test or Mann-Whitney U; paired t-test (pre-post); ANOVA.

TYPICAL RESULTS & DISCUSSION:
  - SUS score: AR app ≥70 (good usability); >80 = excellent.
  - Task time: AR-assisted faster by 15–30% for spatial assembly tasks.
  - Learning gain: AR group pre-test 60%; post-test 82%; non-AR 60% → 71%.
  - NASA-TLX mental demand: AR sometimes higher due to novelty.
  - Tracking accuracy: marker-based <5mm registration error; markerless <1cm.
  Tables: usability scores, performance comparison, knowledge test results.
  Figures: AR application screenshots, SUS score bar chart, task time comparison.

TYPICAL FIGURES:
  - AR application screenshot (in-use visualization).
  - SUS score bar chart with benchmark line (68).
  - Task time comparison: AR vs. non-AR (bar/box plot).
  - Learning gain: pre-post score comparison.
  - NASA-TLX subscale comparison.

TYPICAL TABLES:
  - Participant demographics: n | mean age | gender | prior AR experience.
  - SUS per task/group: group | mean SUS | SD | acceptability.
  - Performance: metric | AR group | control group | p-value.

CONCLUSION CHARACTERISTICS:
  - AR application enhanced performance and/or learning in target domain.
  - Usability confirmed (SUS threshold met).
  - Design recommendations for AR system deployment.
  - Limitations: small sample, novelty effect, device dependency.
  - Future: multi-user AR, AI integration, accessibility for diverse users.

COMMON REFERENCE VENUES:
  IEEE ISMAR, ACM CHI, Computers & Education, Computers in Human Behavior,
  Virtual Reality (Springer), IEEE Transactions on Visualization and Computer Graphics,
  Journal of Computer Assisted Learning, Journal on Multimodal User Interfaces

DOMAIN VOCABULARY:
  AR, MR, XR, SLAM, ARCore, ARKit, Vuforia, HoloLens, marker-based, markerless,
  SUS, NASA-TLX, presence, occlusion, registration error, Unity 3D, Blender,
  constructivism, spatial cognition, task completion time, learning gain

METHODOLOGY KEYWORDS:
  Unity 3D + ARCore/Vuforia development, marker image target design,
  between/within-subjects user study, SUS (System Usability Scale),
  NASA-TLX cognitive load, pre-post knowledge test, Mann-Whitney U, paired t-test
""",

"autonomous_vehicles": """================================================================================
TOPIC GUIDE — Autonomous Vehicles & Self-Driving Systems
================================================================================
FIELD: Computer Science / Automotive Engineering
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Kendaraan Otonom, Persepsi, Perencanaan Jalur, SLAM, V2X, Keselamatan AV

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: AV subsystem or full stack (perception, localization, planning,
  control), dataset or simulation used, proposed algorithm, key metrics (object detection
  mAP %, localization RMSE m, path tracking RMSE m/°, computational latency ms,
  collision rate in simulation), and comparison with baseline.

INTRODUCTION ELEMENTS:
  - AV market growth and SAE automation levels (L0–L5).
  - Safety challenge: AV accidents, edge cases, sensor failure, adversarial attacks.
  - Open research problems: all-weather perception, V2X integration, ethical dilemmas.
  - Research objective: improve perception accuracy, reduce latency, enhance safety.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - Perception: LIDAR (3D point cloud), camera (monocular/stereo), RADAR; sensor fusion.
  - Detection algorithms: PointPillars, VoxelNet, SECOND (LIDAR); YOLO, SSD, Faster-RCNN (camera).
  - Localization/mapping: SLAM (simultaneous localization and mapping); HD maps; GPS/IMU fusion; NDT, ICP.
  - Path planning: A*, Dijkstra, RRT*, Lattice planner; Frenet frame representation.
  - Control: Stanley controller, MPC (model predictive control), PID; vehicle dynamics model.
  - Simulation: CARLA, SUMO, Gazebo, LGSVL for AV testing.
  - V2X: DSRC (IEEE 802.11p), C-V2X (LTE/5G), cooperative perception.
  - Safety: ISO 26262 (functional safety), SOTIF (ISO 21448).

METHODOLOGY:
  Common section name: "Methodology" / "Proposed System"
  - Dataset: KITTI, NuScenes, Waymo Open Dataset, CARLA synthetic.
  - Perception: model architecture, input (point cloud/image), training (GPU, n epochs), evaluation (mAP, precision, recall per class).
  - Localization: EKF/UKF fusion (GPS+IMU+LIDAR); RMSE (m) on test trajectory.
  - Planning: algorithm description, cost function, constraints; benchmark scenarios.
  - Control: vehicle model (kinematic/dynamic bicycle model), gains, deviation metrics.
  - Simulation: scenario setup (CARLA), n=100–1000 scenarios, safety metrics (TTC, collision rate).
  - Real-world (if applicable): test vehicle description, sensor setup, test track.

TYPICAL RESULTS & DISCUSSION:
  - 3D object detection (mAP): LIDAR-based 70–85% on KITTI; camera-based 55–70%.
  - Localization RMSE: GPS-only 1–5m; fused GPS+LIDAR 0.05–0.2m.
  - Path tracking RMSE: lateral error 0.05–0.15m (urban speed); MPC outperforms PID in curves.
  - Computational latency: real-time perception <50ms; planning <100ms.
  - Simulation collision rate: baseline 3–8%; proposed 0.5–2%.
  Tables: detection results by class, localization comparison, planning benchmark.
  Figures: perception output visualization, trajectory plot, speed/lateral error graph.

TYPICAL FIGURES:
  - 3D bounding box visualization on point cloud.
  - Trajectory comparison: ground truth vs. planned vs. executed.
  - Localization error over time/distance.
  - Scenario visualization (CARLA simulation screenshot).
  - mAP comparison bar chart.

TYPICAL TABLES:
  - Detection: class | precision | recall | AP | method comparison.
  - Localization: method | RMSE-x (m) | RMSE-y | RMSE-heading (°).
  - Simulation safety: metric | baseline | proposed | improvement %.

CONCLUSION CHARACTERISTICS:
  - Proposed perception/planning/control method outperforms baseline.
  - Real-time feasibility demonstrated.
  - Safety improvement quantified.
  - Limitations: simulation gap, dataset bias, specific weather conditions.
  - Future: real-world validation, multi-modal sensor fusion, V2X integration, ADAS deployment.

COMMON REFERENCE VENUES:
  IEEE Transactions on Intelligent Transportation Systems,
  IEEE Transactions on Intelligent Vehicles,
  IEEE ITSC, IEEE IV (Intelligent Vehicles Symposium),
  Autonomous Robots, Journal of Field Robotics,
  Transportation Research Part C

DOMAIN VOCABULARY:
  LIDAR, RADAR, camera, sensor fusion, SLAM, HD map, NDT, ICP, EKF,
  RRT*, MPC, Stanley, CARLA, KITTI, NuScenes, mAP, RMSE, TTC,
  SAE L0-L5, ISO 26262, SOTIF, V2X, DSRC, C-V2X

METHODOLOGY KEYWORDS:
  sensor fusion (LIDAR+camera+RADAR), SLAM implementation, EKF/UKF localization,
  CARLA simulation testing, mAP evaluation (KITTI/NuScenes), MPC controller design,
  path planning comparison (A*/RRT*/Lattice), ISO 26262 safety analysis
""",

"biology": """================================================================================
TOPIC GUIDE — Biology (General)
================================================================================
FIELD: Natural Sciences / Biology
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Biologi Umum, Biologi Sel, Ekologi, Evolusi, Fisiologi, Biologi Molekuler Dasar

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: biological organism/system studied, hypothesis, experimental design,
  methods (cell culture, animal model, field sampling, molecular technique), key results
  (growth rate, survival rate, gene expression fold change, enzyme activity, ecological index),
  and biological significance.

INTRODUCTION ELEMENTS:
  - Biological significance of organism or system studied.
  - Problem or phenomenon: population decline, disease mechanism, adaptation, ecological change.
  - Existing knowledge gaps.
  - Hypothesis and research objectives.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Cell biology: cell cycle (G1/S/G2/M), apoptosis (caspase cascade), organelle functions.
  - Genetics/molecular: central dogma (DNA→RNA→protein), gene regulation, epigenetics.
  - Ecology: trophic levels, food web, energy flow; diversity indices (Shannon H', Simpson).
  - Evolution: natural selection, genetic drift, mutation, speciation.
  - Physiology: homeostasis, hormone regulation, nervous system, immune response.
  - Taxonomy/systematics: phylogenetic analysis (ML, Bayesian), barcoding (COI, ITS).

METHODOLOGY:
  Common section name: "Materials and Methods"
  - Cell culture: cell line (ATCC); media (DMEM, RPMI), passage, confluence.
  - Animal model: Mus musculus/Rattus norvegicus; ethics (IACUC); n=5–10 per group.
  - Molecular: DNA extraction (CTAB/kit), PCR (thermocycler conditions), gel electrophoresis; RT-qPCR (2^-ΔΔCt); Western blot.
  - Histology: fixation (formalin 10%), paraffin embedding, H&E stain, microscopy.
  - Ecology: quadrat/transect sampling; species identification; diversity (Shannon H', Simpson D, Margalef R).
  - Phylogenetics: MEGA software; multiple alignment (MUSCLE/CLUSTALW); ML/neighbor-joining tree; bootstrap 1000.
  - Statistical: ANOVA, t-test; non-parametric (Kruskal-Wallis); SPSS/R.

TYPICAL RESULTS & DISCUSSION:
  - Cell viability: MTT IC50 5–50 µM for cytotoxic agent.
  - Gene expression: 2^-ΔΔCt = 2–5 fold up/down regulation; reference gene GAPDH/β-actin.
  - Histopathology: cell density, pathological changes described qualitatively.
  - Diversity indices: Shannon H' = 1.5–3.5 for moderately diverse community.
  - Body weight: treated group -10 to -20% vs. control (toxicity indicator).
  Tables: treatment comparison, diversity index table, PCR primer list.
  Figures: bar chart gene expression, phylogenetic tree, histopathology micrograph.

TYPICAL FIGURES:
  - Bar chart: gene expression (fold change ± SEM).
  - Phylogenetic tree (neighbor-joining or ML bootstrap consensus).
  - Histopathology micrograph (H&E stain).
  - Survival/growth curve over time.
  - Species diversity bar chart by location/treatment.

TYPICAL TABLES:
  - Primer sequences: gene | forward | reverse | product size (bp) | annealing T (°C).
  - Diversity indices by site: site | S | N | H' | D | J'.
  - Treatment comparison: treatment | mean ± SD | ANOVA F | p | notation.

CONCLUSION CHARACTERISTICS:
  - Biological hypothesis supported/rejected with mechanistic explanation.
  - Conservation/medical/agricultural implications.
  - Limitations: model organism generalizability, sample size, controlled conditions.
  - Future: in vivo validation, mechanistic pathway elucidation, larger ecological survey.

COMMON REFERENCE VENUES:
  PLoS ONE, Biology Letters (Royal Society), Journal of Experimental Biology,
  Ecology and Evolution, BMC Biology, Molecular Biology and Evolution,
  Biotropia (SEAMEO BIOTROP), Berita Biologi (LIPI/BRIN)

DOMAIN VOCABULARY:
  cell cycle, apoptosis, caspase, RT-qPCR, 2^-ΔΔCt, GAPDH, Western blot,
  Shannon H', Simpson D, Margalef R, MEGA, MUSCLE, bootstrap, histopathology,
  H&E stain, IACUC, CTAB, thermocycler, neighbor-joining

METHODOLOGY KEYWORDS:
  RT-qPCR (2^-ΔΔCt), MTT viability assay, Western blot, H&E histopathology,
  phylogenetic analysis (MEGA software), Shannon diversity index, quadrat/transect sampling,
  ANOVA + DMRT, IACUC animal ethics
""",

"biomedical_engineering": """================================================================================
TOPIC GUIDE — Biomedical Engineering
================================================================================
FIELD: Engineering / Biomedical Sciences
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Instrumentasi Medis, Biomaterial, Biomekanik, Biosignal Processing, Medical Imaging Engineering

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: biomedical device/system designed, biological target (tissue, organ,
  biosignal), engineering methods (finite element analysis, signal processing, in vitro/in vivo test),
  key performance metrics (sensitivity µV, SNR dB, accuracy %, compressive strength MPa,
  biocompatibility cytotoxicity %), and clinical relevance.

INTRODUCTION ELEMENTS:
  - Clinical need: unmet medical challenge (affordable diagnostic, improved implant, signal noise).
  - Biomedical engineering approach: device design, materials engineering, biosignal processing.
  - Current device limitations: invasiveness, cost, accuracy, biocompatibility issues.
  - Research gap: new material, signal algorithm, device miniaturization.
  - Objectives: design, fabricate, evaluate biomedical system.

LITERATURE REVIEW:
  Common section name: "Background" / "Related Work"
  - Biosignals: ECG (0.5–150 Hz, 0.5–5 mV), EMG (10–500 Hz, 50 µV–5 mV), EEG (0.5–100 Hz, 10–100 µV), SpO2.
  - Signal processing: filtering (Butterworth, Chebyshev, notch 50/60 Hz), FFT, wavelet transform.
  - Biomaterials: metals (Ti-6Al-4V, Co-Cr), ceramics (HA, TCP), polymers (PEEK, UHMWPE), composites.
  - Biocompatibility: ISO 10993 standards; cytocompatibility (cell viability assay).
  - Medical devices: FDA/BPOM classification (Class I/II/III), regulatory pathway.
  - FEA (Finite Element Analysis): bone/implant interaction, stress distribution, fatigue analysis.
  - Machine learning in biomedical: ECG arrhythmia detection, cancer image segmentation.

METHODOLOGY:
  Common section name: "Materials and Methods" / "Design and Methods"
  - Device design: circuit (op-amp, instrumentation amplifier INA128), microcontroller (Arduino, STM32), PCB design.
  - Signal acquisition: sampling rate (1000 Hz for ECG/EMG), resolution (12/16-bit ADC), electrode type.
  - Signal processing: bandpass filter design, baseline wander removal, peak detection algorithm.
  - Biomaterial characterization: XRD (phase), FTIR (functional groups), SEM/EDX (morphology), compressive strength (universal testing machine).
  - Biocompatibility: ISO 10993; MTT assay (cell viability %); hemolysis test (<5%).
  - FEA: ANSYS/Abaqus; mesh convergence; load cases (gait, peak forces).
  - Clinical validation: sensitivity, specificity, comparison vs. gold standard device.

TYPICAL RESULTS & DISCUSSION:
  - ECG amplitude: P-wave 0.1–0.3 mV; QRS complex 0.5–3.0 mV; SNR >30 dB (good quality).
  - EMG classification accuracy (ML): 90–98% for gesture recognition.
  - Implant compressive strength: cortical bone 100–230 MPa; HA scaffold 10–50 MPa.
  - Cell viability (MTT): biocompatible material >80% at 100 µg/mL.
  - FEA von Mises stress: must be < material yield strength with safety factor >2.
  Tables: filter specifications, material mechanical properties, classification performance.
  Figures: ECG signal before/after filtering, SEM micrograph, FEA stress contour.

TYPICAL FIGURES:
  - ECG/EMG signal before and after filtering.
  - SEM micrograph (biomaterial surface morphology).
  - FEA von Mises stress distribution on implant.
  - Frequency spectrum (FFT of biosignal).
  - Confusion matrix (ML classifier).

TYPICAL TABLES:
  - Signal specs: parameter | designed | measured | standard reference.
  - Material properties: material | XRD phases | E (GPa) | σyield | porosity%.
  - Classifier performance: method | accuracy | sensitivity | specificity | F1.

CONCLUSION CHARACTERISTICS:
  - Device/material meets target biomedical performance.
  - Biocompatibility confirmed per ISO 10993.
  - Contribution to affordable/accessible medical technology.
  - Limitations: in vitro only, small clinical sample, single population.
  - Future: clinical trial, miniaturization, wireless/IoT integration, regulatory approval.

COMMON REFERENCE VENUES:
  IEEE Transactions on Biomedical Engineering, Medical & Biological Engineering & Computing,
  Journal of Biomedical Materials Research, Biomaterials,
  Computers in Biology and Medicine, Annals of Biomedical Engineering,
  Biomedical Signal Processing and Control

DOMAIN VOCABULARY:
  ECG, EMG, EEG, SpO2, INA128, ADC, SNR, notch filter, Butterworth,
  HA (hydroxyapatite), TCP, PEEK, ISO 10993, MTT assay, hemolysis,
  FEA, von Mises, ANSYS, XRD, FTIR, SEM/EDX, universal testing machine

METHODOLOGY KEYWORDS:
  instrumentation amplifier circuit design, bandpass/notch filter design,
  XRD/FTIR/SEM characterization, MTT biocompatibility assay (ISO 10993),
  FEA (ANSYS/Abaqus) mesh convergence, clinical validation (sensitivity/specificity),
  ECG peak detection algorithm
""",

"blockchain": """================================================================================
TOPIC GUIDE — Blockchain & Distributed Ledger Technology
================================================================================
FIELD: Computer Science / Information Systems
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Blockchain, Smart Contract, DeFi, NFT, Supply Chain Blockchain, Healthcare Blockchain

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: blockchain application domain, consensus mechanism used,
  system design/architecture, evaluation methodology (testnet deployment, simulation,
  security analysis), key metrics (transaction throughput TPS, latency ms, gas cost,
  security properties), and comparison with centralized alternative.

INTRODUCTION ELEMENTS:
  - Blockchain definition: distributed ledger, immutability, decentralization, trustless.
  - Application domain motivation: supply chain transparency, data integrity, DeFi, identity.
  - Limitations of centralized systems: single point of failure, manipulation, lack of transparency.
  - Research gap: scalability solution, specific domain integration, privacy-preserving approach.
  - Objectives: design, implement, evaluate blockchain-based system.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - Bitcoin (Nakamoto 2008): PoW consensus; UTXO model; mining.
  - Ethereum: smart contracts (Solidity); EVM; PoS (The Merge 2022); ERC-20, ERC-721.
  - Permissioned blockchains: Hyperledger Fabric (Apache), Quorum (JPMorgan); private/consortium.
  - Consensus mechanisms: PoW, PoS, DPoS, PBFT, Raft; throughput/security tradeoff.
  - Scalability: Layer 2 (Lightning Network, Optimistic Rollups, zkRollups), sharding.
  - Privacy: zero-knowledge proofs (ZKP), ring signatures, stealth addresses.
  - Smart contract security: reentrancy, integer overflow, front-running; Mythril, Slither auditing.
  - Supply chain blockchain: Walmart Food Trust (IBM Food Trust), Maersk TradeLens.

METHODOLOGY:
  Common section name: "System Design and Implementation"
  - Architecture: blockchain platform choice (Ethereum/Fabric/Polygon), network topology (nodes, validators).
  - Smart contract development: Solidity/Go Chaincode; features (data recording, access control, event logging).
  - Development tools: Hardhat/Truffle, Ganache (local testnet), MetaMask, IPFS for off-chain storage.
  - Deployment: local testnet, public testnet (Sepolia/Mumbai), or Hyperledger Fabric network.
  - Performance evaluation: Caliper benchmark (Hyperledger); transaction throughput (TPS), latency (ms).
  - Security analysis: Slither/Mythril static analysis; manual code review; attack simulation (reentrancy test).
  - Cost analysis: gas estimation (ETH); operational cost comparison.

TYPICAL RESULTS & DISCUSSION:
  - Throughput: Ethereum mainnet 15–30 TPS; Hyperledger Fabric 100–3000 TPS; Polygon 65,000 TPS.
  - Latency: Ethereum ~13s block time; Fabric 0.5–2s; L2 Rollup 1–5s.
  - Smart contract size: <24KB bytecode limit on Ethereum.
  - Gas cost: ERC-20 transfer ~21,000 gas; complex contract 100,000–500,000 gas.
  - Security: Mythril scan results (0 critical vulnerabilities after fixes).
  Tables: performance comparison (blockchain platforms), gas cost estimation, security audit findings.
  Figures: network architecture diagram, transaction latency CDF, throughput vs. load graph.

TYPICAL FIGURES:
  - System architecture/network topology diagram.
  - Throughput (TPS) vs. transaction load graph.
  - Transaction latency CDF (cumulative distribution).
  - Smart contract workflow sequence diagram.
  - Bar chart: cost comparison (blockchain vs. centralized).

TYPICAL TABLES:
  - Platform comparison: blockchain | consensus | TPS | latency | privacy | cost.
  - Gas cost: function | gas used | ETH cost (current price).
  - Security audit: vulnerability | severity | status (fixed/acknowledged).

CONCLUSION CHARACTERISTICS:
  - Blockchain system achieves transparency, immutability, and decentralization goals.
  - Performance within acceptable bounds for target application.
  - Security vulnerabilities addressed.
  - Limitations: scalability bottleneck, energy cost (PoW), regulatory uncertainty.
  - Future: L2 integration, cross-chain interoperability, zero-knowledge privacy, CBDC.

COMMON REFERENCE VENUES:
  IEEE Access, Future Generation Computer Systems, Computers & Security,
  Journal of Network and Computer Applications, IEEE Transactions on Engineering Management,
  Blockchain: Research and Applications, IEEE ICBC (International Congress on Blockchain and Cryptocurrency)

DOMAIN VOCABULARY:
  blockchain, smart contract, consensus, PoW, PoS, PBFT, Hyperledger Fabric,
  Solidity, EVM, ERC-20, ERC-721, IPFS, ZKP, reentrancy, gas, TPS,
  Layer 2, rollup, DeFi, NFT, Truffle, Hardhat, Slither, Mythril

METHODOLOGY KEYWORDS:
  Solidity smart contract development, Hyperledger Fabric Caliper benchmarking,
  Ganache/Hardhat local testnet deployment, gas estimation, Mythril/Slither security audit,
  throughput/latency measurement, IPFS integration
""",

"chemical_engineering": """================================================================================
TOPIC GUIDE — Chemical Engineering
================================================================================
FIELD: Engineering / Chemical Engineering
DEFAULT CITATION STYLE: APA or AIChE
SUBDISCIPLINE: Teknik Kimia, Proses Kimia, Reaksi Kimia, Pemisahan, Energi Kimia, Bioprosess

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: chemical process or unit operation studied, scale (lab/pilot/industrial),
  operating conditions (T °C, P bar, flow rate L/h, feed concentration mol/L), key results
  (conversion %, yield %, selectivity, energy efficiency, product purity %), and comparison
  with existing process benchmark.

INTRODUCTION ELEMENTS:
  - Industrial process context: petroleum refining, petrochemicals, food/pharma processing, biofuels.
  - Process inefficiency or environmental challenge: energy intensity, waste generation, safety hazard.
  - Research gap: process optimization, new catalyst/solvent, intensification method, green chemistry.
  - Objectives: design, model, optimize, or scale-up chemical process.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Reaction engineering: kinetics (rate law, Arrhenius equation), reactor types (CSTR, PFR, batch).
  - Thermodynamics: phase equilibrium, VLE (vapor-liquid equilibrium), activity coefficients.
  - Separation processes: distillation (McCabe-Thiele), absorption/stripping, extraction, membrane.
  - Catalysis: heterogeneous (surface area BET, pore size, active metal loading), homogeneous, enzymatic.
  - Process simulation: Aspen Plus/HYSYS, CHEMCAD; material/energy balance.
  - Green chemistry: atom economy (% AE), E-factor (kg waste/kg product), solvent selection.
  - Mass and heat transfer: Reynolds analogy, Nusselt number, packed bed pressure drop (Ergun equation).

METHODOLOGY:
  Common section name: "Materials and Methods" / "Experimental Design"
  - Experimental: reactor setup, catalyst preparation (impregnation, sol-gel), characterization (XRD, BET, TPR).
  - Reaction conditions: temperature (°C), pressure (bar), residence time (τ = V/F), feed ratio (stoichiometry).
  - Analytical: GC (conversion/selectivity), HPLC, spectrophotometry, titration.
  - Response Surface Methodology (RSM): Central Composite Design (CCD) or Box-Behnken; ANOVA; optimal conditions.
  - Simulation (Aspen Plus): flowsheet, thermodynamic model (NRTL/UNIQUAC/SRK), convergence.
  - Scale-up: Damköhler number, dimensionless analysis, mass transfer coefficient kLa (bioreactor).
  - Safety: HAZOP (Hazard and Operability Study) for process design.

TYPICAL RESULTS & DISCUSSION:
  - Conversion: equilibrium-limited reactions 60–90%; catalytic 80–99%.
  - Yield: overall process yield 70–95%; side reactions lower selectivity to 85–95%.
  - Catalyst activity: TOF (turnover frequency) = 0.1–10 s⁻¹; stability in 100h test.
  - Energy efficiency: heat integration reduces utility by 20–40%.
  - Separation: distillation column 99+% purity with specific reflux ratio.
  Tables: reaction conditions vs. conversion/yield, catalyst characterization, RSM ANOVA.
  Figures: conversion vs. T/P/time, RSM 3D response surface, process flow diagram.

TYPICAL FIGURES:
  - Conversion/yield vs. temperature or time curve.
  - RSM 3D response surface and contour plot.
  - Aspen Plus process flow diagram (PFD).
  - Catalyst characterization: XRD diffractogram, BET isotherm.
  - Selectivity vs. conversion plot.

TYPICAL TABLES:
  - Experimental matrix (RSM): run | T | P | ratio | conversion | yield.
  - RSM ANOVA: source | SS | df | MS | F | p | R².
  - Catalyst properties: BET area (m²/g) | pore volume (cm³/g) | mean pore size (nm) | metal loading (wt%).

CONCLUSION CHARACTERISTICS:
  - Optimal operating conditions identified with maximized yield/conversion.
  - Catalyst/solvent/process modification effect quantified.
  - Economic/environmental benefit of optimized process.
  - Limitations: lab-scale, simplified model assumptions, single feedstock.
  - Future: pilot-scale demonstration, techno-economic analysis (TEA), lifecycle assessment (LCA).

COMMON REFERENCE VENUES:
  Chemical Engineering Journal, Industrial & Engineering Chemistry Research,
  AIChE Journal, Bioresource Technology, Fuel, Applied Catalysis A/B,
  Separation and Purification Technology, Journal of Cleaner Production

DOMAIN VOCABULARY:
  conversion, yield, selectivity, CSTR, PFR, catalyst, TOF, BET, RSM, CCD,
  Aspen Plus, NRTL, UNIQUAC, E-factor, atom economy, VLE, kLa, HAZOP,
  Arrhenius, McCabe-Thiele, Damköhler number, heat integration, Ergun equation

METHODOLOGY KEYWORDS:
  RSM (Central Composite Design), Aspen Plus simulation, catalyst characterization (XRD/BET/TPR),
  GC/HPLC analysis, ANOVA optimization, kinetic parameter estimation (Arrhenius),
  HAZOP analysis, heat integration (Pinch method), mass transfer coefficient (kLa)
""",

}

def write_topic(name, content):
    path = os.path.join(D, f"{name}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.lstrip())
    print(f"  wrote {name}.txt")

for name, content in TOPICS.items():
    write_topic(name, content)
print(f"gen_08: {len(TOPICS)} topics written.")

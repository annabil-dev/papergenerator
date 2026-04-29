"""Generator: Chemistry, Chemical Engineering, Physics, Materials — 10 topic files"""
import os; D = os.path.dirname(os.path.abspath(__file__))

TOPICS = {

"organic_chemistry_synthesis": """================================================================================
TOPIC GUIDE — Organic Chemistry & Synthesis
================================================================================
FIELD: Chemistry / Organic Chemistry
DEFAULT CITATION STYLE: ACS (American Chemical Society)
SUBDISCIPLINE: Sintesis Organik, Kimia Medisinal, Katalisis Organik, Stereokimia

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: target molecule synthesized, synthetic route (step count),
  yield (%), characterization methods (NMR, MS, IR), key reactivity or biological
  activity (IC50, ee% for asymmetric synthesis).

INTRODUCTION ELEMENTS:
  - Importance of target molecule: pharmaceutical, agrochemical, functional material.
  - Existing synthetic routes and their limitations (low yield, multiple steps, expensive reagents).
  - Research gap: stereoselective synthesis, green chemistry approach, novel scaffold.
  - Objectives: develop efficient synthesis, characterize, evaluate biological activity.

LITERATURE REVIEW:
  Common section name: "Introduction" (integrated literature review typical in ACS style)
  - Target molecule pharmacology/application with key references.
  - Previous synthesis attempts (retrosynthetic analysis).
  - Key reactions used: aldol, Diels-Alder, Suzuki coupling, Grignard, click chemistry.
  - Catalysis: organocatalysis (proline-derived), metal catalysis (Pd, Cu, Ru).
  - Asymmetric synthesis: chiral auxiliaries, asymmetric catalysis, %ee.
  - Green chemistry principles (Anastas & Warner): atom economy, E-factor.

METHODOLOGY:
  Common section name: "Experimental Section" / "Materials and Methods"
  - All reagents: company, purity grade (≥97% typical); anhydrous solvents.
  - Reactions: vessel (flask), atmosphere (N2/Ar), temperature, time, work-up procedure.
  - Purification: column chromatography (silica gel 60, eluent: hexane/EtOAc ratio), recrystallization.
  - Characterization:
    * TLC (Rf values, visualization: UV 254nm or KMnO4 stain).
    * NMR: ¹H NMR (400 or 600 MHz), ¹³C NMR (100 or 150 MHz) — chemical shift δ (ppm), J (Hz).
    * MS: ESI-MS or EI-MS; [M+H]+ or [M+Na]+ m/z values.
    * IR: absorption bands (cm⁻¹) for key functional groups.
    * Melting point (°C) for solids.
  - Biological activity: MTT assay (IC50), enzyme inhibition, antimicrobial MIC.

TYPICAL RESULTS & DISCUSSION:
  - Reaction optimization: yield varies with condition (temperature, catalyst loading, solvent).
  - Typical multistep synthesis yield per step: 60–90%; overall yield: 15–45%.
  - NMR: ¹H NMR data listed with δ, multiplicity (s, d, t, q, m), integration, J values.
  - ¹³C NMR: 8–30 carbon signals depending on complexity.
  - MS: molecular ion peak at correct m/z ± 0.005 Da (HRMS).
  - Biological activity: IC50 5–100 µM (for anticancer/antimicrobial active compounds).
  Tables: reaction condition optimization table (yield vs. variable), compound characterization.
  Figures: NMR spectra, synthetic scheme, structure-activity relationship (SAR) table.

TYPICAL FIGURES:
  - Synthetic scheme (reaction arrows with reagents/conditions above/below).
  - ¹H and ¹³C NMR spectra.
  - ORTEP (crystal structure if X-ray performed).
  - SAR (structure-activity relationship) diagram.
  - Reaction scope table/figure.

TYPICAL TABLES:
  - Optimization table: entry | catalyst | solvent | temp (°C) | time (h) | yield (%).
  - Compound characterization summary: compound # | formula | MW | yield | mp | key NMR.
  - Biological activity: compound | IC50 (µM) | selectivity index.

CONCLUSION CHARACTERISTICS:
  - Successful synthesis with total yield; key steps summarized.
  - Structural confirmation confirmed by spectroscopic data.
  - Biological activity significance if evaluated.
  - Limitations: scale-up feasibility, reaction scope limitations.
  - Future: analog synthesis, in vivo evaluation, process chemistry scale-up.

COMMON REFERENCE VENUES:
  Journal of the American Chemical Society (JACS), Organic Letters,
  Angewandte Chemie International Edition, Chemistry - A European Journal,
  European Journal of Organic Chemistry, Synthesis, Synlett,
  Journal of Organic Chemistry, Organic & Biomolecular Chemistry

DOMAIN VOCABULARY:
  retrosynthesis, yield, ee%, de%, Rf, δ (ppm), J (Hz), m/z, IC50, MTT,
  column chromatography, TLC, recrystallization, aldol, Diels-Alder, Suzuki,
  organocatalysis, chiral, enantiomer, diastereomer, racemic, electrophile, nucleophile

METHODOLOGY KEYWORDS:
  ¹H/¹³C NMR spectroscopy, ESI-MS, HRMS, IR spectroscopy, TLC, column chromatography,
  X-ray crystallography, MTT assay, enzyme inhibition assay, asymmetric synthesis
""",

"analytical_chemistry": """================================================================================
TOPIC GUIDE — Analytical Chemistry
================================================================================
FIELD: Chemistry / Analytical Chemistry
DEFAULT CITATION STYLE: ACS
SUBDISCIPLINE: Kimia Analitik, Pengembangan Metode, Kromatografi, Spektrometri, Sensor, Elektroanalis

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: analyte(s), matrix (water, food, blood, soil),
  method developed (HPLC-UV/MS, GC-FID, voltammetry, colorimetric sensor),
  validation parameters (LOD, LOQ, linear range, recovery %, RSD %), and application.

INTRODUCTION ELEMENTS:
  - Analyte importance: pollutant (pesticide, heavy metal, pharmaceutical), biomarker, food additive.
  - Existing methods and their limitations: complexity, cost, sensitivity, specificity.
  - Research gap: simpler/faster/greener/more sensitive method needed.
  - Objectives: develop, optimize, validate, and apply method in real matrix.

LITERATURE REVIEW:
  Common section name: "Introduction" (integrated in ACS style)
  - Analyte sources, health effects, regulatory limits (WHO, EPA, FDA, BPOM).
  - Existing methods: official methods (AOAC, EPA), literature comparison.
  - Instrumentation principles: HPLC, GC, ICP-OES, AAS, UV-Vis, fluorescence, voltammetry.
  - Sample preparation: SPE, QuEChERS, LLE, DLLME, digestion methods.
  - Green analytical chemistry (GAC): GAPI, AGREE metrics for greenness assessment.

METHODOLOGY:
  Common section name: "Experimental" / "Materials and Methods"
  - Reagents: grade, supplier; reference standards: purity ≥99%.
  - Instrumentation: specific model, detector type, column (stationary phase, size).
  - Chromatographic conditions: mobile phase composition, gradient, flow rate, temperature, injection volume.
  - Sample preparation: extraction procedure (step-by-step).
  - Method validation (ICH Q2(R1) / AOAC):
    * Linearity: concentration range, R² ≥0.9990.
    * LOD = 3.3σ/S; LOQ = 10σ/S (or S/N=3 and S/N=10).
    * Precision: intra-day (RSD% ≤2%) and inter-day (RSD% ≤5%).
    * Accuracy/Recovery: spiked samples at 3 levels, recovery 80–120%.
    * Selectivity: no interference from matrix components.
  - Statistical: regression analysis, ANOVA (method comparison), Student's t-test.

TYPICAL RESULTS & DISCUSSION:
  - Linear range: pesticide in food 0.001–1 mg/L; heavy metal in water 1–500 µg/L.
  - LOD: HPLC-UV 0.01–0.1 mg/L; HPLC-MS/MS 0.001–0.01 µg/L.
  - Recovery: 85–110% (acceptable analytical recovery).
  - RSD%: intra-day <2%; inter-day <5%.
  - R²: ≥0.9990 (excellent linearity).
  - Real sample: analyte detected in X of Y samples; concentration range found.
  Tables: calibration parameters, validation summary, real sample results.
  Figures: calibration curve, chromatogram, sensor response curve, recovery bar chart.

TYPICAL FIGURES:
  - Calibration curve with linear regression equation and R².
  - Chromatogram: blank | standard | spiked sample.
  - Optimization response surface (DoE, if used).
  - Sensor response: cyclic voltammogram or DPV.
  - Recovery bar chart at three concentration levels.

TYPICAL TABLES:
  - Calibration parameters: LOD | LOQ | linear range | R² | slope | intercept.
  - Precision: intra-day | inter-day (mean | RSD%).
  - Recovery: spike level | mean recovery % | RSD%.
  - Method comparison with literature: analyte | method | LOD | matrix.

CONCLUSION CHARACTERISTICS:
  - Method developed, validated, and successfully applied to real samples.
  - Comparison with existing methods: superior sensitivity, simplicity, greener.
  - Limitations: matrix effects, specific instrument required.
  - Future: automation, field-deployable sensor, coupling with other techniques.

COMMON REFERENCE VENUES:
  Analytical Chemistry, Journal of Analytical Atomic Spectrometry,
  Analytica Chimica Acta, Talanta, Microchemical Journal,
  Journal of Chromatography A/B, Food Chemistry, Environmental Science & Technology

DOMAIN VOCABULARY:
  LOD, LOQ, RSD, recovery, linearity, R², SPE, QuEChERS, DLLME, HPLC, GC,
  ICP-OES, AAS, UV-Vis, fluorescence, voltammetry, ICH Q2(R1), AOAC, EPA,
  standard addition, internal standard, matrix effect, signal-to-noise ratio

METHODOLOGY KEYWORDS:
  HPLC-UV, HPLC-MS/MS, GC-FID, GC-MS, ICP-OES, AAS, CV/DPV (voltammetry),
  SPE, QuEChERS, digestion (microwave/wet), method validation (ICH Q2(R1)),
  DoE (response surface methodology), standard addition method
""",

"physical_chemistry": """================================================================================
TOPIC GUIDE — Physical Chemistry & Thermodynamics
================================================================================
FIELD: Chemistry / Physical Chemistry
DEFAULT CITATION STYLE: ACS
SUBDISCIPLINE: Termodinamika, Kinetika Kimia, Elektrokimia, Kimia Kuantum, Permukaan

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: system studied, thermodynamic/kinetic parameters measured
  (ΔG°, ΔH°, ΔS°, kJ/mol; rate constant k; activation energy Ea kJ/mol;
  adsorption capacity qmax mg/g), experimental conditions, main findings.

INTRODUCTION ELEMENTS:
  - Physical chemistry context: reaction mechanism, energy, electrode behavior, adsorption.
  - Specific problem: reaction kinetics, thermodynamic stability, electrode material performance.
  - Theoretical basis: Gibbs free energy, transition state theory, Langmuir/Freundlich isotherm.
  - Research gap: new material, extreme conditions not studied, quantum calculation validation.

LITERATURE REVIEW:
  Common section name: "Introduction" (integrated)
  - Thermodynamic laws and equations: ΔG = ΔH - TΔS; van 't Hoff equation.
  - Reaction kinetics: rate laws, Arrhenius equation (k = Ae^(-Ea/RT)).
  - Electrochemistry: Butler-Volmer equation, Tafel slopes, Cyclic Voltammetry.
  - Adsorption: Langmuir isotherm (monolayer), Freundlich (heterogeneous), BET (multilayer).
  - Computational: DFT calculations (Gaussian, VASP); binding energy, HOMO-LUMO gap.
  - Colloidal chemistry: zeta potential, DLS (dynamic light scattering), particle size.

METHODOLOGY:
  Common section name: "Experimental" / "Materials and Methods"
  - Materials: chemicals, synthesis of nanoparticles/catalyst/electrode.
  - Characterization: XRD (crystal structure, 2θ peaks), FTIR (functional groups, cm⁻¹),
    TGA/DSC (thermal stability, decomposition temperature), BET surface area (m²/g).
  - Electrochemical: cyclic voltammetry (CV), EIS (electrochemical impedance spectroscopy),
    chronoamperometry; reference electrode (Ag/AgCl), counter (Pt), working (modified GCE).
  - Adsorption: batch experiments; varying pH, temperature, initial concentration, contact time.
  - Kinetics: pseudo-first-order and pseudo-second-order models; intraparticle diffusion.
  - Thermodynamics: equilibrium at different temperatures; ln K vs. 1/T (van 't Hoff).
  - DFT: B3LYP/6-311G**, Gaussian09/16 software; geometry optimization, frequency calculation.

TYPICAL RESULTS & DISCUSSION:
  - BET surface area: activated carbon 500–2000 m²/g; MOF 1000–7000 m²/g.
  - Adsorption qmax (Langmuir): methylene blue 50–500 mg/g; heavy metals 20–200 mg/g.
  - Ea (activation energy): typical reactions 20–120 kJ/mol.
  - ΔG°: negative values confirm spontaneous process (typical -5 to -50 kJ/mol).
  - ΔH°: exothermic adsorption -10 to -60 kJ/mol (physisorption <40, chemisorption >40).
  - CV: oxidation/reduction peaks at specific potentials (V vs. Ag/AgCl).
  - DFT HOMO-LUMO gap: organic molecule 3–10 eV.
  Tables: kinetic parameters, isotherm parameters, thermodynamic parameters.
  Figures: adsorption isotherm fit, van 't Hoff plot, CV curve, XRD diffractogram.

TYPICAL FIGURES:
  - Adsorption isotherm: qe vs. Ce with Langmuir/Freundlich fit.
  - van 't Hoff plot: ln K vs. 1/T.
  - CV curves at different scan rates.
  - XRD diffractogram with peak indexing.
  - TGA/DSC thermogram.
  - DFT optimized structure with MEP map.

TYPICAL TABLES:
  - Isotherm parameters: model | qmax (mg/g) | b (L/mg) | R² | χ².
  - Kinetic parameters: model | k | qe (calc) | R².
  - Thermodynamic: T (K) | ΔG° | ΔH° | ΔS° (kJ/mol or J/mol·K).

CONCLUSION CHARACTERISTICS:
  - Main thermodynamic/kinetic findings with physical interpretation.
  - Practical relevance: catalysis, environmental remediation, energy storage.
  - Limitations: ideal conditions, computational basis set limitations.
  - Future: pilot-scale study, molecular dynamics, experimental-computational synergy.

COMMON REFERENCE VENUES:
  Physical Chemistry Chemical Physics, Journal of Physical Chemistry A/B/C,
  Journal of Chemical Physics, Langmuir, Electrochimica Acta,
  Journal of Colloid and Interface Science, Chemical Engineering Journal

DOMAIN VOCABULARY:
  ΔG°, ΔH°, ΔS°, Ea, Arrhenius, Langmuir, Freundlich, BET, XRD, FTIR, TGA,
  DSC, CV, EIS, Tafel, DFT, HOMO-LUMO, zeta potential, DLS, adsorption,
  isotherm, kinetics, pseudo-first-order, pseudo-second-order, chemisorption, physisorption

METHODOLOGY KEYWORDS:
  BET surface area, XRD (Bragg's law), FTIR spectroscopy, TGA/DSC,
  cyclic voltammetry (CV), EIS (Nyquist plot), adsorption batch experiment,
  DFT (Gaussian B3LYP/6-311G**), van 't Hoff analysis, Langmuir/Freundlich fitting
""",

"structural_engineering": """================================================================================
TOPIC GUIDE — Structural Engineering
================================================================================
FIELD: Engineering / Civil Engineering
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Teknik Struktur, Beton Bertulang, Baja, Jembatan, Beban Gempa, Beton Prategang

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: structural element or system studied (beam, column, frame, bridge),
  material properties, loading conditions, analysis method (FEM, experimental, analytical),
  key results (load-carrying capacity kN, deflection mm, ductility ratio, failure mode).

INTRODUCTION ELEMENTS:
  - Structural safety and serviceability importance.
  - Problem: inadequate code for new material/condition, structural deficiency, seismic vulnerability.
  - Research gap: new fiber-reinforced concrete, UHPC, recycled aggregate, combined loading.
  - Objectives: experimental investigation, FEM validation, parametric study.

LITERATURE REVIEW:
  Common section name: "Literature Review"
  - Material mechanics: stress-strain relationship (concrete: Hognestad parabola; steel: bilinear).
  - Reinforced concrete: flexural theory (equivalent stress block ACI 318), shear design.
  - Failure modes: flexure (under-reinforced vs. over-reinforced), shear (diagonal tension), compression.
  - Seismic design: capacity design principle, ductility classification, response spectrum.
  - FEM software: ABAQUS, SAP2000, ANSYS; nonlinear analysis (concrete damage plasticity).
  - Modern materials: GFRP rebar, UHPC, fiber-reinforced concrete (FRC), self-compacting concrete (SCC).
  - Codes: ACI 318, SNI 2847, Eurocode 2 (EC2) design provisions.

METHODOLOGY:
  Common section name: "Experimental Program" / "Methods"
  - Material testing: concrete compressive strength f'c (MPa) — cylinder 150×300mm; steel yield stress fy (MPa).
  - Specimen: dimensions, reinforcement ratio ρ (%), stirrup spacing s (mm).
  - Test setup: loading frame, support conditions (simple span), LVDT for deflection.
  - Loading: monotonic (static); cyclic (seismic simulation); rate of loading 0.2 kN/min.
  - Measurements: load (kN), deflection at midspan (mm), strain gauges on rebar (µε).
  - FEM: ABAQUS; concrete damage plasticity model; mesh size 25mm; validation criteria.
  - Analysis: load-deflection curve, crack pattern, ultimate load, ductility ratio = δu/δy.

TYPICAL RESULTS & DISCUSSION:
  - Concrete strength: normal 20–50 MPa; high strength 50–120 MPa; UHPC >150 MPa.
  - Ultimate load: beam 50–500 kN depending on size and reinforcement.
  - Deflection at service: ≤L/360 (serviceability criterion); at failure: 20–60 mm.
  - Ductility ratio: ductile design ≥3.0; minimum SMRF requirement ≥5.0.
  - FEM vs. experiment deviation: acceptable ≤10%.
  - Crack width: allowed ≤0.3mm (serviceability); first crack load ~30–40% of ultimate.
  Tables: material properties, specimen details, load and deflection at key stages.
  Figures: load-deflection curves, crack patterns at failure, FEM stress contour.

TYPICAL FIGURES:
  - Load-deflection curve with key points marked (cracking, yielding, ultimate).
  - Crack pattern diagram at failure.
  - FEM stress/strain contour plot.
  - Bar chart: ultimate load capacity by variable (reinforcement ratio, concrete grade).
  - Hysteresis loops (for cyclic loading studies).

TYPICAL TABLES:
  - Material properties: f'c (MPa) | fy (MPa) | fu (MPa) | Es (MPa).
  - Specimen data: beam ID | dimensions | ρ (%) | stirrup spacing.
  - Test results: Pcr (kN) | Py (kN) | Pu (kN) | δu (mm) | ductility ratio | failure mode.

CONCLUSION CHARACTERISTICS:
  - Key findings on load capacity, deflection, and failure mode.
  - Effect of variable (reinforcement, concrete grade, fiber content) on performance.
  - FEM model accuracy confirmed.
  - Practical design recommendations.
  - Limitations: scale effect, single load type, monotonic only.
  - Future: full-scale testing, long-term durability, optimization.

COMMON REFERENCE VENUES:
  Engineering Structures, Journal of Structural Engineering (ASCE),
  Construction and Building Materials, Cement and Concrete Composites,
  Structural Concrete, Magazine of Concrete Research, Thin-Walled Structures

DOMAIN VOCABULARY:
  f'c, fy, ACI 318, SNI 2847, EC2, ductility, SMRF, UHPC, FRC, GFRP,
  LVDT, strain gauge, load-deflection, CDP (concrete damage plasticity),
  shear, flexure, torsion, buckling, finite element method, ABAQUS, SAP2000

METHODOLOGY KEYWORDS:
  four-point bending test, axial compression test, cyclic loading test,
  FEM (ABAQUS/ANSYS/SAP2000), concrete damage plasticity model,
  reinforcement strain gauging, LVDT deflection measurement, material coupon test
""",

"geotechnical_engineering": """================================================================================
TOPIC GUIDE — Geotechnical Engineering
================================================================================
FIELD: Engineering / Civil Engineering
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Teknik Geoteknik, Fondasi, Tanah Lunak, Perbaikan Tanah, Longsoran, Terowongan

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: soil type, site location, geotechnical problem
  (foundation settlement, slope stability, liquefaction), method (field test, lab test, FEM),
  key results (bearing capacity kPa, settlement mm, FoS safety factor, undrained shear strength Su kPa).

INTRODUCTION ELEMENTS:
  - Geotechnical problem in the region: soft clay, expansive soil, slope failures.
  - Importance of ground improvement for infrastructure development.
  - Research gap: new improvement technique, new site condition, cost-effective method.
  - Objectives: characterize, analyze, and recommend improvement.

LITERATURE REVIEW:
  Common section name: "Literature Review"
  - Soil classification: USCS, AASHTO; grain size distribution, Atterberg limits.
  - Soft soil characteristics: low bearing capacity, high compressibility (Cc), slow consolidation.
  - Ground improvement: preloading + vertical drains (PVD), deep mixing, stone columns, grouting.
  - Settlement analysis: Terzaghi 1D consolidation; Cc (compression index), Cs (recompression).
  - Slope stability: Bishop simplified method, Fellenius; FoS >1.5 (minimum requirement).
  - Foundation types: shallow (spread footing), deep (pile foundation).
  - SPT (N-value) and CPT (qc, fs) interpretation for soil bearing capacity.

METHODOLOGY:
  Common section name: "Research Method" / "Materials and Methods"
  - Site investigation: borehole logs (BH), SPT N-value, CPT qc (MPa), laboratory samples.
  - Lab tests: grain size analysis, Atterberg limits (LL, PL, PI), consolidation test (Oedometer),
    triaxial test (UU/CU/CD), direct shear, unconfined compressive strength (UCS).
  - Field tests: vane shear test (Su kPa), plate load test, permeability (slug test).
  - Settlement calculation: Terzaghi (St = Cc/(1+e0) × H × log(σ'f/σ'0)).
  - Slope stability: SLOPE/W or GeoStudio FEM; FoS deterministic or probabilistic.
  - Ground improvement monitoring: settlement plates, piezometers, inclinometers.

TYPICAL RESULTS & DISCUSSION:
  - Su (undrained shear strength): soft clay 10–30 kPa; medium 30–60 kPa; stiff >60 kPa.
  - SPT N-value: loose sand N=4–10; medium N=10–30; dense N=30–50.
  - Settlement: total S = 50–500 mm (soft clay under embankment); after improvement 20–100 mm.
  - Time for 90% consolidation: T90 = 6 months – 3 years for soft clay.
  - FoS: unstable slope <1.0; marginal 1.0–1.5; stable >1.5.
  - With PVD: T90 reduced from 2 years to 6–8 months.
  Tables: soil profile summary, lab test results, settlement calculations.
  Figures: borehole log, consolidation curve, FoS vs. time/treatment, settlement monitoring.

TYPICAL FIGURES:
  - Borehole log / CPT profile.
  - Grain size distribution curve.
  - Consolidation curve (e-log p).
  - Settlement vs. time curve (measured vs. predicted).
  - Slope stability analysis output (failure surface with FoS).

TYPICAL TABLES:
  - Soil profile: depth | USCS | N | Su | γ | LL | PL | PI | Cc | Cs | e0.
  - Settlement calculation: layer | H (m) | Cc | e0 | σ'0 | σ'f | ΔS (mm).
  - FoS comparison: method | FoS (original) | FoS (after improvement).

CONCLUSION CHARACTERISTICS:
  - Soil characterization findings.
  - Settlement or stability analysis results.
  - Ground improvement effectiveness.
  - Design recommendations.
  - Limitations: limited boreholes, 2D analysis only.
  - Future: 3D FEM, real-time monitoring, probabilistic analysis.

COMMON REFERENCE VENUES:
  Géotechnique, Canadian Geotechnical Journal, Journal of Geotechnical and Geoenvironmental Engineering (ASCE),
  Computers and Geotechnics, Engineering Geology, Soils and Foundations,
  Geotextiles and Geomembranes, Ground Improvement

DOMAIN VOCABULARY:
  Su, N-value, qc, Cc, Cs, e0, LL, PL, PI, USCS, SPT, CPT, vane shear,
  triaxial test, oedometer, consolidation, preloading, PVD, FoS, Bishop method,
  piezometer, inclinometer, settlement plate, GeoStudio, PLAXIS

METHODOLOGY KEYWORDS:
  SPT, CPT, borehole sampling, Oedometer consolidation test, triaxial test (UU/CU/CD),
  Atterberg limits, grain size analysis, plate load test, vane shear test,
  slope stability analysis (SLOPE/W), FEM (PLAXIS), settlement monitoring
""",

"fluid_mechanics_thermodynamics": """================================================================================
TOPIC GUIDE — Fluid Mechanics & Thermodynamics / Heat Transfer
================================================================================
FIELD: Engineering / Mechanical Engineering
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Mekanika Fluida, Termodinamika, Perpindahan Panas, Turbin, HVAC

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: system studied (heat exchanger, turbine, nozzle, HVAC duct),
  working fluid, operating conditions (pressure kPa, temperature °C, flow rate m/s or L/min),
  analysis method (CFD, experimental, analytical), key results (heat transfer coefficient W/m²K,
  Nusselt number, COP, efficiency %, pressure drop Pa).

INTRODUCTION ELEMENTS:
  - Energy challenge and thermal system efficiency importance.
  - Specific problem: heat exchanger performance, turbine blade cooling, renewable energy system.
  - Research gap: novel geometry, nanofluid, new operating condition, CFD validation need.
  - Objectives: characterize, optimize, improve thermal performance.

LITERATURE REVIEW:
  Common section name: "Literature Review"
  - Governing equations: continuity, Navier-Stokes, energy equation.
  - Dimensionless numbers: Reynolds (Re = ρVD/µ), Nusselt (Nu = hD/k), Prandtl (Pr = µcp/k),
    Grashof (Gr), Rayleigh (Ra = Gr·Pr).
  - Heat transfer correlations: Dittus-Boelter, Gnielinski (convection); Stefan-Boltzmann (radiation).
  - Turbulence models: k-ε, k-ω SST (ANSYS Fluent/CFX).
  - Thermodynamic cycles: Rankine, Brayton, refrigeration (COP).
  - Nanofluids: thermal conductivity enhancement, preparation.
  - Heat exchanger: LMTD method, NTU-ε method, TEMA standards.

METHODOLOGY:
  Common section name: "Experimental Setup and Methodology" / "Numerical Methods"
  - Experimental: test rig description, instrumentation (thermocouples ±0.5°C, pressure transducer ±0.25% FS, flow meter).
  - Fluid: water, air, nanofluid (Al2O3/water, TiO2/water, concentration 0.1–2.0 vol%).
  - CFD: ANSYS Fluent; 3D model; mesh independence study; turbulence model k-ω SST.
  - Boundary conditions: inlet velocity profile, constant wall heat flux or temperature.
  - Measured: inlet/outlet temperature, pressure drop, heat transfer rate Q = ṁ·cp·ΔT.
  - Performance: Nu = f(Re, Pr); friction factor f; thermal performance factor η = (Nu/Nu0)/(f/f0)^(1/3).
  - Uncertainty analysis: Kline & McClintock method.

TYPICAL RESULTS & DISCUSSION:
  - Re range: laminar <2300; transitional 2300–4000; turbulent >4000.
  - Nu: turbulent pipe flow Nu = 0.023·Re^0.8·Pr^0.4 (Dittus-Boelter); experimental matches ±10%.
  - Heat transfer enhancement with nanofluid: 5–25% improvement.
  - COP: air conditioning 3.0–5.0; refrigeration 1.5–3.0.
  - Pressure drop penalty: nanofluid increases ΔP by 3–15%.
  - Thermal performance factor: optimal nanofluid concentration η = 1.1–1.3.
  Tables: nanofluid properties, Nu and f at various Re, CFD vs. experiment comparison.
  Figures: velocity/temperature contour plots (CFD), Nu vs. Re, temperature distribution.

TYPICAL FIGURES:
  - CFD contour: temperature distribution, velocity streamlines, pressure contour.
  - Nu vs. Re curve (comparison: baseline vs. nanofluid/modified geometry).
  - Pressure drop vs. flow rate.
  - Experimental test rig schematic diagram.
  - Uncertainty bar chart.

TYPICAL TABLES:
  - Thermo-physical properties: fluid | density (kg/m³) | cp (J/kgK) | k (W/mK) | µ (Pa·s).
  - Nu and f at different Re: Re | Nu_exp | Nu_corr | deviation% | f_exp | f_corr.
  - CFD mesh independence: mesh size | Nu | f | deviation%.

CONCLUSION CHARACTERISTICS:
  - Performance improvement quantified (Nu increase %, efficiency gain).
  - Optimal operating conditions identified.
  - CFD validated against experiment (within acceptable error %).
  - Practical implications for heat exchanger design.
  - Limitations: steady-state only, single orientation, limited Re range.
  - Future: unsteady analysis, different geometries, cost-benefit analysis.

COMMON REFERENCE VENUES:
  International Journal of Heat and Mass Transfer, Applied Thermal Engineering,
  Energy Conversion and Management, International Communications in Heat and Mass Transfer,
  Journal of Heat Transfer (ASME), Experimental Thermal and Fluid Science, Energy

DOMAIN VOCABULARY:
  Re, Nu, Pr, f, COP, LMTD, NTU-ε, k-ω SST, k-ε, nanofluid, Al2O3, TiO2,
  Dittus-Boelter, Gnielinski, heat flux, convection, conduction, radiation,
  HVAC, turbine, compressor, Rankine cycle, Brayton cycle, entropy, exergy

METHODOLOGY KEYWORDS:
  CFD (ANSYS Fluent), k-ω SST turbulence model, mesh independence study,
  experimental heat exchanger test rig, thermocouple measurement, PIV (if flow visualization),
  LMTD/NTU-ε method, uncertainty analysis (Kline-McClintock), Nusselt correlation
""",

"metallurgy_materials": """================================================================================
TOPIC GUIDE — Metallurgy & Materials Science
================================================================================
FIELD: Materials Science / Metallurgy
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Metalurgi, Korosi, Paduan, Perlakuan Panas, Komposit Metal, Material Fungsional

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: material system (alloy composition, matrix/reinforcement),
  processing route (casting, heat treatment T/time, sintering), characterization methods,
  key mechanical/corrosion properties (UTS MPa, YS MPa, elongation %, HV hardness,
  corrosion rate mm/year, icorr µA/cm²).

INTRODUCTION ELEMENTS:
  - Material application demand: aerospace, automotive, biomedical, energy.
  - Limitation of current material: low strength, poor corrosion resistance, high cost.
  - Research gap: new alloy composition, heat treatment effect, surface modification.
  - Objectives: fabricate, characterize microstructure and properties, evaluate performance.

LITERATURE REVIEW:
  Common section name: "Literature Review"
  - Alloy systems: aluminum alloys (AA2xxx, AA6xxx, AA7xxx series), titanium (Ti-6Al-4V), stainless steel (316L, 304).
  - Microstructure: grain size (µm), phase constitution (XRD), precipitates (TEM/SEM-EDS).
  - Mechanical properties: tensile (UTS, YS, elongation), hardness (HV, HRC), fatigue, fracture.
  - Heat treatment: annealing, quenching, aging (T6 temper: solution + precipitation hardening).
  - Corrosion: galvanic, pitting, crevice; Tafel analysis, EIS (Nyquist plot).
  - Composites: MMC (metal matrix composite) with SiC, Al2O3 reinforcement.

METHODOLOGY:
  Common section name: "Experimental Procedure" / "Materials and Methods"
  - Material: composition (wt%), source, processing (casting, forging, rolling).
  - Heat treatment: furnace temperature (°C), time (h), quench medium, aging temperature/time.
  - Characterization:
    * XRD: 2θ range 20–80°, Cu Kα radiation, Rietveld refinement.
    * SEM: 15–20 kV; morphology, fracture surface; EDS for composition mapping.
    * TEM: 200 kV; phase identification, dislocation density.
  - Mechanical testing: tensile (ASTM E8/E8M); hardness (HV0.5 or HV1); impact (Charpy ASTM E23).
  - Corrosion: 3.5% NaCl solution; potentiodynamic polarization; EIS.
  - Statistical analysis: ANOVA; n ≥3 replicates per condition.

TYPICAL RESULTS & DISCUSSION:
  - Al alloy (T6): UTS = 300–550 MPa; YS = 270–500 MPa; elongation = 8–15%.
  - Hardness: Al alloy T6 HV 100–150; steel 304 HV 200–250; Ti-6Al-4V HV 300–380.
  - Grain size: 10–100 µm (varies with heat treatment); finer = higher strength (Hall-Petch).
  - Corrosion rate: Al alloy 0.01–0.5 mm/year; stainless steel 0.001–0.01 mm/year.
  - Ecorr: Al alloy -0.7 to -1.2 V vs. SCE; icorr 1–100 µA/cm².
  Tables: heat treatment conditions, mechanical properties summary, corrosion parameters.
  Figures: XRD diffractogram, SEM microstructure, tensile stress-strain curve, Nyquist plot.

TYPICAL FIGURES:
  - XRD diffractogram with phase identification.
  - SEM microstructure (before/after heat treatment).
  - Stress-strain curve (tensile test).
  - Potentiodynamic polarization (Tafel) curve.
  - Nyquist and Bode plots (EIS).
  - TEM bright-field/dark-field with diffraction pattern.

TYPICAL TABLES:
  - Alloy composition (wt%) by EDS/XRF.
  - Mechanical properties: condition | UTS | YS | elongation | HV.
  - Corrosion: Ecorr | icorr | βa | βc | CR (mm/year).

CONCLUSION CHARACTERISTICS:
  - Microstructure-property correlation established.
  - Optimal heat treatment condition for best mechanical/corrosion balance.
  - Physical mechanism explanation (precipitation hardening, grain refinement).
  - Limitations: lab scale, single environment, limited alloy compositions.
  - Future: fatigue testing, in-vivo biocompatibility, scale-up fabrication.

COMMON REFERENCE VENUES:
  Acta Materialia, Materials Science and Engineering A, Corrosion Science,
  Journal of Alloys and Compounds, Materials Characterization,
  Metallurgical and Materials Transactions A/B, Surface & Coatings Technology

DOMAIN VOCABULARY:
  UTS, YS, elongation, HV, HRC, XRD, SEM, TEM, EDS, EIS, Ecorr, icorr,
  Hall-Petch, Rietveld, grain size, precipitation hardening, T6 temper, aging,
  MMC, SiC, Al2O3, corrosion rate, Tafel, passivation, dendrite, martensite

METHODOLOGY KEYWORDS:
  tensile test (ASTM E8), Vickers hardness, Charpy impact, XRD Rietveld, SEM-EDS,
  TEM selected area diffraction, potentiodynamic polarization (Tafel), EIS (Nyquist),
  heat treatment furnace, ASTM standards, ANOVA comparison
""",

"polymer_composite": """================================================================================
TOPIC GUIDE — Polymer Science & Composites
================================================================================
FIELD: Materials Science / Polymer Science
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Polimer, Komposit Serat, Biopolimer, Nanokomposit, Teknik Polimer

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: polymer matrix, filler/fiber type, processing method
  (hand lay-up, extrusion, injection molding), characterization (FTIR, TGA, DSC),
  key mechanical/thermal properties (tensile strength MPa, flexural modulus GPa,
  Tg °C, degradation temperature °C).

INTRODUCTION ELEMENTS:
  - Polymer applications and demand for improved properties.
  - Problem: brittleness, low thermal stability, environmental concern (biopolymers).
  - Research gap: new filler, new natural fiber source, new processing route.
  - Objectives: fabrication, characterization, property optimization.

LITERATURE REVIEW:
  Common section name: "Literature Review"
  - Polymer matrix types: thermoplastic (PE, PP, PLA, PA) vs. thermoset (epoxy, polyester, phenolic).
  - Composite fibers: synthetic (glass, carbon, aramid) vs. natural (kenaf, jute, coir, bamboo).
  - Fiber-matrix interface: surface treatment (alkali, silane, acetylation), wettability.
  - Filler: nanoparticles (clay, silica, graphene), short fibers, particulate.
  - Characterization: FTIR, XRD (crystallinity), TGA (thermal stability), DSC (Tg, Tm, crystallinity%).
  - Rule of mixtures: theoretical Young's modulus prediction for composites.
  - Biodegradable polymers: PLA, PHB, PBS; degradation rate; food packaging application.

METHODOLOGY:
  Common section name: "Materials and Methods"
  - Materials: matrix polymer (grade, supplier), fiber/filler (size, surface area), coupling agent.
  - Surface treatment: alkali treatment (NaOH 5% for natural fiber), silane functionalization.
  - Processing: compression molding (temperature T, pressure P, time t), hot press.
  - Specimens: ASTM D638 (tensile), D790 (flexural), D256 (Izod impact) dimensions.
  - Characterization: FTIR (4000–400 cm⁻¹), TGA (25–700°C, 10°C/min, N2), DSC (heating/cooling cycles), XRD (2θ 5–50°).
  - Mechanical tests: tensile (UTM, crosshead speed 2 mm/min), 3-point bend, Izod impact.
  - Statistical: ANOVA, Tukey's test, n=5 specimens.

TYPICAL RESULTS & DISCUSSION:
  - Tensile strength: unfilled PLA 50–65 MPa; with 30 wt% glass fiber 100–150 MPa; natural fiber 40–80 MPa.
  - Young's modulus: PLA 3–4 GPa; glass fiber composite 10–25 GPa.
  - Tg (glass transition): PLA 55–65°C; PA6 40–50°C; epoxy 80–120°C.
  - TGA: onset degradation temperature improvement with filler: 200→250°C.
  - Water absorption: natural fiber composite 1–5 wt%; reduces with surface treatment.
  Tables: mechanical properties at various filler %, thermal analysis summary.
  Figures: FTIR spectra, TGA curves, stress-strain curves, SEM fracture surface.

TYPICAL FIGURES:
  - FTIR spectrum (before/after surface treatment).
  - TGA and DTG curves at various filler content.
  - Stress-strain curve (tensile test).
  - SEM: fracture surface morphology.
  - DSC: Tg and Tm peaks.
  - Bar chart: mechanical properties vs. filler content.

TYPICAL TABLES:
  - Processing parameters: matrix | fiber | wt% | processing T | P | time.
  - Mechanical: wt% | tensile strength | modulus | elongation | impact strength.
  - Thermal: wt% | Tg | Tm | Td (onset) | char yield %.

CONCLUSION CHARACTERISTICS:
  - Optimal fiber/filler content for best property balance.
  - Surface treatment effectiveness on interfacial adhesion.
  - Thermal stability improvement quantified.
  - Limitations: manual processing variability, single matrix, room temperature testing.
  - Future: injection molded specimens, fatigue, biodegradation study.

COMMON REFERENCE VENUES:
  Polymer, Composites Science and Technology, Composites Part A/B,
  Journal of Applied Polymer Science, Polymer Composites,
  Industrial Crops and Products, Polymer Degradation and Stability

DOMAIN VOCABULARY:
  thermoset, thermoplastic, epoxy, PLA, PP, PE, PA, Tg, Tm, Td, FTIR, TGA, DSC,
  XRD crystallinity, fiber volume fraction, alkali treatment, silane, wettability,
  tensile strength, Young's modulus, flexural strength, Izod impact, SEM

METHODOLOGY KEYWORDS:
  hand lay-up, compression molding, tensile test (ASTM D638), flexural test (D790),
  impact test (D256), FTIR spectroscopy, TGA, DSC, SEM fracture analysis,
  water absorption test, ANOVA comparison, surface treatment evaluation
""",

}

def write_topic(name, content):
    path = os.path.join(D, f"{name}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.lstrip())
    print(f"  wrote {name}.txt")

for name, content in TOPICS.items():
    write_topic(name, content)
print(f"gen_05: {len(TOPICS)} topics written.")

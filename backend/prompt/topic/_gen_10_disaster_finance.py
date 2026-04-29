"""Generator 10: disaster_management, economics, edge_ai, education,
electrical_engineering, embedded_systems, energy_storage, entrepreneurship,
environmental_engineering, environmental_science, epidemiology, finance"""
import os; D = os.path.dirname(os.path.abspath(__file__))

TOPICS = {

"disaster_management": """================================================================================
TOPIC GUIDE — Disaster Management & Emergency Response
================================================================================
FIELD: Social Sciences / Environmental Sciences / Engineering
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Manajemen Bencana, Mitigasi, Kesiapsiagaan, Respons Darurat, BNPB, Kebencanaan Indonesia

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: disaster type (earthquake, flood, volcanic eruption, landslide,
  tsunami), study area, methodology (GIS hazard mapping, survey, field assessment, remote sensing),
  key results (risk level, affected population n, evacuation efficiency, preparedness score),
  and disaster risk reduction (DRR) implications.

INTRODUCTION ELEMENTS:
  - Indonesia disaster context: Ring of Fire, high seismicity, volcanic activity, flood-prone.
  - Disaster statistics: BNPB data, Sendai Framework 2015–2030 targets.
  - Specific disaster risk: local geography, population exposure, vulnerability factors.
  - Research gap: risk mapping, community preparedness gap, evacuation plan deficiency.
  - Objectives: assess risk, map hazard, evaluate preparedness, propose mitigation.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Disaster risk equation: Risk = Hazard × Vulnerability / Capacity (UNDRR).
  - Sendai Framework: 4 priorities (understanding risk, governance, investing in DRR, enhance preparedness).
  - Hazard types: geological (earthquake M_w, PGA gal, liquefaction), hydrometeorological (flood IDF curve, return period), volcanic (VEI, pyroclastic flow, lahar).
  - Vulnerability: social (elderly, disability, poverty), structural (building quality), economic.
  - GIS in disaster management: hazard map (USGS ShakeMap, PVMBG), risk map overlay, evacuation route.
  - Remote sensing: Sentinel-1 SAR flood mapping, Landsat NDVI pre/post disaster.
  - Community preparedness: Hyogo Framework, community-based DRR (CBDRM), disaster preparedness index.

METHODOLOGY:
  Common section name: "Research Methodology" / "Methods"
  - Hazard assessment: GIS (ArcGIS/QGIS), spatial data (DEM/SRTM 30m, geological map, land use).
  - Risk mapping: multi-criteria evaluation (weighted overlay: hazard 40%, vulnerability 30%, capacity 30%).
  - Field survey: community preparedness questionnaire (n=50–200 households); structured interview.
  - Rapid damage assessment: visual inspection, damage scoring (Badan Geologi/BMKG protocol).
  - Remote sensing analysis: change detection (pre/post satellite imagery); NDVI, NDWI.
  - Statistical: index score calculation, Likert scale, cluster analysis (preparedness by village).

TYPICAL RESULTS & DISCUSSION:
  - Hazard zone: high, medium, low (color-coded map with percentage area).
  - Risk index: 0–4 scale; areas with score >3 = high priority for intervention.
  - Community preparedness score: <60% = low; 60–80% = moderate; >80% = high.
  - Evacuation route efficiency: travel time to assembly point <15 min (acceptable).
  - Flood inundation area: X km² affected under 100-year return period scenario.
  Tables: risk matrix, preparedness score by village, damage assessment data.
  Figures: hazard/risk map, preparedness score bar chart, evacuation route map.

TYPICAL FIGURES:
  - Hazard zone map (GIS overlay).
  - Risk map (classified: high/medium/low).
  - Evacuation route map with assembly points.
  - Bar chart: community preparedness score by area.
  - Flood inundation map (return period scenarios).

TYPICAL TABLES:
  - Risk matrix: hazard level × vulnerability level → risk class.
  - Preparedness: village | n respondents | preparedness score | category.
  - Damage assessment: element | condition | damage % | recommended action.

CONCLUSION CHARACTERISTICS:
  - Risk level and spatial distribution quantified and mapped.
  - Community preparedness gaps identified.
  - Priority areas for DRR investment recommended.
  - Limitations: DEM resolution, survey sample size, single disaster type.
  - Future: multi-hazard risk assessment, early warning system design, post-disaster recovery planning.

COMMON REFERENCE VENUES:
  Natural Hazards and Earth System Sciences, International Journal of Disaster Risk Reduction,
  Disasters, Natural Hazards, Geomatics Natural Hazards and Risk,
  Jurnal Bumi Indonesia (UGM), IOP Conference Series: Earth and Environmental Science

DOMAIN VOCABULARY:
  Sendai Framework, BNPB, UNDRR, DRR, CBDRM, hazard, vulnerability, risk,
  PGA, ShakeMap, liquefaction, VEI, pyroclastic, lahar, NDWI, SAR,
  IDF curve, return period, evacuation route, DEM, SRTM, PVMBG

METHODOLOGY KEYWORDS:
  GIS multi-criteria evaluation (weighted overlay), remote sensing change detection (Sentinel-1/Landsat),
  community preparedness survey (structured questionnaire), hazard zone classification,
  flood inundation modeling, damage assessment (visual inspection), NDVI/NDWI index
""",

"economics": """================================================================================
TOPIC GUIDE — Economics (General)
================================================================================
FIELD: Social Sciences / Economics
DEFAULT CITATION STYLE: APA or AEA
SUBDISCIPLINE: Ekonomi Makro, Ekonomi Mikro, Ekonomi Pembangunan, Ekonomi Internasional, Ekonomi Indonesia

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: economic phenomenon or policy analyzed, data source
  (BPS, World Bank, IMF), analytical method (regression, time series, panel data, CGE),
  variables (GDP growth %, inflation %, unemployment %, trade balance), statistical results
  (coefficient, p-value, elasticity), and economic policy implications.

INTRODUCTION ELEMENTS:
  - Macroeconomic context: Indonesia GDP growth, inflation, fiscal/monetary policy.
  - Economic problem: income inequality (Gini), poverty, current account deficit, commodity price.
  - Research gap: unexplored determinant, regional variation, post-pandemic recovery.
  - Theoretical framework: Keynesian, neoclassical, institutional, behavioral economics.
  - Research objectives: estimate relationship, test hypothesis, assess policy impact.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Macroeconomics: Solow growth model, Phillips curve, IS-LM, Mundell-Fleming (open economy).
  - Development economics: Kuznets curve, poverty trap, human capital (Becker), Leontief input-output.
  - Trade theory: comparative advantage (Ricardo), Heckscher-Ohlin, gravity model (bilateral trade).
  - Fiscal policy: government spending multiplier, Ricardian equivalence, fiscal consolidation.
  - Monetary policy: Taylor rule, inflation targeting (BI 7-day RR), exchange rate pass-through.
  - Panel data: Hausman test (FE vs. RE), Arellano-Bond GMM, Driscoll-Kraay SE.

METHODOLOGY:
  Common section name: "Data and Methodology" / "Research Methodology"
  - Data: BPS Indonesia (GDP, inflation, employment), World Bank WDI, IMF IFS, CEIC; annual/quarterly.
  - Period: 10–30 years (e.g., 2000–2023 for post-reformasi analysis).
  - Regression: OLS, GLS, WLS; standard errors (HC3 robust, cluster); VIF multicollinearity.
  - Time series: unit root (ADF, KPSS), Johansen cointegration, VECM, ARDL bounds test, VAR/SVAR.
  - Panel data: Hausman test → fixed effect (FE) or random effect (RE); two-way FE; GMM.
  - Causality: Granger causality test (bivariate/multivariate).
  - Tools: Stata, R (plm, lmtest, vars), EViews, Python (statsmodels).

TYPICAL RESULTS & DISCUSSION:
  - GDP growth determinant: investment elasticity 0.3–0.5; human capital 0.2–0.4 (p<0.05).
  - Cointegration: long-run relationship between variables confirmed; ECT -0.15 to -0.45 (significant, negative).
  - Exchange rate pass-through to inflation: 0.1–0.3 (partial pass-through).
  - Panel FE: R² within 0.4–0.7; country FE explains structural differences.
  - Gini coefficient Indonesia: 0.38–0.42 (2010–2023); declining trend.
  Tables: regression results, cointegration test, Hausman test, descriptive statistics.
  Figures: trend plots, IRF (impulse response function), variance decomposition, scatter.

TYPICAL FIGURES:
  - Time series plot (GDP, inflation, trade balance 2000–2023).
  - Impulse response function (VAR/SVAR).
  - Scatter plot (income vs. inequality: Kuznets curve).
  - Variance decomposition bar chart.

TYPICAL TABLES:
  - Descriptive statistics: variable | mean | SD | min | max | source.
  - Regression results: variable | coeff | SE | t-stat | p-value | elasticity.
  - Unit root test: variable | ADF stat | critical value | result.

CONCLUSION CHARACTERISTICS:
  - Key economic determinants identified and quantified.
  - Long-run and short-run dynamics established.
  - Policy implications for government/central bank.
  - Limitations: data availability, endogeneity, structural breaks, model specification.
  - Future: sub-national analysis, CGE simulation, machine learning forecasting.

COMMON REFERENCE VENUES:
  American Economic Review, Journal of Development Economics, World Development,
  Journal of International Economics, Applied Economics, Bulletin of Indonesian Economic Studies (BIES),
  Jurnal Ekonomi dan Keuangan Indonesia (JEKI), Journal of Asian Economics

DOMAIN VOCABULARY:
  GDP, GNI, inflation, Gini coefficient, Solow model, Phillips curve, IS-LM,
  Johansen cointegration, VECM, ARDL, Granger causality, Hausman test, GMM,
  ADF/KPSS, VAR, IRF, FE/RE, elasticity, BPS, WDI, IMF, OLS, ECT

METHODOLOGY KEYWORDS:
  ADF unit root test, Johansen cointegration, VECM/ARDL estimation (EViews/Stata),
  Granger causality test, Hausman test (FE vs. RE), panel data GMM (Arellano-Bond),
  impulse response function (VAR), variance decomposition, OLS robust SE (HC3)
""",

"edge_ai": """================================================================================
TOPIC GUIDE — Edge AI & TinyML
================================================================================
FIELD: Computer Science / Electrical Engineering
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Edge AI, TinyML, Komputasi Edge, AI Terbenam, FPGA AI, Kecerdasan Buatan di IoT

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: AI task deployed at edge (classification, object detection,
  anomaly detection, speech recognition), edge hardware (Raspberry Pi, NVIDIA Jetson,
  Arduino Nano 33 BLE Sense, STM32, ESP32-S3), model compression technique (quantization,
  pruning, KD), metrics (accuracy %, latency ms, power consumption mW, model size KB/MB),
  and comparison with cloud inference.

INTRODUCTION ELEMENTS:
  - IoT data explosion: latency-sensitive applications, privacy concern, bandwidth limit.
  - Edge AI paradigm: move inference from cloud to device.
  - Hardware constraint: limited RAM (100KB–8MB), CPU/MCU (MHz–GHz), power (mW–W).
  - Research gap: new model compression for specific task/hardware, accuracy-efficiency trade-off.
  - Objectives: deploy efficient AI model on edge device with acceptable accuracy.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - Edge computing: fog computing, MEC (mobile edge computing), edge-cloud continuum.
  - TinyML: TensorFlow Lite Micro (TFLM), Edge Impulse, TinyML book (Pete Warden & Daniel Situnayake).
  - Model compression: quantization (post-training PTQ: INT8/INT4, QAT), pruning (structured/unstructured), knowledge distillation (Hinton 2015), NAS (Neural Architecture Search).
  - Efficient architectures: MobileNetV2/V3, EfficientNet-Lite, ShuffleNet, SqueezeNet, Tiny-YOLO, MobileNet-SSD.
  - Hardware accelerators: NVIDIA Jetson (CUDA+TensorRT), Google Coral Edge TPU, Hailo-8, FPGA (Xilinx).
  - Deployment tools: TensorFlow Lite, ONNX Runtime, TensorRT (Jetson), OpenVINO (Intel).

METHODOLOGY:
  Common section name: "System Design" / "Methodology"
  - Hardware: target MCU/SBC specification (RAM, Flash, CPU MHz, power TDP).
  - Task and dataset: classification (CIFAR-10/custom), detection (COCO custom), keyword (Speech Commands).
  - Model design: baseline CNN/YOLO → compress with quantization INT8 (TFLite converter) and/or pruning.
  - Training: full-precision baseline on GPU; quantization-aware training (QAT) for <1% accuracy drop.
  - Deployment: TFLite or Edge Impulse EON compiler; MCU firmware integration.
  - Evaluation: accuracy (vs. full-precision); latency (single inference on device ms); RAM/Flash usage; power (INA219 current sensor, mAh consumption).

TYPICAL RESULTS & DISCUSSION:
  - INT8 quantization: accuracy drop 0.5–2% vs. FP32 baseline; model size 4× reduction.
  - Jetson Nano inference: MobileNetV2 classification ~15ms; Tiny-YOLOv4 ~20ms.
  - Arduino Nano 33 BLE Sense: keyword spotting (2–10 words) 85–94% accuracy; latency <200ms.
  - ESP32-S3: simple CNN image classification 200–500ms; power 150–300mW active.
  - Edge vs. cloud: latency edge 10–500ms vs. cloud 200–2000ms (round-trip); privacy preserved.
  Tables: model size, accuracy, latency, power by hardware and optimization.
  Figures: accuracy-latency trade-off scatter, power consumption timeline, confusion matrix.

TYPICAL FIGURES:
  - Accuracy vs. latency scatter (baseline vs. quantized vs. pruned).
  - Power consumption timeline (idle/inference/sleep cycles).
  - Model size bar chart (FP32 vs. INT8 vs. pruned).
  - Hardware block diagram with AI inference pipeline.
  - Confusion matrix on edge device output.

TYPICAL TABLES:
  - Model comparison: model | params(M) | size(KB) | accuracy(%) | latency(ms) | power(mW).
  - Hardware: device | CPU | RAM | Flash | TDP | cost(USD).
  - Optimization: technique | accuracy drop | size reduction | latency reduction.

CONCLUSION CHARACTERISTICS:
  - AI model successfully deployed on edge device meeting accuracy and latency targets.
  - Optimization technique effectiveness quantified.
  - Edge deployment advantages (privacy, latency, connectivity-independence) demonstrated.
  - Limitations: limited hardware generalizability, task-specific, accuracy trade-off.
  - Future: neural architecture search (NAS) for target hardware, federated learning at edge.

COMMON REFERENCE VENUES:
  IEEE Transactions on Embedded Computing Systems, IEEE Internet of Things Journal,
  IEEE Access, Neural Networks, Edge Computing (IEEE), ACM Transactions on Embedded Computing,
  Applied Sciences (MDPI), Electronics (MDPI)

DOMAIN VOCABULARY:
  TinyML, TensorFlow Lite, TFLM, Edge Impulse, quantization, pruning, KD,
  MobileNet, INT8, PTQ, QAT, TensorRT, Jetson, Coral, FPGA, OpenVINO,
  latency, power consumption, mAh, MEC, fog computing, NAS, EON compiler

METHODOLOGY KEYWORDS:
  INT8 post-training quantization (TFLite), quantization-aware training (QAT),
  model pruning (structured), TFLite deployment on MCU, Edge Impulse EON compiler,
  INA219 power measurement, ONNX/TensorRT optimization, accuracy-latency evaluation
""",

"education": """================================================================================
TOPIC GUIDE — Education & Educational Technology
================================================================================
FIELD: Social Sciences / Education
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Pendidikan, Teknologi Pendidikan, Pembelajaran Online, Kurikulum, Evaluasi Pembelajaran

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: educational intervention, technology/platform, or curriculum evaluated,
  target population (grade level, n students/teachers), study design (experimental, quasi-experimental,
  survey, design-based research), outcome measures (learning achievement scores, n-gain,
  student engagement, motivation), statistical results, and educational implications.

INTRODUCTION ELEMENTS:
  - Educational challenge: low learning outcomes, digital divide, student engagement, 21st-century skills.
  - Policy context: Kurikulum Merdeka (Indonesia), Education for All, SDG 4 (Quality Education).
  - Technology integration: LMS (Moodle, Google Classroom), e-learning, gamification, AR/VR.
  - Research gap: specific learning method, local context, technology integration not evaluated.
  - Research hypotheses or questions.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Learning theories: constructivism (Piaget, Vygotsky ZPD), cognitive load theory (Sweller), TPACK model.
  - Educational technology: e-learning models (ADDIE, SAM), LMS effectiveness (Moodle, Canvas).
  - Active learning: problem-based learning (PBL), project-based learning, flipped classroom, cooperative learning.
  - Assessment: Bloom's taxonomy (revised), authentic assessment, formative/summative, Rasch model.
  - Motivation: self-determination theory (Deci & Ryan), ARCS model (attention, relevance, confidence, satisfaction).
  - Gamification: game elements (points, badges, leaderboard) in education; engagement theory.
  - Indonesia: Kurikulum Merdeka, MBKM, HOTS (Higher Order Thinking Skills), PISA 2022.

METHODOLOGY:
  Common section name: "Research Methodology" / "Methods"
  - Design: quasi-experimental (pretest-posttest control group), RCT, survey, design-based research.
  - Sample: purposive/random sampling; n=30–200 students; power analysis.
  - Instruments: validated questionnaire (Cronbach's α >0.70), achievement test (r >0.30 validity), observation rubric.
  - Intervention: duration (4–12 weeks), group (experimental uses new method; control uses conventional).
  - Statistics: paired t-test (pre-post within group), independent t-test (between groups), N-gain = (post-pre)/(max-pre).
  - N-gain categories: high >0.7, medium 0.3–0.7, low <0.3.
  - Qualitative component: observation notes, interview (n=5–10), thematic analysis.

TYPICAL RESULTS & DISCUSSION:
  - Learning achievement (posttest): experimental 70–85 vs. control 55–70 (out of 100).
  - N-gain: experimental 0.5–0.7 (medium-high); control 0.2–0.4 (low-medium).
  - t-test result: t(df) = X.XX, p < 0.05 = significant difference.
  - Student motivation/engagement score: 3.8–4.5/5.0 (Likert).
  - Cronbach's α questionnaire: 0.80–0.92 (good to excellent).
  Tables: pre/posttest scores, N-gain by class, validity/reliability results.
  Figures: bar chart pre/post comparison, N-gain distribution, learning curve.

TYPICAL FIGURES:
  - Bar chart: pretest vs. posttest scores (control vs. experimental).
  - N-gain category distribution (pie or bar chart).
  - Motivation/engagement score radar chart.
  - Learning activity/observation timeline.

TYPICAL TABLES:
  - Descriptive: group | n | pretest (mean±SD) | posttest (mean±SD) | N-gain.
  - t-test: group pair | mean diff | t | df | p | Cohen's d.
  - Instrument validity: item | r-table | r-count | validity.

CONCLUSION CHARACTERISTICS:
  - Experimental method/technology significantly improves learning outcomes.
  - N-gain level confirms instructional effectiveness.
  - Practical implications for curriculum design and teacher training.
  - Limitations: single school/district, short intervention, Hawthorne effect.
  - Future: longitudinal study, multi-school replication, AI-personalized learning.

COMMON REFERENCE VENUES:
  Computers & Education, British Journal of Educational Technology, Educational Technology Research and Development,
  Journal of Educational Technology & Society, Learning and Instruction,
  Jurnal Pendidikan Indonesia (JPII), International Journal of Science and Math Education,
  Teaching and Teacher Education

DOMAIN VOCABULARY:
  constructivism, Vygotsky ZPD, TPACK, ADDIE, PBL, flipped classroom, Bloom's taxonomy,
  N-gain, ARCS model, gamification, Kurikulum Merdeka, HOTS, LMS, Moodle,
  quasi-experimental, pretest-posttest, Cronbach's alpha, Cohen's d

METHODOLOGY KEYWORDS:
  quasi-experimental design (pretest-posttest), N-gain calculation, independent/paired t-test,
  validated instrument (Cronbach's alpha), purposive sampling, thematic qualitative analysis,
  Rasch model item analysis, ARCS motivation survey
""",

"electrical_engineering": """================================================================================
TOPIC GUIDE — Electrical Engineering
================================================================================
FIELD: Engineering / Electrical
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Teknik Elektro, Sistem Tenaga, Elektronika Daya, Mesin Listrik, Sistem Kontrol, Instrumentasi

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: electrical system or device studied (power system,
  motor drive, converter, sensor instrumentation), analysis/design method (simulation MATLAB/Simulink,
  PSIM, hardware prototype), key metrics (efficiency %, THD %, voltage regulation %,
  power factor, settling time ms, RMSE), and system performance evaluation.

INTRODUCTION ELEMENTS:
  - Electrical system context: power quality issues, renewable energy integration, efficiency demands.
  - Specific problem: high harmonic distortion, poor power factor, converter efficiency, motor vibration.
  - Research gap: new control algorithm, topology, or optimization not applied to target system.
  - Objectives: design, simulate, and/or experimentally validate electrical system.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - Power systems: load flow (Newton-Raphson), fault analysis (symmetrical/asymmetrical), protection (relay coordination).
  - Power electronics: DC-DC converter topologies (buck, boost, buck-boost, SEPIC, Cuk, flyback); inverter (VSI, CSI); AC-DC rectifier.
  - Motor drives: PMSM, BLDC, induction motor (IM); vector control (FOC, DTC); encoder, resolver.
  - Control theory: PID, fuzzy logic control (FLC), model predictive control (MPC), sliding mode control (SMC); Bode/Nyquist analysis.
  - Power quality: THD (IEEE 519), power factor correction (PFC, active/passive), voltage sag/swell (IEC 61000).
  - Renewable energy: MPPT (P&O, INC, PSO-based), solar PV grid-connected (IEEE 1547), wind turbine (DFIG, PMSG).

METHODOLOGY:
  Common section name: "System Design and Simulation" / "Methods"
  - Simulation: MATLAB/Simulink (SimPowerSystems), PSIM, PLECS, LTspice; model validation.
  - Hardware prototype: PCB design (Altium/KiCad), component selection, MCU/DSP (STM32, TMS320F28335).
  - Control implementation: digital control (sampling rate, z-domain discretization); PWM generation.
  - Measurement: oscilloscope (Tektronix/Rigol), power analyzer (Yokogawa), spectrum analyzer.
  - Performance metrics: efficiency η = Pout/Pin × 100%; THD = √(ΣVn²)/V1 × 100%; power factor PF = P/S.
  - Stability analysis: eigenvalue, Bode/Nyquist plot; step response (rise time, settling time, overshoot).

TYPICAL RESULTS & DISCUSSION:
  - DC-DC converter efficiency: boost converter 90–97% at rated load.
  - THD: inverter output <5% (IEEE 519 compliance) with LCL filter.
  - Power factor: PFC circuit >0.99 (vs. uncompensated 0.65–0.80).
  - Voltage regulation: ±1–5% with closed-loop PID control.
  - Motor drive: speed tracking error <2% with FOC; torque ripple <5%.
  - Settling time (step response): PID 50–200ms; MPC 20–80ms.
  Tables: performance comparison (topologies/controllers), harmonic spectrum, efficiency vs. load.
  Figures: simulation waveform, efficiency curve, Bode plot, hardware experimental result.

TYPICAL FIGURES:
  - Simulation waveform (voltage/current, switching signals).
  - Efficiency vs. load curve.
  - Bode plot (gain and phase margin).
  - FFT spectrum (THD analysis).
  - Hardware prototype photograph + measured waveform.

TYPICAL TABLES:
  - Performance comparison: topology/controller | efficiency (%) | THD (%) | regulation (%) | PF.
  - Component specification: component | value | rating | part number.
  - Control parameter: gain | Kp | Ki | Kd | settling time (ms).

CONCLUSION CHARACTERISTICS:
  - Proposed electrical system meets performance specifications.
  - Simulation validated by hardware experiment (within acceptable tolerance).
  - Efficiency/THD/power factor improved vs. conventional design.
  - Limitations: lab-scale prototype, ideal component assumption, temperature effect not studied.
  - Future: SiC/GaN wide-bandgap devices, digital twin, smart grid integration.

COMMON REFERENCE VENUES:
  IEEE Transactions on Power Electronics, IEEE Transactions on Industrial Electronics,
  IEEE Transactions on Energy Conversion, IET Power Electronics, IET Electric Power Applications,
  IEEE Access, Electric Power Systems Research, Jurnal Nasional Teknik Elektro (JNTE)

DOMAIN VOCABULARY:
  THD, power factor, MPPT, PWM, FOC, DTC, MPC, SMC, PID, VSI, CSI,
  buck/boost/SEPIC, PMSM, BLDC, LCL filter, IEEE 519, IEC 61000,
  efficiency, voltage regulation, settling time, MATLAB/Simulink, PSIM, DSP TMS320

METHODOLOGY KEYWORDS:
  MATLAB/Simulink simulation (SimPowerSystems), PSIM power electronics simulation,
  PID/FOC/MPC control design, PWM generation (STM32/TMS320), THD measurement (FFT),
  hardware prototype validation, efficiency curve measurement, Bode/Nyquist stability analysis
""",

"embedded_systems": """================================================================================
TOPIC GUIDE — Embedded Systems
================================================================================
FIELD: Computer Science / Electrical Engineering
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Sistem Tertanam, Mikrokontroler, RTOS, Firmware, Hardware-Software Co-Design, IoT Firmware

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: embedded system application, target hardware (MCU/SoC),
  OS/RTOS (FreeRTOS, Zephyr, bare-metal), implementation methodology, key metrics
  (execution time µs/ms, CPU utilization %, memory footprint KB, power consumption mW,
  real-time task deadline miss rate %), and performance vs. specification.

INTRODUCTION ELEMENTS:
  - Embedded systems ubiquity: automotive (ISO 26262), medical devices (IEC 62304), industrial control (IEC 61131).
  - Real-time constraint: hard RT (air bag), soft RT (video buffering), firm RT (payment terminal).
  - Resource constraint: limited Flash/RAM, single core, no MMU, low power.
  - Research gap: new scheduling algorithm, hardware-software optimization, RTOS adaptation.
  - Objectives: design, implement, verify, and evaluate embedded system meeting requirements.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - MCU/SoC families: ARM Cortex-M (M0/M3/M4/M7/M33/M55), RISC-V (ESP32-C3), Xtensa (ESP32).
  - RTOS: FreeRTOS (tasks, queues, semaphores, mutex, timers), Zephyr, RT-Thread, mbed OS.
  - Scheduling: rate-monotonic (RMS), earliest deadline first (EDF); schedulability analysis (Liu & Layland 1973).
  - Bare-metal vs. RTOS: state machine (HSM), interrupt-driven architecture vs. preemptive multitasking.
  - Communication protocols: UART, SPI, I²C, CAN (automotive), Modbus RTU/TCP, BLE, Zigbee, LoRa.
  - Low power design: sleep modes (deep sleep µA), dynamic voltage/frequency scaling (DVFS), tickless idle.
  - Safety: MISRA C guidelines, ISO 26262 (automotive ASIL), IEC 62304 (medical software).

METHODOLOGY:
  Common section name: "System Design" / "Implementation"
  - Hardware: MCU selection (clock MHz, Flash/RAM KB, peripherals), PCB schematic.
  - Software architecture: task diagram, state machine, data flow; RTOS configuration (tick rate, heap).
  - Firmware: C/C++, HAL (STM32 HAL, ESP-IDF), driver development.
  - Real-time: task period T, WCET (worst-case execution time), utilization U=WCET/T; schedulability U ≤ n(2^(1/n)−1).
  - Testing: unit test (CppUTest, Unity), hardware-in-the-loop (HIL), logic analyzer, JTAG debugger.
  - Power measurement: INA219, power profiler kit (PPK2 Nordic); current trace during operation.
  - Metrics: task deadline miss rate, context switch time, ISR latency.

TYPICAL RESULTS & DISCUSSION:
  - Task execution time (WCET): sensor reading 50–200µs; PID control loop 100–500µs.
  - FreeRTOS context switch time: Cortex-M4 ~1µs.
  - CPU utilization: all tasks ≤70–80% (headroom for interrupts).
  - Memory: Flash usage 20–80% of available; RAM 30–70%.
  - Deep sleep current: ESP32 5–10µA; STM32L4 2–10µA; 18650 battery life weeks-to-months.
  - Task deadline miss rate: 0% for hard RT (mandatory); <0.01% for soft RT.
  Tables: task utilization analysis, resource usage, power comparison (modes).
  Figures: task timing diagram, power consumption trace, state machine diagram.

TYPICAL FIGURES:
  - RTOS task timing diagram (Gantt chart of task scheduling).
  - Power consumption trace (active/sleep cycles).
  - System architecture block diagram.
  - State machine (HSM) diagram.
  - Logic analyzer capture (SPI/I²C/UART).

TYPICAL TABLES:
  - Task analysis: task | period(ms) | WCET(µs) | utilization(%) | priority.
  - Memory usage: section | used(KB) | available(KB) | utilization(%).
  - Power mode: mode | current(mA) | voltage(V) | active component.

CONCLUSION CHARACTERISTICS:
  - Embedded system meets real-time and resource constraints.
  - RTOS scheduling meets schedulability criterion.
  - Power consumption meets battery life target.
  - Limitations: single MCU platform, bench-tested not field-deployed, specific workload.
  - Future: multicore MCU (RP2040, ESP32-S3), HW/SW co-design (FPGA-MCU), OTA firmware update.

COMMON REFERENCE VENUES:
  ACM Transactions on Embedded Computing Systems, IEEE Transactions on Industrial Informatics,
  Microprocessors and Microsystems, Journal of Systems Architecture,
  Real-Time Systems, IEEE Access, Embedded Systems Letters

DOMAIN VOCABULARY:
  MCU, RTOS, FreeRTOS, Zephyr, task, semaphore, mutex, queue, WCET, ISR,
  ARM Cortex-M, RISC-V, ESP32, STM32, UART, SPI, I²C, CAN, Modbus,
  hard RT, soft RT, deep sleep, DVFS, MISRA C, ISO 26262, IEC 62304

METHODOLOGY KEYWORDS:
  FreeRTOS task design, schedulability analysis (Liu & Layland/RMS), WCET measurement (logic analyzer),
  firmware unit test (CppUTest/Unity), INA219 power measurement, JTAG/SWD debugging,
  hardware-in-the-loop (HIL) testing, HAL driver development (STM32 HAL/ESP-IDF)
""",

"energy_storage": """================================================================================
TOPIC GUIDE — Energy Storage Systems
================================================================================
FIELD: Engineering / Energy Technology
DEFAULT CITATION STYLE: IEEE or APA
SUBDISCIPLINE: Penyimpanan Energi, Baterai Li-ion, Superkapasitor, BMS, BESS, Hybrid Storage

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: energy storage technology (Li-ion, LFP, solid-state, supercapacitor,
  flow battery), cell/pack specification, test conditions, key metrics (energy density Wh/kg,
  power density W/kg, cycle life n, Coulombic efficiency %, capacity retention %,
  charging C-rate, temperature range °C), and application context.

INTRODUCTION ELEMENTS:
  - Energy storage importance: grid stability, EV range, renewable intermittency.
  - Technology landscape: Li-ion dominance, emerging solid-state, flow battery for grid.
  - Specific challenge: degradation at high C-rate, thermal runaway, calendar aging, cost.
  - Research gap: new electrolyte, cathode material, thermal management, BMS algorithm.
  - Objectives: characterize, optimize, or model energy storage system.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - Battery chemistry: Li-ion cathodes (NMC, NCA, LFP, LCO, LMFP); anodes (graphite, Si, Li-metal).
  - Solid-state batteries: oxide (LLZO), sulfide (LGPS), polymer electrolyte; challenges (interface resistance, Li dendrite).
  - Supercapacitors: EDLC (activated carbon), pseudocapacitor (RuO₂, MnO₂), hybrid.
  - Battery management system (BMS): SOC estimation (Coulomb counting, EKF, HPPC test), SOH, cell balancing.
  - Electrochemical characterization: EIS (Nyquist plot, SEI resistance), CV, GITT, rate capability.
  - Thermal management: forced air, liquid cooling, phase change material (PCM); thermal runway threshold.
  - Grid-scale BESS: frequency regulation, peak shaving, arbitrage; Tesla Megapack, CATL.

METHODOLOGY:
  Common section name: "Experimental Methods" / "Cell Characterization"
  - Cell: type (18650, 21700, pouch, prismatic), chemistry, nominal capacity Ah, nominal voltage V.
  - Formation cycling: 3–5 cycles at C/10; establish baseline capacity.
  - Rate capability: 0.2C, 0.5C, 1C, 2C, 3C charge/discharge; capacity retention per C-rate.
  - Cycle test: n=200–1000 cycles; capacity fade (% loss per 100 cycles); temperature 25°C or 45°C.
  - HPPC test: 10s pulse at 50% SOC; internal resistance (mΩ); SOC-resistance curve.
  - EIS: 10 mHz–100 kHz; Nyquist plot fitting (ECM: Rs, RSEI, RCT, Warburg).
  - Temperature: -20°C to 60°C range study; thermal chamber (temperature-controlled).

TYPICAL RESULTS & DISCUSSION:
  - Energy density: NMC 200–250 Wh/kg cell-level; LFP 150–180 Wh/kg; LCO 240–270 Wh/kg.
  - Power density: 18650 NMC 500–1000 W/kg; EDLC supercapacitor 10,000–15,000 W/kg.
  - Cycle life: LFP >3000 cycles (80% retention); NMC 800–2000; solid-state >500 cycles (current state).
  - Coulombic efficiency: commercial 18650 99.5–99.9%.
  - EIS: RSEI 5–30 mΩ; RCT 10–50 mΩ for fresh cell.
  - Capacity retention at 3C: 80–90% of 1C capacity.
  Tables: performance summary, EIS parameters, cycle degradation data.
  Figures: charge/discharge curves, EIS Nyquist plot, capacity fade curve, Ragone plot.

TYPICAL FIGURES:
  - Charge/discharge voltage-capacity curves.
  - EIS Nyquist plot with ECM fit.
  - Cycle life curve (capacity retention vs. cycle number).
  - Ragone plot (energy vs. power density).
  - Rate capability bar chart.

TYPICAL TABLES:
  - Battery comparison: chemistry | energy density | power density | cycle life | cost (USD/kWh).
  - Cycle test: cycle # | discharge capacity (Ah) | retention (%) | temperature (°C).
  - EIS parameters: Rs (mΩ) | RSEI (mΩ) | RCT (mΩ) | Warburg | condition.

CONCLUSION CHARACTERISTICS:
  - Battery performance characterized under target operating conditions.
  - Degradation mechanism identified (SEI growth, Li plating, particle cracking).
  - Recommendations for BMS design and operating window.
  - Limitations: single cell only, limited temperature range, accelerated aging not full calendar.
  - Future: silicon anode integration, solid-state prototype, ML-based SOH prediction.

COMMON REFERENCE VENUES:
  Journal of Power Sources, Electrochimica Acta, Journal of The Electrochemical Society,
  Energy Storage Materials, Journal of Energy Storage, Applied Energy,
  Advanced Energy Materials, Batteries (MDPI)

DOMAIN VOCABULARY:
  Li-ion, NMC, LFP, LCO, solid-state, EDLC, BMS, SOC, SOH, HPPC,
  EIS, Nyquist, ECM, SEI, RSEI, RCT, Warburg, Coulombic efficiency,
  energy density, power density, C-rate, formation cycling, Ragone plot

METHODOLOGY KEYWORDS:
  galvanostatic charge/discharge cycling, HPPC test (SOC-resistance curve), EIS characterization,
  rate capability test, Coulombic efficiency measurement, thermal chamber testing,
  ECM fitting (ZView/MATLAB), capacity fade analysis, formation cycling protocol
""",

"entrepreneurship": """================================================================================
TOPIC GUIDE — Entrepreneurship & Innovation
================================================================================
FIELD: Business / Management
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Kewirausahaan, Startup, UMKM, Inovasi, Ekosistem Wirausaha, Wirausaha Digital

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: entrepreneurial phenomenon studied (startup success factors,
  UMKM innovation, ecosystem, digital entrepreneurship), methodology (survey n=,
  case study, SEM-PLS), key findings (factor loadings, success determinants, barrier types),
  and managerial/policy implications.

INTRODUCTION ELEMENTS:
  - Entrepreneurship importance: job creation, economic growth, GDP contribution.
  - UMKM context: Indonesia 99.9% of business units, 60.5% GDP contribution, 97% employment.
  - Digital economy: e-commerce (Tokopedia, Shopee), fintech, digital startup ecosystem.
  - Research gap: specific sector, regional context, post-pandemic recovery, platform economy.
  - Research questions and objectives.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Entrepreneurship theories: Schumpeterian creative destruction, Kirzner opportunity recognition, Sarasvathy effectuation vs. causation.
  - Entrepreneurial intention: Theory of Planned Behavior (Ajzen), EIQ (Entrepreneurial Intention Questionnaire).
  - Innovation: disruptive innovation (Christensen), open innovation (Chesbrough), BMC (Business Model Canvas).
  - UMKM: Undang-Undang No. 20/2008 (classification by assets/turnover); digitalization challenge.
  - Ecosystem: Isenberg (2011) 6-domain model (policy, finance, culture, supports, HR, markets); Silicon Valley vs. emerging market.
  - Resource-based view (RBV): Barney (1991); VRIN (valuable, rare, inimitable, non-substitutable).
  - Digital entrepreneurship: platform economy, gig economy, born-global startups.

METHODOLOGY:
  Common section name: "Research Methodology" / "Methods"
  - Quantitative: survey (n=100–500 entrepreneurs/managers); validated scales; SEM-PLS (SmartPLS 4).
  - Qualitative: case study (multiple cases n=3–10); semi-structured interview; within/cross-case analysis.
  - Mixed: sequential exploratory or sequential explanatory.
  - SEM: measurement model (loadings >0.7, AVE >0.5, CR >0.7, Cronbach's α >0.7, HTMT <0.9); structural model (β, t-stat, R²).
  - Sampling: snowball, purposive; entrepreneurs from BPS registry or incubator database.

TYPICAL RESULTS & DISCUSSION:
  - SEM path: entrepreneurial competency → performance β = 0.45, t = 6.2, p<0.001; R² = 0.38.
  - Digital adoption rate: 35–65% of UMKM use digital platform (survey-based).
  - Innovation barriers: access to capital (62%), technology skills (54%), market access (48%).
  - Startup failure rate: 90% fail within 5 years (Blank 2013); Indonesia 90–95% within 3 years.
  - Gender: female entrepreneur proportion: 50.68% of UMKM (BPS 2021).
  Tables: SEM path results, descriptive statistics, barrier frequency.
  Figures: SEM model diagram, barrier Pareto chart, ecosystem radar.

TYPICAL FIGURES:
  - SEM structural model (PLS path diagram).
  - Barrier frequency Pareto chart.
  - Innovation ecosystem radar chart.
  - Startup growth stage funnel.

TYPICAL TABLES:
  - SEM path: path | coefficient | SE | t-stat | p | decision.
  - Measurement model: construct | loading | AVE | CR | α | HTMT.
  - Barrier frequency: barrier | f | % | rank.

CONCLUSION CHARACTERISTICS:
  - Key success factors and barriers identified and quantified.
  - Policy recommendations for government/incubator support.
  - Theoretical contribution to entrepreneurship literature.
  - Limitations: cross-sectional, self-report, single region.
  - Future: longitudinal tracking, ecosystem index development, comparative study.

COMMON REFERENCE VENUES:
  Journal of Business Venturing, Entrepreneurship Theory and Practice, Small Business Economics,
  Journal of Small Business Management, Technovation, International Journal of Entrepreneurship and Innovation,
  Jurnal Manajemen Indonesia (JMI), Asian Journal of Business Research

DOMAIN VOCABULARY:
  UMKM, VRIN, RBV, BMC, SEM-PLS, SmartPLS, effectuation, causation,
  EIQ, disruptive innovation, open innovation, startup, ecosystem, gig economy,
  digital entrepreneurship, Isenberg, AVE, CR, HTMT, path coefficient

METHODOLOGY KEYWORDS:
  SEM-PLS (SmartPLS 4), PLS bootstrapping (n=5000), measurement model assessment (AVE/CR/HTMT),
  entrepreneurial intention survey (EIQ), case study analysis (Yin 2003),
  multiple-case within/cross-case analysis, purposive sampling
""",

"environmental_engineering": """================================================================================
TOPIC GUIDE — Environmental Engineering
================================================================================
FIELD: Engineering / Environmental Science
DEFAULT CITATION STYLE: APA or IEEE
SUBDISCIPLINE: Teknik Lingkungan, Pengolahan Air, Pengelolaan Limbah, Remediasi, AMDAL, Pencemaran

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: environmental problem addressed (water/wastewater treatment,
  air pollution control, solid waste management, soil remediation), technology or method applied,
  scale (lab/pilot/full-scale), key metrics (removal efficiency %, concentration mg/L before/after,
  BOD₅ mg/L, COD mg/L, turbidity NTU, pH, MPN/100mL), and compliance with standards.

INTRODUCTION ELEMENTS:
  - Environmental problem: water pollution (industrial effluent), air quality (PM2.5, NOx), solid waste.
  - Regulation context: PermenLHK, Baku Mutu Air (PP 22/2021, PP 82/2001), WHO drinking water standards.
  - Impact: public health, ecosystem degradation, SDG 6 (Clean Water), SDG 11, SDG 12.
  - Research gap: novel treatment method, local pollutant not studied, efficiency improvement.
  - Objectives: design, test, and evaluate treatment system performance.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Water quality parameters: BOD₅, COD, TSS, TDS, pH, DO, turbidity, fecal coliform (MPN/100mL).
  - Treatment technologies: coagulation/flocculation (alum, PAC), sedimentation, filtration (sand, media), activated carbon adsorption, chlorination, UV disinfection.
  - Wastewater biological treatment: aerobic (activated sludge, SBR, MBR), anaerobic (UASB), wetland.
  - Air pollution control: cyclone (PM10+), baghouse filter (PM2.5), ESP, scrubber (SO₂, NOx), catalytic converter.
  - Solid waste: 3R (reduce/reuse/recycle), composting, landfill (sanitary vs. open dump), waste-to-energy.
  - Remediation: bioremediation (biosurfactant, bioaugmentation), phytoremediation, pump-and-treat.
  - AMDAL: Environmental Impact Assessment (EIA) Indonesia; ANDAL, RKL-RPL.

METHODOLOGY:
  Common section name: "Materials and Methods" / "Research Method"
  - Sampling: grab/composite sampling per SNI 6989 (water); frequency and location.
  - Analysis: laboratory analysis per SNI (BOD₅ SNI 6989.72, COD SNI 6989.73, TSS SNI 6989.3).
  - Treatment: lab-scale (bench top, batch), pilot-scale (continuous flow), reactor design.
  - Experimental design: factorial (2^k), response surface methodology (RSM/CCD), single-factor.
  - Variables: pH, coagulant dose (mg/L), contact time (min), temperature (°C).
  - Statistical: ANOVA, Tukey's HSD, regression; Design-Expert for RSM.

TYPICAL RESULTS & DISCUSSION:
  - Coagulation: turbidity removal 80–95% at optimal PAC dose 30–60 mg/L; pH 6–7.
  - BOD₅ removal: activated sludge 85–95% (from 200–500 mg/L to <30 mg/L).
  - COD removal: aerobic biological 70–85%; UASB + aerobic 90–96%.
  - Heavy metal adsorption: activated carbon 80–99% removal (Pb, Cd at 10–50 mg/L initial).
  - Air emission: cyclone PM removal 70–80%; ESP PM2.5 removal 95–99%.
  - Effluent vs. standard: BOD₅ <30 mg/L (Class B Indonesian standard).
  Tables: treatment efficiency by condition, analytical results, parameter comparison.
  Figures: removal efficiency vs. dose/pH/time, before/after comparison bar, reactor diagram.

TYPICAL FIGURES:
  - Removal efficiency vs. coagulant dose curve.
  - Before/after treatment bar chart (BOD₅, COD, TSS).
  - Process flow diagram (treatment system).
  - Adsorption isotherm (Langmuir/Freundlich).
  - Response surface plot (RSM optimization).

TYPICAL TABLES:
  - Treatment results: parameter | influent | effluent | removal (%) | standard.
  - RSM ANOVA: source | SS | df | MS | F | p.
  - Water quality: sampling point | pH | BOD₅ | COD | TSS | turbidity.

CONCLUSION CHARACTERISTICS:
  - Treatment technology achieves required removal efficiency meeting regulatory standard.
  - Optimal operating conditions identified.
  - Cost-effectiveness and scalability discussed.
  - Limitations: lab-scale to full-scale gap, seasonal variation, complex real wastewater.
  - Future: pilot plant testing, cost-benefit analysis, integrated water resource management.

COMMON REFERENCE VENUES:
  Journal of Environmental Management, Bioresource Technology, Water Research,
  Chemosphere, Journal of Hazardous Materials, Environmental Technology & Innovation,
  Water Science and Technology, Jurnal Teknologi Lingkungan (ITB)

DOMAIN VOCABULARY:
  BOD₅, COD, TSS, TDS, DO, turbidity, MPN, PAC, coagulation, flocculation,
  activated sludge, SBR, MBR, UASB, adsorption, isotherm, Langmuir, Freundlich,
  AMDAL, ANDAL, baku mutu, SNI 6989, PM2.5, ESP, bioremediation, phytoremediation

METHODOLOGY KEYWORDS:
  coagulation-flocculation jar test, activated sludge treatment, batch/continuous reactor,
  RSM/CCD optimization (Design-Expert), SNI 6989 water quality analysis, BOD₅/COD measurement,
  heavy metal adsorption isotherm (Langmuir/Freundlich), ANOVA with Tukey's HSD
""",

"environmental_science": """================================================================================
TOPIC GUIDE — Environmental Science
================================================================================
FIELD: Natural Sciences / Environmental Studies
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Ilmu Lingkungan, Ekologi, Biodiversitas, Pencemaran Lingkungan, Ekosistem, Konservasi Lingkungan

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: environmental system studied (ecosystem, species, pollutant,
  landscape), study area and scale, methods (field survey, laboratory analysis, GIS, remote sensing),
  key findings (pollutant concentration, biodiversity index, land use change ha/%), and
  environmental management/conservation implications.

INTRODUCTION ELEMENTS:
  - Global and local environmental challenge: biodiversity loss, land degradation, pollution.
  - Ecosystem services: provisioning, regulating, cultural, supporting (MEA 2005).
  - Specific problem: species decline, habitat fragmentation, heavy metal contamination, eutrophication.
  - Research gap: baseline not established, species inventory, pollution status, land change monitoring.
  - Objectives: assess, monitor, characterize, or model environmental condition.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Ecology: community ecology (species richness, diversity, evenness), trophic structure, succession.
  - Biodiversity indices: Shannon-Wiener H', Simpson's D, Margalef's D, species richness S, Pielou's J.
  - Pollution ecology: bioaccumulation factor (BAF), bioconcentration factor (BCF), trophic magnification.
  - Heavy metals: Cd, Pb, Hg, As, Cr in soil/sediment/water; EPA Eco-SSL, WHO soil guidelines.
  - Land use/cover change (LUCC): NDVI, NDBI, deforestation rate, fragmentation (FRAGSTATS metrics: PD, LPI, ENN).
  - Environmental impact assessment (EIA): baseline data, predicted impact, significance determination.
  - Conservation: IUCN Red List categories (CR, EN, VU, NT, LC), key biodiversity areas (KBA).

METHODOLOGY:
  Common section name: "Materials and Methods" / "Research Methods"
  - Field survey: transect, quadrat, point count (birds), pitfall trap (invertebrates); GPS coordinates.
  - Remote sensing: Landsat/Sentinel-2 LULC classification (SVM, Random Forest); NDVI, NDWI, NDBI.
  - GIS: spatial analysis (ArcGIS/QGIS); overlay, buffer, proximity analysis; FRAGSTATS landscape metrics.
  - Sampling: soil/water/sediment sampling (grid/random); n=15–30 composite; preservation, transport.
  - Chemical analysis: heavy metals (AAS/ICP-OES); water quality (multiparameter); sediment grain size.
  - Biodiversity: Shannon H' = -Σpi·ln(pi); Simpson D = Σpi²; evenness J = H'/ln(S); Jaccard similarity.
  - Statistical: ANOVA, Kruskal-Wallis, cluster analysis (UPGMA); Pearson r.

TYPICAL RESULTS & DISCUSSION:
  - Shannon diversity: H' >3.0 = high diversity; H' 1.5–3.0 = moderate; H' <1.5 = low.
  - NDVI change: forest degradation detected, NDVI decline 0.2–0.4 (dense to open/degraded).
  - Heavy metal: Pb in urban soil 50–500 mg/kg (EPA Eco-SSL: 400 mg/kg for ecological risk).
  - Land cover change: 15–30% forest loss over 10 years in study area.
  - Fragmentation: landscape perforated → dissected → fragmented (PD, ENN metrics progression).
  Tables: species list with abundance, pollution concentration vs. standard, land cover area.
  Figures: biodiversity map, land use change map, heavy metal distribution, diversity index chart.

TYPICAL FIGURES:
  - Land use/cover change map (multi-temporal).
  - Biodiversity index bar chart by site.
  - Heavy metal concentration contour map.
  - Species abundance frequency histogram.
  - NDVI change detection map.

TYPICAL TABLES:
  - Species list: species | family | abundance | IVI | status (IUCN).
  - Pollution: site | Pb | Cd | Cr | pH | status vs. guideline.
  - LUCC: class | 2010 area (ha) | 2020 area (ha) | change (ha) | change %.

CONCLUSION CHARACTERISTICS:
  - Environmental status quantified and spatially characterized.
  - Biodiversity level and threats identified.
  - Conservation/management priority areas delineated.
  - Limitations: single season survey, spatial scale, accessible areas only.
  - Future: long-term monitoring, ecosystem services valuation, conservation action plan.

COMMON REFERENCE VENUES:
  Environmental Science & Technology, Ecological Indicators, Science of the Total Environment,
  Biodiversity and Conservation, Landscape Ecology, Applied Geography,
  International Journal of Environmental Research and Public Health, Jurnal Biologi Indonesia

DOMAIN VOCABULARY:
  Shannon H', Simpson D, Pielou J, IVI, NDVI, NDWI, NDBI, FRAGSTATS, PD, LPI, ENN,
  BAF, BCF, AAS, ICP-OES, Eco-SSL, IUCN, LUCC, ecosystem services, eutrophication,
  heavy metals, trophic magnification, UPGMA, Jaccard, keystone species

METHODOLOGY KEYWORDS:
  Landsat/Sentinel-2 LULC classification, FRAGSTATS landscape metrics, Shannon-Wiener diversity index,
  heavy metal analysis (AAS/ICP-OES), GIS spatial overlay (ArcGIS/QGIS),
  NDVI change detection, quadrat/transect field survey, Kruskal-Wallis non-parametric test
""",

"epidemiology": """================================================================================
TOPIC GUIDE — Epidemiology
================================================================================
FIELD: Public Health / Medicine
DEFAULT CITATION STYLE: Vancouver or APA
SUBDISCIPLINE: Epidemiologi, Epidemiologi Penyakit Menular, Epidemiologi Kronis, Surveilans, Outbreak

ABSTRACT CHARACTERISTICS:
  150–250 words (structured preferred). Reports: disease/condition studied, study population
  (n, location, time period), study design (cross-sectional, cohort, case-control, RCT, systematic review),
  exposure(s), key findings (prevalence %, incidence rate/100,000, OR, RR, HR with 95% CI, p-value),
  and public health implications.

INTRODUCTION ELEMENTS:
  - Disease burden: global and Indonesia-specific prevalence/incidence data (WHO, Riskesdas, P2P).
  - Disease risk factors and transmission pathway.
  - Public health significance: mortality, morbidity, DALY (disability-adjusted life years).
  - Research gap: local prevalence unknown, risk factor unexplored, intervention not evaluated.
  - Research objectives and hypotheses.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Epidemiological measures: prevalence, incidence rate (per 100,000 person-years), attack rate, CFR.
  - Study designs: RCT > cohort > case-control > cross-sectional > case series (evidence hierarchy).
  - Epidemiological triangle: agent, host, environment; web of causation.
  - Communicable disease: R₀ (basic reproduction number), serial interval, herd immunity threshold.
  - Non-communicable disease (NCD): COPD, diabetes (HbA1c), hypertension, cardiovascular risk (Framingham).
  - Bias: selection bias, information bias, confounding; Bradford Hill criteria (causation).
  - Regression: logistic regression (OR), Cox regression (HR, Kaplan-Meier), Poisson (rate), multilevel.

METHODOLOGY:
  Common section name: "Materials and Methods" / "Research Method"
  - Study design: cohort (prospective/retrospective), case-control, cross-sectional, ecological.
  - Sample: power calculation (OR 2.0, α=0.05, power 80%); sampling method; inclusion/exclusion criteria.
  - Data collection: questionnaire (interview/self-administered), medical record, laboratory (IgG, IgM, PCR).
  - Exposure measurement: behavioral (dietary, smoking, physical activity), environmental (PM2.5, water quality), biological (BMI, blood pressure).
  - Analysis: descriptive (frequency, mean ± SD, IQR), chi-square, logistic regression (crude OR → adjusted OR), multivariate.
  - Statistical software: SPSS, Stata, R (epiR, survival package).
  - Ethics: ethical approval (KEPK), informed consent, data anonymization.

TYPICAL RESULTS & DISCUSSION:
  - Prevalence: hypertension Indonesia 34.1% (Riskesdas 2018); diabetes 10.9%.
  - OR: smoking → lung cancer OR 15–30 (95% CI 10–45); BMI >25 → diabetes OR 3–5 (95% CI 2–8).
  - Relative risk (cohort): environmental PM2.5 → ISPA RR 1.5–2.5 (95% CI 1.2–3.2).
  - Logistic regression: adjusted for age, sex, SES — obesity → T2DM aOR 3.2 (95% CI 2.1–4.9, p<0.001).
  - Kaplan-Meier: 5-year survival HIV-treated 75–85% vs. untreated 50–65%.
  Tables: characteristics of respondents, bivariate analysis, multivariate logistic regression.
  Figures: Kaplan-Meier curve, forest plot, disease distribution map, epidemic curve.

TYPICAL FIGURES:
  - Epidemic curve (cases vs. time — outbreak investigation).
  - Kaplan-Meier survival curve.
  - Forest plot (systematic review/meta-analysis).
  - Geographic disease distribution map.
  - Dose-response curve.

TYPICAL TABLES:
  - Characteristics: variable | case (n/%) | control (n/%) | p-value.
  - Bivariate: exposure | case | control | crude OR | 95% CI | p.
  - Multivariate: variable | aOR | 95% CI | p-value.

CONCLUSION CHARACTERISTICS:
  - Disease burden quantified; major risk factors identified.
  - Causal relationship strength assessed (Bradford Hill criteria).
  - Public health and prevention recommendations.
  - Limitations: cross-sectional (no temporality), recall bias, residual confounding.
  - Future: prospective cohort, intervention study, molecular epidemiology.

COMMON REFERENCE VENUES:
  American Journal of Epidemiology, International Journal of Epidemiology, Epidemiology & Infection,
  BMC Public Health, Lancet Infectious Diseases, PLOS ONE, BMJ Open,
  Buletin Penelitian Kesehatan (Indonesia), Berita Kedokteran Masyarakat

DOMAIN VOCABULARY:
  prevalence, incidence rate, R₀, serial interval, CFR, DALY, OR, RR, HR,
  95% CI, Kaplan-Meier, Cox regression, logistic regression, Bradford Hill,
  cohort, case-control, cross-sectional, Riskesdas, KEPK, selection bias, confounding

METHODOLOGY KEYWORDS:
  cross-sectional/cohort/case-control study design, logistic regression (crude/adjusted OR),
  Cox proportional hazards regression, Kaplan-Meier analysis, chi-square test,
  power analysis (OR estimation), Riskesdas secondary data, KEPK ethical approval, SPSS/Stata/R
""",

"finance": """================================================================================
TOPIC GUIDE — Finance & Financial Management
================================================================================
FIELD: Business / Economics
DEFAULT CITATION STYLE: APA or APA 7th
SUBDISCIPLINE: Keuangan, Manajemen Keuangan, Pasar Modal, Perbankan, Keuangan Perusahaan, Risiko Keuangan

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: financial topic studied (stock return, firm performance, credit risk,
  financial distress, capital structure, dividend policy), data source (BEI, KSEI, OJK, Bloomberg),
  period (n years), method (regression, event study, SEM, panel data), key results (coefficient,
  statistical significance, R²), and financial/managerial implications.

INTRODUCTION ELEMENTS:
  - Capital market context: BEI (IDX) market capitalization, JCI (IHSG) performance.
  - Financial problem: financial distress, low ROE, high NPL (non-performing loan), capital structure inefficiency.
  - Theoretical context: efficient market hypothesis (Fama), agency theory (Jensen & Meckling), trade-off theory, pecking order theory.
  - Research gap: emerging market evidence, specific sector, post-pandemic period.
  - Research hypotheses based on theory.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Capital structure: trade-off theory (Myers 1984), pecking order (Myers & Majluf 1984); DER, DAR.
  - Firm performance: Tobin's Q, ROA, ROE, EPS; market-based vs. accounting-based.
  - Dividend policy: bird-in-hand (Gordon), MM irrelevance (Modigliani-Miller 1961), signaling theory; DPR.
  - Agency theory: principal-agent (Jensen & Meckling 1976); managerial ownership, board composition.
  - Financial distress: Altman Z-score (1968), Springate S-score; discriminant analysis, logistic regression.
  - Market efficiency: EMH (Fama 1970) — weak, semi-strong, strong form; event study (AR, CAR).
  - Risk: CAPM (β), Fama-French 3-factor, portfolio theory (Markowitz); VaR, CVaR.

METHODOLOGY:
  Common section name: "Research Methodology" / "Data and Method"
  - Data: secondary — annual reports (BEI/IDX), financial statements, stock price data (Yahoo Finance, Bloomberg).
  - Sample: purposive sampling; n=30–200 companies; period 5–10 years; panel data (company × year).
  - Regression: pooled OLS, FE, RE; Hausman test; robust SE (heteroskedasticity/autocorrelation).
  - Event study: event window (-10, +10 days); AR = actual return − expected return (market model); CAR = ΣAR.
  - SEM-PLS or AMOS: structural model with financial constructs.
  - Financial ratio: DER, DAR, ROA, ROE, CR, NPM, Tobin's Q; source from OSIRIS/IDX.

TYPICAL RESULTS & DISCUSSION:
  - DER → ROE: negative significant (β = -0.22, p<0.05) — trade-off theory supported.
  - Altman Z-score: Z>2.99 safe zone; 1.81–2.99 grey; <1.81 distress.
  - Event study CAR: dividend announcement → CAR(0,+5) +1.5–3.5% (positive signal).
  - Tobin's Q: average 1.2–2.5 for IDX LQ45 companies; >1 indicates firm creates value.
  - NPL bank: <5% (OJK threshold); above triggers supervisory action.
  Tables: descriptive statistics, correlation matrix, regression results, Hausman test.
  Figures: ROA/ROE trend, event study CAR timeline, Z-score distribution.

TYPICAL FIGURES:
  - CAR event study graph (days relative to event).
  - ROA/ROE/DER trend line chart.
  - Altman Z-score distribution histogram.
  - Scatter: DER vs. ROE by sector.

TYPICAL TABLES:
  - Descriptive: variable | mean | SD | min | max | n.
  - Regression: variable | coefficient | SE | t-stat | p-value | VIF.
  - Event study: day | AR | t-stat | CAR | significance.

CONCLUSION CHARACTERISTICS:
  - Financial theory supported/rejected based on IDX/emerging market evidence.
  - Determinants of firm performance/capital structure quantified.
  - Managerial and investor implications.
  - Limitations: secondary data reliability, single country, industry-specific, accounting differences.
  - Future: high-frequency trading data, ESG integration, fintech disruption analysis.

COMMON REFERENCE VENUES:
  Journal of Finance, Journal of Financial Economics, Journal of Banking & Finance,
  Pacific-Basin Finance Journal, Finance Research Letters, Jurnal Keuangan dan Perbankan (JKP),
  Jurnal Akuntansi dan Keuangan Indonesia (JAKI), Asian Journal of Finance & Accounting

DOMAIN VOCABULARY:
  ROA, ROE, DER, DAR, EPS, Tobin's Q, CAPM, β, VaR, CVaR, NPL, DPR,
  Altman Z-score, EMH, CAR, AR, event study, trade-off theory, pecking order,
  agency theory, Jensen & Meckling, panel data, Hausman test, BEI/IDX, IHSG

METHODOLOGY KEYWORDS:
  panel data regression (FE/RE, Hausman test), event study (AR/CAR calculation, market model),
  Altman Z-score financial distress analysis, Tobin's Q calculation, SEM-PLS financial constructs,
  pooled OLS with robust SE, financial ratio analysis (IDX annual report data)
""",

}

def write_topic(name, content):
    path = os.path.join(D, f"{name}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.lstrip())
    print(f"  wrote {name}.txt")

for name, content in TOPICS.items():
    write_topic(name, content)
print(f"gen_10: {len(TOPICS)} topics written.")

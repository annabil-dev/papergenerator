"""Generator: CS/AI/IoT/Cybersecurity, Earth Science, Energy — 10 topic files"""
import os; D = os.path.dirname(os.path.abspath(__file__))

TOPICS = {

"machine_learning_ai": """================================================================================
TOPIC GUIDE — Machine Learning & Artificial Intelligence
================================================================================
FIELD: Computer Science / Artificial Intelligence
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Machine Learning, Deep Learning, Computer Vision, NLP, Reinforcement Learning

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: task/problem (classification, detection, regression, generation),
  dataset used, model architecture proposed, benchmark comparison, key metrics
  (accuracy %, F1-score, mAP %, RMSE, AUC-ROC, BLEU score), with baseline comparison.

INTRODUCTION ELEMENTS:
  - Problem context: volume of data, real-world application importance.
  - Limitations of existing approaches: low accuracy, computational cost, lack of explainability.
  - Proposed contribution: novel architecture/module/training strategy.
  - Research questions and hypotheses.
  - Paper organization overview.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - Foundation models: CNNs (VGG, ResNet, EfficientNet), Transformers (ViT, BERT, GPT), RNNs/LSTMs.
  - Task-specific review: image classification, object detection (YOLO family, RCNN), NLP (text classification, NER).
  - Key techniques: batch normalization, dropout, attention mechanism, transfer learning, data augmentation.
  - Loss functions: cross-entropy, focal loss, Dice loss, MSE, contrastive loss.
  - Explainability: Grad-CAM, SHAP, LIME for black-box model interpretation.
  - Datasets: ImageNet (1.2M), COCO (80 classes), CIFAR-10/100, VOC, custom datasets.

METHODOLOGY:
  Common section name: "Methodology" / "Proposed Method"
  - Dataset: source, size (n samples, n classes), train/val/test split (70/15/15 or 80/10/10).
  - Preprocessing: normalization, resizing, augmentation (flip, rotate, color jitter, mixup).
  - Model: architecture description with layer details; parameter count (M).
  - Training: optimizer (Adam, SGD), LR (1e-3 to 1e-5), batch size, epochs (50–300), GPU used.
  - Transfer learning: pretrained weights (ImageNet); fine-tuning strategy (freeze layers).
  - Evaluation: k-fold cross validation (k=5 or 10); confusion matrix; metrics per class.
  - Statistical: McNemar's test for model comparison significance; mean ± std over k folds.
  - Ablation study: contribution of each proposed component.

TYPICAL RESULTS & DISCUSSION:
  - Classification accuracy: CIFAR-10 baseline ~93%; SOTA ~99%; custom medical 75–95%.
  - Object detection mAP50: COCO baseline YOLO 50–70%; proposed improvement +3–8%.
  - AUC-ROC: medical diagnosis binary 0.85–0.97.
  - Precision/Recall/F1: balanced dataset 85–95%; imbalanced 70–85% (macro avg).
  - Training time: typically 2–24h on single GPU (V100/A100).
  Tables: comparison with baselines (model | params | FLOPs | accuracy | F1 | AUC).
  Figures: training/validation loss curves, confusion matrix, Grad-CAM visualization.

TYPICAL FIGURES:
  - Training/validation loss and accuracy curves.
  - Confusion matrix (heatmap).
  - Grad-CAM or SHAP visualization on sample images.
  - Architecture diagram (proposed model).
  - Bar chart: comparison with SOTA methods.
  - ROC curve with AUC values.

TYPICAL TABLES:
  - Comparison: method | year | backbone | dataset | accuracy | F1 | params (M).
  - Ablation study: component added | accuracy change.
  - Per-class metrics: class name | precision | recall | F1.

CONCLUSION CHARACTERISTICS:
  - Proposed method outperforms baselines on key metrics.
  - Ablation confirms contribution of each component.
  - Limitations: dataset size/bias, computational requirements, domain shift.
  - Future: real-time deployment, edge computing, federated learning, domain adaptation.

COMMON REFERENCE VENUES:
  IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI),
  IEEE CVPR, ICCV, ECCV, NeurIPS, ICML, ICLR, AAAI,
  Pattern Recognition, Expert Systems with Applications,
  Neural Networks, Applied Soft Computing, IEEE Access

DOMAIN VOCABULARY:
  CNN, Transformer, ViT, BERT, ResNet, YOLO, mAP, AUC-ROC, F1-score, precision,
  recall, cross-entropy, focal loss, attention, dropout, batch normalization,
  transfer learning, data augmentation, Grad-CAM, SHAP, overfitting, regularization

METHODOLOGY KEYWORDS:
  k-fold cross-validation, hyperparameter tuning, ablation study, confusion matrix,
  Grad-CAM visualization, train/val/test split, PyTorch/TensorFlow training,
  transfer learning fine-tuning, McNemar's test, benchmark comparison
""",

"iot_systems": """================================================================================
TOPIC GUIDE — Internet of Things (IoT) & Embedded Systems
================================================================================
FIELD: Computer Science / Engineering
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: IoT, Sensor, Embedded System, Smart Environment, Edge Computing, MQTT, LoRa

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: IoT application domain (smart agriculture, smart health, smart home,
  industry 4.0), system architecture, sensors used, communication protocol, performance metrics
  (latency ms, packet delivery ratio %, power consumption mW, accuracy %).

INTRODUCTION ELEMENTS:
  - IoT market size (50+ billion connected devices by 2030) and application potential.
  - Specific challenge: real-time monitoring, low power, reliable connectivity, data security.
  - Research gap: new sensor integration, edge computing, protocol comparison, novel application.
  - Objectives: design, implement, evaluate IoT system.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - IoT architecture: perception layer (sensors), network layer (protocols), application layer.
  - Microcontrollers: Arduino (AVR), Raspberry Pi (ARM), ESP32 (dual-core, WiFi+BT), STM32.
  - Communication protocols: MQTT, CoAP, HTTP/REST; wireless: WiFi, ZigBee, LoRa/LoRaWAN, BLE, NB-IoT.
  - Sensors: temperature/humidity (DHT22, SHT31), soil moisture (capacitive), gas (MQ series), IMU (MPU6050).
  - Edge computing: local processing to reduce latency and bandwidth.
  - Security: TLS/SSL encryption, authentication, end-to-end encryption.
  - Platforms: ThingsBoard, AWS IoT, Blynk, Node-RED.

METHODOLOGY:
  Common section name: "System Design and Implementation"
  - Hardware components: MCU model, sensors list, actuators, communication modules.
  - Software: firmware (C/C++, MicroPython), RTOS (FreeRTOS), cloud platform.
  - Communication: MQTT broker (Mosquitto), publish/subscribe pattern, QoS levels.
  - Data flow: sensor → MCU → broker → cloud/edge → dashboard.
  - Performance testing: latency (RTT ms), PDR (packet delivery ratio %, n=1000 packets), power measurement (current sensor INA219).
  - Machine learning at edge: TensorFlow Lite, ONNX runtime for inference.
  - Security: TLS 1.2/1.3, token authentication.

TYPICAL RESULTS & DISCUSSION:
  - Latency: WiFi MQTT 20–100 ms; LoRa 1–10 s (trade-off with range).
  - PDR: WiFi >95%; LoRa long range 80–92%.
  - Power: sleep mode ESP32 10–50 µA; active 80–200 mA; LoRa node 3–5 year battery with AA.
  - Sensor accuracy: temperature ±0.5°C; humidity ±2%; soil moisture ±3%.
  - ML inference at edge: accuracy within 2–5% of cloud model; latency <100 ms.
  Tables: hardware components, protocol comparison, power consumption.
  Figures: system architecture diagram, dashboard screenshot, latency/PDR graphs.

TYPICAL FIGURES:
  - System architecture/block diagram.
  - Sensor data time-series plot.
  - Latency comparison bar chart (WiFi vs. LoRa vs. BLE).
  - Power consumption graph.
  - Dashboard UI screenshot.
  - Network topology diagram.

TYPICAL TABLES:
  - Hardware specifications: component | model | specs | power (mA) | cost.
  - Protocol comparison: protocol | range | data rate | power | latency | security.
  - Test results: metric | measured | target | pass/fail.

CONCLUSION CHARACTERISTICS:
  - System successfully implemented and validated.
  - Performance metrics meet target requirements.
  - Comparison with existing systems showing improvements.
  - Limitations: coverage range, battery life, network congestion.
  - Future: AI integration, 5G/NB-IoT, blockchain for data integrity, commercial deployment.

COMMON REFERENCE VENUES:
  IEEE Internet of Things Journal, Sensors (MDPI), Computers & Electrical Engineering,
  IEEE Transactions on Industrial Informatics, Future Generation Computer Systems,
  Journal of Network and Computer Applications, Wireless Communications and Mobile Computing

DOMAIN VOCABULARY:
  ESP32, Raspberry Pi, MQTT, LoRa, LoRaWAN, ZigBee, BLE, NB-IoT, CoAP,
  PDR, RTT, latency, throughput, ADC, I2C, SPI, UART, DHT22, MPU6050,
  FreeRTOS, TensorFlow Lite, edge computing, fog computing, cloud IoT

METHODOLOGY KEYWORDS:
  prototype implementation, hardware-in-the-loop testing, MQTT stress testing,
  latency measurement (RTT), PDR measurement (packet counter), power profiling (INA219),
  sensor calibration, TinyML deployment, network emulation (ns-3)
""",

"cybersecurity_network": """================================================================================
TOPIC GUIDE — Cybersecurity & Network Security
================================================================================
FIELD: Computer Science / Information Security
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Keamanan Siber, Deteksi Intrusi, Kriptografi, Forensik Digital, Keamanan Jaringan

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: security problem (attack type, vulnerability, threat),
  proposed solution (IDS, cryptographic scheme, authentication protocol), evaluation method,
  performance metrics (detection rate %, FPR %, accuracy, encryption/decryption time ms, throughput).

INTRODUCTION ELEMENTS:
  - Cyberthreat landscape: DDoS, ransomware, APT, IoT attacks, data breaches.
  - Specific vulnerability: protocol weakness, AI model attack, network perimeter breach.
  - Limitations of existing solutions: high FPR, resource intensive, lack of scalability.
  - Research gap: novel attack vector, specific environment (IoT, 5G, cloud), new countermeasure.
  - Objectives: detect, prevent, mitigate specific threat.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - Attack taxonomy: OWASP Top 10, MITRE ATT&CK framework.
  - IDS/IPS: signature-based vs. anomaly-based; Snort, Suricata, ML-based IDS.
  - Datasets: NSL-KDD, CICIDS-2017, UNSW-NB15, KDD Cup 99.
  - Cryptography: symmetric (AES, ChaCha20), asymmetric (RSA, ECC), PQC (post-quantum: CRYSTALS-Kyber, Dilithium).
  - Authentication: multi-factor (MFA), biometrics, zero-trust architecture.
  - Adversarial ML: evasion attacks (FGSM, PGD), poisoning, backdoor; defenses (adversarial training).
  - Blockchain in security: tamper-proof logging, smart contracts for access control.

METHODOLOGY:
  Common section name: "Methodology" / "Proposed Scheme"
  - Environment: testbed (GNS3/NS-3 simulation, QEMU, physical lab), OS (Kali Linux, Ubuntu).
  - Attack simulation: tools (Metasploit, Scapy, hping3), attack types (SYN flood, port scan, DoS).
  - IDS: feature selection (PCA, RF feature importance), ML algorithm (RF, XGBoost, LSTM), training/testing split.
  - Cryptographic evaluation: key generation time, enc/dec throughput (KB/s or MB/s), CPU usage %.
  - Dataset: attack vs. normal traffic ratio, n samples, features used.
  - Metrics: accuracy, precision, recall, F1, FPR (false positive rate), FNR; ROC-AUC.
  - Formal verification (if protocol): ProVerif, Scyther tools.

TYPICAL RESULTS & DISCUSSION:
  - IDS accuracy: ML-based 95–99% on benchmark datasets (NSL-KDD, CICIDS).
  - FPR: target <5%; good results <1%.
  - Detection rate (DR): >95% for known attacks; 80–90% for zero-day.
  - Encryption throughput: AES-256-GCM 500–2000 MB/s on modern CPU.
  - Key exchange time: ECC 256-bit: 0.5–2 ms; PQC Kyber: 0.3–1 ms.
  - Energy cost: IoT device encryption overhead +15–30% power.
  Tables: comparison with SOTA IDS, cryptographic performance, confusion matrix.
  Figures: ROC curve, confusion matrix, traffic volume time series, topology diagram.

TYPICAL FIGURES:
  - ROC curve for IDS (TPR vs. FPR).
  - Confusion matrix (heatmap).
  - Network topology/attack scenario diagram.
  - Throughput/latency comparison bar chart.
  - Time-series: anomaly detection score vs. time.

TYPICAL TABLES:
  - Comparison: method | dataset | accuracy | F1 | FPR | FNR | detection rate.
  - Cryptographic: algorithm | key size | enc time (ms) | dec time (ms) | memory (KB).
  - Feature importance: top 10 features for IDS classification.

CONCLUSION CHARACTERISTICS:
  - Security solution effectiveness demonstrated on standard benchmarks.
  - Trade-off between security, performance, and overhead.
  - OWASP/MITRE coverage of proposed solution.
  - Limitations: controlled environment, limited attack types, hardware-specific.
  - Future: adversarial robustness, 5G/edge deployment, real-world validation.

COMMON REFERENCE VENUES:
  IEEE Transactions on Information Forensics and Security,
  Computers & Security, IEEE Access, Journal of Information Security and Applications,
  ACM CCS, IEEE S&P, NDSS, USENIX Security,
  Future Internet, Journal of Cybersecurity

DOMAIN VOCABULARY:
  IDS, IPS, DDoS, APT, OWASP, MITRE ATT&CK, AES, RSA, ECC, PQC, TLS,
  FPR, FNR, TPR, ROC-AUC, NSL-KDD, CICIDS, XGBoost, LSTM, zero-trust,
  MFA, blockchain, adversarial ML, FGSM, Snort, Metasploit, honeypot

METHODOLOGY KEYWORDS:
  ML-based IDS (RF/XGBoost/LSTM), NSL-KDD/CICIDS dataset evaluation,
  confusion matrix, ROC-AUC, network simulation (NS-3/GNS3),
  cryptographic benchmarking, formal verification (ProVerif), Wireshark capture
""",

"geology_petrology": """================================================================================
TOPIC GUIDE — Geology & Petrology
================================================================================
FIELD: Earth and Planetary Sciences / Geology
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Geologi, Petrologi, Geokimia, Sedimentologi, Geologi Struktur, Vulkanologi

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: study area (location, region), rock unit or geological feature,
  field and lab methods, key findings (rock composition, mineral assemblage, P-T conditions,
  geochemical signature, age Ma, structural orientation).

INTRODUCTION ELEMENTS:
  - Regional geological setting and tectonic framework.
  - Previous work and unresolved questions.
  - Research gap: poorly mapped area, ambiguous genesis, undated formation.
  - Objectives: geological mapping, petrogenesis, geochemistry, structural analysis.

LITERATURE REVIEW:
  Common section name: "Geological Background" / "Regional Geology" / "Literature Review"
  - Regional stratigraphy and tectonic history.
  - Previous geochemical/petrological studies on similar rocks.
  - Plate tectonic setting: arc, ophiolite, continental collision, rift.
  - Geochronology methods: U-Pb zircon, Ar-Ar, Rb-Sr, Sm-Nd.
  - Geochemical discriminant diagrams: TAS (Total Alkali-Silica), AFM, Harker diagrams.
  - Metamorphic grade: P-T path, mineral stability fields.

METHODOLOGY:
  Common section name: "Field and Analytical Methods" / "Methods"
  - Fieldwork: geological mapping (scale 1:10,000 to 1:50,000), structural measurements.
  - Sample collection: representative rock samples (n=20–50), GPS coordinates.
  - Petrography: thin sections, polarized light microscopy; modal analysis.
  - Geochemistry: XRF for major (SiO2, TiO2, Al2O3, etc.) and trace elements (Rb, Sr, Zr, Nb, Y, REE).
  - ICP-MS: trace elements, REE (Rare Earth Elements); detection limits ppb.
  - Geochronology: U-Pb zircon CL imaging + SHRIMP/LA-ICP-MS dating.
  - Isotopes: Sr-Nd (εNd, (87Sr/86Sr)i).
  - P-T thermobarometry: geothermobarometers (garnet-biotite, phengite barometry).

TYPICAL RESULTS & DISCUSSION:
  - Major elements: SiO2 range 45–75 wt%; classification using TAS or QAPF.
  - REE patterns: LREE/HREE ratio (La/YbN = 5–50); Eu anomaly (Eu/Eu*).
  - U-Pb zircon age: reported as X ± Y Ma (2σ); geological significance.
  - εNd values: -5 to +5 for calc-alkaline arc; +8 to +12 for MORB.
  - P-T conditions: T = 550–700°C, P = 5–10 kbar (typical amphibolite facies).
  Tables: whole-rock major/trace element table (n samples), isotopic ratios.
  Figures: TAS diagram, Harker variation diagrams, Chondrite-normalized REE, P-T diagram.

TYPICAL FIGURES:
  - Geological map (study area with legend).
  - Thin section photomicrograph (cross-polarized, plane-polarized).
  - TAS diagram with sample plot.
  - Chondrite-normalized REE spider diagram.
  - Harker variation diagrams (SiO2 vs. major/trace oxides).
  - U-Pb concordia diagram.

TYPICAL TABLES:
  - Whole-rock major element (wt%): SiO2 | TiO2 | Al2O3 | FeOt | MnO | MgO | CaO | Na2O | K2O | P2O5 | LOI.
  - Trace elements (ppm): Rb | Sr | Ba | Zr | Nb | Y | La | Ce | Nd | Sm | Eu | Yb | Lu.
  - Geochronology: sample | mineral | n analyses | age (Ma ± 2σ) | MSWD.

CONCLUSION CHARACTERISTICS:
  - Petrogenesis (magmatic origin, mantle source, crustal contamination) resolved.
  - Tectonic setting interpretation.
  - Geochronological significance.
  - Limitations: limited sample coverage, incomplete isotopic dataset.
  - Future: detailed mapping, more geochronology, P-T path reconstruction.

COMMON REFERENCE VENUES:
  Journal of Petrology, Lithos, Contributions to Mineralogy and Petrology,
  Chemical Geology, Earth and Planetary Science Letters, Precambrian Research,
  Indonesian Journal of Geoscience, Journal of Southeast Asian Earth Sciences

DOMAIN VOCABULARY:
  SiO2, REE, TAS diagram, AFM diagram, Harker plot, Chondrite-normalized,
  εNd, (87Sr/86Sr)i, U-Pb, SHRIMP, LA-ICP-MS, zircon, thermobarometry, P-T path,
  arc, ophiolite, MORB, OIB, tectonic discrimination, modal analysis, LOI

METHODOLOGY KEYWORDS:
  geological mapping, thin section petrography, XRF (major + trace), ICP-MS (REE),
  U-Pb zircon dating (SHRIMP/LA-ICP-MS), Sm-Nd isotopes, thermobarometry,
  TAS diagram, spider diagram normalization, CL imaging of zircons
""",

"oceanography": """================================================================================
TOPIC GUIDE — Oceanography & Marine Science
================================================================================
FIELD: Earth and Planetary Sciences / Oceanography
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Oseanografi Fisik, Kimia Laut, Biologi Laut, Pesisir, Sedimen Laut

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: ocean region studied, parameters measured (T, S, DO, turbidity, nutrients,
  chlorophyll-a µg/L), methods (CTD cast, water sampling, remote sensing, sediment core),
  key findings (spatial/temporal patterns, correlation coefficients, upwelling indicators,
  sediment accumulation rates).

INTRODUCTION ELEMENTS:
  - Ocean's role in climate regulation, biodiversity, fisheries.
  - Specific oceanographic feature: upwelling system, estuary, coral reef, deep sea.
  - Research gap: unstudied area, seasonal pattern, pollution impact, climate change signal.
  - Objectives: characterize, map, quantify oceanographic parameters.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Physical oceanography: thermohaline circulation, ENSO influence, monsoon effect.
  - Chemical oceanography: nutrient cycles (N, P, Si), dissolved oxygen, carbonate system (pH, Ω aragonite).
  - Biological oceanography: phytoplankton dynamics (Chl-a), zooplankton, primary productivity.
  - Sedimentology: grain size, total organic carbon (TOC %), biomarkers.
  - Coastal dynamics: wave height (Hs), tidal current, littoral drift.
  - Ocean acidification: pCO2, pH decline trend, impact on calcifiers.

METHODOLOGY:
  Common section name: "Materials and Methods" / "Study Area and Methods"
  - Field survey: stations (GPS coordinates), seasons (wet/dry), transects.
  - Physical: CTD (conductivity-temperature-depth) cast; T (°C), S (psu), σθ (density).
  - Chemical: dissolved oxygen (Winkler titration), nutrients (NO3, NO2, PO4, SiO4 by spectrophotometry), pH.
  - Biological: chlorophyll-a (fluorometric method, µg/L); plankton net tow, identification.
  - Sediment: box core/gravity core; grain size (sieving/Mastersizer), TOC (CHNS analyzer), 210Pb for dating.
  - Remote sensing: Landsat, Sentinel-2 (SST, turbidity, Chl-a from satellite).
  - Statistical: correlation, PCA for water mass identification, ANOVA (season).

TYPICAL RESULTS & DISCUSSION:
  - SST: tropical Indonesia 27–32°C; upwelling area 22–25°C.
  - Salinity: open ocean 34–36 psu; estuary 0–34 psu mixing.
  - Chl-a: oligotrophic <0.1 µg/L; eutrophic >5 µg/L.
  - DO: well-oxygenated >6 mg/L; hypoxic <2 mg/L (dead zone indicator).
  - NO3: open ocean 0–1 µM; upwelling zone 5–20 µM.
  - Sediment TOC: deep sea 0.5–2%; coastal nearshore 2–5%.
  Tables: station data table (T | S | DO | nutrients | Chl-a by station/depth).
  Figures: T-S diagram, CTD profiles, contour map (interpolated), seasonal comparison.

TYPICAL FIGURES:
  - T-S diagram (water mass identification).
  - CTD vertical profiles: T, S, DO, Chl-a vs. depth.
  - Spatial contour map: interpolated T/Chl-a/turbidity.
  - Seasonal box plot: Chl-a or nutrient concentrations.
  - Remote sensing image: SST or Chl-a color composite.

TYPICAL TABLES:
  - Station data: station ID | lat | lon | depth | T | S | DO | pH | NO3 | PO4 | Chl-a.
  - Seasonal statistics: season | mean T | mean Chl-a | mean NO3 (mean ± SD).
  - Sediment: core depth | grain size D50 | TOC % | δ¹³C | age (year).

CONCLUSION CHARACTERISTICS:
  - Oceanographic characterization of study area completed.
  - Seasonal/spatial variability explained by physical forcing (monsoon, upwelling, ENSO).
  - Marine biodiversity/fishery implications.
  - Limitations: limited sampling frequency, vessel access constraints.
  - Future: multi-year dataset, biogeochemical modeling, acidification monitoring.

COMMON REFERENCE VENUES:
  Deep-Sea Research (Part I & II), Ocean Science, Journal of Geophysical Research (Oceans),
  Estuarine, Coastal and Shelf Science, Marine Pollution Bulletin, Limnology and Oceanography,
  Continental Shelf Research, Remote Sensing of Environment

DOMAIN VOCABULARY:
  CTD, SST, salinity, pycnocline, thermocline, upwelling, Chl-a, DO, NO3, PO4, Si,
  T-S diagram, water mass, eutrophication, carbonate system, pCO2, Ω aragonite,
  sediment TOC, 210Pb dating, phytoplankton bloom, turbidity, bathymetry

METHODOLOGY KEYWORDS:
  CTD profiling, water sampling (Niskin bottle), Winkler DO titration, nutrient analysis
  (AutoAnalyzer/spectrophotometry), fluorometric Chl-a, sediment coring, grain size analysis,
  210Pb dating, remote sensing (MODIS/Sentinel-2), PCA water mass analysis
""",

"solar_renewable_energy": """================================================================================
TOPIC GUIDE — Solar & Renewable Energy Systems
================================================================================
FIELD: Energy / Engineering
DEFAULT CITATION STYLE: APA or IEEE
SUBDISCIPLINE: Energi Surya, PLTS, Energi Angin, Bioenergi, Sistem Penyimpanan Energi, Smart Grid

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: energy system studied (PV, wind, hybrid, storage),
  location/resource, system size (kWp, MW), analysis method (simulation/experimental/techno-economic),
  key results (energy yield kWh/year, capacity factor %, LCOE USD/kWh, CO2 reduction tCO2/year,
  system efficiency %, payback period years).

INTRODUCTION ELEMENTS:
  - Global energy transition: fossil fuel depletion, climate change, renewable targets.
  - Local energy context: electrification rate, solar irradiance potential (Indonesia: 4.5–6 kWh/m²/day).
  - Specific challenge: intermittency, LCOE competitiveness, grid integration.
  - Research gap: specific location not assessed, hybrid system optimization, new technology.
  - Objectives: design, simulate, evaluate techno-economic feasibility.

LITERATURE REVIEW:
  Common section name: "Literature Review"
  - Solar PV: cell technologies (mono-Si, poly-Si, thin film, perovskite), efficiency 15–26%.
  - Wind: turbine types, capacity factor (25–45%), wind speed class (Weibull distribution).
  - Hybrid systems: PV+wind+battery+diesel; optimization methods (HOMER, MINLP, GA).
  - LCOE components: capex (USD/kW), opex (USD/kW/year), interest rate (WACC).
  - Energy storage: Li-ion battery (90–95% round-trip), pumped hydro, hydrogen (electrolysis).
  - Grid: net metering, feed-in tariff, power quality (THD <5%, voltage ±10%).
  - GHI (Global Horizontal Irradiance) data: NASA POWER, PVGIS, SolarAnywhere.

METHODOLOGY:
  Common section name: "System Description and Methodology"
  - Resource assessment: GHI (kWh/m²/day), wind speed (m/s at hub height), NASA POWER or local data.
  - System configuration: PV capacity (kWp), inverter, battery bank, charge controller, load profile.
  - Simulation tool: HOMER Pro, PVsyst, RETScreen, MATLAB/Simulink, SAM (NREL).
  - Economic analysis: NPV (net present value), IRR, LCOE = (Annualized cost)/(Annual energy, kWh).
  - CO2 reduction: = energy generated × grid emission factor (kg CO2/kWh).
  - Experimental (if lab/testbed): I-V curve measurement, soiling effect, MPPT efficiency.
  - Sensitivity: ±20% variation in solar irradiance, fuel price, capex on LCOE.

TYPICAL RESULTS & DISCUSSION:
  - PV capacity factor: tropical region 18–22%; optimal tilt.
  - LCOE: utility-scale PV 0.03–0.05 USD/kWh (2024); off-grid hybrid 0.15–0.30 USD/kWh.
  - Battery storage: 2–4 days autonomy for off-grid; Li-ion cycle 2000–5000.
  - Payback period: grid-tied PV 5–8 years; off-grid 8–15 years.
  - CO2 reduction: 200–400 kgCO2/MWh (vs. coal grid).
  - System efficiency: PV system 75–85% overall (derating factors).
  Tables: energy production summary, economic indicators, sensitivity results.
  Figures: monthly energy production, LCOE sensitivity tornado chart, dispatch graph.

TYPICAL FIGURES:
  - Monthly energy production bar chart (kWh/month).
  - LCOE sensitivity tornado chart.
  - System dispatch graph (power flow over 24h).
  - I-V and P-V curves (if experimental).
  - Site map with solar resource GHI contours.

TYPICAL TABLES:
  - System components: component | capacity | cost | lifetime.
  - Economic: NPV | IRR | LCOE | payback period | CO2 reduction.
  - Sensitivity: parameter ±20% | LCOE impact %; tornado chart data.

CONCLUSION CHARACTERISTICS:
  - System feasibility confirmed (positive NPV, acceptable LCOE).
  - Environmental benefit quantified.
  - Optimal system configuration recommended.
  - Limitations: simulation accuracy, weather uncertainty, policy assumptions.
  - Future: pilot installation, real-time monitoring, AI-based MPPT, grid-scale integration.

COMMON REFERENCE VENUES:
  Applied Energy, Renewable Energy, Energy Conversion and Management,
  Solar Energy, Renewable and Sustainable Energy Reviews, Energy,
  IEEE Transactions on Sustainable Energy, Progress in Photovoltaics

DOMAIN VOCABULARY:
  PV, GHI, capacity factor, LCOE, HOMER, PVsyst, NPV, IRR, payback period,
  Li-ion, MPPT, inverter, tilt angle, soiling, THD, net metering, feed-in tariff,
  Weibull distribution, perovskite, bifacial, storage, dispatch, grid parity

METHODOLOGY KEYWORDS:
  HOMER Pro simulation, PVsyst simulation, resource assessment (NASA POWER/PVGIS),
  LCOE calculation, NPV/IRR/payback analysis, I-V curve measurement, MPPT testing,
  sensitivity analysis, CO2 emission factor, techno-economic feasibility
""",

}

def write_topic(name, content):
    path = os.path.join(D, f"{name}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.lstrip())
    print(f"  wrote {name}.txt")

for name, content in TOPICS.items():
    write_topic(name, content)
print(f"gen_06: {len(TOPICS)} topics written.")

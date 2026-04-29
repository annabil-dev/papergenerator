"""Generator 09: chemistry, civil_engineering, climate_science, cloud_computing,
communication, computer_networks, computer_vision, cybersecurity, data_science,
deep_learning, dentistry, digital_transformation"""
import os; D = os.path.dirname(os.path.abspath(__file__))

TOPICS = {

"chemistry": """================================================================================
TOPIC GUIDE — Chemistry (General)
================================================================================
FIELD: Natural Sciences / Chemistry
DEFAULT CITATION STYLE: ACS or APA
SUBDISCIPLINE: Kimia Umum, Sintesis, Karakterisasi, Kimia Analitik Dasar, Kimia Lingkungan

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: compound or material synthesized/analyzed, method used,
  characterization data (FTIR, NMR chemical shifts ppm, UV-Vis λmax nm, melting point °C),
  and key properties (yield %, purity %, biological activity IC50 µM, degradation efficiency %).

INTRODUCTION ELEMENTS:
  - Chemical or environmental problem: toxic compound removal, drug discovery, material improvement.
  - Research gap: new compound, greener synthesis route, unexplored catalytic system.
  - Theoretical basis: molecular orbital theory, coordination chemistry, reaction mechanism.
  - Objectives: synthesize/characterize/evaluate compound or process.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Organic synthesis: functional group transformations, reaction mechanisms, green chemistry principles.
  - Coordination chemistry: metal complex formation, ligand design, catalytic applications.
  - Analytical methods: NMR (1H, 13C, 2D COSY, HMBC), IR, UV-Vis, MS (ESI-MS, GC-MS), HPLC.
  - Environmental chemistry: heavy metal contamination (Pb, Cd, Hg, As), remediation methods.
  - Natural products: extraction methods (Soxhlet, maceration, UAE), isolation, structure elucidation.
  - Computational chemistry: DFT (B3LYP/6-311G basis), molecular docking, HOMO-LUMO gap.

METHODOLOGY:
  Common section name: "Experimental Procedures" / "Materials and Methods"
  - Reagents: analytical grade (Merck/Sigma-Aldrich), solvent purity, drying procedure.
  - Synthesis: flask setup, reaction conditions (T, time, solvent, catalyst loading wt%), workup (extraction, recrystallization).
  - Characterization: NMR (Bruker 400/500 MHz, in CDCl3/DMSO-d6), FTIR (KBr pellet or ATR), UV-Vis (UV-Vis spectrophotometer), melting point (Stuart apparatus).
  - Purity: TLC (Rf value), HPLC (column C18, UV detection), mass balance.
  - Computational: Gaussian 09/16, B3LYP/6-311+G(d,p), geometry optimization, frequency calculation (no imaginary frequency).
  - Activity testing: antimicrobial (Kirby-Bauer disc diffusion, MIC µg/mL), antioxidant (DPPH IC50).

TYPICAL RESULTS & DISCUSSION:
  - Synthesis yield: 50–90%; typically reported as isolated yield after recrystallization/column.
  - 1H NMR: chemical shifts δ 0–12 ppm with multiplicity (s, d, t, q, m), coupling J (Hz).
  - FTIR: key bands (O-H 3200–3600, C=O 1680–1750, C-H 2850–3000, N-H 3300–3500 cm⁻¹).
  - UV-Vis: λmax 250–400 nm (aromatic/conjugated system).
  - DPPH IC50: potent antioxidant <50 µg/mL; reference vitamin C ~5 µg/mL.
  Tables: spectral data summary (NMR, FTIR, UV), comparison with literature, DFT data.
  Figures: NMR spectrum, FTIR spectrum, UV-Vis absorption curve, crystal structure (if SCXRD).

TYPICAL FIGURES:
  - 1H NMR spectrum with peak assignment.
  - FTIR spectrum with annotated bands.
  - UV-Vis absorption spectrum.
  - Molecular structure with atom numbering.
  - DFT optimized geometry with HOMO-LUMO visualization.

TYPICAL TABLES:
  - NMR data: proton | δ (ppm) | multiplicity | J (Hz) | assignment.
  - FTIR bands: wavenumber (cm⁻¹) | intensity | assignment.
  - Biological activity: compound | IC50 (µM/µg/mL) | reference compound | ratio.

CONCLUSION CHARACTERISTICS:
  - Target compound successfully synthesized and fully characterized.
  - Structure confirmed by spectroscopic evidence.
  - Biological/chemical activity evaluated and compared with reference.
  - Limitations: single solvent system, model organism only, preliminary screening.
  - Future: analogue synthesis (SAR), in vivo testing, scale-up, co-crystallization.

COMMON REFERENCE VENUES:
  Journal of Organic Chemistry, Inorganic Chemistry, ACS Applied Materials & Interfaces,
  Molecules (MDPI), Spectrochimica Acta Part A, Journal of Molecular Structure,
  Environmental Chemistry Letters, RSC Advances, Chemistry Select

DOMAIN VOCABULARY:
  synthesis, yield, NMR (1H, 13C, HMBC, COSY), FTIR, UV-Vis, ESI-MS, HPLC,
  TLC, Rf, Kirby-Bauer, MIC, DPPH IC50, DFT, B3LYP, HOMO-LUMO,
  coordination chemistry, ligand, chelate, green chemistry, E-factor

METHODOLOGY KEYWORDS:
  organic synthesis (reflux/stirring), column chromatography, TLC monitoring,
  NMR characterization (Bruker 400 MHz), FTIR (ATR/KBr), DFT (Gaussian09/16, B3LYP),
  DPPH antioxidant assay, Kirby-Bauer disc diffusion, MIC determination
""",

"civil_engineering": """================================================================================
TOPIC GUIDE — Civil Engineering
================================================================================
FIELD: Engineering / Civil
DEFAULT CITATION STYLE: APA or ASCE
SUBDISCIPLINE: Teknik Sipil, Struktur Bangunan, Transportasi, Geoteknik, Beton, Manajemen Konstruksi

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: civil engineering problem (structural, transportation, geotechnical,
  water resources), method used (experimental, numerical FEM, field measurement), material
  properties or design parameters, key results (compressive strength MPa, bearing capacity kN/m²,
  deflection mm, traffic volume PCU, cost IDR), and engineering significance.

INTRODUCTION ELEMENTS:
  - Infrastructure challenge: aging structures, rapid urbanization, natural disaster vulnerability.
  - Specific engineering problem: structural failure, traffic congestion, soil instability, water shortage.
  - Code/standard context: SNI (Indonesia), ACI, Eurocode, AASHTO.
  - Research gap: new material, analysis method, or local conditions not addressed by standards.
  - Objectives: design, analyze, test, or optimize civil engineering system.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Structural: reinforced concrete (ACI 318), steel (AISC LRFD), timber, composites; beam/column/slab design.
  - Geotechnical: soil classification (USCS), bearing capacity (Terzaghi, Meyerhof), settlement analysis.
  - Transportation: traffic volume (PCU), LOS (Level of Service A–F, HCM), pavement design (CBR, AASHTO).
  - Concrete technology: mix design (SNI 7656:2012), w/c ratio, admixtures (fly ash, silica fume, superplasticizer).
  - Structural analysis: finite element method (SAP2000, ETABS, STAAD.Pro); nonlinear pushover.
  - Hydraulics: open channel flow (Manning's equation), culvert design, flood routing.

METHODOLOGY:
  Common section name: "Materials and Methods" / "Research Method"
  - Material testing: concrete (SNI 1974:2011 compressive strength, splitting tensile, flexural); aggregate gradation; slump test.
  - Structural analysis: FEM modeling (SAP2000/ETABS); load combinations (SNI 1727, SNI 1726 seismic).
  - Geotechnical: SPT, CPT, Atterberg limits, direct shear, triaxial; soil classification.
  - Pavement: Marshall test (asphalt); CBR (California Bearing Ratio); IRI (roughness).
  - Experimental: specimens (3–5 per mix), curing (28 days), loading setup.
  - Statistical: ANOVA, t-test for material properties; regression for pavement performance.

TYPICAL RESULTS & DISCUSSION:
  - Concrete compressive strength: normal 20–30 MPa; high performance 40–80 MPa; fc' 28-day.
  - Fly ash replacement (25%): compressive strength ±5% with improved durability.
  - Bearing capacity: soft clay 30–80 kPa; stiff clay 100–200 kPa; sand 150–500 kPa.
  - Traffic LOS: A (<0.6) to F (>1.0) volume/capacity ratio; C–D acceptable for urban road.
  - Asphalt Marshall: stability 750–1000 kg; flow 2–4 mm (standard specification).
  Tables: material property comparison (mix designs), structural load-deflection table, SPT data.
  Figures: stress-strain curve, load-deflection diagram, structural model, FEM stress contour.

TYPICAL FIGURES:
  - Load-deflection curve (structural testing).
  - Compressive strength bar chart (mix designs comparison).
  - FEM stress distribution contour.
  - Structural cross-section drawing.
  - Soil classification chart / SPT N vs. depth.

TYPICAL TABLES:
  - Mix design: mix | cement | water | FA | CA | admixture | w/c | slump | fc' (MPa).
  - Structural results: element | calculated | capacity | UC ratio.
  - Geotechnical: depth | N-SPT | classification | Cu | φ | γ.

CONCLUSION CHARACTERISTICS:
  - Engineering design meets code requirements with adequate safety margin.
  - Material or method improvement quantified.
  - Cost or efficiency benefit demonstrated.
  - Limitations: lab scale vs. field conditions, idealized loads, single site.
  - Future: field implementation, long-term monitoring, full-scale prototype.

COMMON REFERENCE VENUES:
  Journal of Structural Engineering (ASCE), Construction and Building Materials,
  Engineering Structures, Transportation Research Record, Geotechnique,
  Jurnal Teknik Sipil (ITB/Unibraw), Civil Engineering Dimension,
  Soil Dynamics and Earthquake Engineering

DOMAIN VOCABULARY:
  compressive strength, fc', w/c ratio, fly ash, silica fume, SPT, CPT, CBR,
  bearing capacity, LOS, PCU, SAP2000, ETABS, SNI, ACI 318, AISC LRFD,
  Terzaghi, Meyerhof, Marshall stability, IRI, Atterberg limits, USCS

METHODOLOGY KEYWORDS:
  concrete compressive test (SNI 1974), Marshall asphalt test, SPT/CPT geotechnical,
  FEM (SAP2000/ETABS) structural analysis, seismic load (SNI 1726), mix design,
  28-day curing, pushover nonlinear analysis
""",

"climate_science": """================================================================================
TOPIC GUIDE — Climate Science & Meteorology
================================================================================
FIELD: Earth and Planetary Sciences / Atmospheric Sciences
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Ilmu Iklim, Perubahan Iklim, Meteorologi, Hidrologi, ENSO, Iklim Indonesia

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: climate variable studied (temperature, rainfall, drought index,
  sea level), spatial domain (region, country, watershed), time period (1980–2020),
  methods (GCM simulation, statistical downscaling, trend analysis, remote sensing),
  key findings (trend °C/decade, anomaly magnitude, future projection RCP scenario).

INTRODUCTION ELEMENTS:
  - Global and regional climate change context: IPCC AR6 findings (+1.1°C since pre-industrial).
  - Impact on target sector: agriculture, water resources, coastal areas, public health.
  - Local or regional climate driver: ENSO, IOD (Indian Ocean Dipole), monsoon variability.
  - Research gap: localized trend not quantified, future projection for specific region.
  - Objectives: detect trend, assess variability, project future climate.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Climate change science: greenhouse gas (CO2, CH4, N2O), radiative forcing, global warming potential.
  - IPCC scenarios: SSP1-2.6, SSP2-4.5, SSP3-7.0, SSP5-8.5 (AR6); RCP 2.6, 4.5, 8.5 (AR5).
  - ENSO: El Niño (warm phase, negative IOD), La Niña (cold phase); teleconnections.
  - Indonesia climate: bimodal rainfall, wet/dry season, Borneo/Java/Papua regional patterns.
  - Climate models: GCMs (CMIP6: CESM2, MPI-ESM, ACCESS-CM2), regional models (RegCM, PRECIS).
  - Statistical downscaling: delta method, quantile mapping, BCSD; bias correction.
  - Drought indices: SPI (Standardized Precipitation Index), PDSI, SPEI.
  - Remote sensing: TRMM, GPM (rainfall), MODIS (land surface T), ERA5 reanalysis.

METHODOLOGY:
  Common section name: "Data and Methods" / "Materials and Methods"
  - Data: station observation (BMKG), satellite (GPM IMERG, ERA5), CMIP6 model output.
  - Period: historical 1980–2020 (40 years); future 2021–2100.
  - Trend analysis: Mann-Kendall test (non-parametric, τ), Sen's slope (mm/year or °C/decade); p<0.05.
  - Spatial analysis: IDW/Kriging interpolation; ArcGIS/QGIS mapping.
  - Climate indices: SPI-3, SPI-6, SPI-12 (drought monitoring); ENSO Niño3.4 index correlation.
  - Future projection: bias-corrected CMIP6 output; ensemble mean ± SD for SSP scenarios.
  - Model validation: Taylor diagram; RMSE, bias, correlation for historical simulation.

TYPICAL RESULTS & DISCUSSION:
  - Temperature trend: Indonesia +0.15–0.25°C/decade (1980–2020).
  - Rainfall trend: highly variable; some regions -5% to +10% per decade.
  - ENSO correlation: r = 0.5–0.8 for Java/Sulawesi dry season rainfall (p<0.05).
  - Future T projection (SSP5-8.5): +2.5–4.0°C by 2100 relative to 1981–2010 baseline.
  - Drought frequency: SPI analysis shows 15–25% increase in drought years under SSP3-7.0.
  Tables: trend results by station, climate indices correlation, model skill scores.
  Figures: spatial map of trends, time series with trend line, Taylor diagram, future projection.

TYPICAL FIGURES:
  - Spatial map of temperature/rainfall trend.
  - Time series plot with Mann-Kendall trend line.
  - Taylor diagram (model validation).
  - Box plot: future climate projections under SSP scenarios.
  - Correlation map: ENSO vs. local rainfall.

TYPICAL TABLES:
  - Trend results: station | lat | lon | trend (°C/decade) | Mann-Kendall τ | p-value.
  - Model performance: model | bias | RMSE | r | KGE (Kling-Gupta efficiency).
  - Future projection: scenario | T change 2050 (°C) | T change 2100 | rainfall change %.

CONCLUSION CHARACTERISTICS:
  - Significant warming/drying/wetting trend detected with quantified magnitude.
  - ENSO and other drivers explain inter-annual variability.
  - Future projections indicate increased risk under high-emission scenarios.
  - Limitations: station data gaps, model bias, uncertainty in SSP scenarios.
  - Future: high-resolution downscaling, sectoral impact modeling, adaptation planning.

COMMON REFERENCE VENUES:
  Journal of Climate, Climate Dynamics, Atmospheric Research,
  International Journal of Climatology, Climatic Change,
  Theoretical and Applied Climatology, Journal of Hydrology,
  Climate (MDPI), Jurnal Sains & Teknologi Modifikasi Cuaca (BRIN)

DOMAIN VOCABULARY:
  ENSO, IOD, SSP, RCP, CMIP6, Mann-Kendall, Sen's slope, SPI, SPEI, PDSI,
  GCM, RegCM, ERA5, GPM IMERG, TRMM, BMKG, bias correction, Taylor diagram,
  radiative forcing, greenhouse gas, monsoon, KGE, IDW, Kriging

METHODOLOGY KEYWORDS:
  Mann-Kendall trend test, Sen's slope estimator, quantile mapping (bias correction),
  CMIP6 model evaluation (Taylor diagram/KGE), SPI drought index calculation,
  Kriging/IDW spatial interpolation, ENSO teleconnection correlation analysis
""",

"cloud_computing": """================================================================================
TOPIC GUIDE — Cloud Computing & Distributed Systems
================================================================================
FIELD: Computer Science / Information Technology
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Cloud Computing, Serverless, Microservices, Container, Edge Computing, Cloud Security

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: cloud architecture or service studied, use case (web app,
  ML workload, IoT data), deployment model (IaaS/PaaS/SaaS, public/private/hybrid),
  evaluation metrics (latency ms, throughput req/s, resource utilization %, cost USD/month,
  availability SLA %), comparison with baseline or alternative architecture.

INTRODUCTION ELEMENTS:
  - Cloud adoption growth: cost efficiency, scalability, pay-as-you-go, remote access.
  - Architecture challenge: vendor lock-in, latency, security compliance, resource allocation.
  - Specific problem: auto-scaling bottleneck, cold start in serverless, container orchestration overhead.
  - Research gap: new optimization algorithm, hybrid cloud model, edge-cloud integration.
  - Objectives: design, implement, evaluate cloud-based system architecture.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - Cloud service models: IaaS (EC2, Azure VM), PaaS (App Service, Heroku), SaaS (Office 365, Salesforce); NIST SP 800-145.
  - Containerization: Docker (image, container, registry), Kubernetes (pod, deployment, service, ingress); Helm charts.
  - Microservices: service mesh (Istio, Linkerd), API gateway, circuit breaker pattern.
  - Serverless: AWS Lambda, Azure Functions, Google Cloud Functions; cold start latency 100ms–10s.
  - Resource scheduling: bin packing, Kubernetes HPA (Horizontal Pod Autoscaler), VPA.
  - Cloud-native observability: Prometheus, Grafana, OpenTelemetry; SLO/SLA/SLI.
  - Security: Zero trust (ZTNA), IAM (AWS IAM, RBAC), encryption at rest/in transit (AES-256, TLS 1.3).

METHODOLOGY:
  Common section name: "System Design and Evaluation"
  - Infrastructure: VM specifications (vCPU, RAM, storage), region (AWS/Azure/GCP), deployment.
  - Application: microservice architecture diagram, REST/gRPC APIs, database (RDS, DynamoDB, MongoDB Atlas).
  - Load testing: Apache JMeter, k6, Locust; ramp-up (users), steady state, spike scenarios.
  - Metrics: response time (P50, P95, P99 ms), throughput (RPS), error rate %, CPU/memory utilization %.
  - Autoscaling: HPA trigger (CPU >70%), scale-out time (seconds), scale-in time.
  - Cost: cloud pricing calculator; compute + storage + network cost per month.
  - Comparison: monolith vs. microservices; serverless vs. container.

TYPICAL RESULTS & DISCUSSION:
  - REST API latency (P95): monolith 50–200ms; microservices 20–80ms (with caching).
  - Throughput: basic VM 100–500 req/s; with load balancer 1000–5000 req/s.
  - Serverless cold start: Python Lambda 500ms–2s; Java 2–10s.
  - Kubernetes pod scaling: 30–90s to scale out; HPA response lag.
  - Cost optimization: reserved instances 40–60% cheaper than on-demand.
  - Availability: multi-AZ deployment: 99.99% vs. single-AZ 99.5%.
  Tables: performance comparison, cost analysis, scaling behavior.
  Figures: latency percentile CDF, throughput vs. concurrent users, architecture diagram.

TYPICAL FIGURES:
  - System architecture diagram (cloud-native).
  - Latency CDF (P50/P95/P99) under load.
  - Throughput vs. concurrent users graph.
  - Auto-scaling events timeline (CPU% + pod count).
  - Cost breakdown pie chart.

TYPICAL TABLES:
  - Performance: scenario | throughput (RPS) | P95 latency (ms) | error rate%.
  - Autoscaling: trigger | scale-out pods | scale-out time (s).
  - Cost: service | component | monthly cost (USD).

CONCLUSION CHARACTERISTICS:
  - Cloud architecture meets performance SLAs with efficient resource utilization.
  - Microservices/serverless/container approach advantages quantified.
  - Cost savings demonstrated vs. traditional deployment.
  - Limitations: cloud vendor lock-in, network dependency, specific workload characteristics.
  - Future: multi-cloud, GitOps (ArgoCD/Flux), FinOps, edge-cloud continuum.

COMMON REFERENCE VENUES:
  IEEE Transactions on Cloud Computing, Future Generation Computer Systems,
  Journal of Network and Computer Applications, IEEE Access,
  Cluster Computing, Computing (Springer), Cloud Computing (IEEE)

DOMAIN VOCABULARY:
  IaaS, PaaS, SaaS, Docker, Kubernetes, HPA, VPA, serverless, Lambda,
  microservices, Istio, Prometheus, Grafana, RBAC, IAM, SLA, SLO,
  cold start, bin packing, Helm, k6, JMeter, Locust, REST, gRPC

METHODOLOGY KEYWORDS:
  Docker/Kubernetes deployment, Apache JMeter load testing, Prometheus/Grafana monitoring,
  HPA autoscaling evaluation, latency percentile (P50/P95/P99) measurement,
  cost analysis (cloud pricing calculator), microservices vs. monolith comparison
""",

"communication": """================================================================================
TOPIC GUIDE — Communication Studies & Media Studies
================================================================================
FIELD: Social Sciences / Communication
DEFAULT CITATION STYLE: APA
SUBDISCIPLINE: Komunikasi Massa, Jurnalisme, Komunikasi Digital, Public Relations, Media Sosial

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: communication phenomenon studied, medium/platform analyzed
  (social media, newspaper, TV, organizational communication), methodology (content analysis,
  survey, framing analysis, sentiment analysis), sample (n=), key findings (framing patterns,
  sentiment %, influence factors), and communication implications.

INTRODUCTION ELEMENTS:
  - Media landscape change: digital transformation, social media dominance, declining traditional media.
  - Communication problem: misinformation, crisis communication failure, digital divide, media bias.
  - Theoretical context: framing theory (Entman), agenda-setting (McCombs & Shaw), uses and gratifications.
  - Research gap: specific platform/context, language, or demographic not studied.
  - Research question or hypotheses.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - Communication theories: agenda-setting (McCombs 1972), framing (Entman 1993), cultivation theory (Gerbner), spiral of silence (Noelle-Neumann).
  - Media effects: uses and gratifications (Katz, Blumler, Gurevitch), social learning theory.
  - Digital communication: social media algorithms, filter bubbles, echo chambers (Pariser 2011).
  - Health communication: risk perception, message framing, behavior change (HBM, extended parallel process model).
  - Organizational communication: Grunig's PR models (press agentry, public information, two-way symmetrical).
  - Journalism: gatekeeping theory, news values (Galtung & Ruge), objectivity norms.

METHODOLOGY:
  Common section name: "Research Method" / "Methodology"
  - Content analysis: coding scheme (unitizing, sampling, recording), inter-rater reliability (Cohen's κ >0.7), n=50–500 texts/posts.
  - Framing analysis: Entman's four functions (definition, cause, moral, remedy); qualitative or quantitative.
  - Survey: attitude/behavior/media use questionnaire; Likert scale; n=100–500.
  - Sentiment analysis: VADER (NLTK), TextBlob, BERT-based; Python; dataset (Twitter/Facebook/Instagram API).
  - Social network analysis (SNA): centrality (degree, betweenness), community detection; Gephi/NetworkX.
  - Interview: in-depth (journalists, PR practitioners, n=10–20); thematic analysis.
  - Statistical: chi-square (content categories), Pearson r (media use correlations), regression.

TYPICAL RESULTS & DISCUSSION:
  - Content analysis: thematic categories with frequency (%) and chi-square p<0.05.
  - Cohen's κ: >0.70 = acceptable agreement; >0.80 = strong.
  - Sentiment: positive 40–60%, negative 20–30%, neutral 20–30% (context-dependent).
  - Framing: episodic vs. thematic framing ratio; dominant frames identified.
  - Survey: attitude score mean 3.5–4.2/5.0; regression R² 0.20–0.45.
  Tables: frame/category frequency table, sentiment distribution, inter-rater reliability.
  Figures: word cloud, sentiment trend over time, social network graph, bar chart.

TYPICAL FIGURES:
  - Word cloud of dominant terms.
  - Sentiment trend line over time (crisis communication).
  - Social network graph (nodes = accounts, edges = interactions).
  - Bar chart: frame frequency comparison.
  - Line graph: media coverage volume over event timeline.

TYPICAL TABLES:
  - Content category frequency: category | f | % | chi-square.
  - Inter-rater reliability: coder pair | Cohen's κ | agreement %.
  - Survey regression: variable | B | SE | β | t | p.

CONCLUSION CHARACTERISTICS:
  - Communication patterns described and theoretically interpreted.
  - Implications for media professionals, public communicators, policymakers.
  - Limitations: single platform/period, coder subjectivity, self-report survey bias.
  - Future: longitudinal analysis, cross-platform comparison, experimental design.

COMMON REFERENCE VENUES:
  Journal of Communication, Journalism & Mass Communication Quarterly,
  New Media & Society, Journalism Practice, Media, Culture & Society,
  Asian Journal of Communication, Jurnal Komunikasi (Malaysia/Indonesia),
  Public Relations Review

DOMAIN VOCABULARY:
  framing, agenda-setting, uses and gratifications, gatekeeping, sentiment analysis,
  content analysis, inter-rater reliability, Cohen's κ, social network analysis,
  echo chamber, filter bubble, VADER, BERT, Gephi, episodic/thematic frame

METHODOLOGY KEYWORDS:
  systematic content analysis, framing analysis (Entman), inter-rater reliability (Cohen's κ),
  sentiment analysis (VADER/BERT), social network analysis (Gephi/NetworkX),
  survey questionnaire (Likert), thematic analysis, Twitter/Instagram API data collection
""",

"computer_networks": """================================================================================
TOPIC GUIDE — Computer Networks & Telecommunications
================================================================================
FIELD: Computer Science / Electrical Engineering
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Jaringan Komputer, TCP/IP, QoS, SDN, 5G, MPLS, Protokol Jaringan

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: network protocol/architecture or application studied,
  topology and scale, methodology (simulation NS-3/GNS3, testbed, analytical modeling),
  key metrics (throughput Mbps, latency ms, PDR %, jitter ms, packet loss %, energy efficiency),
  and comparison with existing protocol/configuration.

INTRODUCTION ELEMENTS:
  - Network evolution: from 1G to 5G/6G, SDN/NFV paradigm shift, IoT scale.
  - Problem: congestion, QoS for latency-sensitive traffic, security, energy efficiency.
  - Research gap: new routing algorithm, QoS mechanism, network slicing for specific use case.
  - Objectives: propose, implement, evaluate network protocol or architecture.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - Network protocols: TCP (congestion control: Cubic, BBR, QUIC), UDP, HTTP/2, HTTP/3.
  - QoS: DSCP (Differentiated Services), IntServ, traffic shaping, queuing (WFQ, FIFO, CBWFQ).
  - SDN/NFV: OpenFlow, OpenDaylight, ONOS, RYU controller; network virtualization.
  - Wireless: WiFi (802.11ax/be), LTE, 5G NR (NR-PDCP, NR-MAC); MIMO, beamforming, mmWave.
  - Named Data Networking (NDN): content-centric routing, in-network caching.
  - Network simulation: NS-3, GNS3, Mininet, OPNET; accuracy vs. real testbed.
  - Green networking: energy-proportional networking, sleep scheduling, ECT (Energy Efficient Ethernet).

METHODOLOGY:
  Common section name: "Simulation Setup" / "Experimental Setup"
  - Simulation: NS-3 or GNS3; topology (n nodes, n links, bandwidth, delay parameters).
  - Traffic generator: iperf3, t-rex, CBR/VBR UDP; application mix (video, VoIP, HTTP).
  - Protocol implementation: C++/Python NS-3 module; or SDN controller (Python/Java).
  - Metrics: throughput (Mbps), end-to-end latency (ms), PDR (%), jitter (ms), loss (%).
  - QoS classification: DSCP marking; priority queue evaluation.
  - Statistical: multiple runs (n≥30), mean ± SD; confidence interval 95%.
  - Real testbed (if applicable): Raspberry Pi cluster, Cisco routers, GNS3 live.

TYPICAL RESULTS & DISCUSSION:
  - TCP throughput (100Mbps link): Cubic 70–85 Mbps; BBR 85–95 Mbps; QUIC 80–90 Mbps.
  - Latency (LAN): <1 ms; WAN 50–150 ms; satellite 500–700 ms.
  - PDR: stable network >99%; congested 80–95%.
  - 5G latency target: eMBB <4ms, uRLLC <1ms (theoretical); real deployment 10–20ms.
  - SDN vs. traditional: flow setup time SDN 5–10ms overhead; amortized benefit for large-scale.
  Tables: performance comparison (protocols), QoS before/after, throughput vs. load.
  Figures: throughput/latency vs. time, CDF of latency, network topology diagram.

TYPICAL FIGURES:
  - Network topology diagram.
  - Throughput vs. time (comparison of protocols).
  - Latency CDF (cumulative distribution).
  - PDR vs. node density (wireless scenario).
  - Queue length vs. traffic load.

TYPICAL TABLES:
  - Protocol comparison: protocol | throughput | P95 latency | PDR | jitter | loss.
  - QoS results: traffic class | DSCP | allocated BW | actual throughput | delay.
  - Simulation parameters: parameter | value | range.

CONCLUSION CHARACTERISTICS:
  - Proposed protocol/mechanism outperforms baseline on target metrics.
  - QoS requirements for specific application met.
  - Trade-off between performance metrics discussed.
  - Limitations: simulation idealization, single topology, no real-world validation.
  - Future: real testbed deployment, machine learning for adaptive routing, 6G integration.

COMMON REFERENCE VENUES:
  IEEE Transactions on Communications, IEEE/ACM Transactions on Networking,
  Computer Networks (Elsevier), Computer Communications, Journal of Network and Computer Applications,
  IEEE Communications Letters, IEEE INFOCOM, IEEE GLOBECOM

DOMAIN VOCABULARY:
  TCP, UDP, QoS, DSCP, DSCP, SDN, OpenFlow, NFV, NS-3, Mininet, iperf3,
  throughput, latency, PDR, jitter, packet loss, 5G NR, LTE, MIMO, beamforming,
  QUIC, BBR, WFQ, CBWFQ, traffic shaping, CCN/NDN, energy-efficient Ethernet

METHODOLOGY KEYWORDS:
  NS-3 simulation (C++), GNS3 network emulation, iperf3 throughput measurement,
  Wireshark packet capture, QoS marking (DSCP), SDN controller (RYU/OpenDaylight),
  statistical analysis (multiple runs, 95% CI), PDR measurement
""",

"computer_vision": """================================================================================
TOPIC GUIDE — Computer Vision & Image Processing
================================================================================
FIELD: Computer Science / Artificial Intelligence
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Computer Vision, Deteksi Objek, Segmentasi, Pengenalan Wajah, Analisis Gambar Medis

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: visual task (detection, segmentation, recognition, reconstruction),
  dataset (name, size, classes), proposed method (architecture, module, training strategy),
  key metrics (mAP %, accuracy %, Dice score, PSNR dB, SSIM), baseline comparison, and application.

INTRODUCTION ELEMENTS:
  - Visual intelligence importance: autonomous driving, medical imaging, security, robotics.
  - Specific visual problem: occlusion in detection, class imbalance, small object, domain gap.
  - Limitations of current methods.
  - Proposed contribution: novel architecture, attention mechanism, data augmentation strategy.
  - Research scope and paper organization.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - Classic CV: HOG+SVM, SIFT/SURF feature extraction.
  - CNN backbones: VGG, ResNet (50/101/152), EfficientNet, MobileNet (v2/v3).
  - Object detection: YOLO (v5/v7/v8/v9/v10), SSD, Faster-RCNN, DETR, RT-DETR.
  - Segmentation: FCN, U-Net (medical), DeepLab v3+, SAM (Segment Anything Model).
  - Vision Transformers: ViT, DINO, Swin Transformer; self-supervised pretraining.
  - Image generation/restoration: GAN, Diffusion Models (DDPM), SRGAN, Real-ESRGAN.
  - Medical imaging: chest X-ray (CheXNet), pathology (whole slide image), skin lesion.

METHODOLOGY:
  Common section name: "Methodology" / "Proposed Method"
  - Dataset: source, size (n images, n classes), preprocessing (resize 416/640, normalize), augmentation.
  - Architecture: baseline + proposed modification; parameter count.
  - Training: GPU (V100/A100), batch size, optimizer (Adam/SGD), LR schedule (cosine decay), epochs.
  - Transfer learning: pretrained on ImageNet/COCO; fine-tuning.
  - Evaluation: mAP@0.5, mAP@0.5:0.95, precision, recall, F1 (detection); Dice/IoU (segmentation); PSNR/SSIM (restoration).
  - Ablation: module-by-module contribution.
  - Visualization: Grad-CAM for classification, prediction overlay for detection.

TYPICAL RESULTS & DISCUSSION:
  - Object detection mAP@0.5: YOLOv8 baseline 55–75% on COCO; custom dataset 70–95%.
  - Medical segmentation Dice: U-Net cardiac 85–95%; tumor 75–90%.
  - Face recognition accuracy: 98–99.8% on LFW; real-world 90–95%.
  - Image restoration PSNR: SR (×4): SRGAN ~28–30 dB; diffusion-based 30–32 dB.
  - Inference speed: YOLOv8n 80–100 FPS on T4 GPU; YOLOv8x 20–30 FPS.
  Tables: mAP per class, ablation study, comparison with SOTA.
  Figures: detection output samples, PR curve, mAP bar chart, Grad-CAM.

TYPICAL FIGURES:
  - Detection/segmentation output on sample images.
  - Precision-Recall curve (mAP area under curve).
  - Training/validation loss and mAP curve.
  - Confusion matrix.
  - Grad-CAM activation maps.

TYPICAL TABLES:
  - SOTA comparison: method | backbone | params(M) | FLOPs(G) | mAP@0.5 | mAP@0.5:0.95.
  - Ablation: component | mAP@0.5 | mAP@0.5:0.95 | Δ.
  - Per-class: class | AP | P | R.

CONCLUSION CHARACTERISTICS:
  - Proposed method achieves superior performance on key metrics.
  - Ablation confirms each component contribution.
  - Practical speed-accuracy trade-off discussed.
  - Limitations: domain specificity, computational cost, small dataset.
  - Future: edge deployment, real-time video, multi-task learning, foundation model fine-tuning.

COMMON REFERENCE VENUES:
  IEEE CVPR, ICCV, ECCV, IEEE Transactions on Image Processing,
  IEEE Transactions on Pattern Analysis and Machine Intelligence,
  Pattern Recognition, Image and Vision Computing, Expert Systems with Applications

DOMAIN VOCABULARY:
  CNN, ViT, YOLO, mAP, IoU, Dice, PSNR, SSIM, Grad-CAM, U-Net,
  ResNet, EfficientNet, SAM, DETR, GAN, Diffusion, FPN, NMS,
  bounding box, anchor, stride, backbone, neck, head, transfer learning

METHODOLOGY KEYWORDS:
  YOLOv8 training (Ultralytics), U-Net medical segmentation, mAP@0.5:0.95 evaluation,
  Grad-CAM visualization, data augmentation (albumentations), transfer learning (ImageNet/COCO pretrained),
  ablation study, COCO/VOC evaluation protocol, ONNX/TensorRT deployment
""",

"cybersecurity": """================================================================================
TOPIC GUIDE — Cybersecurity (Applied)
================================================================================
FIELD: Computer Science / Information Security
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Keamanan Siber Terapan, Penetration Testing, Keamanan Web, Keamanan Aplikasi Mobile

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: security assessment target (web app, mobile app, network, IoT device),
  vulnerability discovered, method (penetration testing, SAST/DAST, fuzzing, threat modeling),
  key findings (CVE severity, CVSS score, vulnerability count), remediation, and security improvement.

INTRODUCTION ELEMENTS:
  - Cyberthreat statistics: growing attack surface, data breach cost (IBM: average USD 4.45M in 2023).
  - Target system type and its criticality (healthcare, finance, government, industry).
  - Security challenge: unpatched vulnerabilities, weak authentication, insecure API.
  - Research gap: untested system, novel attack vector, specific environment.
  - Objectives: identify, exploit (with permission), remediate vulnerabilities.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - OWASP Top 10 (2021): Broken Access Control, Cryptographic Failures, Injection, Insecure Design, Security Misconfiguration, Vulnerable Components, Authentication Failures, SSRF, SSTI, Security Logging Failures.
  - Penetration testing methodology: PTES (Penetration Testing Execution Standard), OSSTMM, CEH methodology.
  - Web security: SQL injection, XSS (reflected/stored/DOM), CSRF, IDOR, XXE, path traversal.
  - Mobile security: OWASP Mobile Top 10; reverse engineering (APK decompile, Jadx, Frida).
  - SAST tools: SonarQube, Checkmarx, Bandit (Python); DAST: Burp Suite, ZAP, Nikto.
  - CVSS v3.1: Base score 0–10 (Critical: 9–10, High: 7–8.9, Medium: 4–6.9, Low: 0–3.9).

METHODOLOGY:
  Common section name: "Research Methodology" / "Testing Methodology"
  - Scope definition: authorized target, legal agreement (Rules of Engagement).
  - Reconnaissance: passive (OSINT: Shodan, Google Dork, Whois) + active (Nmap, Nessus scan).
  - Vulnerability scanning: Nessus, OpenVAS; authenticated scan.
  - Exploitation: Metasploit, manual exploitation; proof-of-concept (PoC) only, no damage.
  - Web testing: Burp Suite Pro; manual testing for OWASP Top 10.
  - Static analysis: SonarQube on source code; Semgrep rules.
  - Reporting: vulnerability description, CVSS score, PoC screenshot, remediation recommendation.

TYPICAL RESULTS & DISCUSSION:
  - Vulnerability count: critical 1–5, high 5–15, medium 10–30 (typical web app pentest).
  - CVSS scores: critical ≥9.0 (e.g., SQL injection = 9.8 network/critical/no priv).
  - SQL injection: test parameter, payload ('; OR 1=1 --), successful extraction confirmed.
  - XSS: reflected XSS found in n=X parameters; stored XSS in comment/profile field.
  - Before/after remediation: critical reduced from 5 to 0, high from 15 to 2.
  Tables: vulnerability register (ID | type | location | CVSS | severity | status).
  Figures: vulnerability distribution pie chart, attack tree diagram, remediation timeline.

TYPICAL FIGURES:
  - Vulnerability severity distribution (pie/bar chart).
  - Attack tree or kill chain diagram.
  - Screenshot: Burp Suite intercepted request with vulnerability evidence.
  - Before/after remediation comparison chart.
  - OWASP coverage heatmap.

TYPICAL TABLES:
  - Vulnerability register: ID | vulnerability | location | CVSS base | severity | recommendation.
  - OWASP mapping: OWASP category | found | total tested | coverage%.
  - Remediation tracking: vulnerability | priority | owner | status | completion date.

CONCLUSION CHARACTERISTICS:
  - Security posture of target assessed with quantified risk.
  - Critical and high-severity vulnerabilities require immediate remediation.
  - Security improvement roadmap recommended.
  - Limitations: authorized scope only, static point-in-time assessment, no DoS testing.
  - Future: continuous penetration testing (DevSecOps), red team exercise, bug bounty program.

COMMON REFERENCE VENUES:
  IEEE Symposium on Security and Privacy (S&P), ACM CCS, USENIX Security,
  Computers & Security, Journal of Information Security and Applications,
  IEEE Access, Digital Investigation, Security and Communication Networks

DOMAIN VOCABULARY:
  OWASP Top 10, SQL injection, XSS, CSRF, IDOR, CVSS, PTES, OSSTMM,
  Burp Suite, Metasploit, Nmap, Nessus, Shodan, SonarQube, SAST, DAST,
  CVE, penetration testing, PoC, Frida, APK decompile, JWT, SSRF

METHODOLOGY KEYWORDS:
  PTES penetration testing methodology, Nmap port scanning, Nessus vulnerability scan,
  Burp Suite web application testing, OWASP Top 10 manual testing,
  CVSS 3.1 scoring, SonarQube SAST, Metasploit exploitation (authorized), OSINT reconnaissance
""",

"data_science": """================================================================================
TOPIC GUIDE — Data Science & Analytics
================================================================================
FIELD: Computer Science / Statistics
DEFAULT CITATION STYLE: IEEE or APA
SUBDISCIPLINE: Ilmu Data, Analitik Data, Big Data, Data Mining, Visualisasi Data, Prediksi

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: data domain (healthcare, finance, transportation, social media),
  dataset size, data science methodology (EDA, feature engineering, ML modeling, time series),
  key results (accuracy %, RMSE, AUC, prediction horizon, insights discovered), and application value.

INTRODUCTION ELEMENTS:
  - Data explosion context: volume, velocity, variety (3Vs) of big data.
  - Business/scientific problem: prediction, anomaly detection, pattern discovery, recommendation.
  - Challenges: data quality, class imbalance, feature selection, interpretability.
  - Research gap: domain-specific dataset, novel pipeline, explainable AI integration.
  - Objectives: build predictive/descriptive model, extract insights from data.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - Data science process: CRISP-DM (6 phases), KDD process, OSEMN framework.
  - EDA: summary statistics, correlation matrix, distribution analysis, outlier detection (IQR, Z-score).
  - Feature engineering: normalization, encoding (label, one-hot, target), feature selection (RFECV, SHAP).
  - ML algorithms: Linear/Logistic Regression, Decision Tree, Random Forest, XGBoost/LightGBM, SVM, k-NN.
  - Time series: ARIMA, SARIMA, Prophet, LSTM, TCN; stationarity (ADF test), ACF/PACF.
  - Big data: Apache Spark, Hadoop; data lake, data warehouse (Snowflake, BigQuery).
  - Explainability: SHAP (SHapley Additive exPlanations), LIME, permutation importance.

METHODOLOGY:
  Common section name: "Methodology" / "Data Analysis Pipeline"
  - Data collection: API, web scraping (BeautifulSoup, Scrapy), SQL query, Kaggle dataset.
  - Preprocessing: missing value imputation (mean/median/KNN), outlier removal, feature scaling.
  - Exploratory: descriptive statistics, correlation heatmap, PCA (first 2 components).
  - Modeling: train/test split (80/20), cross-validation (k=5), hyperparameter tuning (GridSearchCV/Optuna).
  - Evaluation: classification (accuracy, F1, AUC-ROC, confusion matrix); regression (MAE, MSE, RMSE, MAPE, R²).
  - Tools: Python (Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn), Jupyter Notebook.

TYPICAL RESULTS & DISCUSSION:
  - Classification AUC: Random Forest 0.85–0.95; XGBoost 0.88–0.97.
  - Regression MAPE: good prediction <10%; acceptable <20%.
  - Feature importance: top 5 features explain 60–80% of model variance (SHAP).
  - Time series RMSE: LSTM outperforms ARIMA by 15–30% for nonlinear patterns.
  - Dataset size: typically 1,000–100,000 rows; results vary significantly with size.
  Tables: model comparison, feature importance, hyperparameter settings.
  Figures: SHAP beeswarm/waterfall, confusion matrix, ROC curve, actual vs. predicted.

TYPICAL FIGURES:
  - ROC curve (AUC for multiple models).
  - Confusion matrix (heatmap).
  - SHAP feature importance (beeswarm plot).
  - Actual vs. predicted plot (regression).
  - Correlation heatmap (EDA).

TYPICAL TABLES:
  - Model comparison: model | accuracy | F1 | AUC | training time.
  - Hyperparameters: model | param | range | optimal.
  - Evaluation metrics: model | MAE | RMSE | MAPE | R².

CONCLUSION CHARACTERISTICS:
  - Best-performing model identified with justification.
  - Key features driving predictions explained (SHAP).
  - Actionable insights for domain stakeholders.
  - Limitations: dataset recency, class imbalance, single domain.
  - Future: production deployment (MLflow, FastAPI), real-time data pipeline, model monitoring.

COMMON REFERENCE VENUES:
  Journal of Big Data, Data Mining and Knowledge Discovery, Expert Systems with Applications,
  Knowledge-Based Systems, IEEE Transactions on Knowledge and Data Engineering,
  Applied Sciences (MDPI), Information Sciences, PLoS ONE (data science papers)

DOMAIN VOCABULARY:
  CRISP-DM, EDA, feature engineering, SHAP, LIME, XGBoost, LightGBM, ARIMA,
  LSTM, AUC-ROC, RMSE, MAPE, cross-validation, GridSearchCV, Optuna,
  Scikit-learn, Pandas, Jupyter, data lake, BigQuery, Apache Spark, RFECV

METHODOLOGY KEYWORDS:
  EDA (correlation heatmap, outlier analysis), feature selection (SHAP/RFECV),
  XGBoost/LightGBM modeling, k-fold cross-validation, GridSearchCV tuning,
  SHAP explainability analysis, confusion matrix, ROC-AUC evaluation
""",

"deep_learning": """================================================================================
TOPIC GUIDE — Deep Learning
================================================================================
FIELD: Computer Science / Artificial Intelligence
DEFAULT CITATION STYLE: IEEE
SUBDISCIPLINE: Deep Learning, Neural Network, CNN, RNN, Transformer, Generative Models

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: deep learning task, dataset, proposed architecture
  (novel module, loss function, training strategy), metrics (accuracy %, F1, mAP, BLEU,
  PSNR), comparison with SOTA baselines, computational cost (parameters M, FLOPs G), and application.

INTRODUCTION ELEMENTS:
  - DL revolution since AlexNet (2012) and Transformer (Attention is All You Need, 2017).
  - Task-specific problem: overfitting on small data, class imbalance, slow convergence, domain shift.
  - Limitations of existing architectures.
  - Proposed innovation: new block, attention mechanism, training trick, loss function.
  - Research hypotheses and contribution claims.

LITERATURE REVIEW:
  Common section name: "Related Work" / "Background"
  - Foundational: LeNet (1998), AlexNet (2012), VGG (2014), ResNet (2015), DenseNet.
  - Modern architectures: EfficientNet, RegNet, ConvNeXt, Vision Transformer (ViT, DeiT, Swin).
  - Sequence models: LSTM, GRU, Bidirectional; Transformer encoder (BERT), decoder (GPT), encoder-decoder (T5).
  - Generative: VAE, GAN (DCGAN, StyleGAN, BigGAN), Diffusion models (DDPM, DDIM, Stable Diffusion).
  - Training techniques: learning rate warmup, cosine annealing, mixed precision (AMP), gradient clipping.
  - Regularization: dropout (Srivastava 2014), weight decay, label smoothing, mixup, CutMix.
  - Self-supervised/pre-training: BERT masked LM, DINO, MAE (masked autoencoder), CLIP.

METHODOLOGY:
  Common section name: "Proposed Method" / "Methodology"
  - Architecture design: module-level description, layer dimensions, activation functions.
  - Implementation: PyTorch/TensorFlow; training details (GPU, batch, epochs, optimizer).
  - Dataset: split strategy; augmentation pipeline (albumentations/torchvision transforms).
  - Training: loss function (cross-entropy, focal, BCE+Dice, contrastive); LR schedule.
  - Evaluation: standard benchmark protocol; held-out test set; n-fold CV.
  - Ablation study: add/remove each proposed module.
  - Computational cost: parameter count (M), FLOPs (G), inference time (ms), GPU memory (GB).

TYPICAL RESULTS & DISCUSSION:
  - Image classification (ImageNet): ResNet-50 baseline 76%; EfficientNetB7 84%; ViT-L 85%.
  - NLP (GLUE benchmark): BERT-base 78.3; RoBERTa-large 88.9 (average).
  - Object detection mAP (COCO): ResNet-50 Faster RCNN 37%; Swin-T DINO 54%.
  - Ablation: each proposed component contributes +0.5–3% to main metric.
  - Computational: efficiency-accuracy trade-off (FLOPs vs. accuracy scatter plot).
  Tables: architecture ablation, SOTA comparison, training hyperparameters.
  Figures: architecture diagram, training curves, attention visualization, output samples.

TYPICAL FIGURES:
  - Proposed architecture block diagram.
  - Training/validation loss and accuracy curves.
  - Attention map visualization (ViT/Transformer).
  - Accuracy vs. FLOPs scatter (efficiency comparison).
  - Generated sample images (generative models).

TYPICAL TABLES:
  - SOTA comparison: method | year | params(M) | FLOPs(G) | accuracy/mAP.
  - Ablation: configuration | accuracy | F1 | improvement.
  - Training details: LR | batch | optimizer | epochs | scheduler.

CONCLUSION CHARACTERISTICS:
  - Proposed method achieves new SOTA on target benchmark with fewer parameters.
  - Ablation confirms each contribution.
  - Practical utility demonstrated (speed/accuracy balance).
  - Limitations: single modality, single task, GPU-intensive training.
  - Future: multi-modal learning, parameter-efficient fine-tuning (LoRA, adapters), edge deployment.

COMMON REFERENCE VENUES:
  NeurIPS, ICML, ICLR, CVPR, ICCV, ACL, EMNLP,
  IEEE Transactions on Neural Networks and Learning Systems,
  Pattern Recognition, Neural Networks, Knowledge-Based Systems

DOMAIN VOCABULARY:
  CNN, RNN, LSTM, Transformer, ViT, BERT, GPT, ResNet, attention, self-attention,
  loss function, Adam optimizer, cosine LR, AMP (mixed precision), dropout,
  data augmentation, ablation, FLOPs, parameters, SOTA, backpropagation, gradient

METHODOLOGY KEYWORDS:
  PyTorch/TensorFlow training, cosine LR schedule, focal loss, mixup/CutMix augmentation,
  ablation study, FLOPs/parameter count, ONNX export, TensorRT optimization,
  k-fold cross-validation, confusion matrix, attention visualization
""",

"dentistry": """================================================================================
TOPIC GUIDE — Dentistry & Oral Health
================================================================================
FIELD: Medicine / Dentistry
DEFAULT CITATION STYLE: Vancouver or APA
SUBDISCIPLINE: Kedokteran Gigi, Konservasi Gigi, Orthodonti, Periodontologi, Bedah Mulut, Kedokteran Gigi Komunitas

ABSTRACT CHARACTERISTICS:
  150–250 words (structured for clinical studies). Reports: patient population (n, age, sex,
  diagnosis), dental procedure or material studied, study design (RCT, in vitro, cohort),
  outcome measures (bond strength MPa, marginal seal, pocket depth mm, plaque index,
  patient satisfaction VAS), statistical results.

INTRODUCTION ELEMENTS:
  - Prevalence of oral disease (caries, periodontitis, malocclusion) in target population.
  - Clinical challenge: treatment failure, material limitation, patient compliance.
  - Research gap: new material/technique not evaluated in local population, comparison study.
  - Objectives: evaluate efficacy of dental treatment, material, or intervention.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Background"
  - Dental caries: Keyes' four factors (tooth, bacteria, substrate, time); DMFT/DMFS indices.
  - Restorative materials: composite resin, glass ionomer cement (GIC), amalgam; bond strength evaluation (ISO 6872, ISO 4049).
  - Periodontitis: Armitage classification (2017); pocket depth (PD), clinical attachment level (CAL), bleeding on probing (BOP).
  - Orthodontics: Angle classification (I/II/III); PAR index; bracket bonding, bracket failure rate.
  - Oral surgery: extraction difficulty (Pederson scale), healing assessment, dry socket incidence.
  - Dental materials: flexural strength (ISO 6872), compressive strength, Vickers hardness (HV), roughness (Ra µm).
  - Community dentistry: DMFT index WHO standards; oral health-related quality of life (OHRQoL, OHIP-14).

METHODOLOGY:
  Common section name: "Materials and Methods" / "Research Method"
  - Study design: RCT, quasi-experimental, cross-sectional, in vitro, systematic review.
  - Sample: patients (n=30–100); inclusion/exclusion criteria; power analysis.
  - Clinical measurements: PD, CAL (Florida probe), DMFT, plaque index (O'Leary), gingival index (Löe & Silness).
  - In vitro (material testing): specimen preparation (n=10–20 per group), ISO standards; universal testing machine (UTM), SEM, FTIR.
  - Bond strength: shear bond strength (SBS), microtensile bond strength (µTBS); specimens prepared per ISO 11405.
  - Statistical: ANOVA, Kruskal-Wallis (non-parametric), Mann-Whitney, Fisher's exact; Bonferroni post-hoc; α=0.05.

TYPICAL RESULTS & DISCUSSION:
  - DMFT: WHO 2018 Indonesia national average 7.0 (adults); acceptable goal <3 for 12-year-olds.
  - Shear bond strength: composite resin to enamel 20–35 MPa; dentine 15–25 MPa.
  - Flexural strength (zirconia): 900–1200 MPa; lithium disilicate 400–500 MPa.
  - Pocket depth: healthy <3mm; moderate periodontitis 4–6mm; severe >6mm.
  - Reduction in BOP after scaling/root planing: 60–80% reduction at 6 weeks.
  Tables: material properties comparison, clinical measurement comparison, DMFT data.
  Figures: SEM micrograph of fracture surface, clinical pre/post photo, box plot PD.

TYPICAL FIGURES:
  - SEM micrograph (material fracture surface or adhesive interface).
  - Box plot: pocket depth before and after treatment.
  - Bar chart: DMFT by age group.
  - Clinical photographs: pre/post treatment.
  - Survival curve (Kaplan-Meier for prosthetic survival).

TYPICAL TABLES:
  - Material properties: material | flexural strength (MPa) | hardness (HV) | Ra (µm).
  - Clinical outcome: group | PD (mm) | CAL (mm) | BOP (%) | plaque index.
  - DMFT: group | age | n | D | M | F | DMFT | SD.

CONCLUSION CHARACTERISTICS:
  - Dental material/procedure meets clinical performance criteria.
  - Treatment protocol effectively reduces disease parameters.
  - Community oral health recommendations.
  - Limitations: single-center, short follow-up, specific patient population.
  - Future: multicenter RCT, long-term follow-up (2–5 years), cost-effectiveness analysis.

COMMON REFERENCE VENUES:
  Journal of Dentistry, Clinical Oral Investigations, Dental Materials,
  Journal of Dental Research, International Journal of Oral and Maxillofacial Surgery,
  Community Dentistry and Oral Epidemiology, Journal of Periodontology,
  Jurnal Kedokteran Gigi Universitas Indonesia (JKGUI)

DOMAIN VOCABULARY:
  DMFT, DMFS, caries, periodontitis, PD, CAL, BOP, plaque index, SBS, µTBS,
  composite resin, GIC, zirconia, lithium disilicate, ISO 6872, flexural strength,
  Vickers hardness, OHIP-14, PAR index, Angle classification, dry socket

METHODOLOGY KEYWORDS:
  DMFT examination (WHO criteria), pocket depth/CAL measurement (Florida probe),
  shear bond strength testing (ISO 11405), universal testing machine, SEM analysis,
  RCT design, Kruskal-Wallis, Mann-Whitney, Bonferroni correction, OHRQoL (OHIP-14)
""",

"digital_transformation": """================================================================================
TOPIC GUIDE — Digital Transformation
================================================================================
FIELD: Business / Information Systems
DEFAULT CITATION STYLE: APA or IEEE
SUBDISCIPLINE: Transformasi Digital, Industri 4.0, Digitalisasi, UMKM Digital, e-Government, Strategi Digital

ABSTRACT CHARACTERISTICS:
  150–250 words. Reports: organization type (SMEs, government, healthcare, manufacturing),
  digital transformation stage or initiative studied, methodology (case study, survey, TAM/UTAUT,
  mixed methods), key results (technology adoption rate %, performance improvement %, barrier factors,
  digital maturity score), and strategic implications.

INTRODUCTION ELEMENTS:
  - Industry 4.0 and digital economy context: GDP contribution, SME competitiveness.
  - Specific DX challenge: resistance to change, IT infrastructure gap, digital skills gap, investment cost.
  - Theoretical framing: TAM (Davis 1989), UTAUT (Venkatesh 2003), dynamic capabilities (Teece).
  - Research gap: specific sector/country, maturity assessment framework, barrier analysis.
  - Objectives: assess adoption, identify barriers, measure impact of digital transformation.

LITERATURE REVIEW:
  Common section name: "Literature Review" / "Theoretical Framework"
  - DX definition: Vial (2019) — technology-enabled change in business model, process, people, culture.
  - Industry 4.0 technologies: IoT, cloud computing, big data analytics, AI/ML, robotics, blockchain, additive manufacturing.
  - Technology acceptance: TAM (perceived usefulness, ease of use); UTAUT (performance expectancy, effort expectancy, social influence, facilitating conditions).
  - Digital maturity models: CMMI, Gartner Digital Maturity, Forrester DX model (5 stages).
  - Change management: Lewin's model, Kotter's 8-step, ADKAR.
  - e-Government: e-services adoption, GovTech, OpenGov data, digital public services.
  - SME digital transformation: resource constraints, digital readiness, ecosystem support.

METHODOLOGY:
  Common section name: "Research Methodology" / "Methods"
  - Quantitative: survey (n=50–500 employees/managers); Likert scale; TAM/UTAUT questionnaire; SEM-PLS (SmartPLS) or AMOS.
  - Qualitative: case study (Yin 2003); semi-structured interview (n=10–20); thematic analysis.
  - Mixed methods: survey + interview; sequential explanatory.
  - Digital maturity assessment: framework-based scoring (0–5 scale per dimension).
  - Performance metrics: operational efficiency (cost/time reduction %), digital revenue %, customer satisfaction.
  - Statistical (quantitative): SEM (path coefficient, R², AVE, CR); PLS bootstrapping (n=5000); HTMT for discriminant validity.

TYPICAL RESULTS & DISCUSSION:
  - TAM/UTAUT path coefficients: perceived usefulness → intention: β 0.4–0.6 (p<0.001).
  - Technology adoption rate: SMEs Indonesia 30–60% using digital tools (UMKM survey).
  - Digital maturity score: 2.1–3.5/5.0 (developing stage for most SMEs/government agencies).
  - Barrier factors: IT cost (60–75%), lack of skills (55–70%), lack of leadership support (40–60%).
  - Performance: DX implementation → 20–35% cost reduction, 25–40% operational efficiency gain.
  Tables: SEM path results, digital maturity matrix, barrier frequency table.
  Figures: SEM diagram, digital maturity radar chart, adoption rate bar chart.

TYPICAL FIGURES:
  - SEM structural model diagram (with path coefficients).
  - Digital maturity radar chart (per dimension).
  - Bar chart: barrier frequency ranking.
  - Technology adoption progression timeline.

TYPICAL TABLES:
  - SEM results: path | coefficient | t-stat | p | R² | conclusion.
  - Reliability/validity: construct | CR | AVE | Cronbach's α | HTMT.
  - Maturity assessment: dimension | score | gap | priority.

CONCLUSION CHARACTERISTICS:
  - Key drivers and barriers of digital transformation identified.
  - Digital maturity assessment provides actionable roadmap.
  - Policy/management implications.
  - Limitations: self-report bias, cross-sectional, single sector/country.
  - Future: longitudinal, objective KPI measurement, cross-sector comparison.

COMMON REFERENCE VENUES:
  Journal of Business Research, International Journal of Information Management,
  Computers in Human Behavior, Business Process Management Journal,
  Technological Forecasting and Social Change, Industrial Management & Data Systems,
  Government Information Quarterly, Journal of Information Technology

DOMAIN VOCABULARY:
  TAM, UTAUT, SEM-PLS, SmartPLS, AMOS, digital maturity, Industry 4.0,
  digital transformation, AVE, CR, HTMT, path coefficient, dynamic capabilities,
  Kotter, ADKAR, e-government, GovTech, IoT, cloud, AI, SME digital

METHODOLOGY KEYWORDS:
  TAM/UTAUT survey design, SEM-PLS (SmartPLS 4), PLS bootstrapping (n=5000),
  Cronbach's alpha, AVE/CR validity, HTMT discriminant validity,
  digital maturity framework scoring, case study (Yin), thematic analysis
""",

}

def write_topic(name, content):
    path = os.path.join(D, f"{name}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.lstrip())
    print(f"  wrote {name}.txt")

for name, content in TOPICS.items():
    write_topic(name, content)
print(f"gen_09: {len(TOPICS)} topics written.")

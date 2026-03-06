"""
IEEE Paper Generator
- System prompt & user template di-embed langsung dalam kode
- .env               → OPENAI_API_KEY, OPENAI_MODEL
- Input: JUDUL dan CUSTOM PROMPT dari user
- Record waktu + token
- Simpan hasil JSON ke output/
"""

import os
import re
import sys
import json
import time
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from json_repair import repair_json

# ── Config ────────────────────────────────────────────────────────────────────
BASE_DIR   = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

load_dotenv(BASE_DIR / ".env")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# ── Embedded Prompts ──────────────────────────────────────────────────────────
SYSTEM_PROMPT = """\
You are a senior IEEE conference paper author with 15+ years of publication experience.
Your task is to generate a COMPLETE, PUBLICATION-READY IEEE conference paper in strict JSON format.

═══════════════════════════════════════════════════════════════
SECTION I: LANGUAGE & WRITING STYLE (match authentic IEEE papers)
═══════════════════════════════════════════════════════════════
Write in formal, academic English consistent with top IEEE venues (CVPR, ICRA, ICCV, IROS, T-ITS, TPAMI).

Mandatory academic phrases:
- "We propose [X], a novel approach to..."
- "The proposed [module/method] is designed to..."
- "Extensive experiments on [Dataset] demonstrate that..."
- "Our method achieves [X]% [metric] on [benchmark], outperforming..."
- "The main contributions of this work can be summarized as follows:"
- "Despite achieving [X], [prior work] suffers from [limitation]..."
- "To address this challenge, we introduce..."
- "As shown in Fig. [N], the overall architecture consists of..."
- "As presented in Table [Roman], the proposed method surpasses..."
- "Specifically, [module A] reduces [metric] by [X]% while..."

Word count targets:
- Abstract: 150–200 words (problem, method, key quantitative results)
- Introduction: 450–550 words (background, problem, gap, contributions list, paper organization)
- Related Work: 350–450 words per subsection
- Methodology: 300–450 words per subsection (must include math formulas)
- Experiments: 250–400 words per subsection (must reference tables and figures)
- Conclusion: 150–250 words (summary, key metrics, limitations, future work)
TOTAL body text: MINIMUM 3500 words across all sections.

In-text citations: always use [1], [2], [3]–[6], [7][8] format matching the "references" array.
Figure references: always "Fig. 1", "Fig. 2" (never "Figure 1" or "figure 1")
Table references: always "Table I", "Table II", "Table III" (Roman numerals)
Equation references: always "(1)", "(2)", "(3)"

═══════════════════════════════════════════════════════════════
SECTION II: MATHEMATICAL FORMULA RULES (CRITICAL — NO ERRORS)
═══════════════════════════════════════════════════════════════
All formulas inside JSON string values use LaTeX delimiters:
  • $...$ for inline math  (e.g., inside a sentence)
  • $$...$$ for display/block math (standalone equation on its own line)
The "equations" array uses RAW LaTeX only (NO $ delimiters).

CORRECT LaTeX syntax examples (use these exact patterns):

Greek letters:       $\\alpha$, $\\beta$, $\\gamma$, $\\lambda$, $\\sigma$, $\\theta$, $\\omega$
Vectors/matrices:    $\\mathbf{x}$, $\\mathbf{W}$, $\\mathbf{F}$, $\\mathbf{K}$
Calligraphic:        $\\mathcal{L}$, $\\mathcal{F}$, $\\mathcal{A}$
Sets/spaces:         $x \\in \\mathbb{R}^{N \\times C}$, $\\mathbb{R}^{H \\times W \\times C}$
Fractions:           $\\frac{a}{b}$  (NOT a/b inside math)
Subscripts:          $f_{\\text{fused}}$, $\\mathcal{L}_{\\text{cls}}$, $TP_c$
Superscripts:        $x^{(t)}$, $\\mathbf{W}^T$, $e^{-x}$
Summation:           $\\sum_{c=1}^{C} \\frac{TP_c}{TP_c + FP_c + FN_c}$
Product:             $\\prod_{i=1}^{N}$
Square root:         $\\sqrt{d_k}$
Text in math mode:   $\\text{mIoU}$, $\\text{FPS}$, $\\text{Softmax}$
Operators:           $\\operatorname{softmax}(\\cdot)$, $\\operatorname{ReLU}(\\cdot)$
Norms:               $\\|\\mathbf{x}\\|_2$, $\\|\\mathbf{F} - \\hat{\\mathbf{F}}\\|_F$
Conditional:         $P(y \\mid x)$
Argmax:              $\\arg\\max_{\\theta}$
Absolute value:      $|x|$, $\\lvert x \\rvert$

REAL formula examples from published IEEE papers:

Poly learning rate schedule (HANDNet, INDICON 2024):
$$lr = lr_{\\text{init}} \\times \\left(1 - \\frac{\\text{iter}}{\\text{max\\_iter}}\\right)^{\\text{power}}$$

Class weighting (HANDNet, INDICON 2024):
$$w_{\\text{class}} = \\frac{1}{\\ln\\left(c + p_{\\text{class}}\\right)}$$

mIoU metric (standard IEEE definition):
$$\\text{mIoU} = \\frac{1}{C} \\sum_{c=1}^{C} \\frac{TP_c}{TP_c + FP_c + FN_c}$$

Scaled dot-product attention (Transformer):
$$\\text{Attention}(\\mathbf{Q}, \\mathbf{K}, \\mathbf{V}) = \\operatorname{softmax}\\!\\left(\\frac{\\mathbf{Q}\\mathbf{K}^{T}}{\\sqrt{d_k}}\\right)\\mathbf{V}$$

Feature fusion with multi-head self-attention (FusionNet, CVCI 2025):
$$\\mathbf{E}_{\\text{mhsa}} = \\text{LayerNorm}\\left(\\mathbf{E} + \\text{MHSE}(\\mathbf{E})\\right)$$

Multi-modal feature aggregation:
$$\\mathbf{f}_{\\text{fused},i} = \\text{MLP}\\left(\\mathbf{F}_{\\text{lidar}}(\\mathbf{f}_{\\text{lidar},i}) \\oplus \\mathbf{F}_{\\text{cam}}(\\mathbf{f}_{\\text{cam},i})\\right)$$

Cross-modal softmax normalization:
$$\\mathbf{D}^{T}_{\\text{lidar}} = \\left[\\operatorname{softmax}\\left(\\mathbf{D}'_{\\text{lidar}}[:,j]\\right)\\right]_{j=1}^{N_{\\text{cls}}}$$

Total loss function:
$$\\mathcal{L}_{\\text{total}} = \\mathcal{L}_{\\text{cls}} + \\lambda_1 \\mathcal{L}_{\\text{reg}} + \\lambda_2 \\mathcal{L}_{\\text{aux}}$$

Tensor dimensions notation: use $\\mathbf{X} \\in \\mathbb{R}^{N \\times C \\times H \\times W}$

FORBIDDEN (will cause rendering errors):
  ✗ DO NOT use plain text fractions: a/b inside $$
  ✗ DO NOT use × symbol inside $ (use \\times)
  ✗ DO NOT use unescaped backslashes in JSON strings (always double: \\\\alpha for \\alpha)
  ✗ DO NOT put display equations on same line as surrounding text without \\n separation
  ✗ DO NOT write $L_{total}$ (should be $\\mathcal{L}_{\\text{total}}$)
  ✗ DO NOT write $sigma$ (should be $\\sigma$)
  ✗ DO NOT write $sum_{...}$ (should be $\\sum_{...}$)
  ✗ DO NOT use word "equation" inline — use "(1)", "(2)" only

REQUIRED: Include at LEAST 6 formulas inline ($...$) AND 4 display equations ($$...$$) distributed across subsections III and IV.

═══════════════════════════════════════════════════════════════
SECTION III: EXACT JSON SCHEMA — RETURN ONLY THIS JSON
═══════════════════════════════════════════════════════════════
{
  "title": "Specific technical title, max 15 words, includes method name and task",
  "authors": [
    {
      "name": "Firstname Lastname",
      "affiliation": "Department of Computer Science, University Name",
      "location": "City, Country",
      "email": "author@university.edu"
    },
    {
      "name": "Second Author",
      "affiliation": "School of Engineering, Institute Name",
      "location": "City, Country",
      "email": "author2@institute.edu"
    }
  ],
  "abstract": "WRITE 150-200 WORDS HERE. Start with the problem context. State key limitations of prior work. Describe the proposed method and its key innovations (2-3 sentences). Give specific quantitative results: '[method] achieves [X]% [metric] on [dataset], outperforming [baseline] by [Y]%'. End with the broader impact.",
  "keywords": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5", "keyword6"],
  "sections": [
    {
      "id": "id-sec1",
      "number": "I",
      "title": "INTRODUCTION",
      "content": "WRITE 450-550 WORDS HERE. Structure: (1) Broad context and motivation (1-2 paragraphs). (2) Review of prior work limitations [1][2][3]. (3) Statement of the problem gap. (4) 'The main contributions of this work can be summarized as follows:' — then list 3-4 bullet contributions inline using \\n• syntax. (5) Paper organization: 'The remainder of this paper is organized as follows. Section II reviews... Section III presents... Section IV describes... Section V concludes...' Include inline math where natural: e.g., $\\text{mIoU}$, $\\mathbf{F} \\in \\mathbb{R}^{N \\times C}$.",
      "subsections": []
    },
    {
      "id": "id-sec2",
      "number": "II",
      "title": "RELATED WORK",
      "content": "WRITE 150-200 WORD OVERVIEW HERE. Introduce the three main research threads covered in subsections.",
      "subsections": [
        {
          "id": "id-sub2a",
          "letter": "A",
          "title": "Related Category A (e.g., CNN-based Semantic Segmentation)",
          "content": "WRITE 300-400 WORDS. Review 5-7 seminal works chronologically: FCN [1], SegNet [2], DeepLab [3], PSPNet [4], etc. Discuss limitations that motivate your approach. Use pattern: 'Although [method] achieves [metric], it suffers from [limitation] due to [reason].'",
          "numberedItems": []
        },
        {
          "id": "id-sub2b",
          "letter": "B",
          "title": "Related Category B (e.g., Attention Mechanisms / Transformers)",
          "content": "WRITE 300-400 WORDS. Review attention-based methods [5][6][7]. Compare channel attention [8], spatial attention [9], self-attention [10]. Note accuracy-efficiency tradeoffs. Include: $d_{\\text{model}}$ dimension, $h$ attention heads.",
          "numberedItems": []
        },
        {
          "id": "id-sub2c",
          "letter": "C",
          "title": "Related Category C (e.g., Real-Time Efficiency Techniques)",
          "content": "WRITE 250-350 WORDS. Depth-wise separable conv [11], dilated convolutions, knowledge distillation. 'While [method] runs at [X] FPS, its [Y]% mIoU falls short of real-world requirement.'",
          "numberedItems": []
        }
      ]
    },
    {
      "id": "id-sec3",
      "number": "III",
      "title": "PROPOSED METHOD",
      "content": "WRITE 100-150 WORDS. Overview of the proposed framework: 'In this section, we present the proposed [method name]. As illustrated in Fig. 1, the overall architecture consists of [encoder / feature extractor / fusion module / decoder]. We first define the problem formulation in Section III-A, then describe the network architecture in Section III-B and III-C, and detail the training objective in Section III-D.'",
      "subsections": [
        {
          "id": "id-sub3a",
          "letter": "A",
          "title": "Problem Formulation",
          "content": "WRITE 250-350 WORDS with MANDATORY DISPLAY FORMULAS. Define the task formally. Example format: 'Given an input image $\\mathbf{X} \\in \\mathbb{R}^{3 \\times H \\times W}$, the goal is to predict a dense semantic label map $\\mathbf{Y} \\in \\{1, \\ldots, C\\}^{H \\times W}$, where $C$ denotes the number of semantic categories. Formally, we seek a mapping function $f_{\\theta}: \\mathbb{R}^{3 \\times H \\times W} \\rightarrow \\{1,\\ldots,C\\}^{H \\times W}$ parameterized by $\\theta$.' Include at least 2 display formulas ($$...$$) defining key variables and transformations, each followed by explanation of terms.",
          "numberedItems": []
        },
        {
          "id": "id-sub3b",
          "letter": "B",
          "title": "Network Architecture",
          "content": "WRITE 350-450 WORDS with MULTIPLE INLINE formulas. Describe the encoder, feature extraction module, and decoder. Reference Fig. 1 and Fig. 2. Example: 'The encoder $\\mathcal{E}$ processes the input through three stages. At stage $s$, the feature map $\\mathbf{F}^{(s)} \\in \\mathbb{R}^{C_s \\times H_s \\times W_s}$ is downsampled by a factor of $2^s$. The depthwise separable convolution at each stage requires only $1/N$ parameters compared to standard convolution, where $N$ is the filter size.' Add display formula for key feature transformation: $$\\mathbf{F}^{(s+1)} = \\mathcal{D}\\!\\left(\\text{BN}\\left(\\text{DWConv}\\left(\\mathbf{F}^{(s)}\\right)\\right)\\right)$$ where DWConv denotes depthwise convolution, BN is batch normalization, and $\\mathcal{D}$ is the downsampling operation.",
          "numberedItems": []
        },
        {
          "id": "id-sub3c",
          "letter": "C",
          "title": "Feature Enhancement Module",
          "content": "WRITE 350-450 WORDS with DISPLAY FORMULAS. Describe the key proposed module. Include transformer/attention equations or multi-scale feature aggregation. Example attention formula: $$\\text{Attn}(\\mathbf{Q},\\mathbf{K},\\mathbf{V}) = \\operatorname{softmax}\\!\\left(\\frac{\\mathbf{Q}\\mathbf{K}^T}{\\sqrt{d_k}}\\right)\\mathbf{V}$$ followed by explanation: 'where $\\mathbf{Q} \\in \\mathbb{R}^{N \\times d_k}$, $\\mathbf{K} \\in \\mathbb{R}^{M \\times d_k}$, and $\\mathbf{V} \\in \\mathbb{R}^{M \\times d_v}$ are the query, key, and value matrices, respectively.' Reference Fig. 2 for module diagram. Discuss multi-scale dilation rates: $r \\in \\{1, 2, 4, 8\\}$.",
          "numberedItems": []
        },
        {
          "id": "id-sub3d",
          "letter": "D",
          "title": "Loss Function",
          "content": "WRITE 250-350 WORDS with DISPLAY FORMULA. Define the total training objective: $$\\mathcal{L}_{\\text{total}} = \\mathcal{L}_{\\text{cls}} + \\lambda_1 \\mathcal{L}_{\\text{aux}} + \\lambda_2 \\mathcal{L}_{\\text{reg}}$$ where $\\mathcal{L}_{\\text{cls}}$ is the cross-entropy classification loss, $\\mathcal{L}_{\\text{aux}}$ is an auxiliary segmentation loss at an intermediate feature level, and $\\mathcal{L}_{\\text{reg}}$ is a regularization term. Set $\\lambda_1 = 0.4$ and $\\lambda_2 = 1 \\times 10^{-4}$ experimentally. Also define the class-weighted loss: $$w_{\\text{class}} = \\frac{1}{\\ln\\left(c + p_{\\text{class}}\\right)}$$ where $c = 1.02$ is a smoothing constant and $p_{\\text{class}}$ is the normalized class frequency. Explain the Online Hard Example Mining (OHEM) strategy and why it addresses class imbalance.",
          "numberedItems": []
        }
      ]
    },
    {
      "id": "id-sec4",
      "number": "IV",
      "title": "EXPERIMENTAL RESULTS",
      "content": "WRITE 80-120 WORDS. 'In this section, we evaluate the proposed method through comprehensive experiments. We first describe the datasets and evaluation metrics in Section IV-A and IV-B. Implementation details are provided in Section IV-C. Section IV-D presents ablation studies validating each component. Finally, we compare against state-of-the-art methods in Section IV-E.'",
      "subsections": [
        {
          "id": "id-sub4a",
          "letter": "A",
          "title": "Datasets",
          "content": "WRITE 250-350 WORDS. Describe the benchmark dataset(s) used. Include: name, total images, training/validation/test split, number of classes, image resolution, annotation type. Example: 'We evaluate on the Cityscapes dataset [X], which contains 5,000 finely annotated driving images ($1024 \\times 2048$ pixels) with 19 semantic categories. The dataset is split into 2,975 training, 500 validation, and 1,525 test images. Following the standard protocol [Y], models are trained on the training set and evaluated on the validation set. To report test-set performance, predictions are submitted to the official evaluation server.' Also mention any data augmentation: random horizontal flipping, Gaussian noise, random scaling in $[0.5, 2.0]$.",
          "numberedItems": []
        },
        {
          "id": "id-sub4b",
          "letter": "B",
          "title": "Evaluation Metrics",
          "content": "WRITE 150-250 WORDS. Define all metrics used: $$\\text{mIoU} = \\frac{1}{C} \\sum_{c=1}^{C} \\frac{TP_c}{TP_c + FP_c + FN_c}$$ where $TP_c$, $FP_c$, $FN_c$ are true positives, false positives, and false negatives for class $c$, respectively. Also define parameters (M) for model size, FLOPs (G) for computational complexity, and frames per second (FPS) for inference speed. FPS is measured on [specific GPU model] with input size $[WxH]$.",
          "numberedItems": []
        },
        {
          "id": "id-sub4c",
          "letter": "C",
          "title": "Implementation Details",
          "content": "WRITE 250-350 WORDS. Include exact hyperparameters referencing Table I: optimizer (SGD with momentum $\\mu = 0.9$, weight decay $\\gamma = 1 \\times 10^{-4}$), 'poly' learning rate schedule: $$lr = lr_{\\text{init}} \\times \\left(1 - \\frac{\\text{iter}}{\\text{max\\_iter}}\\right)^{\\text{power}}$$ where $lr_{\\text{init}} = 4.5 \\times 10^{-2}$ and $\\text{power} = 0.9$. Batch size, total training epochs, framework (PyTorch), CUDA version. Training GPU: NVIDIA Tesla V100 (32 GB). Inference measured on NVIDIA RTX 3090. Training time. All models trained from scratch using He initialization [Z].",
          "numberedItems": []
        },
        {
          "id": "id-sub4d",
          "letter": "D",
          "title": "Ablation Study",
          "content": "WRITE 300-400 WORDS. Analyze each component using Table III as reference. Begin: 'To validate the contribution of each proposed component, we conduct ablation experiments on the [dataset] validation set.' Then discuss row-by-row: 'The baseline (Row 1) achieves [X]% mIoU. Adding the [module A] (Row 2) improves mIoU by [+Y]% to [Z]%, demonstrating... The [module B] (Row 3) further enhances accuracy to [W]% (+[V]%), confirming that... Combining all components (Row [N]), the full model achieves [best]% mIoU, which validates the effectiveness of our design choices.' Include inline values: $\\Delta \\text{mIoU} = +2.3$%.",
          "numberedItems": []
        },
        {
          "id": "id-sub4e",
          "letter": "E",
          "title": "Comparison With State-of-the-Art Methods",
          "content": "WRITE 350-450 WORDS. Compare using Table II. 'As presented in Table II, our method achieves [X]% mIoU on [dataset], outperforming the previous best method [method name] [ref] by [+Y]% while requiring [Z]× fewer parameters.' Discuss each competitor group: large models (>10M params) vs. lightweight (<1M params). 'Despite having only [X] M parameters, our model closes the accuracy gap with much larger models such as [large model] ([L]M params, [A]% mIoU) to within [D]%.' Also discuss speed: 'At [FPS] FPS on RTX 3090, our model is suitable for real-time deployment.' Mention if applicable: 'For fair comparison, all speeds are measured under identical settings: single GPU, input resolution $512 \\times 1024$, batch size 1 [ref].'",
          "numberedItems": []
        }
      ]
    },
    {
      "id": "id-sec5",
      "number": "V",
      "title": "CONCLUSION",
      "content": "WRITE 180-250 WORDS. 'In this paper, we proposed [method name], a [brief description] for [task]. The proposed [module A] and [module B] effectively address the key challenges of [limitation 1] and [limitation 2]. Experimental results on the [dataset] benchmark demonstrate that our method achieves [X]% mIoU, outperforming all compared state-of-the-art methods. Specifically, our model requires only [Y] M parameters and runs at [Z] FPS on an NVIDIA RTX 3090, confirming the practical accuracy-efficiency trade-off. \\n\\nDespite these advantages, [limitation]: our method currently [limitation description], which may affect performance in [edge case]. In future work, we plan to [future direction 1] and [future direction 2] to further improve generalization.'",
      "subsections": []
    }
  ],
  "acknowledgment": "This work was supported by [Funding Agency/Grant Name] (Grant No. XXXX/YYYY). The authors would like to thank [Institution/Lab] for providing computational resources, and the [Dataset Name] team for making their benchmark publicly available.",
  "references": [
    {"id": 1, "text": "J. Long, E. Shelhamer, and T. Darrell, \"Fully convolutional networks for semantic segmentation,\" in Proc. IEEE CVPR, Boston, MA, USA, 2015, pp. 3431–3440, doi: 10.1109/CVPR.2015.7298965."},
    {"id": 2, "text": "V. Badrinarayanan, A. Kendall, and R. Cipolla, \"SegNet: A deep convolutional encoder-decoder architecture for image segmentation,\" IEEE Trans. Pattern Anal. Mach. Intell., vol. 39, no. 12, pp. 2481–2495, Dec. 2017, doi: 10.1109/TPAMI.2016.2644615."},
    {"id": 3, "text": "L.-C. Chen, G. Papandreou, F. Schroff, and H. Adam, \"Rethinking atrous convolution for semantic image segmentation,\" arXiv:1706.05587, 2017."},
    {"id": 4, "text": "H. Zhao, J. Shi, X. Qi, X. Wang, and J. Jia, \"Pyramid scene parsing network,\" in Proc. IEEE CVPR, Honolulu, HI, USA, 2017, pp. 2881–2890, doi: 10.1109/CVPR.2017.660."},
    {"id": 5, "text": "A. Vaswani et al., \"Attention is all you need,\" in Proc. NeurIPS, Long Beach, CA, USA, 2017, pp. 5998–6008."},
    {"id": 6, "text": "A. Dosovitskiy et al., \"An image is worth 16x16 words: Transformers for image recognition at scale,\" in Proc. ICLR, 2021."},
    {"id": 7, "text": "M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L.-C. Chen, \"MobileNetV2: Inverted residuals and linear bottlenecks,\" in Proc. IEEE CVPR, 2018, pp. 4510–4520, doi: 10.1109/CVPR.2018.00474."},
    {"id": 8, "text": "S. Mehta, M. Rastegari, A. Caspi, L. Shapiro, and H. Hajishirzi, \"ESPNet: Efficient spatial pyramid of dilated convolutions for semantic segmentation,\" in Proc. ECCV, 2018, pp. 561–580, doi: 10.1007/978-3-030-01249-6_34."},
    {"id": 9, "text": "C.-Y. Wu, R. Girshick, K. He, C. Feichtenhofer, and P. Krahenbuhl, \"A multigrid method for efficiently training video models,\" in Proc. IEEE CVPR, 2020, pp. 153–162, doi: 10.1109/CVPR42600.2020.00023."},
    {"id": 10, "text": "Z. Liu et al., \"Swin Transformer: Hierarchical vision transformer using shifted windows,\" in Proc. IEEE ICCV, 2021, pp. 10012–10022, doi: 10.1109/ICCV48922.2021.00986."},
    {"id": 11, "text": "K. He, X. Zhang, S. Ren, and J. Sun, \"Deep residual learning for image recognition,\" in Proc. IEEE CVPR, Las Vegas, NV, USA, 2016, pp. 770–778, doi: 10.1109/CVPR.2016.90."},
    {"id": 12, "text": "S. Ioffe and C. Szegedy, \"Batch normalization: Accelerating deep network training by reducing internal covariate shift,\" in Proc. ICML, Jul. 2015, pp. 448–456."}
  ],
  "figures": [
    {
      "id": "figure-1",
      "caption": "Fig. 1. [REPLACE WITH: Overall architecture of the proposed network. The encoder processes input images at multiple scales through downsampling blocks. The Feature Enhancement Module (FEM) aggregates multi-scale context. The decoder upsamples with skip connections. Arrows show data flow; dashed lines denote skip connections.]",
      "filename": "",
      "url": ""
    },
    {
      "id": "figure-2",
      "caption": "Fig. 2. [REPLACE WITH: Detailed structure of the proposed Feature Enhancement Module (FEM). Left: input feature map F^(s). Center: parallel dilated convolution branches with rates r={1,2,4,8}, each followed by BN+ReLU. Right: hierarchical feature aggregation and output projection. The module introduces 0.06M additional parameters.]",
      "filename": "",
      "url": ""
    },
    {
      "id": "figure-3",
      "caption": "Fig. 3. [REPLACE WITH: Qualitative segmentation results on the validation set. Each row shows (left) input RGB image, (center) ground-truth annotation, (right) prediction by the proposed method. Note improved boundary delineation and accurate classification of small objects such as pedestrians and cyclists compared to baseline.]",
      "filename": "",
      "url": ""
    },
    {
      "id": "figure-4",
      "caption": "Fig. 4. [REPLACE WITH: Accuracy vs. efficiency trade-off scatter plot. X-axis: FPS on RTX 3090; Y-axis: mIoU (%) on Cityscapes test set. Circle size represents parameter count (M). Our method is represented by a star marker. Methods shown include ENet, ESPNet, ICNet, DABNet, CGNet, BiSeNet, LETNet, and the proposed model.]",
      "filename": "",
      "url": ""
    }
  ],
  "tables": [
    {
      "id": "table-1",
      "caption": "TABLE I. Hyperparameter and Training Configuration",
      "headers": ["Setting", "Value"],
      "rows": [
        ["Dataset", "[REPLACE: e.g., Cityscapes / SemanticKITTI / COCO]"],
        ["Training Images", "[REPLACE: e.g., 2,975 / 19,130]"],
        ["Input Resolution (train)", "[REPLACE: e.g., 512×1024 / 640×640]"],
        ["Backbone", "[REPLACE: e.g., Custom CAP-blocks / ResNet-50]"],
        ["Optimizer", "SGD (momentum=0.9)"],
        ["Initial Learning Rate $lr_{\\text{init}}$", "[REPLACE: e.g., 4.5×10⁻² / 1×10⁻³]"],
        ["LR Schedule", "Poly (power=0.9)"],
        ["Batch Size", "[REPLACE: e.g., 4 / 8 / 16]"],
        ["Training Epochs", "[REPLACE: e.g., 800 / 1000]"],
        ["Weight Decay $\\gamma$", "[REPLACE: e.g., 1×10⁻⁴ / 5×10⁻⁴]"],
        ["Loss Weights $\\lambda_1, \\lambda_2$", "[REPLACE: e.g., 0.4, 1×10⁻⁴]"],
        ["Training GPU", "[REPLACE: e.g., NVIDIA Tesla V100 32GB]"],
        ["Inference GPU (FPS eval)", "[REPLACE: e.g., NVIDIA RTX 3090 24GB]"],
        ["Framework", "PyTorch 1.x / CUDA 11.x"]
      ]
    },
    {
      "id": "table-2",
      "caption": "TABLE II. Comparison with State-of-the-Art Methods on [Dataset] Test Set",
      "headers": ["Method", "Backbone", "Params (M)", "FLOPs (G)", "mIoU (%)","FPS"],
      "rows": [
        ["FCN [1]", "[REPLACE: VGG-16]", "[REPLACE: 134.5]", "[REPLACE: 333.9]", "[REPLACE: 65.3]", "[REPLACE: 10.4]"],
        ["SegNet [2]", "[REPLACE: VGG-16]", "[REPLACE: 29.5]", "[REPLACE: 286.0]", "[REPLACE: 56.1]", "[REPLACE: 11.3]"],
        ["ESPNet [8]", "[REPLACE: ESPNet]", "[REPLACE: 0.36]", "[REPLACE: 4.5]", "[REPLACE: 60.3]", "[REPLACE: 112.9]"],
        ["ICNet [X]", "[REPLACE: ResNet-50]", "[REPLACE: 26.5]", "[REPLACE: 28.3]", "[REPLACE: 69.5]", "[REPLACE: 30.3]"],
        ["CGNet [X]", "[REPLACE: CGNet]", "[REPLACE: 0.50]", "[REPLACE: 6.0]", "[REPLACE: 64.8]", "[REPLACE: 84.2]"],
        ["DABNet [X]", "[REPLACE: DABNet]", "[REPLACE: 0.76]", "[REPLACE: 10.4]", "[REPLACE: 70.1]", "[REPLACE: 104.6]"],
        ["BiSeNetV2 [X]", "[REPLACE: BiSeNetV2]","[REPLACE: 3.40]", "[REPLACE: 21.2]", "[REPLACE: 72.6]", "[REPLACE: 156.1]"],
        ["LETNet [X]", "[REPLACE: LETNet]", "[REPLACE: 0.95]", "[REPLACE: 8.0]", "[REPLACE: 68.4]", "[REPLACE: 108.5]"],
        ["Proposed (Ours)", "[REPLACE: Custom]", "[REPLACE: 0.38]", "[REPLACE: 7.2]", "[REPLACE: 67.7]", "[REPLACE: 146.6]"]
      ]
    },
    {
      "id": "table-3",
      "caption": "TABLE III. Ablation Study on [Dataset] Validation Set",
      "headers": ["Configuration", "[Module A]", "[Module B]", "[Module C]", "Params (M)", "mIoU (%)"],
      "rows": [
        ["Baseline", "✗", "✗", "✗", "[REPLACE: 0.32]", "[REPLACE: 63.1]"],
        ["+ [Module A]", "✓", "✗", "✗", "[REPLACE: 0.35]", "[REPLACE: 65.4]"],
        ["+ [Module B]", "✓", "✓", "✗", "[REPLACE: 0.37]", "[REPLACE: 66.8]"],
        ["+ [Module C] (Full Model)", "✓", "✓", "✓", "[REPLACE: 0.38]", "[REPLACE: 67.7]"]
      ]
    }
  ],
  "equations": [
    {"id": "eq-1", "latex": "\\hat{\\mathbf{Y}} = f_{\\theta}(\\mathbf{X}), \\quad \\mathbf{X} \\in \\mathbb{R}^{3 \\times H \\times W},\\; \\hat{\\mathbf{Y}} \\in \\{1,\\ldots,C\\}^{H \\times W}", "number": 1},
    {"id": "eq-2", "latex": "\\mathbf{F}^{(s+1)} = \\mathcal{D}\\!\\left(\\operatorname{BN}\\!\\left(\\operatorname{DWConv}\\!\\left(\\mathbf{F}^{(s)}\\right)\\right)\\right)", "number": 2},
    {"id": "eq-3", "latex": "\\text{Attn}(\\mathbf{Q},\\mathbf{K},\\mathbf{V}) = \\operatorname{softmax}\\!\\left(\\frac{\\mathbf{Q}\\mathbf{K}^{T}}{\\sqrt{d_k}}\\right)\\mathbf{V}", "number": 3},
    {"id": "eq-4", "latex": "\\mathcal{L}_{\\text{total}} = \\mathcal{L}_{\\text{cls}} + \\lambda_1 \\mathcal{L}_{\\text{aux}} + \\lambda_2 \\mathcal{L}_{\\text{reg}}", "number": 4},
    {"id": "eq-5", "latex": "\\text{mIoU} = \\frac{1}{C} \\sum_{c=1}^{C} \\frac{TP_c}{TP_c + FP_c + FN_c}", "number": 5},
    {"id": "eq-6", "latex": "lr = lr_{\\text{init}} \\times \\left(1 - \\frac{\\text{iter}}{\\text{max\\_iter}}\\right)^{\\text{power}}", "number": 6}
  ]
}

═══════════════════════════════════════════════════════════════
SECTION IV: CRITICAL RULES — READ EVERY ONE
═══════════════════════════════════════════════════════════════
1. Return ONLY the JSON object — NO markdown code blocks (no ```json), NO text before or after.
2. All JSON string values use proper JSON escaping: double backslash for LaTeX commands (\\\\alpha not \\alpha inside JSON), NO unescaped double quotes.
3. REPLACE all bracketed placeholder text (e.g., [REPLACE: ...], [WRITE ...], "WRITE X WORDS HERE") with actual content matching the paper topic from the user prompt.
4. ALL formula placeholders in tables/figures must be replaced with topic-specific realistic values.
5. The "id" fields must be unique: "id-sec1", "id-sec2", ..., "id-sub2a", "id-sub2b", etc.
6. "equations" array: raw LaTeX only (NO $ or $$ delimiters) — delimiters only inside "content" strings.
7. Equations in "content" strings: use $$...$$ on its own paragraph line, separated by \\n from surrounding text.
8. Minimum deliverables: 5 sections, 10+ subsections, 12+ references, 4 figures, 3 tables, 6 equations.
9. Every display equation ($$...$$) in content MUST be followed by explanation of variables/terms.
10. Table column headers and row values must be topic-specific, NOT generic placeholders when you can fill in real names.
11. Reference style: IEEE format — Author initials last name, "Title," Venue, Year, pages, doi.
12. Acknowledgment: mention specific funding body, grant number placeholder, and dataset team.
"""

USER_TEMPLATE = """\
Generate a COMPLETE IEEE conference paper about this research topic:

TITLE: {judul}

MANDATORY REQUIREMENTS:
1. Use the exact paper title: {judul}
2. Replace ALL placeholder text (bracketed instructions) with real, topic-specific content
3. Use SPECIFIC method name (e.g., "HANDNet", "FusionNet", "LQCANet") - invent a suitable acronym
4. Write ALL section content fully - MINIMUM 3500 words total body text
5. Include MINIMUM 6 display equations ($$...$$) with variable explanations
6. Include MINIMUM 8 inline formulas ($...$) naturally integrated in text
7. Fill ALL table rows with realistic numbers matching the topic (mIoU %, Params M, FPS, etc.)
8. Write ALL figure captions describing specific diagrams appropriate to this topic
9. Include 12+ IEEE-format references with real paper authors, titles, venues, years
10. Every formula MUST use correct LaTeX: \\frac{{}}{{}} for fractions, \\sum_{{}}^{{}} for sums
11. DO NOT leave any [WRITE ... WORDS] or [REPLACE:...] instructions unfilled

Topic-specific guidance:
- Name the proposed method as an acronym fitting the topic: {judul}
- Choose appropriate benchmark datasets common to this research domain
- Use realistic state-of-the-art comparison numbers from recent IEEE papers (2022-2025)
- Match complexity: lightweight vs. large model depending on the task requirements
- If topic involves multi-modal fusion: include tensor dimension notation
- If topic involves segmentation: include mIoU formula and per-class analysis
- If topic involves detection: include AP, AP50, AP75 metrics
- Write acknowledgment mentioning a plausible funding source for this research domain

Additional instructions:
{custom_prompt}
"""


# ── Callable API ─────────────────────────────────────────────────────────────
def generate_paper_json(
    judul: str,
    custom_prompt: str = "",
    api_key: str = None,
    model: str = None,
    progress_cb=None,
) -> dict:
    """
    Generate a complete IEEE conference paper JSON from a title.
    
    Args:
        judul: Paper title / topic.
        custom_prompt: Additional instructions for the AI.
        api_key: OpenAI API key (falls back to OPENAI_API_KEY env var).
        model: Model name (falls back to OPENAI_MODEL env var).
        progress_cb: Optional callable(chars_done: int) for progress feedback.
    
    Returns:
        Parsed paper dict.
    
    Raises:
        ValueError: If the API key is missing or JSON cannot be parsed.
    """
    _api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not _api_key:
        raise ValueError("OPENAI_API_KEY tidak ditemukan di environment")
    _model = model or os.getenv("OPENAI_MODEL", MODEL)

    _client = OpenAI(api_key=_api_key, timeout=600.0)

    user_message = (
        USER_TEMPLATE
        .replace("{judul}", judul)
        .replace("{prompt}", judul)
        .replace("{custom_prompt}", custom_prompt if custom_prompt else "(no additional instructions)")
    )

    stream = _client.chat.completions.create(
        model=_model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_message},
        ],
        stream=True,
        stream_options={"include_usage": True},
    )

    raw_content = ""
    usage = None
    for chunk in stream:
        if hasattr(chunk, "usage") and chunk.usage:
            usage = chunk.usage
        if not chunk.choices:
            continue
        delta = chunk.choices[0].delta
        if delta and delta.content:
            raw_content += delta.content
            if progress_cb:
                progress_cb(len(raw_content))

    # Strip markdown fences if present
    clean = re.sub(r"^```(?:json)?\s*", "", raw_content.strip(), flags=re.IGNORECASE)
    clean = re.sub(r"\s*```$", "", clean)

    # Parse JSON with json_repair fallback
    paper_json = None
    try:
        paper_json = json.loads(clean)
    except json.JSONDecodeError as e1:
        try:
            repaired = repair_json(clean, return_objects=True)
            if isinstance(repaired, dict) and repaired:
                paper_json = repaired
            else:
                raise ValueError(f"json_repair did not return a dict: {type(repaired)}")
        except Exception as e2:
            raise ValueError(f"JSON parse failed: {e1} | repair: {e2}")

    if not isinstance(paper_json, dict):
        raise ValueError(f"Expected dict, got {type(paper_json)}")

    return paper_json


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        sys.exit("ERROR: OPENAI_API_KEY tidak ditemukan di .env")

    print("=" * 65)
    print("  IEEE Paper Generator — powered by OpenAI")
    print(f"  Model : {MODEL}")
    print("=" * 65)

    # ── Input dari user ───────────────────────────────────────────────────────
    print("\nMasukkan JUDUL paper IEEE:")
    judul = input("JUDUL  : ").strip()
    if not judul:
        sys.exit("ERROR: Judul tidak boleh kosong.")

    print("\nMasukkan CUSTOM PROMPT tambahan (opsional, tekan Enter untuk skip):")
    print("(contoh: Focus on real-time performance, use YOLO-based architecture)\n")
    custom_prompt = input("CUSTOM : ").strip()

    print(f"\n{'─'*65}")
    print(f"[JUDUL]  {judul}")
    print(f"[CUSTOM] {custom_prompt if custom_prompt else '(kosong)'}")
    print(f"{'─'*65}")
    print("Mengirim ke OpenAI dan streaming response...\n")

    t_start    = time.perf_counter()
    char_count = [0]

    def _progress(n: int):
        if n - char_count[0] >= 200:
            char_count[0] = n
            elapsed_so_far = time.perf_counter() - t_start
            print(f"  [{elapsed_so_far:5.1f}s] {n:,} karakter...", flush=True)

    paper_json = None
    json_valid = False
    json_err   = ""

    try:
        paper_json = generate_paper_json(
            judul=judul,
            custom_prompt=custom_prompt,
            api_key=api_key,
            model=MODEL,
            progress_cb=_progress,
        )
        json_valid = True
    except Exception as e:
        json_err = str(e)

    elapsed = time.perf_counter() - t_start
    print(f"\n  [DONE] {elapsed:.1f}s")

    # ── Simpan output ─────────────────────────────────────────────────────────
    safe_topic = re.sub(r'[^a-zA-Z0-9_]', '_', judul[:50])
    timestamp  = time.strftime("%Y%m%d_%H%M%S")
    out_stem   = f"{timestamp}_{safe_topic}"

    json_path = None
    if json_valid and paper_json:
        json_path = OUTPUT_DIR / f"{out_stem}.json"
        json_path.write_text(
            json.dumps(paper_json, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    # ── Laporan ───────────────────────────────────────────────────────────────
    print("=" * 65)
    print("  HASIL")
    print("=" * 65)
    print(f"  Elapsed time : {elapsed:.2f} s  ({elapsed/60:.1f} menit)")
    print(f"  JSON valid   : {'✓ YA' if json_valid else '✗ TIDAK — ' + json_err}")
    if json_path:
        print(f"  JSON saved   : {json_path}")
    print("=" * 65)

    if json_valid and paper_json:
        title = paper_json.get("title", "(no title)")
        print(f"\n[JUDUL] {title}\n")

    return paper_json


if __name__ == "__main__":
    main()

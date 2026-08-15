# Week 1 — Literature Review + Image Segmentation

**Duration:** Days 1–7  
**Goal:** Understand the research problem deeply, survey the literature, and get hands-on with a segmentation algorithm.

---

## Part A: Literature Review (Days 1–4)

### Papers to Read

All papers are in the `papers/` directory. Read them in this order:

| # | File | What to focus on |
|---|------|-----------------|
| 1 | `AI-based_dietary_assessment_systematic_review.pdf` | Broad landscape of AI dietary assessment; understand current approaches and their limitations |
| 2 | `nutrients-14-00221.pdf` | Methodology detail on digital imagery dietary methods |
| 3 | `applsci-13-05742.pdf` | Applied segmentation/classification for food images |
| 4 | `s41598-021-03972-8.pdf` | Deep learning in food/nutrition context |
| 5 | `VLM_for_Dietary_Assessment.pdf` | Vision-Language Models applied to dietary assessment |
| 6 | `Romero-Tapiador_VLMs_Dietary_Assessment_CVPR2025.pdf` | State-of-the-art VLM benchmarking for this domain (2025) |

### For Each Paper, Fill In a Summary

Use the template in `paper_summary_template.md`. Your summary for each paper should answer:

1. **What problem does it solve?**
2. **What dataset(s) were used?**
3. **What AI/ML method was applied?**
4. **What were the key results / metrics?**
5. **What are the limitations?**
6. **How does it relate to our project?**

Save your summaries as `week1/summaries/paper_N_summary.md`.

### Key Concepts to Understand After Week 1

By the end of this part, you should be able to explain:
- What "dietary assessment" means and why accuracy matters
- Why digital imagery (DI) is better than self-report
- What the four-step AI pipeline for this project is
- What AUROC, RMSE, and NRMSE mean as evaluation metrics
- What "inter-rater reliability" means and why 0.94–0.99 is important

---

## Part B: Image Segmentation (Days 3–7)

This part overlaps slightly with Part A — you can start reading about segmentation while finishing your paper summaries.

### What is Image Segmentation?

Image segmentation is the process of dividing an image into meaningful regions. In our project, we need to **separate individual food items from the cafeteria tray and background**. There are three main types:

| Type | Description | Example |
|------|-------------|---------|
| **Semantic segmentation** | Label every pixel with a class | "This pixel is pizza, this is salad..." |
| **Instance segmentation** | Distinguish separate objects of the same class | "This is pizza slice #1, this is pizza slice #2" |
| **Panoptic segmentation** | Combines both | Full scene understanding |

### Segmentation Algorithms to Study

Work through these in order of complexity:

#### Classical Methods (understand conceptually)
- **Thresholding** (Otsu's method) — pixel intensity-based
- **K-means clustering** — group pixels by color similarity
- **GrabCut** — interactive foreground/background separation (OpenCV)
- **Watershed algorithm** — region growing from "seeds"

#### Deep Learning Methods (hands-on)
- **FCN** (Fully Convolutional Network, 2015) — the ancestor of modern segmentation nets
- **U-Net** (2015) — encoder-decoder with skip connections; extremely popular in medical/food imaging
- **DeepLab v3+** (2018) — uses atrous (dilated) convolutions for better scale handling
- **Mask R-CNN** (2017) — instance segmentation; detects + segments individual objects
- **SAM** (Segment Anything Model, Meta 2023) — foundation model for zero-shot segmentation; highly relevant for our use case

> **Why U-Net?** The Iftekharuddin lab (our collaborators) already uses a **context-aware 3D U-Net** for brain tumor MRI segmentation. The exact same architecture family will be adapted for food segmentation. Make sure you understand U-Net deeply.

#### Resources
- [U-Net paper](https://arxiv.org/abs/1505.04597)
- [Mask R-CNN paper](https://arxiv.org/abs/1703.06870)
- [Segment Anything (SAM)](https://arxiv.org/abs/2304.02643)
- [Papers With Code — Semantic Segmentation](https://paperswithcode.com/task/semantic-segmentation)
- [Roboflow — Image Segmentation Guide](https://roboflow.com/learn/image-segmentation)

---

### Kaggle Competition: Get Hands-On

#### Recommended Competition: [2018 Data Science Bowl](https://www.kaggle.com/c/data-science-bowl-2018)
- **Task:** Detect and segment cell nuclei in microscopy images
- **Why it's perfect for us:** Instance segmentation of small, distinct objects on a background — directly analogous to segmenting food items on a tray
- **Dataset:** ~600 labeled images with instance masks — small enough to train quickly
- **Winning solutions:** Heavily U-Net-based; many great public notebooks to learn from

#### Steps to Complete
1. Create a free Kaggle account at [kaggle.com](https://www.kaggle.com)
2. Join the 2018 Data Science Bowl competition (late submissions allowed for learning)
3. Download the dataset
4. Start with a public notebook — search for "U-Net nuclei segmentation" in the competition notebooks
5. Run the notebook end-to-end, understand each step
6. **Try to improve it:** experiment with one change (different backbone, data augmentation, loss function)
7. Submit predictions and note your score

#### Stretch Goal — Food-Specific Dataset
If you finish early, try applying your segmentation model to a food dataset:
- **FoodSeg103** — 103-class food segmentation dataset ([paper](https://arxiv.org/abs/2105.05409), [GitHub](https://github.com/LARC-CMU-SMU/FoodSeg103-Benchmark-v1))
- **UEC Food-256** — 256 Japanese food categories with bounding boxes
- **iFood-2019** Kaggle competition (fine-grained food classification, good preprocessing practice)

---

## Deliverables by End of Week 1

- [ ] 6 paper summaries saved in `week1/summaries/`
- [ ] Written explanation (1 page) of the 4-step AI pipeline for our project
- [ ] A working Kaggle notebook with a U-Net segmentation model on the Data Science Bowl dataset
- [ ] Brief written reflection: what segmentation challenges are specific to food images vs. cell images?

---

## Helpful References

- [Stanford CS231n — Lecture 11: Detection and Segmentation](http://cs231n.stanford.edu/slides/2022/lecture_11.pdf)
- [Towards Data Science — U-Net explained](https://towardsdatascience.com/u-net-b229b32b4a71)
- [PyImageSearch — Image Segmentation with OpenCV](https://pyimagesearch.com/category/image-segmentation/)

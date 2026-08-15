# Pilot Project Onboarding — 3-Week Training Plan

Welcome! This repository is your guided onboarding into the **AI-driven dietary assessment research project**. The goal of this project is to build a machine-learning pipeline that automatically estimates food consumption from paired before/after meal images captured in school cafeteria settings — replacing expensive manual human rating.

You will spend three weeks building up the technical foundation needed to contribute meaningfully to this work. Each week has its own folder with detailed instructions, resources, and starter code.

---

## Project Background

The project applies AI/ML to automate dietary intake assessment from digital meal images. A prior NIH-funded study produced **7,663 labeled pre/post tray image pairs** rated by trained humans (inter-rater reliability: 0.94–0.99). The AI pipeline must:

1. Pre-process images (correct for orientation, lighting, scale)
2. **Segment** individual food items from the tray
3. **Classify** which items were selected
4. **Estimate consumption** by comparing pre vs. post images

Your learning path maps directly to steps 2–4, plus the foundational AI tooling (LLMs and RAG) that will support future pipeline stages.

---

## Three-Week Overview

| Week | Theme | Key Deliverable |
|------|-------|----------------|
| [**Week 1**](./week1/README.md) | Literature Review + Image Segmentation | Paper summaries + working segmentation notebook on a Kaggle dataset |
| [**Week 2**](./week2/README.md) | LLM Basics — Open vs. Closed Source | Script that calls both a cloud LLM API and a local model; written comparison |
| [**Week 3**](./week3/README.md) | Retrieval-Augmented Generation (RAG) | RAG pipeline over project papers using a local LLM |

---

## Repository Structure

```
pilot-onboarding/
├── README.md                  ← You are here
├── papers/                    ← Research papers to review (Week 1)
├── week1/
│   ├── README.md              ← Week 1 instructions
│   └── paper_summary_template.md
├── week2/
│   ├── README.md              ← Week 2 instructions
│   └── starter_code/
│       ├── openai_call.py     ← Cloud LLM example
│       └── ollama_call.py     ← Local LLM example
└── week3/
    ├── README.md              ← Week 3 instructions
    └── starter_code/
        └── rag_pipeline.py    ← RAG starter code
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- `git` and a GitHub account
- A free [Kaggle account](https://www.kaggle.com) (Week 1)
- [Ollama](https://ollama.com) installed (Weeks 2 & 3) — see Week 2 README
- (Optional) An OpenAI API key for Week 2 cloud LLM examples

### Setup

```bash
# Clone the repo
git clone https://github.com/mtoumi12/pilot-onboarding.git
cd pilot-onboarding

# Create a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows

# Install dependencies (added progressively each week)
pip install -r requirements.txt
```

---

## Weekly Schedule at a Glance

### Week 1 — Literature Review + Segmentation
- Read and summarize the 6 research papers in `papers/`
- Understand the project's motivation, dataset, and evaluation metrics
- Learn about image segmentation algorithms (classical → deep learning)
- Find and enter a Kaggle segmentation competition; apply a segmentation model

### Week 2 — LLM Basics
- Understand what an LLM is and how inference works
- Learn the difference between **closed-source** (OpenAI GPT, Claude, Gemini) and **open-source** (LLaMA, Mistral, Phi) models
- Install **Ollama** and run a small LLM locally on your machine
- Make API calls to both a cloud LLM and your local model

### Week 3 — Retrieval-Augmented Generation (RAG)
- Understand why RAG exists and when to use it
- Build a RAG pipeline over the project papers from Week 1
- Use your locally-downloaded Ollama model as the LLM backend
- Query the system with research-relevant questions

---

## Questions & Contact

If you have questions while working through the material, open a GitHub **Issue** in this repository and tag it with the relevant week label. This creates a log of questions and answers that will be useful for future students.

---

*This onboarding plan was designed for a three-week independent study period. Estimated time commitment: ~20–25 hours/week.*

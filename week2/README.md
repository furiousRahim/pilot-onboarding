# Week 2 — LLM Basics: Open Source vs. Closed Source

**Duration:** Days 8–14  
**Goal:** Understand how Large Language Models work, the difference between open and closed source models, and get a local LLM running on your own machine.

---

## Part A: What is an LLM? (Days 8–9)

### Core Concepts to Understand

#### How LLMs Work (High-Level)
- LLMs are trained on massive text corpora to predict the next token
- At inference time, they generate text autoregressively (one token at a time)
- **Context window** — the amount of text (tokens) the model can "see" at once
- **Temperature** — controls randomness of output (0 = deterministic, 1+ = creative)
- **System prompt vs. user prompt** — how to structure instructions

#### Key Terms
| Term | Meaning |
|------|---------|
| **Token** | Roughly 3/4 of a word; the unit LLMs process |
| **Parameters** | Weights in the neural network; "size" of a model (e.g., 7B = 7 billion params) |
| **Fine-tuning** | Further training a pre-trained model on a specific dataset |
| **Prompt engineering** | Crafting inputs to get better outputs without retraining |
| **Embeddings** | Dense vector representations of text (critical for Week 3 RAG) |

#### Resources
- [3Blue1Brown — "But what is a GPT?" (YouTube)](https://www.youtube.com/watch?v=wjZofJX0v4M) — the best visual intro
- [Andrej Karpathy — "Intro to Large Language Models" (YouTube)](https://www.youtube.com/watch?v=zjkBMFhNj_g)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)

---

## Part B: Open Source vs. Closed Source LLMs (Day 9–10)

### Closed Source (Proprietary) Models

These are models where the weights are not publicly released. You access them via an API.

| Model | Company | Notes |
|-------|---------|-------|
| GPT-4o / GPT-4.1 | OpenAI | Most widely used; strong general capability |
| Claude 3.5 / Claude 4 | Anthropic | Strong reasoning; long context window |
| Gemini 1.5 / 2.0 | Google | Multimodal; integrates with Google services |
| Command R+ | Cohere | Strong for RAG tasks specifically |

**Pros:** Very capable; no hardware required; simple API  
**Cons:** Cost per token; data sent to third-party servers; no offline use; no customization of weights

### Open Source Models

These models have publicly available weights. You can download and run them locally.

| Model | Organization | Size | Notes |
|-------|-------------|------|-------|
| **LLaMA 3.2** | Meta | 1B, 3B, 8B, 70B | Excellent quality; most widely used open model family |
| **Mistral 7B** | Mistral AI | 7B | Fast and efficient; great for RAG |
| **Phi-3 / Phi-4 Mini** | Microsoft | 3.8B | Surprisingly strong at small size |
| **Gemma 2** | Google | 2B, 9B, 27B | Good quality; Google's open release |
| **Qwen 2.5** | Alibaba | 0.5B–72B | Very strong multilingual; good instruction-following |
| **DeepSeek-R1** | DeepSeek | 7B–671B | Strong reasoning model |

**Pros:** Free; private (data never leaves your machine); customizable; works offline; no API rate limits  
**Cons:** Requires hardware (RAM/VRAM); smaller models less capable than top closed-source; you manage updates

### Key Comparison Points to Write Up

Write a 1–2 page comparison covering:
1. **Privacy** — which is appropriate when?
2. **Cost** — token pricing vs. hardware cost
3. **Capability** — benchmarks like MMLU, HumanEval, MATH
4. **Customization** — fine-tuning possibilities
5. **Relevance to research** — why a local model might be preferable for sensitive medical/dietary data

---

## Part C: Run a Local LLM with Ollama (Days 10–12)

### Why Ollama?

[Ollama](https://ollama.com) is the simplest way to run open-source LLMs locally. It handles model downloads, quantization, and a local REST API automatically.

### Installation

```bash
# macOS
brew install ollama

# Or download the installer from https://ollama.com
```

### Recommended Model for Learning

For a laptop with 8–16 GB RAM, pull **Phi-4 Mini** or **LLaMA 3.2 3B**:

```bash
# Start the Ollama server (runs in background)
ollama serve

# Pull a small, capable model (~2 GB download)
ollama pull phi4-mini

# Or LLaMA 3.2 3B (~2 GB)
ollama pull llama3.2:3b

# Test it immediately in the terminal
ollama run phi4-mini "Explain what image segmentation is in 3 sentences."
```

> **Model selection guide:**  
> - 8 GB RAM → `phi4-mini` or `llama3.2:3b`  
> - 16 GB RAM → `llama3.2:8b` or `mistral:7b`  
> - 32 GB RAM+ → `llama3.1:8b` or `gemma2:9b`

### Explore the Ollama Model Library

Browse available models at [ollama.com/library](https://ollama.com/library). Try pulling at least two different models and compare their responses to the same prompt.

---

## Part D: Make LLM API Calls in Python (Days 12–14)

Run the starter scripts in `week2/starter_code/`:

### Cloud LLM Example (`openai_call.py`)

Requires: `pip install openai` and an OpenAI API key in your environment:

```bash
export OPENAI_API_KEY="sk-..."
python week2/starter_code/openai_call.py
```

### Local Ollama Example (`ollama_call.py`)

Requires: Ollama running (`ollama serve`) and a model pulled.

```bash
python week2/starter_code/ollama_call.py
```

### Exercises

1. Change the **system prompt** in both scripts — how does it affect output quality?
2. Try different **temperature values** (0.0, 0.5, 1.0) — what changes?
3. Ask both models: *"What are the main challenges in food image segmentation?"* — compare answers
4. Try **streaming** responses (see the starter code comments)

---

## Deliverables by End of Week 2

- [ ] Written comparison of open-source vs. closed-source LLMs (1–2 pages)
- [ ] Ollama installed with at least two models downloaded and tested
- [ ] Both starter scripts running successfully
- [ ] Notes on what you observed: differences between local and cloud models

---

## Helpful References

- [Ollama documentation](https://ollama.com/docs)
- [OpenAI Python SDK docs](https://platform.openai.com/docs/libraries)
- [Open LLM Leaderboard (HuggingFace)](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — compare model benchmarks
- [LMSYS Chatbot Arena](https://chat.lmsys.org) — see how models rank by human preference

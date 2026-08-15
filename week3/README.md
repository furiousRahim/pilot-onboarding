# Week 3 — Retrieval-Augmented Generation (RAG)

**Duration:** Days 15–21  
**Goal:** Understand RAG, build a working RAG pipeline over the project's research papers, and query it using the local LLM you downloaded in Week 2.

---

## Part A: What is RAG and Why Does it Exist? (Days 15–16)

### The Problem RAG Solves

LLMs have two fundamental limitations:
1. **Knowledge cutoff** — they only know what was in their training data; they don't know about new papers, internal documents, or private data
2. **Context window limits** — you can't paste an entire document library into a prompt

**RAG (Retrieval-Augmented Generation)** solves this by connecting an LLM to an external knowledge source:

```
User Question
     ↓
[Retriever] → searches a vector database of document chunks
     ↓
Relevant chunks fetched
     ↓
[LLM] receives: system prompt + relevant chunks + user question
     ↓
Grounded, accurate answer
```

### Why RAG Matters for This Project

In the future, we may want to:
- Query all dietary assessment literature at once
- Ground model responses in specific papers (no hallucination)
- Ask questions about our experimental results stored in documents
- Build a Q&A interface over the project's internal notes

What you build in Week 3 is the foundation for all of this.

---

## Part B: RAG Architecture in Depth (Day 16)

### The Two Phases

#### Indexing Phase (done once, offline)
1. **Load** documents (PDFs, text files, etc.)
2. **Chunk** — split documents into overlapping text segments (~200–500 tokens each)
3. **Embed** — convert each chunk into a vector using an embedding model
4. **Store** — save vectors + metadata in a vector database

#### Querying Phase (done at runtime)
1. **Embed** the user's question into a vector
2. **Search** the vector database for the most similar chunks (cosine similarity)
3. **Retrieve** the top-k chunks
4. **Augment** — inject the chunks into the LLM's prompt as context
5. **Generate** — LLM produces a grounded answer

### Key Components

| Component | What it does | Tools we'll use |
|-----------|-------------|----------------|
| **Document loader** | Read PDFs into text | `pypdf`, `langchain` |
| **Text splitter** | Chunk documents | `RecursiveCharacterTextSplitter` |
| **Embedding model** | Text → vectors | `nomic-embed-text` (via Ollama, free & local) |
| **Vector store** | Store & search embeddings | `Chroma` (local, no server needed) |
| **LLM** | Generate answers | `phi4-mini` or `llama3.2:3b` via Ollama |
| **Orchestration** | Wire it all together | `LangChain` or `LlamaIndex` |

---

## Part C: Setup (Day 16)

```bash
# Make sure you're in your virtual environment
source .venv/bin/activate

# Install RAG dependencies
pip install langchain langchain-community langchain-ollama chromadb pypdf sentence-transformers

# Pull the embedding model via Ollama (small, fast, local)
ollama pull nomic-embed-text

# Confirm your LLM is still available
ollama list
```

---

## Part D: Build the RAG Pipeline (Days 17–19)

Run and study the starter script:

```bash
python week3/starter_code/rag_pipeline.py
```

The script will:
1. Load all PDFs from `papers/`
2. Chunk them into segments
3. Embed them and store in a local Chroma vector database
4. Accept a question from the command line
5. Retrieve the most relevant chunks
6. Generate a grounded answer using your local Ollama model

### Try These Questions

Once the pipeline is running, ask it:

```
python week3/starter_code/rag_pipeline.py "What are the main methods used for food image segmentation?"
python week3/starter_code/rag_pipeline.py "What datasets have been used to evaluate AI dietary assessment systems?"
python week3/starter_code/rag_pipeline.py "What is the typical accuracy of automated dietary assessment compared to human raters?"
python week3/starter_code/rag_pipeline.py "What are Vision Language Models and how are they used for dietary assessment?"
```

---

## Part E: Experiments and Improvements (Days 19–21)

Try at least two of the following modifications and document what changes:

### Experiment 1: Chunk Size
Change `chunk_size` from 500 to 200 or 1000 in the text splitter. How does this affect answer quality?

### Experiment 2: Number of Retrieved Chunks (top-k)
Change `k=3` to `k=1` or `k=8` in the retriever. What happens to answers?

### Experiment 3: Different Embedding Model
Replace `nomic-embed-text` with `mxbai-embed-large` (pull via Ollama). Does retrieval quality improve?

```bash
ollama pull mxbai-embed-large
```

### Experiment 4: Add Source Citations
Modify the pipeline to include the source file name and page number in the answer. This is critical for research use.

### Experiment 5: Evaluate Retrieval Quality
For one question, print the retrieved chunks *before* sending them to the LLM. Are the chunks actually relevant? What does this tell you about retrieval quality?

---

## Deliverables by End of Week 3

- [ ] Working RAG pipeline that ingests all papers from `papers/`
- [ ] Answers to at least 5 research questions documented in `week3/results.md`
- [ ] Brief write-up (1 page): what are the limitations of the RAG system you built? What would you improve?
- [ ] Notes on at least one experiment (chunk size, top-k, or embedding model)

---

## Conceptual Questions to Reflect On

1. What happens if the question is completely outside the document corpus?
2. Why do we use an embedding model separate from the LLM?
3. What is the difference between RAG and fine-tuning? When would you use each?
4. How would you adapt this pipeline to work with images instead of text? (Think ahead to our project's actual data.)

---

## Helpful References

- [LangChain RAG tutorial (official docs)](https://python.langchain.com/docs/tutorials/rag/)
- [LlamaIndex documentation](https://docs.llamaindex.ai) — alternative RAG framework
- [Chroma documentation](https://docs.trychroma.com)
- [Ollama + LangChain integration](https://python.langchain.com/docs/integrations/llms/ollama/)
- [What is RAG? — IBM explainer](https://www.ibm.com/topics/retrieval-augmented-generation)
- ["Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (original RAG paper)](https://arxiv.org/abs/2005.11401)

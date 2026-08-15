"""
Week 2 Starter: Making a call to a local LLM via Ollama
---------------------------------------------------------
Requirements:
    1. Install Ollama: https://ollama.com
    2. In a terminal, run: ollama serve
    3. Pull a model:  ollama pull phi4-mini
       (or llama3.2:3b if you prefer)
    4. pip install ollama

Run:
    python week2/starter_code/ollama_call.py
"""

import ollama

MODEL = "phi4-mini"   # change to "llama3.2:3b" or any model you pulled

SYSTEM_PROMPT = """You are a helpful research assistant specializing in 
computer vision and dietary assessment. Answer concisely and accurately."""

USER_QUESTION = "What is image segmentation and why is it useful for analyzing food images?"


def simple_call():
    """Basic single-turn call to the local Ollama model."""
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_QUESTION},
        ],
        options={"temperature": 0.7},
    )
    answer = response["message"]["content"]
    print(f"=== {MODEL} Response ===")
    print(answer)
    return answer


def streaming_call():
    """Stream response tokens as they are generated."""
    print(f"=== {MODEL} Streaming Response ===")
    stream = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_QUESTION},
        ],
        stream=True,
    )
    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)
    print()


def list_available_models():
    """Show all models you have downloaded locally."""
    print("=== Locally Available Models ===")
    models = ollama.list()
    for m in models["models"]:
        size_gb = m["size"] / 1e9
        print(f"  {m['name']:30s}  {size_gb:.1f} GB")


def compare_temperatures():
    """
    Run the same prompt at temperature 0 (deterministic) and 1.0 (creative).
    Observe how answers differ.
    """
    prompt = "Describe three challenges in food image segmentation."
    for temp in [0.0, 1.0]:
        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": temp},
        )
        print(f"\n--- Temperature {temp} ---")
        print(response["message"]["content"])


if __name__ == "__main__":
    list_available_models()
    print()
    simple_call()
    # streaming_call()
    # compare_temperatures()

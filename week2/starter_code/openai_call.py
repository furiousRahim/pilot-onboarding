"""
Week 2 Starter: Making a call to a cloud LLM (OpenAI GPT)
----------------------------------------------------------
Requirements:
    pip install openai

Set your API key:
    export OPENAI_API_KEY="sk-..."

Run:
    python week2/starter_code/openai_call.py
"""

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are a helpful research assistant specializing in 
computer vision and dietary assessment. Answer concisely and accurately."""

USER_QUESTION = "What is image segmentation and why is it useful for analyzing food images?"


def simple_call():
    """Basic single-turn LLM call."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",   # cheap + fast; swap for "gpt-4o" for higher quality
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_QUESTION},
        ],
        temperature=0.7,       # 0 = deterministic, 1+ = creative
        max_tokens=300,
    )
    answer = response.choices[0].message.content
    print("=== GPT Response ===")
    print(answer)
    print(f"\n[Tokens used: {response.usage.total_tokens}]")
    return answer


def streaming_call():
    """Stream the response token-by-token (useful for long outputs)."""
    print("=== GPT Streaming Response ===")
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_QUESTION},
        ],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()  # newline at end


def multi_turn_conversation():
    """Demonstrate a multi-turn (back-and-forth) conversation."""
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    turns = [
        "What is U-Net and what was it originally designed for?",
        "How could U-Net be adapted for food segmentation instead?",
        "What evaluation metrics would you use to measure segmentation quality?",
    ]

    print("=== Multi-Turn Conversation ===")
    for user_input in turns:
        print(f"\nUser: {user_input}")
        messages.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3,
        )
        assistant_reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_reply})
        print(f"GPT: {assistant_reply}")


if __name__ == "__main__":
    # Run each demo — comment/uncomment as needed
    simple_call()
    # streaming_call()
    # multi_turn_conversation()

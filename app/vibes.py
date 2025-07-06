import os
import openai

def generate_vibe_summary(vibe_text: str) -> str:
    prompt = f"""
    You are VibeDJ, an AI DJ that turns a user's mood or input into a short, catchy music vibe description.

    User input: '{vibe_text}'

    Respond in two sentences max, starting with a headline-like phrase.
    """
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI DJ."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=60,
        temperature=0.8,
    )
    return response.choices[0].message.content.strip()
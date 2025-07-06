# app/vibes.py
import os
import openai
from dotenv import load_dotenv

load_dotenv(dotenv_path=('/env/.env'))
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_vibe_summary(vibe_text: str) -> str:
    prompt = (
        "You are VibeDJ, an AI DJ that turns a user’s mood/input into a short, catchy music vibe description. "
        f"User input: '{vibe_text}'.\n"
        "Respond in two sentences max, starting with a headline-like phrase."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI DJ."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60,
        temperature=0.8,
    )
    return response.choices[0].message.content.strip()

# app/vibes.py
import os
import openai
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'env', '.env')
load_dotenv(dotenv_path=dotenv_path)
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_vibe_summary(vibe_text: str) -> str:
    """
    Generate a short, catchy music vibe description based on user input.
    Uses the new OpenAI Python v1 API interface.
    """
    prompt = (
        "You are VibeDJ, an AI DJ that turns a user’s mood/input into a short, catchy music vibe description. "
        f"User input: '{vibe_text}'.\n"
        "Respond in two sentences max, starting with a headline-like phrase."
    )

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI DJ."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=60,
        temperature=0.8,
    )

    content = response.choices[0].message.content.strip()
    return content

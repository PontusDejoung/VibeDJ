# app/tts.py
import os
import hashlib
import pyttsx3

# Directory to store generated audio files
STATIC_DIR = os.path.join(os.path.dirname(__file__), "..", "static")
os.makedirs(STATIC_DIR, exist_ok=True)

# Initialize TTS engine once
engine = pyttsx3.init()
# Optionally, configure voice properties (e.g., rate, volume)
engine.setProperty('rate', 150)  # speaking rate (words per minute)
engine.setProperty('volume', 0.8)  # volume (0.0 to 1.0)


def generate_dj_voice(text: str) -> str:
    """
    Generate a fake DJ voice MP3 file from the given text.
    Returns the URL path to the generated audio file.
    """
    # Create a unique filename based on text hash
    hash_digest = hashlib.md5(text.encode('utf-8')).hexdigest()
    filename = f"dj_{hash_digest}.mp3"
    file_path = os.path.join(STATIC_DIR, filename)

    # If file already exists, return the existing URL
    if not os.path.exists(file_path):
        # Save speech to file
        engine.save_to_file(text, file_path)
        engine.runAndWait()

    # Return the relative URL to serve
    return f"/static/{filename}"

# app/main.py (FastAPI)
from fastapi import FastAPI
from pydantic import BaseModel
from .vibes import generate_vibe_summary
from .suggester import suggest_playlist
from .tts import generate_dj_voice  # valfritt

class VibeRequest(BaseModel):
    vibe: str

app = FastAPI()

@app.post("/vibe")
async def vibe_endpoint(req: VibeRequest):
    summary = generate_vibe_summary(req.vibe)
    songs = suggest_playlist(req.vibe)
    dj_audio_url = generate_dj_voice(summary)  # valfritt
    return {
        "vibe_summary": summary,
        "songs": songs,
        "dj_audio_url": dj_audio_url,
    }

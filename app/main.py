import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

# Load .env
env_path = os.path.join(os.path.dirname(__file__), '..', 'env', '.env')
load_dotenv(dotenv_path=env_path)

from .vibes import generate_vibe_summary
from .suggester import suggest_playlist

app = FastAPI()

class VibeRequest(BaseModel):
    vibe: str

@app.post("/vibe")
async def vibe_endpoint(req: VibeRequest):
    summary = generate_vibe_summary(req.vibe)
    songs = suggest_playlist(req.vibe)
    return {
        "vibe_summary": summary,
        "songs": songs,
    }
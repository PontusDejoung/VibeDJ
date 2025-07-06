# tests/test_app.py
"""
Simple test script without pytest for VibeDJ API.
Run with: python tests/test_app.py
"""
import os
import json
import sys
from fastapi.testclient import TestClient
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'env', '.env')
load_dotenv(dotenv_path=dotenv_path)

# Import app
from main import app

client = TestClient(app)

def test_vibe_endpoint(vibe_input):
    print(f"\n--- Testing vibe: '{vibe_input}' ---")

    # 1. Call /vibe endpoint\   
    resp = client.post("/vibe", json={"vibe": vibe_input})
    if resp.status_code != 200:
        print(f"ERROR: status code {resp.status_code}")
        print(resp.text)
        return False
    data = resp.json()

    # 2. Print response data
    print("vibe_summary:", data.get("vibe_summary"))
    print("songs:")
    for song in data.get("songs", []):
        print(f" - {song['title']} by {song['artist']}")

    return True

if __name__ == '__main__':
    # List of test inputs
    inputs = [
        "chill evening",         # chill
        "angry breakup",         # angry
        "morning run",           # run
        "random mood text",      # random
        "late-night coding",     # random/focus
        "upbeat party time",     # party
        "deep concentration",    # focus
        "melancholic reflection",# sad
        "high-energy workout",   # run/party
        "stressful day at work", # random/angry
    ]

    all_passed = True
    for vibe in inputs:
        ok = test_vibe_endpoint(vibe)
        if not ok:
            all_passed = False

    if all_passed:
        print("\nAll tests passed.")
        sys.exit(0)
    else:
        print("\nSome tests failed.")
        sys.exit(1)

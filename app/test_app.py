# tests/test_app.py
"""
Simple test script without pytest for VibeDJ API.
Run with: python tests/test_app.py
"""
import os
import json
import sys
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_vibe_endpoint(vibe_input):
    print(f"\n--- Testing vibe: '{vibe_input}' ---")
 
    resp = client.post("/vibe", json={"vibe": vibe_input})
    if resp.status_code != 200:
        print(f"ERROR: status code {resp.status_code}")
        print(resp.text)
        return False
    data = resp.json()

    print("vibe_summary:", data.get("vibe_summary"))
    print("songs:")
    for song in data.get("songs", []):
        print(f" - {song['title']} by {song['artist']}")

    return True

if __name__ == '__main__':
    inputs = [
        "chill evening",         
        "angry breakup",         
        "morning run",           
        "random mood text",      
        "late-night coding",     
        "upbeat party time",     
        "deep concentration",    
        "melancholic reflection",
        "high-energy workout",   
        "stressful day at work", 
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

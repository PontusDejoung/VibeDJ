# app/suggester.py
MOCK_PLAYLISTS = {
    "chill": [
        {"title": "Sunset Lover", "artist": "Petit Biscuit"},
        {"title": "Weightless", "artist": "Marconi Union"},
        {"title": "River Flows in You", "artist": "Yiruma"},
    ],
    "angry": [
        {"title": "Break Stuff", "artist": "Limp Bizkit"},
        {"title": "Killing in the Name", "artist": "Rage Against The Machine"},
        {"title": "Bulls on Parade", "artist": "Rage Against The Machine"},
    ],
    "run": [
        {"title": "Can't Hold Us", "artist": "Macklemore & Ryan Lewis"},
        {"title": "Eye of the Tiger", "artist": "Survivor"},
        {"title": "Run the World (Girls)", "artist": "Beyoncé"},
    ],
}

def suggest_playlist(vibe_text: str):
    key = vibe_text.lower().split()[0]
    return MOCK_PLAYLISTS.get(key, MOCK_PLAYLISTS["chill"])

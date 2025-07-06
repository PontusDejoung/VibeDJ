import os
import openai

# Initialize OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Predefined mock playlists
MOCK_PLAYLISTS = {
    "chill": [
        {"title": "Sunset Lover",          "artist": "Petit Biscuit"},
        {"title": "Weightless",            "artist": "Marconi Union"},
        {"title": "River Flows in You",    "artist": "Yiruma"},
        {"title": "Night Owl",             "artist": "Galimatias"},
        {"title": "Lost in Thoughts",      "artist": "Honesty"},
    ],
    "angry": [
        {"title": "Break Stuff",                   "artist": "Limp Bizkit"},
        {"title": "Killing in the Name",           "artist": "Rage Against The Machine"},
        {"title": "Bulls on Parade",               "artist": "Rage Against The Machine"},
        {"title": "Duality",                       "artist": "Slipknot"},
        {"title": "Down with the Sickness",        "artist": "Disturbed"},
    ],
    "run": [
        {"title": "Can't Hold Us",             "artist": "Macklemore & Ryan Lewis"},
        {"title": "Eye of the Tiger",          "artist": "Survivor"},
        {"title": "Run the World (Girls)",     "artist": "Beyoncé"},
        {"title": "Stronger",                  "artist": "Kanye West"},
        {"title": "Thunderstruck",             "artist": "AC/DC"},
    ],
    "happy": [
        {"title": "Happy",                     "artist": "Pharrell Williams"},
        {"title": "Walking on Sunshine",       "artist": "Katrina & The Waves"},
        {"title": "Good as Hell",              "artist": "Lizzo"},
        {"title": "Sugar",                     "artist": "Maroon 5"},
        {"title": "Shake It Off",              "artist": "Taylor Swift"},
    ],
    "focus": [
        {"title": "Time",                      "artist": "Hans Zimmer"},
        {"title": "Spiegel im Spiegel",        "artist": "Arvo Pärt"},
        {"title": "Experience",                "artist": "Ludovico Einaudi"},
        {"title": "Prelude in E Minor",        "artist": "Frédéric Chopin"},
        {"title": "An Ending (Ascent)",        "artist": "Brian Eno"},
    ],
    "party": [
        {"title": "Uptown Funk",               "artist": "Mark Ronson ft. Bruno Mars"},
        {"title": "Don't Stop the Music",      "artist": "Rihanna"},
        {"title": "Can't Stop the Feeling!",   "artist": "Justin Timberlake"},
        {"title": "Levitating",               "artist": "Dua Lipa"},
        {"title": "I Gotta Feeling",           "artist": "The Black Eyed Peas"},
    ],
    "sad": [
        {"title": "Someone Like You",          "artist": "Adele"},
        {"title": "Fix You",                   "artist": "Coldplay"},
        {"title": "Skinny Love",               "artist": "Bon Iver"},
        {"title": "The Night We Met",          "artist": "Lord Huron"},
        {"title": "All I Want",                "artist": "Kodaline"},
    ],
}


# List of valid categories
CATEGORIES = list(MOCK_PLAYLISTS.keys())

def classify_vibe(vibe_text: str) -> str:
    prompt = f"""
        You are an autonomous classification engine.
        Your task is to assign the user's “vibe” to exactly one of these categories:
        {', '.join(CATEGORIES)}

        Only output exactly the category name—no quotes, no extra text or explanation.

        User input:
        '{vibe_text}'
        """
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a classifier for music vibes."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
        max_tokens=10,
    )
    category = response.choices[0].message.content.strip().lower()
    return category if category in MOCK_PLAYLISTS else "chill"

def suggest_playlist(vibe_text: str):
    category = classify_vibe(vibe_text)
    return MOCK_PLAYLISTS.get(category, MOCK_PLAYLISTS["chill"])
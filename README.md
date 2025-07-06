# VibeDJ

VibeDJ is a simple demo app that takes a user’s “vibe” (e.g. “chill evening”, “angry breakup”), uses OpenAI to generate a short, catchy vibe summary, and classifies the input into one of several predefined mood categories. It then returns a mock playlist of song suggestions matching that mood.

## Features

- **POST /vibe** endpoint: accepts JSON `{ "vibe": "<your text here>" }`
- **AI Summary**: generates a brief description of the mood
- **Mood Classification**: GPT model assigns the input to one of these categories: chill, angry, run, happy, focus, party, sad
- **Mock Playlist**: returns five example tracks per category

## Installation

1. Clone the repository and navigate into it:
   ```bash
    git clone https://github.com/PontusDejoung/VibeDJ.git
    cd vibedj
    ```
2. Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a .env file in the project root with your OpenAI key:
    ```bash
    OPENAI_API_KEY=sk-...
    ```
## Running the App 
    ```bash
    uvicorn app.main:app --reload --port 8000
    ```
## Usage
# Send a POST request to /vibe:
    ```bash
    curl -X POST http://127.0.0.1:8000/vibe \
        -H "Content-Type: application/json" \
        -d '{"vibe":"chill evening"}'
    ```
# Example Response
{
  "vibe_summary": "Smooth Sunset: soft guitar chords and mellow beats for a relaxed evening.",
  "songs": [
    { "title": "Sunset Lover", "artist": "Petit Biscuit" },
    { "title": "Weightless", "artist": "Marconi Union" },
    { "title": "River Flows in You", "artist": "Yiruma" },
    { "title": "Night Owl", "artist": "Galimatias" },
    { "title": "Lost in Thoughts", "artist": "Honesty" }
  ]
}

## Project Structure
vibedj/
├── .gitignore
├── README.md
├── requirements.txt
├── env/           # optional folder for .env
│   └── .env
└── app/
    ├── main.py        # Application entrypoint
    ├── suggester.py   # Mood classification and mock playlists
    ├── test_app.py    # Standalone smoke-test script for /vibe endpoint
    └── vibes.py       # OpenAI-based vibe summarization


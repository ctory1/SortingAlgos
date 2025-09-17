Here’s the quickest way to run and test the Live Voice Translator with what’s in your repo.

Prereqs

Node.js 18+ and npm
Python 3 available as python on PATH
For default provider “googletrans”: pip install googletrans==4.0.0rc1
Use Chrome (best Web Speech API support) and allow microphone access
Option A: Dev Mode (recommended)

Start API server
cd server
npm install
Optional: set provider (see Provider Setup below)
npm start (serves API on http://127.0.0.1:3001)
Start Vite dev server
cd app
npm install
npm run dev (serves UI on http://127.0.0.1:5173)
Test the page
Open http://127.0.0.1:5173/live-translation.html
Click “Start Mic”, speak Spanish, see English translation update
Option B: Single Port (build + serve via API)

Build the frontend
cd app
npm install
npm run build (outputs to app/dist)
Start API server (serves the built UI too)
cd server
npm install
Optional: set provider (see below)
npm start
Test the page
Open http://127.0.0.1:3001/live-translation.html
Provider Setup

Default (no env vars): TRANSLATE_PROVIDER=googletrans uses local Python, calls SpanishTranslator_MX.py. Requires googletrans==4.0.0rc1.
PowerShell example: $env:TRANSLATE_PROVIDER='googletrans'; $env:PYTHON_BIN='python'; npm start
Google Cloud: set TRANSLATE_PROVIDER=google and GOOGLE_API_KEY (charges apply)
$env:TRANSLATE_PROVIDER='google'; $env:GOOGLE_API_KEY='YOUR_KEY'; npm start
OpenAI: set TRANSLATE_PROVIDER=openai and OPENAI_API_KEY
$env:TRANSLATE_PROVIDER='openai'; $env:OPENAI_API_KEY='sk-...'; npm start
Notes

Voice recognition is browser‑side (Web Speech API). No server SpeechRecognition needed.
If you browse via a LAN IP (not 127.0.0.1/localhost), Chrome may block mic on HTTP. Either use localhost or enable the flag shown in the UI tip.
The voice component calls /api/translate (server path: server/index.js). It does not use the MX/NI endpoints.
Do you want me to update the zip to include the minimal run scaffolding too (app/package.json, server/package.json, and the Python translator scripts) so it runs standalone outside the repo?

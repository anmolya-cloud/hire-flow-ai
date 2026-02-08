import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_llama(prompt: str):
    payload = {
        "model": "phi3",
        "prompt": prompt,
        "stream": False

    }
    r = requests.post(OLLAMA_URL, json=payload, timeout=120)
    return r.json()["response"]
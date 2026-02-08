from fastapi import FastAPI
from app.ollama_client import ask_llama

app = FastAPI()

@app.get("/test-llm")
def test_llm():
    return {"response": ask_llama("Say hello in one line")}
@app.get("/")
def health():
    return {"status": "AI-TESTCO backend running"}
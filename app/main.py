from fastapi import FastAPI
from app.ollama_client import ask_llama
from app.resume_parser import parse_resume
from app.jd_matcher import match_resume_to_jd
from pydantic import BaseModel

app = FastAPI()


class ResumeIn(BaseModel):
    text: str


class JDIn(BaseModel):
    resume: dict
    jd: str



@app.post("/parse-resume")
def parse_resume_api(data: ResumeIn):
    return {"parsed": parse_resume(data.text)}


@app.post("/match-jd")
def match_jd_api(data: JDIn):
    return match_resume_to_jd(data.resume, data.jd)



@app.get("/test-llm")
def test_llm():
    return {"response": ask_llama("Say hello in one line")}

@app.get("/")
def health():
    return {"status": "AI-TESTCO backend running"}
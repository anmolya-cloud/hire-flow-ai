from fastapi import FastAPI, UploadFile, File
from app.ollama_client import ask_llama
from app.resume_parser import parse_resume
from app.jd_matcher import match_resume_to_jd
from pydantic import BaseModel
from app.file_extractors import extract_text_from_pdf, extract_text_from_docx, extract_text_from_image
from app.text_cleaner import clean_text


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

@app.post("/upload-resume")
def upload_resume(file: UploadFile = File(...)):
    file_bytes = file.file.read()
    text = ""

    if file.content_type == "application/pdf":
        text = extract_text_from_pdf(file_bytes)
    elif file.content_type in [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/msword"
    ]:
        text = extract_text_from_docx(file_bytes)
    elif file.content_type.startswith("image/"):
        text = extract_text_from_image(file_bytes)
    else:
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "message": "Unsupported file type for now"
        }

    cleaned_text = clean_text(text)
    return {"text": cleaned_text[:5000]}  # preview
import json
import re
from app.ollama_client import ask_llama

def match_resume_to_jd(resume_json: dict, jd_text: str):
    prompt = f"""
You are an ATS system.

Resume:
{resume_json}

Job Description:
{jd_text}

Return ONLY raw JSON with:
match_score (number)
strengths (array)
gaps (array)
"""
    raw = ask_llama(prompt)
    raw = raw.replace("```json", "").replace("```", "").strip()

    match = re.search(r"\{[\s\S]*\}", raw)
    if not match:
        return {"error": "No JSON", "raw": raw}

    try:
        return json.loads(match.group())
    except Exception as e:
        return {"error": "Parse failed", "reason": str(e), "raw": raw}

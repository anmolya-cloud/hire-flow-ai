import json
import re
from app.ollama_client import ask_llama

def parse_resume(text: str):
    prompt = f"""
Extract structured JSON from this resume text.

Return ONLY raw JSON.
No markdown, no comments, no trailing commas.

Keys:
skills (array)
experience (array)
education (array)

Resume:
{text}
"""
    raw = ask_llama(prompt)

    # clean markdown
    raw = raw.replace("```json", "").replace("```", "").strip()

    # extract first JSON block safely
    match = re.search(r"\{[\s\S]*\}", raw)
    if not match:
        return {"error": "No JSON returned", "raw": raw}

    try:
        return json.loads(match.group())
    except Exception as e:
        return {
            "error": "JSON parse failed",
            "reason": str(e),
            "raw": match.group()
        }

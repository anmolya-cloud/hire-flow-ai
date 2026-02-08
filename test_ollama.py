import requests

url = "http://localhost:11434/api/generate"
prompt = """
Extract skills only.

Return JSON ONLY. No explanation.

Format:
{
  "skills": [
    {
      "name": "",
      "category": "technical or soft"
    }
  ]
}

Text:
Python developer with Django, AWS, and leadership experience
"""
payload = {
    "model": "phi3",
    "prompt": prompt,
    "stream": False,
    "options": {
        "num_predict": 150
    }
}

response = requests.post(url, json=payload)

print("MODEL RESPONSE:")
print(response.json()["response"])
import re

def clean_text(text: str) -> str:
    # Fix only letters separated by spaces (single letters)
    # Matches sequences like: A N M O L → ANMOL
    text = re.sub(r'\b(?:\w\s){1,}\w\b', lambda m: m.group(0).replace(' ', ''), text)

    # Fix broken hyphen spacing
    text = re.sub(r'\s*-\s*', '-', text)

    # Normalize multiple spaces and newlines
    text = re.sub(r'\n{2,}', '\n', text)
    text = re.sub(r' {2,}', ' ', text)

    # Add space after punctuation if missing
    text = re.sub(r'([,.:;])([A-Za-z])', r'\1 \2', text)

    return text.strip()


from pytesseract import image_to_string
from PIL import Image
from pdf2image import convert_from_bytes
from io import BytesIO
from docx import Document
from pypdf import PdfReader
import pytesseract

def extract_text_from_pdf(file_bytes: bytes) -> str:
    try:
        reader = PdfReader(BytesIO(file_bytes))
        text = [page.extract_text() for page in reader.pages if page.extract_text()]
        return "\n".join(text) if text else ocr_pdf(file_bytes)
    except:
        return ocr_pdf(file_bytes)
    
def ocr_pdf(file_bytes: bytes) -> str:
    try: 
        images = convert_from_bytes(file_bytes)
        text = []
        for img in images:
            text.append(pytesseract.image_to_string(img))
        return "\n".join(text)
    except:
        return "Unable to extract text from PDF"
    
def extract_text_from_docx(file_bytes: bytes) -> str:
    try:
        doc = Document(BytesIO(file_bytes))
        text = [para.text for para in doc.paragraphs if para.text]
        return "\n".join(text)
    except:
        return "unable to extract text from Docx"

def extract_text_from_image(file_bytes: bytes) -> str:
    try:
        img = Image.open(BytesIO(file_bytes))
        return pytesseract.image_to_string(img)
    except:
        return "Unable to extract text from image"
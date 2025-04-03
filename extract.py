import fitz
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        blocks = page.get_text("blocks")
        text += "\n".join([block[4] for block in blocks]) + "\n"
    return text.strip()

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\d+\.\s', '', text)
    text = re.sub(r'[^\w\s.,;\'"-]', '', text)
    return text.strip()

pdf_path = "02072017173241MCR final pdf updated as on 08122016.pdf"
extracted_text = extract_text_from_pdf(pdf_path)

cleaned_text = clean_text(extracted_text)
print(cleaned_text[770:2500])

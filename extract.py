import fitz
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        blocks = page.get_text("blocks")
        text += "\n".join([block[4] for block in blocks]) + "\n"
    return text.strip()

def clean_and_split_text(text):
    text = re.sub(r'\s+', ' ', text)  # Normalize spaces
    text = re.sub(r'[^\w\s.,;\'"-]', '', text)  # Remove unwanted characters

    # Splitting based on numbered sections (e.g., "1. Title", "2. Definitions")
    sections = re.split(r'(\d+\.\s[A-Z][^\n]*)', text)  # Keep headers in the split

    structured_data = {}
    current_section = "INTRODUCTION"  # Default name for pre-section text

    for i in range(1, len(sections), 2):  # Process sections in pairs
        title = sections[i].strip()
        content = sections[i + 1].strip() if i + 1 < len(sections) else ""
        structured_data[title] = content

    return structured_data

pdf_path = "02072017173241MCR final pdf updated as on 08122016.pdf"
extracted_text = extract_text_from_pdf(pdf_path)

split_text = clean_and_split_text(extracted_text)

# Print a sample section
for title, content in list(split_text.items())[:5]:  # Print first 5 sections
    print(f"\nTITLE: {title}\nCONTENT: {content[:500]}...\n")

import pdfplumber
import pytesseract
from pdf2image import convert_from_path
import os

def extract_text_from_pdf(pdf_path):
    """
    Extrai texto de um PDF usando pdfplumber.
    Se o PDF for escaneado (sem texto nativo), usa OCR via pytesseract.
    """
    text = ""
    try:
        # Tenta extrair usando pdfplumber (bom para PDFs nativos)
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        
        # Se não encontrou texto, tenta OCR
        if not text.strip():
            print(f"[{os.path.basename(pdf_path)}] Nenhum texto nativo encontrado. Tentando OCR (Tesseract)...")
            images = convert_from_path(pdf_path)
            for img in images:
                text += pytesseract.image_to_string(img, lang="por") + "\n"
    except Exception as e:
        print(f"Erro ao processar {pdf_path}: {e}")
        
    return text

import PyPDF2
from docx import Document


def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_text_from_docx(file):
    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_text(file):
    if file.name.lower().endswith(".pdf"):
        return extract_text_from_pdf(file)

    elif file.name.lower().endswith(".docx"):
        return extract_text_from_docx(file)

    else:
        return "Unsupported file format."
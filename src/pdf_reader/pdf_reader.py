import pdfplumber as pdfp

def extract_text_from_pdf(pdf_file):
    text=""

    with pdfp.open(pdf_file) as pdf:
        for pages in pdf.pages:
            page_text = pages.extract_text() + '\n'

            if page_text is not None:
                    text += page_text + "\n"
    return text
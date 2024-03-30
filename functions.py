from PyPDF2 import PdfReader

def read_pdf_resume(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

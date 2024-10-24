import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        content = ''
        for i in range(num_pages):
            page = reader.pages[i]
            content += page.extract_text()
        return content


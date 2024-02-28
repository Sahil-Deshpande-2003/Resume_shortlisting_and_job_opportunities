import PyPDF2
import re
def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text
# not working
def remove_extra_spaces(text):
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Remove unnecessary spaces after specific characters like ':', ',', etc.
    text = re.sub(r'\s*([:;,])\s*', r'\1 ', text)
    return text.strip()  
def parse_resume(text):
    # Dummy parsing logic for demonstration
    # name_pattern = r"Name: (.+)"
    email_pattern = r"Email  : (.+)"
    # print(f"email_pattern = {email_pattern}")
    phone_pattern = r"Mobile  : (.+)"
    # print(f"phone_pattern = {phone_pattern}")
    education_pattern = r"College : (.+)"
    # experience_pattern = r"Experience: (.+)"
    
    # name_match = re.search(name_pattern, text)
    email_match = re.search(email_pattern, text)
    # print(f"email_match = {email_match}")
    phone_match = re.search(phone_pattern, text)
    # print(f"phone_match = {phone_match}")
    education_match = re.search(education_pattern, text)
    # print(f"education_match = {education_match}")
    # experience_match = re.search(experience_pattern, text)
    
    # name = name_match.group(1) if name_match else ""
    email = email_match.group(1) if email_match else ""
    # print(f"email = {email}")
    phone = phone_match.group(1) if phone_match else ""
    # print(f"phone = {phone}")
    education = education_match.group(1) if education_match else ""
    # print(f"education = {education}")
    # experience = experience_match.group(1) if experience_match else ""
    
    return  email, phone, education


def write_to_csv(data, csv_file):
    import csv
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "Phone", "Education"])
        writer.writerow(data)

if __name__ == "__main__":
    pdf_file = "Resume_Sahil_Deshpande.pdf"  # Change this to your PDF file path
    csv_file = "resume_info.csv"  # Change this to your desired CSV file path
    
    text = extract_text_from_pdf(pdf_file)
    # print(text)
    # print("***************************")
    # text = remove_extra_spaces(text)
    print(text)
    email, phone, education = parse_resume(text)
    data = [ email, phone, education]
    write_to_csv(data, csv_file)


import import_nlp
import pandas as pd 
import Extract_Text_from_pdf
import re
from nltk.corpus import stopwords
import skill_arr
import Job_Description_matrix


text = Extract_Text_from_pdf.text
nlp = import_nlp.nlp


extracted_text= {}

def get_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

email = get_email_addresses(text)


extracted_text["E-Mail"] = email

def get_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', num) for num in phone_numbers] 

phone_number= get_phone_numbers(text)


extracted_text["Phone Number"] = phone_number




def extract_skills(resume_text):

    tokens = resume_text.split('Technical Proficiency')[0].split()
    skillset = []


    for token in tokens:
    
        for skill in skill_arr.skill_arr:
            if token.lower() == skill.lower():
                skillset.append(token)
                break 
    
    pattern = '|'.join(map(re.escape, skill_arr.skill_arr))
    regex = re.compile(pattern, re.IGNORECASE)   
    if "Technical Proficiency" in resume_text:
        remaining_text = resume_text.split('Technical Proficiency')[1]
        remaining_tokens = [token.strip() for token in remaining_text.split(',')]
        
        for token in remaining_tokens:
            if regex.match(token):
                print(f"Matched token = {token}")
                skillset.append(token)
           

    return skillset


skills = []

skills = extract_skills(text)

nlp_text = nlp(text)
extracted_text["Skills"] = skills

STOPWORDS = set(stopwords.words('english'))

EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S', 
            'ME', 'M.E', 'M.E.', 'MS', 'M.S', 
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH', 
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
        ]

def extract_education(resume_text):
    nlp_text = nlp(resume_text)


    nlp_text = [sent.text.strip() for sent in nlp_text.sents] 

    edu = {}

    for index, text in enumerate(nlp_text):
       
        for tex in text.split():

            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in EDUCATION and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]

    education = []
    for key in edu.keys():
        year = re.search(re.compile(r'(((20|19)(\d{2})))'), edu[key])
        if year:
            education.append((key, ''.join(year[0]))) 
        else:
            education.append(key)
    return education


education = extract_education(text)

extracted_text["Qualification"] = education 



def format_resume_text(extracted_text):
    resume_text = ""

    if 'Name' in extracted_text:
        resume_text += f"{extracted_text['Name']}\n"

    if 'E-Mail' in extracted_text:
        resume_text += f"Email: {', '.join(extracted_text['E-Mail'])}\n"

    if 'Phone Number' in extracted_text:
        resume_text += f"Phone: {', '.join(extracted_text['Phone Number'])}\n"

    if 'Skills' in extracted_text:
        resume_text += f"\nSkills: {', '.join(extracted_text['Skills'])}\n"

    if 'Qualification' in extracted_text:
        qualifications = extracted_text['Qualification']
        if isinstance(qualifications, list):
            for qualification in qualifications:
                if isinstance(qualification, tuple):
                    resume_text += f"{qualification[0]} {qualification[1]}\n"
                else:
                    resume_text += f"{qualification}\n"
        else:
            resume_text += f"{qualifications}\n"

    return resume_text


resume_text = format_resume_text(extracted_text)


tfidf_matrix_resume = Job_Description_matrix.vect.transform([resume_text])
tfidf_matrix_resume  = tfidf_matrix_resume
tfidf_df = pd.DataFrame(tfidf_matrix_resume.toarray(), columns=Job_Description_matrix.vect.get_feature_names_out())

tfidf_df_transposed = tfidf_df.T

tfidf_df_transposed.to_csv('tfidf_matrix_transposed_resume.csv')
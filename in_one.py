import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from tika import parser
file = r'Resume_Sahil_Deshpande.pdf'
file_data = parser.from_file(file)
text = file_data['content']
# print(text)
import warnings

# Suppress CuPy CUDA path warning
warnings.filterwarnings("ignore", message="CUDA path could not be detected.", category=UserWarning)

# Suppress PyTorch and transformers warnings
warnings.filterwarnings("ignore", category=UserWarning, module="transformers")
warnings.filterwarnings("ignore", category=UserWarning, module="torch")


#E-MAIL
import re
def get_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)
extracted_text= {}
email = get_email_addresses(text)
print(email)

extracted_text["E-Mail"] = email

def get_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', num) for num in phone_numbers]

phone_number= get_phone_numbers(text)
print(phone_number)

extracted_text["Phone Number"] = phone_number



#Name
import spacy
from spacy.matcher import Matcher

# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# initialize matcher with a vocab
matcher = Matcher(nlp.vocab)

# def extract_name(resume_text):
#     nlp_text = nlp(resume_text)
    
#     # First name and Last name are always Proper Nouns
#     pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    
#     matcher.add('NAME', [pattern], on_match = None)
    
#     matches = matcher(nlp_text)
    
#     for match_id, start, end in matches:
#         span = nlp_text[start:end]
#         return span.text
    
    
# name = extract_name(text)
# print(name)
# extracted_text["Name"] = name




import spacy

# load pre-trained model
nlp = spacy.load('en_core_web_sm')


def extract_skills(resume_text):
    print(resume_text)
    nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    
    skills = ["machine learning",
             "deep learning",
             "nlp",
             "natural language processing",
             "mysql",
             "sql",
             "django",
             "computer vision",
              "tensorflow",
             "opencv",
             "mongodb",
             "artificial intelligence",
             "ai",
             "flask",
             "robotics",
             "data structures",
             "python",
             "c++",
             "matlab",
             "css",
             "html",
             "github",
             "php"]
    
    skillset = []
    
    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
    
    # check for bi-grams and tri-grams (example: machine learning)
    for token in nlp_text.noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)
    
    return [i.capitalize() for i in set([i.lower() for i in skillset])]

skills = []
skills = extract_skills(text)

extracted_text["Skills"] = skills
print(skills)



import re
import spacy
from nltk.corpus import stopwords

# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# Grad all general stop words
STOPWORDS = set(stopwords.words('english'))

# Education Degrees
EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S', 
            'ME', 'M.E', 'M.E.', 'MS', 'M.S', 
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH', 
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
        ]

def extract_education(resume_text):
    nlp_text = nlp(resume_text)

    # Sentence Tokenizer
    nlp_text = [sent.text.strip() for sent in nlp_text.sents]

    edu = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            # Replace all special symbols
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
print(education)
extracted_text["Qualification"] = education 




# import re
# sub_patterns = ['[A-Z][a-z]* University','[A-Z][a-z]* Educational Institute',
#                 'University of [A-Z][a-z]*',
#                 'Ecole [A-Z][a-z]*']
# pattern = '({})'.format('|'.join(sub_patterns))
# matches = re.findall(pattern, text)

# extracted_text["Institutes"] = matches
# print(matches)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Hardcoded job descriptions
job_descriptions = [
    "We are looking for a Python Developer with experience in Django and Flask frameworks.",
    "We are seeking a Data Scientist proficient in machine learning and deep learning techniques.",
    "Join our team as a Frontend Developer specializing in HTML, CSS, and JavaScript.",
    "We have an opening for a Software Engineer experienced in C++ and Python programming languages.",
    "An exciting opportunity for a Computer Vision Engineer with expertise in OpenCV and TensorFlow.",
    "Looking for an AI Researcher with knowledge of natural language processing and artificial intelligence.",
    "Join our robotics team as a Robotics Engineer with hands-on experience in robotics frameworks.",
    "We are hiring a MySQL Database Administrator with expertise in managing large databases.",
    "An opportunity for a Web Developer skilled in PHP, MySQL, and JavaScript.",
    "Seeking a Software Tester with experience in manual and automated testing."
]

# Example resume text (replace with the extracted resume text)
# resume_text = """
# Sahil Deshpande
# Email: sahildeshpandde@gmail.com
# Phone: 8799979808

# Skills: Python, Django, HTML, CSS, C++, Data structures

# Qualifications: BTech 2025
# """

# Preprocess job descriptions and resume
# (Tokenization, stop word removal, etc. - you can add more preprocessing steps as needed)

# Compute TF-IDF vectors

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

# Generate resume text from extracted_text
resume_text = format_resume_text(extracted_text)

print(resume_text)


# extracted_text_str = ' '.join([str(value) for value in extracted_text.values()])
# print(extracted_text_str)
vectorizer = TfidfVectorizer()
tfidf_matrix_job = vectorizer.fit_transform(job_descriptions)
tfidf_matrix_resume = vectorizer.transform([resume_text])

# Calculate cosine similarity
similarity_scores = cosine_similarity(tfidf_matrix_resume, tfidf_matrix_job)

# Rank job opportunities based on similarity scores
ranked_jobs = sorted(
    zip(range(len(job_descriptions)), similarity_scores[0]),
    key=lambda x: x[1],
    reverse=True
)

# Print the ranked list of job opportunities
print("Ranked Job Opportunities:")
for idx, score in ranked_jobs:
    print(f"{job_descriptions[idx]}      :          Similarity Score = {score:.2f}\n")

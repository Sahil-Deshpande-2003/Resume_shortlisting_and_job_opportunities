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
    r = re.compile(r'[\w\.-]+@[\w\.-]+') # [\w\.-]+: This part matches one or more word characters (letters, digits, or underscores), dots, or hyphens before the "@" symbol. and [\w\.-]+: This matches one or more word characters, dots, or hyphens after the "@" symbol.
    return r.findall(string)
extracted_text= {}
email = get_email_addresses(text)
print(email)

extracted_text["E-Mail"] = email

def get_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})') #I think last one is only for 7 digits
    
    # r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}')
    '''
    So, this regular expression pattern matches common formats of phone numbers, such as "123-456-7890", "(123) 456-7890", or "1234567890".
1st 123-456-7890
    \d{3}: This matches exactly three digits.
    [-\.\s]??: This matches optional occurrences of hyphens, dots, or whitespace characters. The ?? makes it non-greedy.
    \d{3}: This matches exactly three digits.
    [-\.\s]??: This again matches optional occurrences of hyphens, dots, or whitespace characters.
    \d{4}: This matches exactly four digits.
    |: This is the alternation operator, allowing different patterns to match.
2nd (123) 456-7890
    \(\d{3}\)\s*: This matches an optional set of parentheses surrounding three digits, followed by optional whitespace characters.
    \d{3}: This matches exactly three digits.
    [-\.\s]??: This matches optional occurrences of hyphens, dots, or whitespace characters.
    \d{4}: This matches exactly four digits.
    \d{3}[-\.\s]??\d{4}: This matches a pattern of three digits followed by optional hyphens, dots, or whitespace characters, and then followed by four digits.
    '''
    phone_numbers = r.findall(string) # to find all matches in the input string 
    return [re.sub(r'\D', '', num) for num in phone_numbers] # : This line returns a list comprehension that iterates over each phone number in phone_numbers. For each phone number, it uses re.sub() to remove all non-digit characters (\D) and returns the cleaned-up version of each phone number

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

def matches_skill(token, skill):
    # Compile a regex pattern to match variations of the skill (e.g., "machine learning" -> "machine[ -]learning")
    pattern = re.compile(r'\b' + re.escape(skill) + r'\b', re.IGNORECASE)
    return re.search(pattern, token)

nlp = spacy.load('en_core_web_sm')
# def extract_skills(resume_text):
#     print(resume_text)
#     nlp_text = nlp(resume_text)

#     # removing stop words and implementing word tokenization
#     tokens = [token.text for token in nlp_text if not token.is_stop]
    
#     skills = ["machine learning",
#              "deep learning",
#              "nlp",
#              "natural language processing",
#              "mysql",
#              "sql",
#              "django",
#              "computer vision",
#               "tensorflow",
#              "opencv",
#              "mongodb",
#              "artificial intelligence",
#              "ai",
#              "flask",
#              "robotics",
#              "data structures",
#              "python",
#              "c++",
#              "matlab",
#              "css",
#              "html",
#              "github",
#              "php"]
    
#     skillset = []
    
#     # check for one-grams (example: python)
#     for token in tokens:
#         for skill in skills:
#             if matches_skill(token.lower(), skill.lower()):
#                 skillset.append(token)
#                 # break  # Move to the next token if a match is found

#     # Check for bi-grams and tri-grams
#     for token in nlp_text.noun_chunks:
#         token = token.text.lower().strip()
#         for skill in skills:
#             if matches_skill(token, skill):
#                 skillset.append(token)
    
#     return [i.capitalize() for i in set([i.lower() for i in skillset])]

def extract_skills(resume_text):
    print(resume_text)
    nlp_text = nlp(resume_text) # It uses SpaCy's natural language processing capabilities to tokenize the input text (nlp_text = nlp(resume_text)).

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop] # It removes stop words from the tokenized text. Stop words are common words like "is", "and", "the", etc., that typically do not carry significant meaning in text analysis (if not token.is_stop).
# The resulting tokens are stored in the tokens list.
    
    
    skills = [
"machine learning",
"deep learning",
"natural language processing",
"mysql",
"sql",
"django",
"computer vision",
"tensorflow",
"opencv",
"mongodb",
"artificial_intelligence",
"flask",
"robotics",
"data structures",
"python",
"c++",
"matlab",
"css",
"html",
"gitHub",
"php",
"java",
"javascript",
"node",
"react",
"angularjs",
"vue",
"typescript",
"shell scripting",
"linux administration",
"network security",
"cybersecurity",
"devops",
"docker",
"kubernetes",
"azure",
"golang",
"ruby",
"unity",
"mobile app development",
"ruby",
"swift",
"kotlin",
"typeScript",
"rust",
"perl",
"objective-c",
"scala",
"r",
"bash" ,
"powershell",
"lua",
"dart"]
    
    skillset = []
    
    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
    
    # check for bi-grams and tri-grams (example: machine learning)
    '''
    for token in nlp_text.noun_chunks:: This line iterates over the noun chunks identified in the resume text by SpaCy's natural language processing capabilities. Noun chunks are phrases containing a noun and the words describing the noun. For example, in the sentence "The quick brown fox jumps over the lazy dog," noun chunks would include "The quick brown fox" and "the lazy dog."

token = token.text.lower().strip(): Within the loop, for each noun chunk identified, this line retrieves the text of the noun chunk, converts it to lowercase, and removes any leading or trailing whitespace. This ensures consistency in comparison since the skills in the skills list are also in lowercase.
    '''
    for token in nlp_text.noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)
    
    return [i.capitalize() for i in set([i.lower() for i in skillset])]

skills = []
skills = extract_skills(text)

extracted_text["Skills"] = skills
print(f"skills = {skills}")



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
    nlp_text = [sent.text.strip() for sent in nlp_text.sents] # Tokenizes the text into sentences using SpaCy's sentence tokenizer (nlp_text.sents) and stores them as a list of strings.It means breaking down the text into individual sentences.

    edu = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        '''
        Splits each sentence into words and checks if any word matches an entry in the EDUCATION list.
If a match is found, it removes any special symbols from the word and checks if it's not in the set of stopwords. If so, it adds the degree as a key in the edu dictionary with its associated text.
        '''
        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in EDUCATION and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]

    education = []
    for key in edu.keys():
        year = re.search(re.compile(r'(((20|19)(\d{2})))'), edu[key]) # The regular expression re.compile(r'(((20|19)(\d{2})))') searches for a pattern in the text that matches a year in the range 1900-2099 (e.g., 20xx or 19xx).re.search() searches for this pattern within the text associated with the current degree (edu[key]).
        if year:
            education.append((key, ''.join(year[0]))) # year[0] represents the matched year
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
vectorizer = TfidfVectorizer() # vectorizer = TfidfVectorizer(): This line creates an instance of the TfidfVectorizer class. This class is used to convert a collection of raw documents into a matrix of TF-IDF features.
tfidf_matrix_job = vectorizer.fit_transform(job_descriptions) # The fit_transform method learns the vocabulary from the job descriptions and converts it into a matrix of TF-IDF features.
tfidf_matrix_resume = vectorizer.transform([resume_text])

# Calculate cosine similarity
similarity_scores = cosine_similarity(tfidf_matrix_resume, tfidf_matrix_job) # Cosine similarity measures the cosine of the angle between two vectors and is  used to measure the similarity between two documents represented as vectors.

'''
zip(range(len(job_descriptions)), similarity_scores[0]):

This part zips together the indices of the job descriptions with their corresponding similarity scores to the resume text.
range(len(job_descriptions)) generates a sequence of numbers from 0 to len(job_descriptions) - 1. This represents the indices of the job descriptions.
similarity_scores[0] retrieves the similarity scores of the resume text with each job description. Since similarity_scores is a matrix, similarity_scores[0] retrieves the similarity scores of the first row, which corresponds to the resume text.
'''
# Rank job opportunities based on similarity scores
ranked_jobs = sorted(
    
    zip(range(len(job_descriptions)), similarity_scores[0]), # This part zips together the indices of the job descriptions with their corresponding similarity scores to the resume text.
    key=lambda x: x[1],
    reverse=True
)

# Print the ranked list of job opportunities
print("Ranked Job Opportunities:")
for idx, score in ranked_jobs:
    print(f"{job_descriptions[idx]}      :          Similarity Score = {score:.2f}\n") #  formats the similarity score to display only two decimal places.

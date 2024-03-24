import spacy
import csv
import preprocess_text
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from tika import parser
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
file = r'Resume_Sahil_Deshpande_test.pdf'
file_data = parser.from_file(file)
text = file_data['content']
import warnings
import re
import spacy
from nltk.corpus import stopwords
warnings.filterwarnings("ignore", message="CUDA path could not be detected.", category=UserWarning)
warnings.filterwarnings("ignore", category=UserWarning, module="transformers")
warnings.filterwarnings("ignore", category=UserWarning, module="torch")
import skill_arr
import job_descriptions


# import re
# sub_patterns = ['[A-Z][a-z]* University','[A-Z][a-z]* Educational Institute',
#                 'University of [A-Z][a-z]*',
#                 'Ecole [A-Z][a-z]*']
# pattern = '({})'.format('|'.join(sub_patterns))
# matches = re.findall(pattern, text)

# extracted_text["Institutes"] = matches
# ##print(matches)


# initialize matcher with a vocab


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
# ##print(name)
# extracted_text["Name"] = name


# def extract_skills(resume_text):
#     ##print(resume_text)
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


#E-MAIL
extracted_text= {}

def get_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

email = get_email_addresses(text)
##print(f"extracted email = {email}")

extracted_text["E-Mail"] = email

def get_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', num) for num in phone_numbers] 

phone_number= get_phone_numbers(text)
##print(f"phone_number = {phone_number}")

extracted_text["Phone Number"] = phone_number



matcher = Matcher(nlp.vocab)

import re

def extract_skills(resume_text):
    # Tokenize the resume text based on commas
    tokens = resume_text.split('Technical Proficiency')[0].split()

    # Initialize an empty list to store the extracted skills
    skillset = []

    # Iterate through the tokens
    for token in tokens:
        print(f"token1 = {token}")
        # Check if the token is a valid skill
        for skill in skill_arr.skill_arr:
            if token.lower() == skill.lower():
                skillset.append(token)
                break  # Move to the next token if a match is found

    # If "Technical Proficiency" is found, split further based on commas
    
    pattern = '|'.join(map(re.escape, skill_arr.skill_arr))
    regex = re.compile(pattern, re.IGNORECASE)
    print(f"regex = {regex}")
    
    if "Technical Proficiency" in resume_text:
        remaining_text = resume_text.split('Technical Proficiency')[1]
        remaining_tokens = [token.strip() for token in remaining_text.split(',')]

        # Check if the remaining tokens match any skills
        for token in remaining_tokens:
            print(f"token2 = {token}")
            if regex.match(token):
                print(f"Matched token = {token}")
                skillset.append(token)
           

    return skillset



# def extract_skills(resume_text):
    
#     nlp_text = nlp(resume_text)
#     complete_filtered_tokens = [
#      preprocess_text.preprocess_token(token)
#      for token in nlp_text
#      if preprocess_text.is_token_allowed(token)
#  ]
    
 
#     #print("About to #print length of nlp text")
#     #print(len(complete_filtered_tokens))
#     #print("About to #print nlp text")
#     #print(complete_filtered_tokens)
#     text_df = pd.DataFrame({"text": [text]})
# # Save text to CSV
#     text_df.to_csv('text.csv', index=False)

# # Convert nlp_text to DataFrame

#     nlp_text_df = pd.DataFrame({"token": complete_filtered_tokens})
# # Save nlp_text to CSV
#     nlp_text_df.to_csv('nlp_text.csv', index=False)
#     ##print("SAB CHUP I am ##printing nlp text")
#     ##print(resume_text)
#     # tokens = [token.text for token in nlp_text if not token.is_stop] 
    
#     # Construct a regular expression pattern to match skills
#     pattern = '|'.join(map(re.escape, skill_arr.skill_arr))
#     regex = re.compile(pattern, re.IGNORECASE)
#     ##print(f"regex = {regex}")
    
#     skillset = []

#     # Extract skills using regular expression matching
#     for token in complete_filtered_tokens:
#         if (token == "machine learning"):
#             pass
#             ##print("SMELL SUCCESS 1")
#         if (token == "Vue.js"):
#             pass
#             ##print("Hitler1!")
#         if regex.match(token):
#             pass
#             ##print(f"token={token}")
#             skillset.append(token)
            
#     # for chunk in nlp_text.noun_chunks:
#     #     chunk_text = chunk.text.lower().strip()
#     #     if (chunk_text == "machine learning"):
#     #         pass
#     #         ##print("SMELL SUCCESS 1")
#     #     for skill in skill_arr.skill_arr:
#     #         if skill in chunk_text:
#     #             ##print(f"Superman skill = {skill}")
#     #             skillset.append(skill)

#     return list(set(skillset))



# def extract_skills(resume_text):
#     ##print(resume_text)
#     nlp_text = nlp(resume_text) 
#     tokens = [token.text for token in nlp_text if not token.is_stop] 
    
    
 
    
#     skillset = []
    
#     for token in tokens:
#         if (token == "Vue.js"):
#             ##print("Hitler1!")
#         if token.lower() in skill_arr.skill_arr  :
#             skillset.append(token)

#     for token in nlp_text.noun_chunks:
#         if (token == "Vue.js"):
#             ##print("Hitler2!")
#         token = token.text.lower().strip()
#         if token in skills:
#             skillset.append(token)
    
#     return [i.capitalize() for i in set([i.lower() for i in skillset])]

skills = []
#print("About to #print len of text..")
#print(len(text))
skills = extract_skills(text)
#print(f"Extracted skills = {skills}")
nlp_text = nlp(text)
extracted_text["Skills"] = skills
##print(f"extarcted skills = {skills}")

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
##print(f"extracted education = {education}")
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

print(f"extracted resume text using extracted_text = **************************\n{resume_text}")

vectorizer = TfidfVectorizer() 




def custom_tokenizer(text):
    
    tokens = re.findall(r'\b\w+\b', text.lower())
   
    # tokens = text.split()

    tokens.append("C++")
    return tokens



vect = TfidfVectorizer(tokenizer=custom_tokenizer,stop_words="english")
# vect = TfidfVectorizer(stop_words="english")

tfidf = vect.fit_transform(job_descriptions.job_descriptions)

##print("I am Death destroyer of world")
##print(vect.get_feature_names_out())

# tfidf_df = pd.DataFrame(tfidf.toarray(), columns=vect.get_feature_names_out())

# tfidf_df_transposed = tfidf_df.T

# tfidf_df_transposed.to_csv('tfidf_matrix_transposed_job_description_matrix.csv')



tfidf_matrix_resume = vect.transform([resume_text])




tfidf_df = pd.DataFrame(tfidf_matrix_resume.toarray(), columns=vect.get_feature_names_out())

tfidf_df_transposed = tfidf_df.T

tfidf_df_transposed.to_csv('tfidf_matrix_transposed_resume.csv')

# similarity_scores = cosine_similarity(tfidf_matrix_resume, tfidf_matrix_job) 
# similarity_scores = cosine_similarity(tfidf_matrix_resume, tfidf) 


# ranked_jobs = sorted(
    
#     zip(range(len(job_descriptions.job_descriptions)), similarity_scores[0]), 
#     key=lambda x: x[1],
#     reverse=True
# )


# ##print("Ranked Job Opportunities:")
# for idx, score in ranked_jobs:
#     ##print(f"{job_descriptions.job_descriptions[idx]}      :          Similarity Score = {score:.2f}\n") 
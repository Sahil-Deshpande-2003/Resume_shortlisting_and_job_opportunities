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
# #######print(matches)


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
# #######print(name)
# extracted_text["Name"] = name


# def extract_skills(resume_text):
#     #######print(resume_text)
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
#######print(f"extracted email = {email}")

extracted_text["E-Mail"] = email

def get_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', num) for num in phone_numbers] 

phone_number= get_phone_numbers(text)
#######print(f"phone_number = {phone_number}")

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
        #####print(f"token1 = {token}")
        # Check if the token is a valid skill
        for skill in skill_arr.skill_arr:
            if token.lower() == skill.lower():
                skillset.append(token)
                break  # Move to the next token if a match is found

    # If "Technical Proficiency" is found, split further based on commas
    
    pattern = '|'.join(map(re.escape, skill_arr.skill_arr))
    regex = re.compile(pattern, re.IGNORECASE)
    #####print(f"regex = {regex}")
    
    if "Technical Proficiency" in resume_text:
        remaining_text = resume_text.split('Technical Proficiency')[1]
        remaining_tokens = [token.strip() for token in remaining_text.split(',')]

        # Check if the remaining tokens match any skills
        for token in remaining_tokens:
            #####print(f"token2 = {token}")
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
    
 
#     ######print("About to ######print length of nlp text")
#     ######print(len(complete_filtered_tokens))
#     ######print("About to ######print nlp text")
#     ######print(complete_filtered_tokens)
#     text_df = pd.DataFrame({"text": [text]})
# # Save text to CSV
#     text_df.to_csv('text.csv', index=False)

# # Convert nlp_text to DataFrame

#     nlp_text_df = pd.DataFrame({"token": complete_filtered_tokens})
# # Save nlp_text to CSV
#     nlp_text_df.to_csv('nlp_text.csv', index=False)
#     #######print("SAB CHUP I am #######printing nlp text")
#     #######print(resume_text)
#     # tokens = [token.text for token in nlp_text if not token.is_stop] 
    
#     # Construct a regular expression pattern to match skills
#     pattern = '|'.join(map(re.escape, skill_arr.skill_arr))
#     regex = re.compile(pattern, re.IGNORECASE)
#     #######print(f"regex = {regex}")
    
#     skillset = []

#     # Extract skills using regular expression matching
#     for token in complete_filtered_tokens:
#         if (token == "machine learning"):
#             pass
#             #######print("SMELL SUCCESS 1")
#         if (token == "Vue.js"):
#             pass
#             #######print("Hitler1!")
#         if regex.match(token):
#             pass
#             #######print(f"token={token}")
#             skillset.append(token)
            
#     # for chunk in nlp_text.noun_chunks:
#     #     chunk_text = chunk.text.lower().strip()
#     #     if (chunk_text == "machine learning"):
#     #         pass
#     #         #######print("SMELL SUCCESS 1")
#     #     for skill in skill_arr.skill_arr:
#     #         if skill in chunk_text:
#     #             #######print(f"Superman skill = {skill}")
#     #             skillset.append(skill)

#     return list(set(skillset))



# def extract_skills(resume_text):
#     #######print(resume_text)
#     nlp_text = nlp(resume_text) 
#     tokens = [token.text for token in nlp_text if not token.is_stop] 
    
    
 
    
#     skillset = []
    
#     for token in tokens:
#         if (token == "Vue.js"):
#             #######print("Hitler1!")
#         if token.lower() in skill_arr.skill_arr  :
#             skillset.append(token)

#     for token in nlp_text.noun_chunks:
#         if (token == "Vue.js"):
#             #######print("Hitler2!")
#         token = token.text.lower().strip()
#         if token in skills:
#             skillset.append(token)
    
#     return [i.capitalize() for i in set([i.lower() for i in skillset])]

skills = []
######print("About to ######print len of text..")
######print(len(text))
skills = extract_skills(text)
######print(f"Extracted skills = {skills}")
nlp_text = nlp(text)
extracted_text["Skills"] = skills
#######print(f"extarcted skills = {skills}")

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
#######print(f"extracted education = {education}")
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

####print(f"extracted resume text using extracted_text = **************************\n{resume_text}")

vectorizer = TfidfVectorizer() 


combined_phrases = ["machine learning", "deep learning", "natural language processing","python developer","data scientist","data engineer","data analyst"]

def remove_combined_phrases(tokens):
   
    i = 0
    # ####print("####printing those tokens which remove func has received...")
    # for i in range(len(tokens)):
        # ####print(f"token = {tokens[i]}")
    # ####print("Ghar Jaa..")
    # ####print("Checking is deep learning token ... before redemption")
    # for i in range(len(tokens)):
        # if (tokens[i] == 'deep learning'):
        #     ####print("Some Hope!")
        # ####print(f"Received tokens = {tokens[i]}")
        
    while i < len(tokens):
        
        for phrase in combined_phrases:
            
            if re.fullmatch(phrase, tokens[i]):
                
                # #print(f"phrase = {phrase}")
                
                words = tokens[i].split()
                
                ####print(f"word = {words}")
                
                for word in words:
                    if word in tokens:
                        #print(f"Detective word = {word}")
                        tokens.remove(word)
        i = i+1
   
        
        
        
    # while i < len(tokens):
 
    #     for phrase in combined_phrases:
    #         # Using regex for a complete match of the phrase
    #         ####print(f"tokens[i] = {tokens[i]}")
    #         if re.fullmatch(phrase, tokens[i]):
    #             ####print(f"Full matched token = {tokens[i]}")
    #             words = tokens[i].split()
    #             # ####print(f"words = {words}")
    #             for word in words:
    #                 if word in tokens:
    #                     # ####print(f"Removed word = {word}")
    #                     tokens.remove(word)
    #                     # for i in range(len(tokens)):
    #                         # if (tokens[i] == "deep"):
    #                             # ####print("Still Trouble")

    #             i += len(words)
    #             break
    #     i+=1
 
    
    # ####print("Checking is deep learning token ... after redemption")
    # for i in range(len(tokens)):
        # if (tokens[i] == 'deep learning'):
            # ####print("Strange!")
    return tokens

def custom_tokenizer(text):
    

    
    nlp_text = nlp(text)
    complete_filtered_tokens = [
     preprocess_text.preprocess_token(token)
     for token in nlp_text
     if preprocess_text.is_token_allowed(token)
 ]
    
    # #print(f"nlp_text inside custom tokenizer = \n{nlp_text}")
    
    # #print("Over...")
    
    # #print(f"Job Desc preprocessed tokens = \n{complete_filtered_tokens}")
    
    # tokens = re.findall(r'\b\w+\b', text.lower())
    tokens = [match.lower() for token in complete_filtered_tokens for match in re.findall(r'\b\w+\b', token.lower())]
    
    temp_tokens = re.findall(r'\b\w+\b|\"[\w\s]+\"', text.lower())
    
    #####print(f"temp_tokens  =  \n{tokens}")
    
    # #####print("Over...")
   
    # tokens = text.split()

    tokens.append("C++")
    
    for i in range(len(tokens)):
        
        #print(f"wow = {tokens[i]}")
        pass
        
    

    i = 0
    while i < len(temp_tokens):
        # ####print(f"curr = {tokens[i]}")
        if i+1 < len(temp_tokens) and " ".join(temp_tokens[i:i+2]) in combined_phrases:
            #print(f"REMOVING {tokens[i]}...")
            tokens.remove(tokens[i])
            #print(f"wildcard = {temp_tokens[i:i+2]}")
            tokens.append(" ".join(temp_tokens[i:i+2]))
            i += 2
        else:
            # ####print(f"Normal entry = {temp_tokens[i]}")
            tokens.append(temp_tokens[i])
            i += 1
    
    # ####print("Fax...")
    
    # for i in range(len(tokens)):
        
    #     ####print(f"token = {tokens[i]}")
        
    # ####print("Over...")
    
    tokens  = remove_combined_phrases(tokens)
    
    
    return tokens



'''
Pehle ka

vect = TfidfVectorizer(tokenizer=custom_tokenizer,stop_words="english")
# #####print(vect)
# vect = TfidfVectorizer(tokenizer=custom_tokenizer)
# vect = TfidfVectorizer(stop_words="english")

tfidf_job_description = vect.fit_transform(job_descriptions.job_descriptions)

#####print("I am Death destroyer of world")
###print(vect.get_feature_names_out())

tfidf_df = pd.DataFrame(tfidf_job_description.toarray(), columns=vect.get_feature_names_out())

tfidf_df_transposed = tfidf_df.T

tfidf_df_transposed.to_csv('tfidf_matrix_transposed_job_description_matrix.csv')
'''



'''
Wrong Output:

C++,0.08199556295715016,0.06521938701143161,0.06580221223160536,0.06369318429091664,0.06369318429091664,0.05848469173461117,0.04631509555371133,0.06190886392025806,0.07306106684865611,0.06871516089903096,0.12597453965309421,0.09175058069807811,0.08996873424252969 for 

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
    "Seeking a Software Tester with experience in manual and automated testing.",
    "We are looking for a Rust Developer",
    "We are looking for a Git and Github Expert",
    "We are looking for a PHP,Vue,Express developer"
]
'''
# vector = TfidfVectorizer(stop_words="english")

# tp = vector.fit_transform(job_descriptions.job_descriptions)
def extract_skills(resume_text):
    # Tokenize the resume text based on commas

    
      
    nlp_text = nlp(resume_text) # 145 to 92
    complete_filtered_tokens = [
     preprocess_text.preprocess_token(token)
     for token in nlp_text
     if preprocess_text.is_token_allowed(token)
 ]
    
    pattern = '|'.join(map(re.escape, skill_arr.skill_arr))
    regex = re.compile(pattern, re.IGNORECASE)
    
    skillset = []
    
        
    token_arr_temp = []
    
    for i in range(len(complete_filtered_tokens)):
        token_arr_temp.append(complete_filtered_tokens[i])

    i = 0
    while i < len(token_arr_temp):
        # #####print(f"curr = {tokens[i]}")
        if i+1 < len(token_arr_temp) and " ".join(token_arr_temp[i:i+2]) in combined_phrases:
            # print(f"REMOVING {token_arr_temp[i]}...")
            complete_filtered_tokens.remove(token_arr_temp[i])
            # print(f"wildcard = {token_arr_temp[i:i+2]}")
            complete_filtered_tokens.append(" ".join(token_arr_temp[i:i+2]))
            i += 2
        else:
            i += 1

    # print(complete_filtered_tokens)
    
    for i in range(len(complete_filtered_tokens)):
            
            token = complete_filtered_tokens[i]
            # print(f"token = {token}")
            if regex.match(token):
                # print(f"Matched token = {token}")
                skillset.append(token)
  
        
    
    
    # Tested -> to add Machine Learning and removing Machine


    
    
    # tokens  = remove_combined_phrases(complete_filtered_tokens) # removes Learning 
    

    
    
    return skillset
        





vect = TfidfVectorizer(tokenizer=extract_skills,stop_words="english")
tfidf_job_description = vect.fit_transform(job_descriptions.job_descriptions)
tfidf_df = pd.DataFrame(tfidf_job_description.toarray(), columns=vect.get_feature_names_out())

tfidf_df_transposed = tfidf_df.T

tfidf_df_transposed.to_csv('tfidf_matrix_transposed_job_description_matrix_new.csv')

tfidf_matrix_resume = vect.transform([resume_text])
# tfidf_matrix_resume = vector.transform([resume_text])




tfidf_df = pd.DataFrame(tfidf_matrix_resume.toarray(), columns=vect.get_feature_names_out())

tfidf_df_transposed = tfidf_df.T

tfidf_df_transposed.to_csv('tfidf_matrix_transposed_resume.csv')

similarity_scores = cosine_similarity(tfidf_matrix_resume, tfidf_job_description) 



ranked_jobs = sorted(
    
    zip(range(len(job_descriptions.job_descriptions)), similarity_scores[0]), 
    key=lambda x: x[1],
    reverse=True
)


print("Ranked Job Opportunities:")
for idx, score in ranked_jobs:
    
    print(f"{job_descriptions.job_descriptions[idx]}      :          Similarity Score = {score:.2f}\n") 
    pass
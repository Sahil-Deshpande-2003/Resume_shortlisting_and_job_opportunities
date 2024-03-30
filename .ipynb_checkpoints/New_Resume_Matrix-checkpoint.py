
import import_nlp
import pandas as pd 
import Extract_Text_from_pdf
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import skill_arr
import Job_Description_matrix


text = Extract_Text_from_pdf.text
nlp = import_nlp.nlp

import gpt
extracted_text= {}





def extract_skills(resume_text):

    tokens = resume_text.split('Technical Proficiency')[0].split()

    skillset = {}

    skillset = set()


    for token in tokens:
    
        for skill in skill_arr.skill_arr:
            if token.lower() == skill.lower():
                skillset.add(token.lower())
                break 
    
 
    if "Technical Proficiency" in resume_text:
        remaining_text = resume_text.split('Technical Proficiency')[1]
    
        remaining_tokens  = gpt.two_level_tokenizing(remaining_text)

        for token in remaining_tokens:
           
            string_check = "" 
            for i in range(len(token)):

                for skill in skill_arr.skill_arr:

                    if token[i].lower() == skill.lower():
                        
                        skillset.add(token[i].lower())
                        break 

                string_check+=token[i]
                string_check+=" "
                stripped_text = string_check.strip()
                test = stripped_text.lower()
                if (test in skill_arr.skill_arr):
                    
                    skillset.add(test)
               

    return skillset





skills = extract_skills(text)



import numpy as np


all_skills = list(skills)


# matrix = np.zeros((len(skills), len(all_skills)), dtype=int)
matrix = np.zeros(( len(skill_arr.skill_arr),len(skills)), dtype=int)


for i in range(len(skill_arr.skill_arr)):

    for j in range(len(skills)):

        if (skill_arr.skill_arr[i] == skills[j]):

            matrix[i][j] = 1

skills_matrix = pd.DataFrame(matrix, columns=skills)

print(skills_matrix)

# nlp_text = nlp(text)
# extracted_text["Skills"] = skills

# STOPWORDS = set(stopwords.words('english'))








# tfidf_matrix_resume = Job_Description_matrix.vect.transform([resume_text])
# print(f"tfidf_matrix_resume = \n{tfidf_matrix_resume}")
# tfidf_df = pd.DataFrame(tfidf_matrix_resume.toarray(), columns=Job_Description_matrix.vect.get_feature_names_out())

# tfidf_df_transposed = tfidf_df.T

# tfidf_df_transposed.to_csv('tfidf_matrix_transposed_resume.csv')
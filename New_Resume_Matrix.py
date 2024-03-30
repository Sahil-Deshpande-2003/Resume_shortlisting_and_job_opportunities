import import_nlp
import pandas as pd 
import Extract_Text_from_pdf
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import skill_arr


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





skills = list(extract_skills(text))


# skills = list(skills)

# print(f"skills = {skills}")

import numpy as np


matrix = np.zeros(( len(skill_arr.skill_arr),len(skill_arr.skill_arr)), dtype=int)


# for i in range(len(skill_arr.skill_arr)):

#     for j in range(len(skills)):

     

#         if (skill_arr.skill_arr[i] == skills[j] and skills[j] == 'c++'):


#             matrix[i][j] = 1

for i in range(len(skill_arr.skill_arr)):

    for j in range(len(skill_arr.skill_arr)):

        if (i == j):

            skill = skill_arr.skill_arr[i]

            for k in range(len(skills)):

                if (skills[k] == skill):

                    matrix[i][j]  = 1


skills_matrix = pd.DataFrame(matrix, columns=skill_arr.skill_arr)


# with pd.option_context('display.max_rows',None,'display.max_columns',None):
#     print(skills_matrix)
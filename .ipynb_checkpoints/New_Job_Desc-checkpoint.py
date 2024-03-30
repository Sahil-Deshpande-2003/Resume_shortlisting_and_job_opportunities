
import skill_arr
import job_descriptions
import gpt
import checking
import pandas as pd
def extract_skills(job_desc):

  

    skillset = {}

    skillset = set()


    for element in job_desc:


        
        for subelement in element:


            list1 = []

            for i in range(len(subelement)):

                
                
                check_string = subelement[i].lower().strip()

                

                list1.append(check_string)

                temp_string = ""

                for key in range(len(list1)):
                    temp_string+=list1[key]
                    if (key!=(len(list1)-1)):
                        temp_string+=" "
                
              
                    
                if (i>0):
                    del list1[0]

                for skill in skill_arr.skill_arr:

                   

                    if (check_string == skill.lower()):
                        # print(f"check_string = {check_string}")
                        skillset.add(temp_string)
                        pass

                    if (temp_string == skill.lower()):
                         
                         
                        #  print(f"Matched skill =  {temp_string}")
                         skillset.add(temp_string)


    return skillset

# job_desc = job_descriptions.job_descriptions

skills = extract_skills(checking.tokenized_descriptions)

import numpy as np

# Get all unique skill names
all_skills = list(skills)

# Initialize a matrix filled with zeros
matrix = np.zeros((len(skills), len(all_skills)), dtype=int)

# Populate the diagonal with 1s
for i, skill_number in enumerate(skills):
    for j, skill_name in enumerate(all_skills):
        if i == j:
            matrix[i, j] = 1

# Convert the matrix to DataFrame for better visualization
skills_matrix = pd.DataFrame(matrix, columns=all_skills)

print(skills_matrix)

import skill_arr
import job_descriptions
import gpt
import checking
import pandas as pd
import numpy as np
ct = 0
def extract_skills(job_desc):

  

    skillset = {}

    skillset = set()

    skills_2D = []

    


    for element in job_desc:

       
        # print("**************")


        # print(f"element = {element}")

        


        list1 = []

        row_skill_set = {}

        row_skill_set = set()

        for i in range(len(element)):

                
                
                check_string = element[i].lower().strip()

                # print(f"check_string = {check_string}")

                

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
                        row_skill_set.add(check_string)
                        skillset.add(check_string)
                        pass

                    if (temp_string == skill.lower()):
                         
                         
                        #  print(f"Matched skill =  {temp_string}")
                         row_skill_set.add(temp_string)
                         skillset.add(temp_string)
        # print(f"rowset = {row_skill_set}")
        skills_2D.append(row_skill_set)
           
    # return skillset
    return skills_2D

skills_2D = extract_skills(checking.tokenized_descriptions)
# print(f"skills = {skills_2D}")
# print(f"len = {len(skills_2D)}")
# print(f"skills = {skills_2D}")
# print(f"ct = {ct}")

# skills = extract_skills(checking.tokenized_descriptions)

# skills = list(skills)









# matrix = np.zeros(( len(skill_arr.skill_arr),len(skill_arr.skill_arr)), dtype=int)


# for i in range(len(skill_arr.skill_arr)):

#     for j in range(len(skills)):

     

#         if (skill_arr.skill_arr[i] == skills[j] and skills[j] == 'c++'):


#             matrix[i][j] = 1

# for i in range(len(skill_arr.skill_arr)):

#     for j in range(len(skill_arr.skill_arr)):

#         if (i == j):

#             skill = skill_arr.skill_arr[i]

#             for k in range(len(skills)):

#                 if (skills[k] == skill):

#                     matrix[i][j]  = 1


# skills_matrix = pd.DataFrame(matrix, columns=skill_arr.skill_arr)


# with pd.option_context('display.max_rows',None,'display.max_columns',None):
#     print(skills_matrix)
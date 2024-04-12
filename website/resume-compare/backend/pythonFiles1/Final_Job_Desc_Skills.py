import skill_arr

import tokenizing_file_for_job_desc

def extract_skills(job_desc):

 
    skills_2D = []
    
    for element in job_desc:


        row_skill_set = []

        for i in range(len(element)):
        
            
                                
            check_string = element[i].lower().strip()

            for skill in skill_arr.skill_arr:
                    
                if (check_string == skill.lower()):
                        
                    row_skill_set.append(check_string)
                    break
                        
        
        skills_2D.append(row_skill_set)
  
    return skills_2D

skills_2D = extract_skills(tokenizing_file_for_job_desc.tokenized_descriptions)

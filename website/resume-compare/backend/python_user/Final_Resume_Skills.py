import Extract_Text_from_pdf
import skill_arr

text = Extract_Text_from_pdf.text

import tokenizing_file_for_resume

def extract_skills(resume_text):

    
    tokens = resume_text.split('Technical Proficiency')[0].split()

    skillset = []


    for token in tokens:
    
        for skill in skill_arr.skill_arr:

            if token.lower() == skill.lower():
            
                skillset.append(token.lower())

                break
    
                 
    
 
    if "Technical Proficiency" in resume_text:
        remaining_text = resume_text.split('Technical Proficiency')[1]
    
        remaining_tokens  = tokenizing_file_for_resume.two_level_tokenizing(remaining_text)

        for token in remaining_tokens:

                for skill in skill_arr.skill_arr:

                    if token.lower() == skill.lower():
                        
                        skillset.append(token.lower())
                        break 



    return skillset

skills = (extract_skills(text))

# print(f"skills = {skills}") # bas linked list wale node ko bhi node.js samaj ke node bana le raha hai and c++ ka c bhi alag se le raha hai
import tokenizing_file_for_job_desc
import pickle
import nltk
from nltk.tokenize import word_tokenize

# Deserialize (Load) the Trie from disk
with open('skill_trie.pkl', 'rb') as f:
    skill_trie = pickle.load(f)

# Function to extract skills from resume text using Trie
def extract_skills_from_resume(resume_text, trie):
    resume_text = resume_text.lower()  # Convert to lowercase for case-insensitive matching
    tokens = word_tokenize(resume_text)
    
    extracted_skills = set()
    for token in tokens:
        if trie.search(token):
            extracted_skills.add(token)
    
    return extracted_skills

def extracted_skills(job_desc):
    skills_2D = []
    for element in job_desc:
       row_skill_set = extract_skills_from_resume(element, skill_trie)
       skills_2D.append(row_skill_set)
    return skills_2D

skills_2D = extracted_skills(tokenizing_file_for_job_desc.job_description)



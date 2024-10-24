from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import Final_Job_Desc_Skills
# import Final_Resume_Skills
import job_descriptions
import skill_extraction
import Extract_Text_from_pdf
import re
import json

Resume_skills = skill_extraction.extracted_skills([Extract_Text_from_pdf.read_pdf('aman_resume')])
resume_skills_str = " ".join(Resume_skills[0])

# Convert JSON string to Python dictionary
all_job_desc_data = job_descriptions.get_job_description(resume_skills_str)

only_job_descr = []

Job_Desc_Skills_2D_array = []
job_desc_array = []
parsed_json_array = []

for i in all_job_desc_data:

    ## Replace single quotes with double quotes
    json_str = i.replace("\'", '\"')

    ## Remove problematic escape sequences
    json_str = json_str.replace('\\', '')

    parsed_json = json.loads(json_str)

    parsed_json_array.append(parsed_json)

    Job_Desc_Skills_2D_array.append(parsed_json["skills"])

# Join the sets into strings
job_descriptions_str = [" ".join(jd) for jd in Job_Desc_Skills_2D_array]

# Combine resume skills with job description skills for TF-IDF vectorization
documents = [resume_skills_str] + job_descriptions_str

# Initialize the TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words="english")

# Fit the model and transform the documents into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(documents)

# Compute the cosine similarity between the resume and all job descriptions
similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

# Get the similarity scores
similarity_scores = similarity_matrix[0]

# Get index and score tuple
similarity_scores_tuple = [(index, score) for index, score in enumerate(similarity_scores)]

# Get sorted similarity scores
sorted_similarity_scores_tuple = sorted(similarity_scores_tuple, key=lambda x: x[1], reverse=True)

# collect card data to display
card_data = []

for idx, score in sorted_similarity_scores_tuple:
    card_data.append(parsed_json_array[idx])
    # print(f"Similarity score with job description {idx + 1}: {score:.4f}")
    # print(parsed_json_array[idx])
    # print()

print(card_data)

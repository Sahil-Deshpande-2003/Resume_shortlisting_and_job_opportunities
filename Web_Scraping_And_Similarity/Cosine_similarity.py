from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import New_Job_Desc
import New_Resume_Matrix
import job_descriptions
# skills_2D = [{'flask', 'python', 'django'}, {'machine learning', 'deep learning'}]
skills_2D = New_Job_Desc.skills_2D
# print(f"len = {len(skills_2D)}")
# print(f"skills_2D = {skills_2D}")
# skills = ['rust', 'c', 'github', 'vue.js', 'linux', 'css', 'data structures', 'git', 'django', 'html', 'c++', 'php', 'flask', 'react', 'node', 'java', 'python', 'mysql', 'sqlite', 'networking', 'machine learning', 'node.js', 'javascript']
skills = New_Resume_Matrix.skills
# print(f"skills = {skills}")

skills_2D_concatenated = [' '.join(skill_set) for skill_set in skills_2D]


vect = TfidfVectorizer(stop_words="english")
tfidf_job_description = vect.fit_transform(skills)


# for i in range(len(skills_2D_concatenated)):
#     print("***********")
#     # print(f"skills_2D_concatenated[i] = {skills_2D_concatenated[i]}")
#     tfidf_matrix_resume = vect.transform([skills_2D_concatenated[i]])
#     similarity_scores = cosine_similarity(tfidf_matrix_resume, tfidf_job_description)
#     # print(f"Similarity scores for skills_2D[{i}]: {similarity_scores}")
#     average_similarity = np.mean(similarity_scores)
#     print(f"{job_descriptions.job_descriptions[i]}: {average_similarity}")


similarity_scores = []
for i in range(len(skills_2D_concatenated)):
    tfidf_matrix_resume = vect.transform([skills_2D_concatenated[i]])
    similarity_scores.append((i, np.mean(cosine_similarity(tfidf_matrix_resume, tfidf_job_description))))


sorted_job_descriptions = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

for i, similarity_score in sorted_job_descriptions:
    print("******************")
    print(f"{job_descriptions.job_descriptions[i]}: {similarity_score}")
    pass
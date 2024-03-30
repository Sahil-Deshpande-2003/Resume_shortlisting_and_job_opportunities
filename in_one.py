import job_descriptions
import Resume_matrix
import Job_Description_matrix
from sklearn.metrics.pairwise import cosine_similarity




similarity_scores = cosine_similarity(Resume_matrix.tfidf_matrix_resume, Job_Description_matrix.tfidf_job_description) 


ranked_jobs = sorted(
    
    zip(range(len(job_descriptions.job_descriptions)), similarity_scores[0]), 
    key=lambda x: x[1],
    reverse=True
)


print("Ranked Job Opportunities:")
for idx, score in ranked_jobs:
    
    print(f"{job_descriptions.job_descriptions[idx]}      :          Similarity Score = {score:.2f}\n") 
    pass
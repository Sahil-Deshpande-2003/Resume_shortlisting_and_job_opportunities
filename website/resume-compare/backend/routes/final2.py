import pdfplumber
import spacy
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
import numpy as np
# Load English language model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_resume(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

def custom_tokenizer(text):
    doc = nlp(text)
    return [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]

if __name__ == "__main__":
    # Path to the directory containing resume PDFs
    pdf_path = sys.argv[1]
    job_descriptions = []
    argument = sys.argv[2]
    job_descriptions.append(argument)

    extracted_text = extract_text_from_resume(pdf_path)


    vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")

    # Fit the vectorizer on the job descriptions
    vectorizer.fit(job_descriptions)

    # Dictionary to store candidates for each job
    all_candidates = {}

    # Iterate over each job description
    for job_desc in job_descriptions:
        candidates = []
        job_desc_tfidf = vectorizer.fit_transform([job_desc])
        if extracted_text:
            resume_tfidf = vectorizer.transform([extracted_text])
            similarity_scores = cosine_similarity(resume_tfidf, job_desc_tfidf)
            similarity_score_mean = np.mean(cosine_similarity(resume_tfidf, job_desc_tfidf))
            # candidates.append((pdf_path, similarity_scores[0][0]))
            candidates.append((pdf_path, similarity_score_mean))
        else:
            print(f"Text extraction failed for {pdf_path}. Please check the PDF file.")

        candidates.sort(key=lambda x: x[1], reverse=True)
        all_candidates[job_desc.strip()] = candidates

    # Create an array to store candidates and their scores, sorted by score in descending order
    sorted_candidates = []
    for job_desc, candidates in all_candidates.items():
        for candidate, score in candidates:
            sorted_candidates.append((job_desc, candidate, score))

    # Sort the array based on the similarity score in descending order
    sorted_candidates.sort(key=lambda x: x[2], reverse=True)

    import json


    print(json.dumps(sorted_candidates))

    # Print the sorted array
    # for job_desc, candidate, score in sorted_candidates:
    #     print(f"Job Description: {job_desc}")
    #     print(f"Candidate: {candidate}, Similarity Score: {score}\n")





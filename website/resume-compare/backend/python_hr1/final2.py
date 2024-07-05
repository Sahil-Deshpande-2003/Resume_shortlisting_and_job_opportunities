import pdfplumber
import spacy
import os
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
        print(f"Error extracting text from PDF: {e}")
        return None

def custom_tokenizer(text):
    doc = nlp(text)
    return [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]

def save_to_mongodb(data, collection):
    try:
        collection.insert_one(data)
        print(f"Successfully saved resume to MongoDB: {data['_id']}")
    except Exception as e:
        print(f"Error saving to MongoDB: {e}")

if __name__ == "__main__":
    # Path to the directory containing resume PDFs
    resume_dir = "resumes/"

    # Get the current directory of the script
    current_dir = os.path.dirname(__file__)

    # Path to the file containing job descriptions
    job_description_file = os.path.join(current_dir, "job_descriptions.txt")

    # MongoDB connection setup
    # client = MongoClient("mongodb://localhost:27017/")
    # db = client["resume_database"]
    # project_collection = db["ResumeProject"]

    # Extract text from job descriptions
    with open(job_description_file, "r") as f:
        job_descriptions = f.readlines()

    # Process job descriptions and extract words
    job_description_words = set()
    for job_desc in job_descriptions:
        doc = nlp(job_desc.lower())
        job_description_words.update([token.text.lower() for token in doc if not token.is_stop and not token.is_punct])

    # Create TF-IDF vectorizer with words from job descriptions as vocabulary
    vectorizer = TfidfVectorizer(tokenizer=custom_tokenizer, vocabulary=job_description_words, token_pattern='')

    # Dictionary to store candidates for each job
    all_candidates = {}

    # Iterate over each job description
    for job_desc in job_descriptions:
        # Initialize list to store candidates for current job
        candidates = []

        # Calculate TF-IDF vectors for current job description
        job_desc_tfidf = vectorizer.fit_transform([job_desc])

        # Iterate over each resume
        for resume_file in os.listdir(resume_dir):
            resume_path = os.path.join(resume_dir, resume_file)
            resume_text = extract_text_from_resume(resume_path)

            if resume_text:
                # Save resume text to MongoDB with a project identifier
                # resume_data = {
                    # "_id": resume_file,
                    # "project": "ResumeProject",
                    # "text": resume_text
                # }
                # save_to_mongodb(resume_data, project_collection)

                # Fit and transform resume text
                resume_tfidf = vectorizer.transform([resume_text])

                # Calculate cosine similarity between resume and current job description
                similarity_scores = cosine_similarity(resume_tfidf, job_desc_tfidf)

                # Add candidate to list with similarity score
                candidates.append((resume_file, similarity_scores[0][0]))

            else:
                print(f"Text extraction failed for {resume_file}. Please check the PDF file.")

        # Sort candidates based on similarity score (highest to lowest)
        candidates.sort(key=lambda x: x[1], reverse=True)

        # Store candidates for current job
        all_candidates[job_desc.strip()] = candidates

    # Print candidates for each job
    for job_desc, candidates in all_candidates.items():
        print(f"Candidates for job: {job_desc}")
        for rank, (candidate, score) in enumerate(candidates, 1):
            print(f"{rank}. Candidate: {candidate}, Similarity Score: {score}")
        print()

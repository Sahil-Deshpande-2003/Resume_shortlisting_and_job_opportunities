import pdfplumber
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load English language model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_resume(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def calculate_cosine_similarity(doc_vector, keyword_vectors):
    similarity_scores = cosine_similarity([doc_vector], keyword_vectors)
    return similarity_scores.flatten()

if __name__ == "__main__":
    # Path to the PDF resume
    pdf_path = "resume.pdf"

    # Extract text from the resume
    resume_text = extract_text_from_resume(pdf_path)

    # Process resume text with spaCy
    resume_doc = nlp(resume_text)

    # Predefined list of keywords
    predefined_keywords = [
    "skill", "java","web","technology", "tech", "digital", "software", "email", "processing", "data", "management",  "database", "programming", "project", "engineer", "engineering", "design", "cyber","sql", "fresher","experience","operation", "data","english", "c", "python", "html", "css", "cgpa", "french", "hindi", "japanese", "system","linux", "git", "networking", "degree", "diploma", "major", "minor", "bachelor's","scholarship","assignment", "project", "first", "name", "last", "full", "middle", "surname","spanish", "german", "chinese", "japanese", "italian", "russian","grammar","dialect"
    ]

    # Convert predefined keywords to spaCy tokens and get their vectors
    keyword_vectors = [nlp(keyword).vector for keyword in predefined_keywords]

    # Calculate vector for the resume
    resume_vector = resume_doc.vector

    # Calculate cosine similarity between resume vector and keyword vectors
    similarity_scores = calculate_cosine_similarity(resume_vector, keyword_vectors)

    # Print the cosine similarity scores
    for keyword, score in zip(predefined_keywords, similarity_scores):
        print(f"Cosine Similarity with '{keyword}': {score}")


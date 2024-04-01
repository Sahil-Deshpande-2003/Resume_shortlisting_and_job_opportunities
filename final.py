import pdfplumber
import spacy
import os
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

if __name__ == "__main__":
    # Path to the directory containing resume PDFs
    resume_dir = "resumes/"

    # Path to the file containing job descriptions
    job_description_file = "job_descriptions.txt"

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

    # Iterate over each resume
    for resume_file in os.listdir(resume_dir):
        resume_path = os.path.join(resume_dir, resume_file)
        resume_text = extract_text_from_resume(resume_path)

        if resume_text:
            # Fit and transform resume text
            resume_tfidf = vectorizer.fit_transform([resume_text])

            # Iterate over each job description
            for job_desc in job_descriptions:
                # Calculate TF-IDF vectors for current job description
                job_desc_tfidf = vectorizer.transform([job_desc])

                # Calculate cosine similarity between resume and current job description
                similarity_scores = cosine_similarity(resume_tfidf, job_desc_tfidf)

                # Print the similarity score between current resume and job description
                print(f"Similarity between {resume_file} and job description: {similarity_scores[0][0]}")
        else:
            print(f"Text extraction failed for {resume_file}. Please check the PDF file.")


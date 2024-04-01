import pdfplumber
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load English language model
nlp = spacy.load("en_core_web_sm")

def extract_keywords_from_resume(pdf_path):
    keywords = []

    # Extract text from PDF
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            doc = nlp(text)

            # Extract keywords using spaCy
            for token in doc:
                # Consider only nouns, verbs, adjectives, and adverbs
                if token.pos_ in ["NOUN", "VERB", "ADJ", "ADV"]:
                    keywords.append(token.text.lower())

    return keywords

def calculate_cosine_similarity(vectors):
    # Convert list of vectors to numpy array
    vectors = np.array(vectors)
    
    # Calculate cosine similarity matrix
    similarity_matrix = cosine_similarity(vectors)
    return similarity_matrix

if __name__ == "__main__":
    # Path to the PDF resume
    pdf_path = "resume.pdf"
    
    # Extract keywords from the resume
    keywords = extract_keywords_from_resume(pdf_path)
    
    # Convert keywords to spaCy tokens and get their vectors
    keyword_vectors = [nlp(keyword).vector for keyword in keywords]
    
    # Calculate cosine similarity between keyword vectors
    similarity_matrix = calculate_cosine_similarity(keyword_vectors)
    
    # Print the cosine similarity matrix
    print("Cosine Similarity Matrix:")
    print(similarity_matrix)


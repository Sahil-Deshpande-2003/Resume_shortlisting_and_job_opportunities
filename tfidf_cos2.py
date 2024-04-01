import pdfplumber
import spacy
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
    # Path to the PDF resume
    pdf_path = "resume.pdf"

    # Extract text from the resume
    resume_text = extract_text_from_resume(pdf_path)

    if resume_text:
        # Predefined list of keywords
        predefined_keywords = [
            "skill", "java", "web", "technology", "tech", "digital", "software", "email", "processing", "data",
            "management", "database", "programming", "project", "engineer", "engineering", "design", "cyber", "sql",
            "fresher", "experience", "operation", "english", "c", "python", "html", "css", "cgpa", "french",
            "hindi", "japanese", "system", "linux", "git", "networking", "degree", "diploma", "major", "minor",
            "bachelor's", "scholarship", "assignment", "first", "name", "last", "full", "middle",
            "surname", "spanish", "german", "chinese", "japanese", "italian", "russian", "grammar", "dialect"
        ]

        # Remove duplicate keywords and convert to lowercase
        predefined_keywords = list(set(predefined_keywords))
        predefined_keywords_lower = [keyword.lower() for keyword in predefined_keywords]

        # Create TF-IDF vectorizer with custom tokenizer
        vectorizer = TfidfVectorizer(tokenizer=custom_tokenizer, vocabulary=predefined_keywords_lower)

        # Fit and transform resume text
        resume_tfidf = vectorizer.fit_transform([resume_text])

        # Calculate TF-IDF vectors for predefined keywords
        keyword_tfidf = vectorizer.transform(predefined_keywords_lower)

        # Calculate cosine similarity between resume and keywords
        similarity_scores = cosine_similarity(resume_tfidf, keyword_tfidf)

        # Print the cosine similarity scores
        for keyword, score in zip(predefined_keywords, similarity_scores.flatten()):
            print(f"Cosine Similarity with '{keyword}': {score}")
    else:
        print("Text extraction failed. Please check the PDF file.")


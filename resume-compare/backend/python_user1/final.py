from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re
import functions as func
import sys

# Path to the PDF resume file
# pdf_resume_path = 'aman_resume'

# Read the PDF resume
# resume_text = func.read_pdf_resume(pdf_resume_path)
resume_text = sys.argv[1]

# Print the extracted text
# print(resume_text)

# merge documents into a single corpus
string = [resume_text]

# create object
tfidf = TfidfVectorizer(stop_words="english")

# get tf-df values
# do tokenization internally and also remove stop words
# also convert words to lowercase
result = tfidf.fit_transform(string)

def preprocess_text(text):
    # Implement text preprocessing steps such as removing punctuation, stop words, etc.
    # Example:
    # Remove punctuation and convert to lowercase
    text = text.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    return text

def calculate_cosine_similarity(resume, job_descriptions):
    # Preprocess the text
    processed_resume = preprocess_text(resume)
    processed_job_descriptions = [preprocess_text(desc) for desc in job_descriptions]

    # Calculate TF-IDF vectors
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([processed_resume] + processed_job_descriptions)

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(vectors[0:1], vectors[1:])[0]

    return similarity_scores

# Example usage
# resume_text = "Your resume text goes here"
job_descriptions = [
    "We are looking for a Python Developer with experience in Django and Flask frameworks.",
    "We are seeking a data scientist proficient in machine learning and deep learning techniques.",
    # "We are seeking a proficient in machine learning and deep learning techniques.",
    "Join our team as a Frontend Developer specializing in HTML, CSS, and JavaScript.",
    "We have an opening for a Software Engineer experienced in C++ and Python programming languages.",
    "An exciting opportunity for a Computer Vision Engineer with expertise in OpenCV and TensorFlow.",
    "Looking for an AI Researcher with knowledge of natural language processing and artificial intelligence.",
    "Join our robotics team as a Robotics Engineer with hands-on experience in robotics frameworks.",
    "We are hiring a MySQL Database Administrator with expertise in managing large databases.",
    "An opportunity for a Web Developer skilled in PHP, MySQL, and JavaScript.",
    "Seeking a Software Tester with experience in manual and automated testing.",
    "We are looking for a Rust Developer",
    "We are looking for a Git and Github Expert",
    "We are looking for a PHP,Vue.js,Express.js developer"
]

similarity_scores = calculate_cosine_similarity(resume_text, job_descriptions)
print("Cosine Similarity Scores:")
for score, description in zip(similarity_scores, job_descriptions):
    print(f"'{description}': {score}")

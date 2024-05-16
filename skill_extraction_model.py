import PyPDF2
import csv
import nltk
import spacy
from spacy.matcher import PhraseMatcher
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data (if not already downloaded)
nltk.download('wordnet')

# Get English stopwords
stop_words = set(stopwords.words('english'))

# Initialize WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Create an empty list to store filtered and lemmatized tokens
filtered_lemmatized_tokens_list = []

# Specify the path to your CSV file
csv_file_path = 'skill2vec_50K.csv'

# Create an empty list to store filtered tokens
filtered_tokens_list = []

# Open the CSV file in read mode
with open(csv_file_path, mode='r',encoding="utf8") as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Tokenize the text in each non-empty column of the row
        for text in row:
            if text:  # Check if text is not empty
                # Replace commas with whitespace
                text = text.replace(',', ' ').replace('_', ' ').replace('(', ' ').replace(')', ' ')
                # Tokenize text based on whitespace and commas
                tokens = text.split()  # Split using whitespace by default
                # Remove specific characters like '/', '-'
                tokens = [re.sub(r'[\/\-]', '', token) for token in tokens]
                # Filter out empty tokens
                tokens = [token for token in tokens if token]
                # Remove stop words and numbers
                filtered_lemmatized_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens 
                                               if token.lower() not in stop_words and not token.isdigit()]
                # Append filtered tokens to the list
                if filtered_lemmatized_tokens:
                    filtered_lemmatized_tokens_list.extend(filtered_lemmatized_tokens)

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Define list of skills
skills_list = filtered_lemmatized_tokens_list

# print(f"Printing skills_list")

# print(f"{skills_list}")

# Initialize PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp(skill) for skill in skills_list]
matcher.add("SKILL", None, *patterns)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

# Function to extract skills from text
def extract_skills_from_text(text):
    doc = nlp(text)
    matches = matcher(doc)
    # matched_skills = [doc[start:end].text for match_id, start, end in matches]
    # return matched_skills
    for match_id, start, end in matches:
        span = doc[start:end]
        # print(span.text)

# Path to the PDF file
pdf_file_path = 'D:\DS_Project_endgame\Resume_shortlisting_and_job_opportunities\Resume_Sahil_Deshpande_test.pdf'

# Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_file_path)

# print(f"Printing pdf text")

# print(f"{pdf_text}")

# Extract skills from the text
extracted_skills = extract_skills_from_text(pdf_text)

# Print extracted skills
# print("Extracted Skills:")
# print(extracted_skills)

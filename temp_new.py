import spacy
import PyPDF2
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher
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

# Open the CSV file in read mode
# with open(csv_file_path, mode='r',encoding="utf8") as file:
#     # Create a CSV reader object
#     csv_reader = csv.reader(file)

#     # Iterate over each row in the CSV file
#     for row in csv_reader:
#         # Tokenize the text in each non-empty column of the row
#         for text in row:
#             if text:  # Check if text is not empty
#                 # Replace commas with whitespace


#                 # if (text == "Machine Learning"):

#                 #     print("Hey I am Machine Learning")
                    


#                 flag = 0


#                 if (text == "Machine Learning"):

                    
#                     flag = 1

#                     print("Hey I am Machine Learning")



#                 text = text.replace(',', ' ').replace('_', ' ').replace('(', ' ').replace(')', ' ')

#                 if (flag == 1):

#                     print(f"New Machine Learning = {text}")
#                 # Tokenize text based on whitespace and commas
#                 tokens = text.split()  # Split using whitespace by default
#                 # Remove specific characters like '/', '-'
#                 tokens = [re.sub(r'[\/\-]', '', token) for token in tokens]
#                 # Filter out empty tokens
#                 tokens = [token for token in tokens if token]

#                 if (flag == 1):

#                     print(f"Tokens = {tokens}")
#                 # Remove stop words and numbers

#                 filtered_lemmatized_tokens = tokens

#                 # filtered_lemmatized_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens 
#                                             #    if token.lower() not in stop_words and not token.isdigit()] # lemmitizing css to cs
                
#                 if (flag == 1):

#                     print(f"filtered_lemmatized_tokens = {filtered_lemmatized_tokens}")
#                 # Append filtered tokens to the list
#                 if filtered_lemmatized_tokens:
#                     filtered_lemmatized_tokens_list.extend(filtered_lemmatized_tokens)

# Load English language model
with open(csv_file_path, mode='r', encoding="utf8") as file:
    # Create a CSV reader object
    # print("I am here")
    csv_reader = csv.reader(file)


    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Join the text in each row with commas

        # print(f"row = {row}")


        text = ','.join(row)

        if ("Machine Learning" in text):
            
            print(f"Some Hope in text")

        # Tokenize text based on commas
        tokens = text.split(',')  
        # tokens = row.split(',')  

        # print(f"tokens = {tokens}")

        if ("Machine Learning" in tokens):
            
            print(f"Some Hope in tokens")

        # Remove specific characters like '_', '(', ')', and filter out empty tokens
        tokens = [re.sub(r'[_() ]', '', token) for token in tokens if token.strip()]  



        # Filter out tokens that contain digits
        tokens = [token for token in tokens if not any(char.isdigit() for char in token)]

        # Append filtered tokens to the list
        filtered_lemmatized_tokens_list.extend(tokens)



skills_list = filtered_lemmatized_tokens_list



# print(len(filtered_lemmatized_tokens_list))

print("Printing skills_list")

print(skills_list)

def case_insensitive_text(text):
    return text.lower()

# Load English tokenizer, tagger, parser, and NER
# nlp = spacy.load("en_core_web_sm")

from pathlib import Path

# Path where you want to save the model
output_dir = Path("D:\DS_Project_endgame\Resume_shortlisting_and_job_opportunities")

nlp = spacy.load(output_dir / "Skills_Model")

# Initialize the PhraseMatcher with a shared vocab

# print("Printing nlp vocab")
# print(nlp.vocab)

matcher = PhraseMatcher(nlp.vocab)



fruit_list = skills_list


patterns = [nlp.make_doc(fruit.lower()) for fruit in fruit_list]

# Add the pattern to the matcher
matcher.add("FRUIT_PATTERN", patterns)

# Process some text
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

# pdf_file_path = 'D:\DS_Project_endgame\Resume_shortlisting_and_job_opportunities\Resume_Sahil_Deshpande_test_added_CSS.pdf'
pdf_file_path = 'D:\DS_Project_endgame\Resume_shortlisting_and_job_opportunities\Resume_Sahil_Deshpande_test.pdf'

# Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_file_path)

# Convert the text to lowercase for case-insensitive matching
pdf_text_lower = case_insensitive_text(pdf_text)

# print("Printing pdf_text_lower")

# print(f"{pdf_text_lower}")

# Process the text
doc = nlp(pdf_text_lower)

# Define a custom extension attribute for the lowercase text
Span.set_extension("lower_text", getter=case_insensitive_text, force=True)

# Match against the lowercased text
matches = matcher(doc)

resume_skills = []

for match_id, start, end in matches:
    span = doc[start:end]
    # print("Match found:", span.text)

    resume_skills.append(span.text)

print("*********************************************")

print(resume_skills)

# from pathlib import Path

# Path where you want to save the model
# output_dir = Path("D:\DS_Project_endgame\Resume_shortlisting_and_job_opportunities")

# nlp.to_disk(output_dir / "SKills_Model")


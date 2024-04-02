import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy
from spacy.matcher import PhraseMatcher
import re


# Download NLTK data (if not already downloaded)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

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
with open(csv_file_path, mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Tokenize the text in each non-empty column of the row
        for text in row:
            if text:  # Check if text is not empty
                
                # tokens = word_tokenize(text)

                 # Replace commas with whitespace
                text = text.replace(',', ' ').replace('_', ' ').replace('(', ' ').replace(')', ' ')
                
                # Tokenize text based on whitespace and commas
                tokens = text.split()  # Split using whitespace by default
                
                # Remove specific characters like '/', '-'
                tokens = [re.sub(r'[\/\-]', '', token) for token in tokens]

                # Filter out empty tokens
                tokens = [token for token in tokens if token]
                
                # Remove stop words and numbers
                # filtered_tokens = [token for token in tokens if token.lower() not in stop_words and not token.isdigit()]

                filtered_lemmatized_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens 
                                               if token.lower() not in stop_words and not token.isdigit()]
                
                # Append filtered tokens to the list
                if filtered_lemmatized_tokens:
                    # filtered_tokens_list.append(filtered_tokens)
                    # filtered_tokens_list.extend(filtered_tokens)

                
                    # Extend the list with filtered and lemmatized tokens
                    filtered_lemmatized_tokens_list.extend(filtered_lemmatized_tokens)

# Load English language model
nlp = spacy.load("en_core_web_sm")
# print(nlp)

# Sample resume text (replace this with your actual resume text)
# resume_text = """
# Experienced software engineer proficient in Python, Java, and JavaScript. Skilled in web development, database management, and cloud computing. Strong problem-solving skills and ability to work in a team environment c++.
# """

# Define list of skills
skills_list = filtered_lemmatized_tokens_list

# Initialize PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp(skill) for skill in skills_list]
# print(patterns)
matcher.add("SKILL", None, *patterns)

# Save the pre-trained model to disk
nlp.to_disk("pretrained_model")

# import required module
import re  
import functions as func
# Import the re module for regular expressions
from sklearn.feature_extraction.text import TfidfVectorizer

# Path to the PDF resume file
pdf_resume_path = 'aman_resume'

# Read the PDF resume
resume_text = func.read_pdf_resume(pdf_resume_path)

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
print(result)

# TODO: filter out technical words from result of tokenised words
# do here

# get idf values
# print('\nidf values:')
# for ele1, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
#     print(ele1, ':', ele2)

# get indexing
# print('\nWord indexes:')
# print(tfidf.vocabulary_)

# in matrix form
print('\ntf-idf values in matrix form:')
print(result.toarray())

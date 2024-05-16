import spacy
import PyPDF2
#import the phrase matcher
from spacy.matcher import PhraseMatcher
#load a model and create nlp object
nlp = spacy.load("en_core_web_sm")
#initilize the matcher with a shared vocab
matcher = PhraseMatcher(nlp.vocab)
#create the list of words to match
# fruit_list = ['apple','orange','banana',]
def case_insensitive_text(text):
    return text.lower()
fruit_list = ['Python','Django']
#obtain doc object for each word in the list and store it in a list
# patterns = [nlp(fruit) for fruit in fruit_list]
patterns = [nlp.make_doc(fruit.lower()) for fruit in fruit_list]
print(f"patterns = {patterns}")
#add the pattern to the matcher
matcher.add("FRUIT_PATTERN", patterns)
#process some text
# doc = nlp("An orange contains citric acid and an apple contains oxalic acid")
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

pdf_file_path = 'D:\DS_Project_endgame\Resume_shortlisting_and_job_opportunities\Resume_Sahil_Deshpande_test.pdf'

# Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_file_path) # str
pdf_text_lower = case_insensitive_text(pdf_text)
# doc = nlp("An orange contains citric acid and an apple contains oxalic acid")
doc = nlp(pdf_text_lower)
print(f"pdf_text = {pdf_text}")
Span.set_extension("lower_text", getter=case_insensitive_text, force=True)
matches = matcher(doc)
print(f"matches = {matches}")

for match_id, start, end in matches:
 print("I am here")
 span = doc[start:end]
 print(f" ans = {span.text}")
import re
import job_descriptions
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

'''
1.Splitting based on commas after double quotes
2.Splitting based on spaces
3.Splitting based on punctuation marks by removing one or more non-word characters
'''


def tokenize_job_description(description):
    
    # print(f"description = {description}")

    tokens = re.split(r'(?<="),', description) # Splitting based on commas after double quotes
    processed_tokens = []

    for token in tokens:
        # Splitting based on spaces
        space_tokens = token.split()
        for space_token in space_tokens:
            # Splitting based on punctuation marks
 

            if ('C++' in space_token):

                processed_tokens.append('C++')

            '''
            This is a regular expression pattern that matches one or more non-word characters. \W matches any non-alphanumeric character (equivalent to [^a-zA-Z0-9_]), and + means one or more occurrences of the preceding pattern

            Eg "Split this string with multiple spaces and tabs!"

            Output: ["Split", "this", "string", "with", "multiple", "spaces", "and", "tabs"]

            '''

            punctuation_tokens  = re.split(r'\W+', space_token)
            processed_tokens.extend(punctuation_tokens)
    
    return processed_tokens


def remove_stop_words(tokens):
    sublist = []


    for token in tokens:

        row_list = []

        for subtoken in token:

            if (subtoken not in stop_words):

                row_list.append(subtoken)
        
        sublist.append(row_list)
           

    return sublist


tokenized_descriptions = [tokenize_job_description(desc) for desc in job_descriptions.job_descriptions]

new_tokens = remove_stop_words(tokenized_descriptions) # 177 to 118


tokenized_descriptions = new_tokens



import nltk
from nltk.corpus import stopwords
import re
nltk.download('stopwords')


stop_words = set(stopwords.words('english'))


def remove_stop_words(tokens):

    sublist = []

    for token in tokens:

        for subtoken in token:

            if (subtoken not in stop_words):

                sublist.append(subtoken)
           

    return sublist


'''
1.Splitting based on commas 
2.Splitting based on spaces
3.Splitting based on punctuation marks by removing one or more non-word characters
4. Treating C++ as a special case
'''


def two_level_tokenizing(input_string):
  
    input_string = input_string.replace("C++", "C_plusplus_token,") # maybe C++, kar diya to bhi chal jayga

    tokens_level1 = input_string.split(',')


    final_tokens = []


    for token in tokens_level1:

        if "C_plusplus_token" in token:
            token = token.replace("C_plusplus_token", "C++")
            final_tokens.append([token.strip()])
        else:
  
            token_list = token.strip().split()
            
  
            temp_tokens = []
            for token in token_list:
               
                split_tokens = re.split(r'\W+', token) # removing punctuation marks
   
                split_tokens = [t for t in split_tokens if t.strip()]
          
                temp_tokens.extend(split_tokens)
       
            final_tokens.append(temp_tokens)

    new_tokens = remove_stop_words(final_tokens) # Org len1 = 581 and new Len is 412
    
    return new_tokens 

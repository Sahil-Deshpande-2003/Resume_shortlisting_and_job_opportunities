# import re
# sub_patterns = ['[A-Z][a-z]* University','[A-Z][a-z]* Educational Institute',
#                 'University of [A-Z][a-z]*',
#                 'Ecole [A-Z][a-z]*']
# pattern = '({})'.format('|'.join(sub_patterns))
# matches = re.findall(pattern, text)

# extracted_text["Institutes"] = matches
# #######print(matches)


# initialize matcher with a vocab


# def extract_name(resume_text):
#     nlp_text = nlp(resume_text)
    
#     # First name and Last name are always Proper Nouns
#     pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    
#     matcher.add('NAME', [pattern], on_match = None)
    
#     matches = matcher(nlp_text)
    
#     for match_id, start, end in matches:
#         span = nlp_text[start:end]
#         return span.text
    
    
# name = extract_name(text)
# #######print(name)
# extracted_text["Name"] = name


# def extract_skills(resume_text):
#     #######print(resume_text)
#     nlp_text = nlp(resume_text)

#     # removing stop words and implementing word tokenization
#     tokens = [token.text for token in nlp_text if not token.is_stop]
    
#     skills = ["machine learning",
#              "deep learning",
#              "nlp",
#              "natural language processing",
#              "mysql",
#              "sql",
#              "django",
#              "computer vision",
#               "tensorflow",
#              "opencv",
#              "mongodb",
#              "artificial intelligence",
#              "ai",
#              "flask",
#              "robotics",
#              "data structures",
#              "python",
#              "c++",
#              "matlab",
#              "css",
#              "html",
#              "github",
#              "php"]
    
#     skillset = []
    
#     # check for one-grams (example: python)
#     for token in tokens:
#         for skill in skills:
#             if matches_skill(token.lower(), skill.lower()):
#                 skillset.append(token)
#                 # break  # Move to the next token if a match is found

#     # Check for bi-grams and tri-grams
#     for token in nlp_text.noun_chunks:
#         token = token.text.lower().strip()
#         for skill in skills:
#             if matches_skill(token, skill):
#                 skillset.append(token)
    
#     return [i.capitalize() for i in set([i.lower() for i in skillset])]



# def extract_skills(resume_text):
    
#     nlp_text = nlp(resume_text)
#     complete_filtered_tokens = [
#      preprocess_text.preprocess_token(token)
#      for token in nlp_text
#      if preprocess_text.is_token_allowed(token)
#  ]
    
 
#     ######print("About to ######print length of nlp text")
#     ######print(len(complete_filtered_tokens))
#     ######print("About to ######print nlp text")
#     ######print(complete_filtered_tokens)
#     text_df = pd.DataFrame({"text": [text]})
# # Save text to CSV
#     text_df.to_csv('text.csv', index=False)

# # Convert nlp_text to DataFrame

#     nlp_text_df = pd.DataFrame({"token": complete_filtered_tokens})
# # Save nlp_text to CSV
#     nlp_text_df.to_csv('nlp_text.csv', index=False)
#     #######print("SAB CHUP I am #######printing nlp text")
#     #######print(resume_text)
#     # tokens = [token.text for token in nlp_text if not token.is_stop] 
    
#     # Construct a regular expression pattern to match skills
#     pattern = '|'.join(map(re.escape, skill_arr.skill_arr))
#     regex = re.compile(pattern, re.IGNORECASE)
#     #######print(f"regex = {regex}")
    
#     skillset = []

#     # Extract skills using regular expression matching
#     for token in complete_filtered_tokens:
#         if (token == "machine learning"):
#             pass
#             #######print("SMELL SUCCESS 1")
#         if (token == "Vue.js"):
#             pass
#             #######print("Hitler1!")
#         if regex.match(token):
#             pass
#             #######print(f"token={token}")
#             skillset.append(token)
            
#     # for chunk in nlp_text.noun_chunks:
#     #     chunk_text = chunk.text.lower().strip()
#     #     if (chunk_text == "machine learning"):
#     #         pass
#     #         #######print("SMELL SUCCESS 1")
#     #     for skill in skill_arr.skill_arr:
#     #         if skill in chunk_text:
#     #             #######print(f"Superman skill = {skill}")
#     #             skillset.append(skill)

#     return list(set(skillset))



# def extract_skills(resume_text):
#     #######print(resume_text)
#     nlp_text = nlp(resume_text) 
#     tokens = [token.text for token in nlp_text if not token.is_stop] 
    
    
 
    
#     skillset = []
    
#     for token in tokens:
#         if (token == "Vue.js"):
#             #######print("Hitler1!")
#         if token.lower() in skill_arr.skill_arr  :
#             skillset.append(token)

#     for token in nlp_text.noun_chunks:
#         if (token == "Vue.js"):
#             #######print("Hitler2!")
#         token = token.text.lower().strip()
#         if token in skills:
#             skillset.append(token)
    
#     return [i.capitalize() for i in set([i.lower() for i in skillset])]

    # while i < len(tokens):
 
    #     for phrase in combined_phrases:
    #         # Using regex for a complete match of the phrase
    #         ####print(f"tokens[i] = {tokens[i]}")
    #         if re.fullmatch(phrase, tokens[i]):
    #             ####print(f"Full matched token = {tokens[i]}")
    #             words = tokens[i].split()
    #             # ####print(f"words = {words}")
    #             for word in words:
    #                 if word in tokens:
    #                     # ####print(f"Removed word = {word}")
    #                     tokens.remove(word)
    #                     # for i in range(len(tokens)):
    #                         # if (tokens[i] == "deep"):
    #                             # ####print("Still Trouble")

    #             i += len(words)
    #             break
    #     i+=1
 
    
    # ####print("Checking is deep learning token ... after redemption")
    # for i in range(len(tokens)):
        # if (tokens[i] == 'deep learning'):
            # ####print("Strange!")
            
'''
Pehle ka

vect = TfidfVectorizer(tokenizer=custom_tokenizer,stop_words="english")
# #####print(vect)
# vect = TfidfVectorizer(tokenizer=custom_tokenizer)
# vect = TfidfVectorizer(stop_words="english")

tfidf_job_description = vect.fit_transform(job_descriptions.job_descriptions)

#####print("I am Death destroyer of world")
###print(vect.get_feature_names_out())

tfidf_df = pd.DataFrame(tfidf_job_description.toarray(), columns=vect.get_feature_names_out())

tfidf_df_transposed = tfidf_df.T

tfidf_df_transposed.to_csv('tfidf_matrix_transposed_job_description_matrix.csv')
'''



'''
Wrong Output:

C++,0.08199556295715016,0.06521938701143161,0.06580221223160536,0.06369318429091664,0.06369318429091664,0.05848469173461117,0.04631509555371133,0.06190886392025806,0.07306106684865611,0.06871516089903096,0.12597453965309421,0.09175058069807811,0.08996873424252969 for 

# Hardcoded job descriptions
job_descriptions = [
    "We are looking for a Python Developer with experience in Django and Flask frameworks.",
    "We are seeking a Data Scientist proficient in machine learning and deep learning techniques.",
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
    "We are looking for a PHP,Vue,Express developer"
]
'''


'''
def remove_combined_phrases(tokens):
   
    i = 0        
    while i < len(tokens):
        
        for phrase in combined_phrases.combined_phrases:
            
            if re.fullmatch(phrase, tokens[i]):
                                         
                words = tokens[i].split()          
                for word in words:
                    if word in tokens:
                        tokens.remove(word)
        i = i+1
   
        
        
        

    return tokens

def custom_tokenizer(text):
    

    
    nlp_text = nlp(text)
    complete_filtered_tokens = [
     preprocess_text.preprocess_token(token)
     for token in nlp_text
     if preprocess_text.is_token_allowed(token)
 ]
    

    tokens = [match.lower() for token in complete_filtered_tokens for match in re.findall(r'\b\w+\b', token.lower())]
    
    temp_tokens = re.findall(r'\b\w+\b|\"[\w\s]+\"', text.lower())
    


    tokens.append("C++")
    
    for i in range(len(tokens)):

        pass
        
    

    i = 0
    while i < len(temp_tokens):
        # ####print(f"curr = {tokens[i]}")
        if i+1 < len(temp_tokens) and " ".join(temp_tokens[i:i+2]) in combined_phrases.combined_phrases:
            #print(f"REMOVING {tokens[i]}...")
            tokens.remove(tokens[i])
            #print(f"wildcard = {temp_tokens[i:i+2]}")
            tokens.append(" ".join(temp_tokens[i:i+2]))
            i += 2
        else:
            # ####print(f"Normal entry = {temp_tokens[i]}")
            tokens.append(temp_tokens[i])
            i += 1
                
    tokens  = remove_combined_phrases(tokens)

    return tokens

'''
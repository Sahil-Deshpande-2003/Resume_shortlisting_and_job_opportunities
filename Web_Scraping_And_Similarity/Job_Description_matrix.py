import preprocess_text
import import_nlp
nlp = import_nlp.nlp
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import skill_arr
import job_descriptions
import combined_phrases

def extract_skills_tokenize(resume_text):
      
    nlp_text = nlp(resume_text) # 145 to 92
    complete_filtered_tokens = [
     preprocess_text.preprocess_token(token)
     for token in nlp_text
     if preprocess_text.is_token_allowed(token)
 ]
    
    pattern = '|'.join(map(re.escape, skill_arr.skill_arr))
    regex = re.compile(pattern, re.IGNORECASE)
    
    skillset = []
    
        
    token_arr_temp = []
    
    for i in range(len(complete_filtered_tokens)):
        token_arr_temp.append(complete_filtered_tokens[i])

    i = 0
    while i < len(token_arr_temp):
        # #####print(f"curr = {tokens[i]}")
        if i+1 < len(token_arr_temp) and " ".join(token_arr_temp[i:i+2]) in combined_phrases.combined_phrases:
            # print(f"REMOVING {token_arr_temp[i]}...")
            complete_filtered_tokens.remove(token_arr_temp[i])
            # print(f"wildcard = {token_arr_temp[i:i+2]}")
            complete_filtered_tokens.append(" ".join(token_arr_temp[i:i+2]))
            i += 2
        else:
            i += 1

    
    for i in range(len(complete_filtered_tokens)):
            
            token = complete_filtered_tokens[i]        
            if regex.match(token):
                skillset.append(token)
  
    
    # Tested -> to add Machine Learning and removing Machine

    # tokens  = remove_combined_phrases.combined_phrases(complete_filtered_tokens) # removes Learning 

     
    return skillset
        



vect = TfidfVectorizer(tokenizer=extract_skills_tokenize,stop_words="english")
tfidf_job_description = vect.fit_transform(job_descriptions.job_descriptions)

tfidf_df = pd.DataFrame(tfidf_job_description.toarray(), columns=vect.get_feature_names_out())

tfidf_df_transposed = tfidf_df.T

tfidf_df_transposed.to_csv('tfidf_matrix_transposed_job_description_matrix_new.csv')
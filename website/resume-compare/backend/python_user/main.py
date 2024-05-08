from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import Final_Job_Desc_Skills
import Final_Resume_Skills
import job_descriptions
import re


def custom_tokenizer(text): # So that 'C' is not ignored which is ignored whenever we instantiate tfidfvectorizer

    # print("Input text:", text)

    special_cases = {"c++": "cplusplus", "c#": "csharp"}

    tokens = re.split(r'\s*,\s*', text)

    for i, token in enumerate(tokens):
        if token in special_cases.keys():
            tokens[i] = token.replace("++", "plusplus").replace("#", "sharp")


    tokens = [re.sub(r'\W+', '', token) for token in tokens]

    '''
    This line of code removes non-alphanumeric characters from each token in a list called tokens

    Input = ["apple!", "banana123", "$$cherry$$", "grape?"]
    Output = ['apple', 'banana123', 'cherry', 'grape']

    '''

    '''
    With enumerate(), you don't need to manually index into the list (tokens[i]). Instead, you directly get both the index (i) and the value (token) in each iteration of the loop.
    '''
    
    for i, token in enumerate(tokens):

        if token in special_cases.values():
            
            for key, value in special_cases.items():
                if value == token:
                    tokens[i] = key
                      
    return tokens


Job_Desc_Skills_2D_array = Final_Job_Desc_Skills.skills_2D

Resume_skills = Final_Resume_Skills.skills

# print("Resume skills:", Resume_skills)

vect = TfidfVectorizer(tokenizer=custom_tokenizer,stop_words="english")

tfidf_job_description = vect.fit_transform(Resume_skills)


similarity_scores = []

for i in range(len(Job_Desc_Skills_2D_array)):

    row = Job_Desc_Skills_2D_array[i]

    final_score = 0

    for skill in row:

        tfidf_matrix_resume = vect.transform([skill])

        similarity  = cosine_similarity(tfidf_matrix_resume, tfidf_job_description)


        curr_score = np.mean(similarity)

        final_score+=curr_score


    similarity_scores.append((i,final_score))
  

sorted_job_descriptions = sorted(similarity_scores, key=lambda x: x[1], reverse=True)



# print("Sorted job descriptions:", sorted_job_descriptions)

list_ret = []

for i, similarity_score in sorted_job_descriptions:
    list_ret.append([job_descriptions.job_descriptions[i]])
    
# print("Hi Sahhil")

print(list_ret)

import re
import job_descriptions
def tokenize_job_description(description):
    # Splitting based on commas after double quotes
    tokens = re.split(r'(?<="),', description)
    processed_tokens = []
    
    # Processing tokens
    for token in tokens:
        # Splitting based on spaces
        space_tokens = token.split()
        for space_token in space_tokens:
            # Splitting based on punctuation marks
            punctuation_tokens = re.findall(r'\w+|[^\w\s]', space_token)
            processed_tokens.extend(punctuation_tokens)
    
    return processed_tokens

# Tokenize all job descriptions
tokenized_descriptions = [tokenize_job_description(desc) for desc in job_descriptions.job_descriptions]

# Printing tokenized job descriptions
# for idx, tokens in enumerate(tokenized_descriptions):
#     print(f"Tokens for job description {idx+1}:")
#     print(tokens)
#     print()

# print(len(job_descriptions.job_descriptions))
# print(len(tokenized_descriptions))
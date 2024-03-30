def two_level_tokenizing(input_string):
    # Split the string based on comma
    tokens_level1 = input_string.split(',')

    # Split each token based on space
    tokens_level2 = [token.strip().split() for token in tokens_level1]

    return tokens_level2

# Example usage
# input_string = "apple, banana orange, grape, kiwi, mango"
# result = two_level_tokenizing(input_string)
# print(result)

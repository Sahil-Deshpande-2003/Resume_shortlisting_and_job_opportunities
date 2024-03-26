from tika import parser
file = r'Resume_Sahil_Deshpande_test.pdf'
file_data = parser.from_file(file)
text = file_data['content']
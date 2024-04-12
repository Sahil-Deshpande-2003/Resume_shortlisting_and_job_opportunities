from tika import parser
file = r'aman_resume'
file_data = parser.from_file(file)
text = file_data['content']

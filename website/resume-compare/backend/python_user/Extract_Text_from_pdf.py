from tika import parser
file=r'D:\Data_Science_Project\Endgame\Resume_shortlisting_and_job_opportunities\Resume_shortlisting_and_job_opportunities\website\resume-compare\backend\python_user\Resume_Sahil_Deshpande_test.pdf'
file_data = parser.from_file(file)
text = file_data['content']
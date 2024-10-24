# Resume shortlisting and job opportunities

**Our project focuses on 2 aspects**

## Candidate Applying for Jobs

### Resume Upload:
- The candidate uploads their resume into the system, which contains details such as skills, education, and work experience.

### Company Data Scraping:
- The system scrapes job opportunity data from the CareerBuilder website based on the skills listed in the candidate’s resume. This scraping process retrieves job descriptions that are likely to be relevant to the candidate's qualifications and skills.

### Preprocessing:

- **Tokenization**: The text from the resume is split into individual tokens (words or phrases), making it easier to process.
- **Stopwords Removal**: Common words (such as "the", "and", "is") that do not contribute to the skill matching process are removed.
- **Skills Extraction**: The system extracts relevant skills from the resume, focusing on keywords that are directly related to the candidate's qualifications, such as programming languages, tools, or certifications.
### TF-IDF Vectorization:

- The extracted skills from the resume are then converted into a numerical form using the TF-IDF (Term Frequency-Inverse Document Frequency) method. This method assigns a weight to each skill based on how often it appears in the resume and how important it is relative to other terms in the job description data.
- The goal of this vectorization is to represent the resume in a way that emphasizes relevant skills while reducing the importance of less significant words.

### Cosine Similarity Calculation:

- The system compares the vectorized resume with the vectorized job descriptions that were scraped from CareerBuilder. To do this, it calculates the cosine similarity between the vectors. Cosine similarity measures the angle between two vectors; the closer the angle is to zero, the more similar the two vectors are.
- In this context, a higher similarity score indicates a better match between the candidate’s skills and the job descriptions.
### Job Recommendation:

- Based on the calculated similarity scores, the system ranks the job descriptions. The candidate is then presented with a list of job opportunities where their skills and qualifications are the best fit.
- This personalized job recommendation helps the candidate quickly identify which companies and job roles are most aligned with their resume.


## HR Recruiting Candidates

### Job Description Input:
- The HR personnel or recruiter uploads the job description into the system. This description typically includes the required skills, qualifications, responsibilities, and any other relevant criteria for the position.

### Resume Upload:
- The HR uploads multiple resumes (from candidates who have applied or from their own candidate pool). Each resume is then processed by the system.

### Preprocessing:
- **Tokenization**: Both the job description and resumes are tokenized (split into words or phrases) to prepare the text for further processing.
- **Stopwords Removal**: Common words are removed from both the job description and the resumes to ensure that only meaningful terms (like skills and qualifications) are analyzed.
- **Skills Extraction**: Relevant skills are extracted from the job description and each resume, focusing on key terms that indicate a candidate's qualifications (such as required programming languages, tools, certifications, etc.).

### TF-IDF Vectorization:

- Both the job description and the resumes are converted into vectors using the TF-IDF method. In this case, the job description is treated as a reference, and the system analyzes how well each resume aligns with it in terms of the skills and qualifications mentioned.
- TF-IDF ensures that common words are given less weight while highlighting terms that are particularly important for this specific job posting.

### Cosine Similarity Calculation:

- The system calculates the cosine similarity between the vector representing the job description and the vectors representing each of the resumes. This similarity score quantifies how closely a candidate’s qualifications (from the resume) match the job requirements.
- A higher cosine similarity score means a better match between the job description and the resume in terms of skills and qualifications.

### Resume Ranking and Recommendation:

- The system ranks all the uploaded resumes based on their similarity scores to the job description.
- The HR personnel is then provided with a list of the top resumes, highlighting the candidates who are the best match for the job position. This simplifies the recruitment process by automatically filtering and ranking candidates according to how well they fit the job’s requirements.

## Technologies used
- React - Frontend
- Express.js and Node.js - Backend
- Mongodb - Database
- Beautiful soup - Web scraping
- Python - Web scraping and to find Similarity

## How to run 
- Install necessary node modules
```
    npm install
```

- Start mongodb-compass
```
    mongodb-compass
```

- Run the website at localhost
```
    npm run dev
```


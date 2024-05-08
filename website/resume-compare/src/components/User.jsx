import React, { useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';
import 'react-pdf/dist/esm/Page/AnnotationLayer.css';
import './User.css';
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

function User() {
  const [file, setFile] = useState(null);
  const [backendResponse, setBackendResponse] = useState('');

  const onFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
  };

  const fetchData = async (value) => {
    try {
      const url = `http://localhost:3000/api/user?searchTerm=${encodeURIComponent(value)}`;
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Failed to execute Python script');
      }

      const result = await response.json();
      setBackendResponse(result['result']);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const extractText = (file) => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = async function (event) {
        const arrayBuffer = event.target.result;
        const pdf = await pdfjs.getDocument(arrayBuffer).promise;
        let text = '';
        for (let i = 1; i <= pdf.numPages; i++) {
          const page = await pdf.getPage(i);
          const pageText = await page.getTextContent();
          text += pageText.items.map((item) => item.str).join(' ');
        }
        resolve(text);
      };
      reader.onerror = reject;
      reader.readAsArrayBuffer(file);
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const text = await extractText(file);
    fetchData(text);
  };

  return (
    <div className="App">
      {backendResponse ? (
        <div style={{textAlign:'center',alignItems:'center'}} className='center'>
          <div>
            <h1>Recommended Job Openings</h1>
            {console.log("About to print backend response 1")}
            {console.log(backendResponse)}
            {console.log("Printing type")}
            {console.log(typeof backendResponse)}
            
            {backendResponse.replace(/"/g, '').replace(/\xa0/g, '').replace(/\\x/g, '')};
            {console.log("About to print backend response 2")}
            {console.log(backendResponse)}
            {backendResponse = JSON.parse(backendResponse)}
            
            {backendResponse.split('\n').map((job, index) => {
               const cleanedStr = job.replace(/'/g, '"').replace(/\xa0/g, ' ').replace(/\\x/g, '').replace(/\xa0/g, ' ');
               {console.log("Character at position 92:", cleanedStr.charAt(1346))}
              const parsedJob = JSON.parse(cleanedStr);
              console.log("About to print parsed Job")
              console.log(parsedJob)
              return (
                <div className="card" key={index}>
                  <div className="card-body">
                    {/* <h5 className="card-title">{parsedJob.title}</h5> */}
                    {/* <p className="card-text">{parsedJob.description}</p> */}
                    <a href={parsedJob.url} className="btn btn-primary">Apply</a>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      ) : (
        <div className="center">
          <form className="formStyle" onSubmit={handleSubmit}>
            <h1>Upload PDF here</h1>
            <br />
            <input type="file" className="form-control" accept="application/pdf" required onChange={onFileChange} />
            <br />
            <button className="btn btn-primary" type="submit" disabled={!file}>
              Submit
            </button>
          </form>
        </div>
      )}
    </div>
  );
}

export default User;

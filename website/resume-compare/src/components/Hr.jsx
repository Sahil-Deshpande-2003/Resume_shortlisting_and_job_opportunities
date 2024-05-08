import React, { useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';
import 'react-pdf/dist/esm/Page/AnnotationLayer.css';
import axios from 'axios';
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

function Hr() {
  const [description, setDescription] = useState('');
  const [files, setFiles] = useState(null); // Store file object
  const [backendResponse, setBackendResponse] = useState('');

  const handleFileChange = (e) => {
    const fileList = Array.from(e.target.files);
    // Append the newly selected files to the existing list of files
    setFiles((prevFiles) => prevFiles ? [...prevFiles, ...fileList] : fileList);
  };
  

  const handleDescriptionChange = (e) => {
    setDescription(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Your axios post request here
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  };

  return (
    <div className="container">
      <div className="row justify-content-center align-items-center">
        <div className="col-md-6">
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <h2 className="text-center mb-4" style={{margin:'30px'}}>Enter Job Description</h2>
              <textarea
                className="form-control"
                id="exampleFormControlTextarea1"
                rows="5"
                value={description}
                onChange={handleDescriptionChange}
                required
              ></textarea>
            </div>
            <div className="mb-3">
              <input type="file" className="form-control" accept="application/pdf" required multiple onChange={handleFileChange} />
            </div>
            <div className="mb-3 text-center">
              <button className="btn btn-primary" style={{ marginBottom: '20px' }} type="submit" disabled={!files}>
                Submit
              </button>
            </div>
          </form>
        </div>
      </div>

      {files && files.length > 0 && (
        <div className="mb-3 text-center">
          <h3 style={{ marginBottom: '30px' }}>Selected Files</h3>
          <div style={{ display: 'inline-block', textAlign: 'left' }}>
            {files.map((file, index) => (
              <div key={index} style={{ marginBottom: '20px' }}>{index + 1}: {file.name}</div>
            ))}
          </div>
        </div>
      )}

      {console.log("About to print backend response")}

      {console.log(backendResponse)}

      {backendResponse && (
        <div>
          <h3>Extracted Text</h3>
          <p>{backendResponse}</p>
        </div>
      )}
    </div>
  );
}

export default Hr;
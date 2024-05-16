// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'

// function App() {
//   const [title, setTitle] = useState("");
//   const [files, setFiles] = useState("");


import React from 'react';
import { useState } from 'react';
// import './App.css';
import { Document, Page, pdfjs } from 'react-pdf'; // Import necessary components from react-pdf
import 'react-pdf/dist/esm/Page/AnnotationLayer.css'; // Import CSS for react-pdf

// Set up pdfjs worker
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

function User() {
  const [title, setTitle] = useState('');
  const [file, setFile] = useState(null); // Store file object
  const [numPages, setNumPages] = useState(null); // State to store the number of pages
  const [pdfText, setPdfText] = useState(''); // State to store extracted text
  const [backendResponse, setbackendResponse] = useState('')

  const onFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
  };

  const onDocumentLoadSuccess = ({ numPages }) => {
    setNumPages(numPages);
  };


  const fetchData = async (value, check) => {
    try {
      console.log("Inside fetchData");
      console.log("Printing value....");
      console.log(value);
      // props.setProgress(20);

      const url = `http://localhost:3000/api/user?searchTerm=${encodeURIComponent(
        value
      )}`;

      // // props.setProgress(50);

      const response = await fetch(url, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
        // Convert search term to JSON and send it as the query parameter
      });

      if (!response.ok) {
        throw new Error("Failed to execute Python script");
      }

      const result = await response.json();
      console.log("Result from backend:", result["result"]);
      setbackendResponse(result["result"])

      // const dead = result["result"];
      // console.log("Printing type of dead:", typeof dead);
      // console.log("Original JSON string:", dead);

      // const cleanedStr = dead.replace(/'/g, '"').replace(/,\s+/g, ",");
      // console.log("Cleaned JSON string:", cleanedStr);

      // const list = JSON.parse(cleanedStr);

      // console.log("Parsed JSON data:", list);

      // console.log("Printing type of list:", typeof list);

      // setProducts(list);
    } catch (error) {
      console.error("Error:", error);
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
        resolve(text); // Resolve the promise with the extracted text
      };
      reader.onerror = reject; // Reject the promise if an error occurs
      reader.readAsArrayBuffer(file);
    });
  };
  

  const handleSubmit = async (e) => {
    e.preventDefault();
    const text = await extractText(file);
    // setTimeout(1)
    fetchData(text);
  };

  return (
    <div className="App">
      <form className="formStyle" onSubmit={handleSubmit}>
        <h2>Upload PDF here</h2>
        <br />
        <input type="file" className="form-control" accept="application/pdf" required onChange={onFileChange} />
        <br />
        <button className="btn btn-primary" type="submit" disabled={!file}>
          Submit
        </button>
      </form>
      {backendResponse && (
        <div>
          <h3>Extracted Text</h3>
          <p>{backendResponse}</p>
        </div>
      )}
    </div>

  );
}

export default User;

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
import axios from 'axios';

// Set up pdfjs worker
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

function Hr() {
  const [description, setDescription] = useState('');
  const [files, setFiles] = useState(null); // Store file object
  const [numPages, setNumPages] = useState(null); // State to store the number of pages
  const [pdfText, setPdfText] = useState(''); // State to store extracted text
  const [backendResponse, setbackendResponse] = useState('')
  const [jobList, setJobList] = useState([]);

  const [extractedTexts, setExtractedTexts] = useState([]);

  const handleFileChange = async (e) => {
    const fileList = Array.from(e.target.files);
    setFiles(fileList);

    const texts = [];
    texts.push(description)
    for (const file of fileList) {
      const text = await extractText(file);
      texts.push(text);
    }
    setExtractedTexts(texts);
  };
//   const onFileChange =  (e) => {
//     // const selectedFiles = await e.target.files;
//     const fileList = Array.from(e.target.files);
//     console.log(fileList)
//     // setFiles(fileList);
//     setFiles(fileList);
//   };

  const handleDescriptionChange = (e) => {
    setDescription(e.target.value);
  };
//   const onDocumentLoadSuccess = ({ numPages }) => {
//     setNumPages(numPages);
//   };


  const fetchData = async (value, check) => {
    try {
      console.log("Inside fetchData");
      console.log("Printing value....");
      console.log(value);
      // props.setProgress(20);

      const url = `http://localhost:3000/api/hr?searchTerm=${encodeURIComponent(
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

    //   setExtractedTexts(str())
    
    const extractedText = JSON.stringify(extractedTexts);
    // setPdfText(JSON.stringify(extractedTexts));
    console.log(extractedText)
    
    try {
        // Send extracted text data to backend server at localhost:3000
        const response = await axios.post('http://localhost:3000/api/text', {description, extractedText});
        console.log("Response" , response.data);

        console.log("Response: ", typeof response);
        if (response.statusText !== "OK") {
          throw new Error("Failed to execute Python script");
        }
        
        // const result = await response.data.json();
        console.log("Result from backend:", response.data["result"]);
        setbackendResponse(response.data["result"])

        // Reset form after successful <submission></submission>
        // setDescription('');
        // setFiles([]);
      } catch (error) {
        console.error('Error submitting data:', error);
      }
      
    // fetchData(extractedTextsAsString);
    //   setDescription(""); // Reset description input
    //   setFiles([]); // Clear file input
  };

  return (
    <div className="App">
      <form className="formStyle" onSubmit={handleSubmit} style={{width: "60%"}}>
        <h2>Upload PDF here</h2>
        <div>
          <label>Description:</label>
          <textarea value={description} onChange={handleDescriptionChange} style={{ height: "200px", width: "100%" }}/>
        </div>
        <br />
        <input type="file" className="form-control" accept="application/pdf" required multiple onChange={handleFileChange} />
        <br />
        <button className="btn btn-primary" type="submit" disabled={!files}>
          Submit
        </button>
      </form>

         
      {
        <div>
            <br /> 
            <h3> Files </h3>
            {files && files.map((file, index) => {
                return (
                    <div key={index}> {index} : {file.name} </div>
                )
            })} 
        </div>
      }
      {backendResponse && (
        <div>
          <br />
          <h3>Extracted Text</h3>
          <p>{backendResponse}</p>
        </div>
      )}
    </div>

  );
}

export default Hr;

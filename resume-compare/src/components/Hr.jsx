import React, { useState } from 'react';
import axios from 'axios';

function Hr(props) {
  const [description, setDescription] = useState('');
  // const [description, setDescription] = useState([]);
  const [file, setFile] = useState(null);
  const [sortedCandidates, setSortedCandidates] = useState([]);
  
  let { showAlert } = props;

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleDescriptionChange = (e) => {
    setDescription(e.target.value); // Update as string
  };
  

  const handleSubmit = async (e) => {
    e.preventDefault();

    showAlert("PDF Submitted Successfully", "success");

    if (!file) {
      alert('Please select a file.');
      return;
    }

    const formData = new FormData();
    formData.append('resume', file);
    console.log("Saved  description = " + description)
    formData.append('description', JSON.stringify([description])); // Convert to array and stringify


    try {
      const response = await axios.post('http://localhost:3000/api/text',formData, {
        headers: {
          'Content-Type': 'multipart/form-data' // Set the Content-Type header for file uploads
        },
      });

      console.log("Life after response")
      console.log(response)

      if (response.status === 200) {
        const result = response.data;
        console.log("About to print result");
        console.log(result);
        setSortedCandidates(result.sortedCandidates)
        // Update state with sorted candidates if needed
      } else {
        console.error('Error:', response);
        // Handle error if necessary
      }
    } catch (error) {
      console.error('Error submitting data:', error);
      // Handle error if necessary
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit} style={{ width: '60%' }}>
        <h2>Upload PDF here</h2>
        <div>
          <label>Description:</label>
          <textarea value={description} onChange={handleDescriptionChange} style={{ height: '200px', width: '100%' }} />
        </div>
        <br />
        <input type="file" className="form-control" accept="application/pdf" required onChange={handleFileChange} />
        <br />
        <button className="btn btn-primary" type="submit">
          Submit
        </button>
      </form>

      {console.log("About to print sortedCandidates in frontend!!")}

      {console.log(sortedCandidates)}

    {sortedCandidates.length > 0 && (
      <div>
        <br />
        <h3>Sorted Candidates</h3>
        <ul>
          {sortedCandidates.map((candidate, index) => (
            <li key={index}>{candidate[1]} - Score: {candidate[2]}</li>
          ))}
        </ul>
      </div>
    )}

    </div>
  );
}

export default Hr;

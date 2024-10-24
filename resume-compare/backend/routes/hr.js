const express = require('express');
const multer = require('multer');
const { execFile } = require('child_process');
const fs = require('fs');
const path = require('path');
const { MongoClient } = require('mongodb');

const router = express.Router();

// Middleware for parsing application/json
router.use(express.json());

// Set up Multer for file uploads
const upload = multer({ dest: 'uploads/' });

// Endpoint to handle file uploads and text extraction
router.post('/', upload.single('resume'), (req, res) => {

    console.log("Received POST request at /api/text");
  
    if (!req.file) {
        return res.status(400).send('No file uploaded.');
    }

    // const filePath = path.join(__dirname, req.file.path);

    const filePath = req.file.path;

    // console.log("req.file.path = " + req.file.path)
    // const description = req.body.description;

    const description = JSON.parse(req.body.description); // Parse the description string back into an array

    
    for (let index = 0; index < description.length; index++) {
        const element = description[index];
        console.log("element in hr.js = " + element)
        
    }




    const pythonScriptPath = path.join(__dirname, 'final2.py');

    console.log("req.file.path = " + filePath)

    // Run the Python script with the uploaded file
    execFile('python', [pythonScriptPath, filePath,description], (error, stdout, stderr) => {
        if (error) {
            console.error('Error executing Python script:', stderr);
            return res.status(500).send('Error processing file.');
        }

        // const sortedCandidates = stdout();

        const sortedCandidates = JSON.parse(stdout.trim());

        console.log("Trying to print sorted Candidates inside hr.js!!!")

        console.log(sortedCandidates)

        // Parse the Python script output
        // const extractedText = stdout.trim();

        // console.log("Life before extractedText")
        // console.log(extractedText)

        // Save extracted text to MongoDB

        res.json({ message: 'File processed successfully', sortedCandidates })

        saveToMongoDB(sortedCandidates, req.file.originalname)
            .then(() => {
                // Cleanup uploaded file
                fs.unlink(filePath, (err) => {
                    if (err) {
                        console.error('Error deleting uploaded file:', err);
                    }
                });

                // Send success response
                console.log("Trying to send data to frontend!!")
                res.json({ message: 'File processed successfully', sortedCandidates });

                // res.send(sortedCandidates);
            })
            .catch((err) => {
                console.error('Error saving to database:', err);
                res.status(500).send('Error saving to database.');
            });
    });
});

// Function to save extracted text to MongoDB
const saveToMongoDB = (text, fileName) => {
    return new Promise((resolve, reject) => {
        const url = 'mongodb://localhost:27017';
        const dbName = 'resumeData';

        MongoClient.connect(url, { useNewUrlParser: true, useUnifiedTopology: true }, (err, client) => {
            if (err) {
                return reject(err);
            }

            const db = client.db(dbName);
            const collection = db.collection('ResumeProject');

            const doc = { fileName, text, project: 'ResumeProject' };

            collection.insertOne(doc, (err, result) => {
                client.close();
                if (err) {
                    reject(err);
                } else {
                    resolve(result);
                }
            });
        });
    });
};

module.exports = router;

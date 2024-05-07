const express = require("express");
const { spawn } = require("child_process");
const path = require("path");
const router = express.Router();

// import { json } from "express";

// const bodyParser = require('body-parser');
const TextModel = require('../mongoose');

// app.use(bodyParser.json());


const executePython = async (script, args) => {
  console.log("Inside executePython");
  const arguments = args.map((arg) => arg.toString());

  const py = spawn("python", [script, ...arguments]);

  console.log("After py");

  let result = "";

  py.stdout.on("data", (data) => {
    console.log("About to print data");
    // const decoder = new TextDecoder('utf-8')
    // const decodedString = Buffer.from(data, 'utf-8').toString();
    console.log(data);
    result += data.toString();
    // console.log(result)
  });

  py.stderr.on("data", (data) => {
    console.error(`[python] Error occurred: ${data}`);
  });

  return new Promise((resolve, reject) => {
    py.on("exit", (code) => {
      console.log("Aman");
      console.log(`Child process exited with code ${code}`);
      if (code === 0) {
        resolve(result);
      } else {
        reject(`Error occurred in ${script}`);
      }
    });
  });
};

router.post("/", async (req, res) => {
  console.log("Inside hr");
  try {
    const { description, extractedText} = await req.body;
    // console.log(extractedText)
    // const newText = new TextModel({ description, extractedText});
    // await newText.save();
    // res.json({ message: 'Text data saved successfully' });
    const resume_text = extractedText;
    // const reqProduct = JSON.parser(product);

    console.log("Resume text: " + resume_text);

    const scriptPath = path.join(__dirname, "..", "pythonFiles3", "final2.py");
    // const scriptPath = "/python/similar_products.py";
    // const result = await executePython(scriptPath, ["camera"]);
    const result = await executePython(scriptPath, [resume_text]);

    console.log("Result from Python script:", result);

    res.json({ 'result': result});
  } catch (error) {
    console.error('Error saving text data:', error);
    res.status(500).json({ error: 'Internal server error' });
    console.log(error);
  }

});

module.exports = router;


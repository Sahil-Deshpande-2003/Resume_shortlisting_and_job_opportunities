require("dotenv").config();
const express = require("express");
const app = express();
const port = process.env.port || 3000;

const cors = require("cors");
// app.use(cors());
app.use(express.json());

// const cors = require('cors');
app.use(cors({ origin: 'http://localhost:5173' }));


const bodyParser = require('body-parser');
const TextModel = require('./mongoose');

app.use(bodyParser.json());



app.get("/", (req, res) => {
  res.send("Hello World!");
});

// Route for storing text data
// app.post('/api/text', async (req, res) => {
//     // Extract data from the request body
//     // const { description, extractedTextsAsString } = req.body;

//     // // Handle the data as needed (e.g., save to MongoDB)
//     // console.log('Received data:', { description, extractedTextsAsString });
  
//     // // Send a response (optional)
//     // res.status(200).send('Data received successfully');
//   try {
//     const { description, extractedText} = await req.body;
//     console.log(extractedText)
//     const newText = new TextModel({ description, extractedText});
//     await newText.save();
//     res.json({ message: 'Text data saved successfully' });
//   } catch (error) {
//     console.error('Error saving text data:', error);
//     res.status(500).json({ error: 'Internal server error' });
//   }
// });
app.use("/api/user", require("./routes/user"));
app.use("/api/text", require("./routes/hr"));
// app.use("/api/text", require("./routes/"))

app.listen(port, () => {
  console.log(`Compare Craft listening on port http://localhost:${port}`);
});

require("dotenv").config();
const express = require("express");
const app = express();
const port = process.env.port || 3000;

const cors = require("cors");
app.use(cors());
app.use(express.json());



const bodyParser = require('body-parser');
const TextModel = require('./mongoose');

app.use(bodyParser.json());



app.get("/", (req, res) => {
  res.send("Hello World!");
});


app.use("/api/text", require("./routes/hr"));

app.listen(port, () => {
  console.log(`Compare Craft listening on port http://localhost:${port}`);
});

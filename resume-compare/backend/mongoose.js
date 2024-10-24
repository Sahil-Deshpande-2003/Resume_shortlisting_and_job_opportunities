// mongoose.js

const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/resumeData', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for text data
const textSchema = new mongoose.Schema({
  description: String,
  extractedText: String,
});

// Create model
const TextModel = mongoose.model('Text', textSchema);

module.exports = TextModel;

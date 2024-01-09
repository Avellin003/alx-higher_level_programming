#!/usr/bin/node
const fs = require('fs');

// Get the file paths from command line arguments
const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

// Check if all arguments are provided
if (!sourceFilePath1 || !sourceFilePath2 || !destinationFilePath) {
  console.log('error');
  process.exit(1); // Exit with an error code
}

// Read the contents of the first source file
const content1 = fs.readFileSync(sourceFilePath1, 'utf8');

// Read the contents of the second source file
const content2 = fs.readFileSync(sourceFilePath2, 'utf8');

// Concatenate the contents of both files
const concatenatedContent = content1 + content2;

// Write the concatenated content to the destination file
fs.writeFileSync(destinationFilePath, concatenatedContent);

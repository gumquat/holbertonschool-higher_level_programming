const fs = require('fs');

function readFile(filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
	if (err) {
		console.error(err);
	} else {
		console.log(data);
	}
  });
}

const filePath = process.argv[2];
if (!filePath) {
	console.log('Please provide the file path as an argument.');
} else {
	readFile(filePath);
}


<h1 align="center">Hi 👋, I'm Evan Newman</h1>
<h3 align="center">A passionate frontend developer from Oklahoma</h3>

- 🔭 I’m currently working on [Full Stack Web Development](https://github.com/gumquat)

- 🌱 I’m currently learning **at Holberton School Tulsa**

- 🤝 I’m looking for help with **software to improve lives**

- 👨‍💻 All of my projects are available at [https://github.com/gumquat](https://github.com/gumquat)

- 💬 Ask me about **anything! I'm open to talk.**

- 📫 How to reach me **gumquat@gmail.com**

- ⚡ Fun fact **I NEED 2 monitors to function.**

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/evan newman" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="evan newman" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.blender.org/" target="_blank" rel="noreferrer"> <img src="https://download.blender.org/branding/community/blender_community_badge_white.svg" alt="blender" width="40" height="40"/> </a> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.cprogramming.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" alt="c" width="40" height="40"/> </a> <a href="https://www.cockroachlabs.com/product/cockroachdb/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/cockroachdb.svg" alt="cockroachdb" width="40" height="40"/> </a> <a href="https://www.w3schools.com/cs/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/csharp/csharp-original.svg" alt="csharp" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://gulpjs.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/gulp/gulp-plain.svg" alt="gulp" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.adobe.com/in/products/illustrator.html" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/adobe_illustrator/adobe_illustrator-icon.svg" alt="illustrator" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg" alt="nginx" width="40" height="40"/> </a> <a href="https://www.photoshop.com/en" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/photoshop/photoshop-line.svg" alt="photoshop" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> <a href="https://unity.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/unity3d/unity3d-icon.svg" alt="unity" width="40" height="40"/> </a> <a href="https://unrealengine.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/kenangundogan/fontisto/036b7eca71aab1bef8e6a0518f7329f13ed62f6b/icons/svg/brand/unreal-engine.svg" alt="unreal" width="40" height="40"/> </a> </p>

# Problem Solutions

## problem 0
```
#!/usr/bin/node
const fs = require('fs');

function readFile (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {

if (err) {
        console.error(err);
} else {
        console.log(data);
    }
  });
}

//if no filepath is provided this looks for one
//and then reads the file as normal using the readFile func
const filePath = process.argv[2];

if (!filePath) {
  console.error(err);
} else {
  readFile(filePath);
}
```
* 1. `const fs = require('fs');`: This line imports the built-in Node.js module `fs`, which provides file system-related functionality.
* 2. `function readFile(filePath) {`: This line defines a function named `readFile` that takes a `filePath` parameter. This function will be used to read the content of the file.
* 3. `fs.readFile(filePath, 'utf-8', (err, data) => {`: This line uses the `readFile` method from the `fs` module to read the content of the file specified by `filePath`. It takes three arguments: the file path, the encoding (in this case, 'utf-8' for UTF-8 encoding), and a callback function that will be executed when the reading is complete.
* 4. `if (err) { console.error(err); } else { console.log(data); }`: This block of code is the callback function passed to `readFile`. It checks if an error occurred during the reading. If an error exists, it is printed to the console using `console.error`. Otherwise, the content of the file is printed to the console using `console.log`.
* 5. `const filePath = process.argv[2];`: This line retrieves the file path from the command-line arguments. `process.argv` is an array that contains the command-line arguments passed to the script. The file path is stored in the variable `filePath`.
* 6. `if (!filePath) { console.log('Please provide the file path as an argument.'); } else { readFile(filePath); }`: This block of code checks if a file path was provided as a command-line argument. If no file path is provided, it prints a message asking the user to provide the file path. Otherwise, it calls the `readFile` function with the `filePath` argument to read and print the content of the file.

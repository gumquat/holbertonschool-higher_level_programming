<h1 align="center">Hi 👋, I'm Evan Newman</h1>
<h3 align="center">A passionate full stack web developer from Oklahoma</h3>

- 🔭 I’m currently working on [Full Stack Web Development](https://github.com/gumquat)

- 🌱 I’m currently learning **at Holberton School Tulsa**

- 🤝 I’m looking for help with **software to improve lives**

- 👨‍💻 All of my projects are available at [https://github.com/gumquat](https://github.com/gumquat)

- 💬 Ask me about **anything! I'm open to talk.**

- 📫 How to reach me **gumquat@gmail.com**

- ⚡ Fun fact **I NEED 2 monitors to function.**

<h3 align="left">Connect with me:</h3>
<p align="left">
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.blender.org/" target="_blank" rel="noreferrer"> <img src="https://download.blender.org/branding/community/blender_community_badge_white.svg" alt="blender" width="40" height="40"/> </a> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.cprogramming.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" alt="c" width="40" height="40"/> </a> <a href="https://www.cockroachlabs.com/product/cockroachdb/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/cockroachdb.svg" alt="cockroachdb" width="40" height="40"/> </a> <a href="https://www.w3schools.com/cs/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/csharp/csharp-original.svg" alt="csharp" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://gulpjs.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/gulp/gulp-plain.svg" alt="gulp" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.adobe.com/in/products/illustrator.html" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/adobe_illustrator/adobe_illustrator-icon.svg" alt="illustrator" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg" alt="nginx" width="40" height="40"/> </a> <a href="https://www.photoshop.com/en" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/photoshop/photoshop-line.svg" alt="photoshop" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> <a href="https://unity.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/unity3d/unity3d-icon.svg" alt="unity" width="40" height="40"/> </a> <a href="https://unrealengine.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/kenangundogan/fontisto/036b7eca71aab1bef8e6a0518f7329f13ed62f6b/icons/svg/brand/unreal-engine.svg" alt="unreal" width="40" height="40"/> </a> </p>

# NOTES per problem
## problem 0
```
#!/usr/bin/node
class Rectangle {
}
module.exports = Rectangle;
```
* Line 1: The #!/usr/bin/node line is a shebang line. Shebang lines are used to tell the operating system what interpreter to use to execute a file. In this case, the shebang line tells the operating system to use the Node.js interpreter to execute the file.
* Line 2-3: The class Rectangle {} line defines a new class called Rectangle. A class is a blueprint for creating objects. The Rectangle class has no properties or methods, so it is essentially a placeholder.
* Line 4: The module.exports = Rectangle; line exports the Rectangle class so that it can be used by other modules. The module.exports property is used to export variables and objects from a module. In this case, the module.exports property is exporting the Rectangle class.
## problem 1
```
#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
```
* Line 2-7: The class Rectangle {} line defines a new class called Rectangle. A class is a blueprint for creating objects. The Rectangle class has a constructor method that takes two arguments, w and h, which are the width and height of the rectangle. The constructor method sets the width and height properties of the Rectangle object to the values of w and h.
* Line 8: The module.exports = Rectangle; line exports the Rectangle class so that it can be used by other modules. The module.exports property is used to export variables and objects from a module. In this case, the module.exports property is exporting the Rectangle class.
## problem 2
```
#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
```
* Line 2-9: The class Rectangle {} line defines a new class called Rectangle. A class is a blueprint for creating objects. The Rectangle class has a constructor method that takes two arguments, w and h, which are the width and height of the rectangle. The constructor method checks if the width and height are greater than or equal to 1. If they are, the constructor method sets the width and height properties of the Rectangle object to the values of w and h.
* Line 10: The module.exports = Rectangle; line exports the Rectangle class so that it can be used by other modules. The module.exports property is used to export variables and objects from a module. In this case, the module.exports property is exporting the Rectangle class.
## problem 3
```
#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let xCounter;
    let yCounter;
    let output = '';
    for (xCounter = 0; xCounter < this.width; xCounter++) {
      output += 'X';
    }
    for (yCounter = 0; yCounter < this.height; yCounter++) {
      console.log(output);
    }
  }
}

module.exports = Rectangle;
```
* Line 2-8: The class Rectangle {} line defines a new class called Rectangle. A class is a blueprint for creating objects. The Rectangle class has a constructor method that takes two arguments, w and h, which are the width and height of the rectangle. The constructor method checks if the width and height are greater than or equal to 1. If they are, the constructor method sets the width and height properties of the Rectangle object to the values of w and h.
* Line 10-21: The print() method prints the rectangle to the console. The method starts by creating a variable called output and initializing it to an empty string. The method then loops through the width of the rectangle, adding an X to the output string for each iteration. The method then loops through the height of the rectangle, printing the output string to the console for each iteration.
* Line 23: The module.exports line exports the Rectangle class so that it can be used by other modules. The module.exports property is used to export variables and objects from a module. In this case, the module.exports property is exporting the Rectangle class.
## problem 4
```
#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let yCounter;
    for (yCounter = 0; yCounter < this.height; yCounter++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
```
* Line 2-8: The class Rectangle {} line defines a new class called Rectangle. A class is a blueprint for creating objects. The Rectangle class has a constructor method that takes two arguments, w and h, which are the width and height of the rectangle. The constructor method checks if the width and height are greater than or equal to 1. If they are, the constructor method sets the width and height properties of the Rectangle object to the values of w and h.
* Line 10-27:
  * The print() method prints the rectangle to the console. The method starts by creating a variable called yCounter and initializing it to 0. The method then loops through the height of the rectangle, printing a string of X characters to the console for each iteration. The length of the string is equal to the width of the rectangle.
  * The rotate() method rotates the rectangle by swapping the width and height properties of the Rectangle object.
  * The double() method doubles the width and height of the rectangle by multiplying them by 2.
* Line 29: The module.exports line exports the Rectangle class so that it can be used by other modules. The module.exports property is used to export variables and objects from a module. In this case, the module.exports property is exporting the Rectangle class.
## problem 5
```
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
```
* Line 2:  The const Rectangle = require('./4-rectangle'); line imports the Rectangle class from the file 4-rectangle.js. The require() function is used to import modules in Node.js. In this case, the require() function is importing the Rectangle class from the file 4-rectangle.js.
* Line 4-8:  The class Square extends Rectangle {} line defines a new class called Square. The Square class extends the Rectangle class. This means that the Square class inherits all of the properties and methods of the Rectangle class. The Square class also has a constructor method that takes one argument, size, which is the size of the square. The constructor method calls the super() method to pass the size argument to the Rectangle constructor method. This ensures that the Square object has the same width and height as the Rectangle object.
* Line 9: The module.exports = Square; line exports the Square class so that it can be used by other modules. The module.exports property is used to export variables and objects from a module. In this case, the module.exports property is exporting the Square class.
## problem 6
```
#!/usr/bin/node
const DefSquare = require('./5-square');

class Square extends DefSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let yCounter;
    for (yCounter = 0; yCounter < this.height; yCounter++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
```
* Line 2:  imports the DefSquare class from the file 5-square.js. The require() function is used to import modules in Node.js. In this case, the require() function is importing the DefSquare class from the file 5-square.js.
* Line 4-7:  defines a new class called Square. The Square class extends the DefSquare class. This means that the Square class inherits all of the properties and methods of the DefSquare class. The Square class also has a constructor method that takes one argument, size, which is the size of the square. The constructor method calls the super() method to pass the size argument to the DefSquare constructor method. This ensures that the Square object has the same width and height as the DefSquare object.
* Line 9-18: The charPrint() method prints the square to the console. The method starts by checking if the c argument is undefined. If it is, the method sets c to the string 'X'. The method then loops through the height of the square, printing a string of c characters to the console for each iteration. The length of the string is equal to the width of the square.
* Line 20: The module.exports = Square; line exports the Square class so that it can be used by other modules. The module.exports property is used to export variables and objects from a module. In this case, the module.exports property is exporting the Square class.
# problem 7
```
#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      counter += 1;
    }
  }
  return counter;
};
```
* Line 2:  defines a function called nbOccurences. The nbOccurences function takes two arguments, list and searchElement. The list argument is an array of elements, and the searchElement argument is the element that we are looking for in the array.
* Line 3:  declares a variable called counter and initializes it to 0. The counter variable will be used to keep track of the number of times the searchElement element appears in the list array.
* Line 4-10:
  *  starts a for loop that will iterate through the list array. The for loop will iterate list.length times, where list.length is the length of the list array.
  *  checks if the element at index i in the list array is equal to the searchElement element. If it is, the counter variable is incremented by 1.
  *  increments the counter variable by 1.
  *  returns the value of the counter variable. The counter variable contains the number of times the searchElement element appears in the list array.
# problem 8
```
#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 1; i > -1; i--) {
    newList.push(list[i]);
  }
  return newList;
};
```
* Line 2:  defines a function called esrever. The esrever function takes one argument, list. The list argument is an array of elements. The esrever function reverses the order of the elements in the list array.
* Line 3:  declares a variable called newList and initializes it to an empty array. The newList array will be used to store the reversed list of elements.
* Line 4-8:
  *  starts a for loop that will iterate through the list array in reverse order. The for loop will iterate list.length times, where list.length is the length of the list array.
  *  pushes the element at index i in the list array to the newList array.
  *  returns the value of the newList variable. The newList variable contains the reversed list of elements.
## problem 9
```
#!/usr/bin/node
let counter = 0;
exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter++;
};
```
* Line 2:  declares a variable called counter and initializes it to 0. The counter variable will be used to keep track of the number of times the logMe function has been called.
* Line 3-6:
  *  defines a function called logMe. The logMe function takes one argument, item. The item argument is the element that we want to log.
  *  logs the value of the counter variable, followed by a colon, followed by the value of the item argument.
  *  increments the counter variable by 1.
## problem 10
```
#!/usr/bin/node
exports.converter = function (base) {
  return function converToBaseN (num) {
    return (num.toString(base));
  };
};
```
* Line 2-6:
  *   defines a function called converter. The converter function takes one argument, base. The base argument is the base that we want to convert the number to.
  *   defines a nested function called converToBaseN. The converToBaseN function takes one argument, num. The num argument is the number that we want to convert to base base.
  *   returns the string representation of the number num in base base.

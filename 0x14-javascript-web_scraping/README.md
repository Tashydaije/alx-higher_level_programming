## JavaScript - Web scraping
# Learning Objectives

# Why JavaScript programming is amazing

* Browser compatibility: Since JavaScript is the language of the web, it can interact directly with web pages in a browser environment, making it ideal for scraping dynamic content.
* Asynchronous capabilities: JavaScript supports asynchronous programming, which is crucial for handling multiple HTTP requests efficiently during web scraping.
* DOM manipulation: JavaScript allows you to manipulate the Document Object Model (DOM) of a webpage, making it easy to extract and interact with specific elements on the page.
* Libraries and frameworks: There are many JavaScript libraries and frameworks available for web scraping, such as Puppeteer and Cheerio, which provide powerful tools for automating browser interactions and parsing HTML respectively.

# How to manipulate JSON data

* JSON.parse(): This method is used to parse a JSON string and convert it into a JavaScript object.
* JSON.stringify(): This method is used to convert a JavaScript object into a JSON string.
* You can also access and modify JSON data like any other JavaScript object, using dot notation or bracket notation.

# How to use request and fetch API

* Request API: In Node.js, you can use the request module to make HTTP requests. First, you need to install the module using npm (npm install request). Then, you can use it to send GET, POST, PUT, DELETE, etc., requests to a server and handle the responses.
* Fetch API: In the browser environment, you can use the Fetch API to make HTTP requests. It provides a more modern and flexible interface compared to the older XMLHttpRequest (XHR) object. You can use fetch() to make requests and handle responses using promises or async/await syntax.

# How to read and write a file using fs module

In Node.js, the fs module provides functions for interacting with the file system.
* To read a file, you can use fs.readFile() or fs.readFileSync() to asynchronously or synchronously read the contents of a file respectively.
* To write to a file, you can use fs.writeFile() or fs.writeFileSync() to asynchronously or synchronously write data to a file respectively.
* Additionally, there are other functions available in the fs module for manipulating files and directories, such as fs.rename(), fs.unlink(), fs.readdir(), etc.

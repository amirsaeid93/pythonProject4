'use strict';
const names = ['John', 'Paul', 'Jones'];

// Get the element with id="target"
const targetElement = document.getElementById('target');

// Create a string to hold the HTML content
let htmlContent = '';

// Loop through the names array and create <li> elements
for (let i = 0; i < names.length; i++) {
htmlContent += `<li>${names[i]}</li>`;
}

// Set the innerHTML of the target element to the generated HTML content
targetElement.innerHTML = htmlContent;
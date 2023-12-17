'use strict';

const names = ['John', 'Paul', 'Jones'];


const targetElement = document.getElementById('target');


let htmlContent = '';


for (let i = 0; i < names.length; i++) {
htmlContent += `<li>${names[i]}</li>`;
}


targetElement.innerHTML = htmlContent;
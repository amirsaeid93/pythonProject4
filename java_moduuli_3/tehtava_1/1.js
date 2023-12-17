// Get the element by its ID
let targetElement = document.getElementById('target');

// Add the class 'my-list' to the element
targetElement.classList.add('my-list');

// Define the list items
let listItems = `
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
`;

// Append the list items to the element using innerHTML
targetElement.innerHTML += `<ul>${listItems}</ul>`;

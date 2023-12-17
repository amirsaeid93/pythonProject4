'use strict'
const form = document.getElementById('searchForm');

form.addEventListener('submit', async function(event) {
event.preventDefault();


const userInput = document.getElementById('query').value;

// Make a request to the TVMaze API
const response = await fetch(`https://api.tvmaze.com/search/shows?q=${userInput}`);
const data = await response.json();

if (data && data.length > 0) {
const show = data[0].show;
console.log('Show Name:', show.name);
console.log('Show ID:', show.id);
console.log('Show Summary:', show.summary);
console.log('Show URL:', show.url);

} else {
console.log('Sorry, no information was found regarding the inputed TV show.');
}
});
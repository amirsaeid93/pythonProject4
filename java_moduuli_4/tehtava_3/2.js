'use strict'

const form = document.getElementById('searchForm');

const resultsContainer = document.getElementById('results');

form.addEventListener('submit', async function(event) {
event.preventDefault();


const userInput = document.getElementById('query').value;


const response = await fetch(`https://api.tvmaze.com/search/shows?q=${userInput}`);
const data = await response.json();

resultsContainer.innerHTML = '';

if (data && data.length > 0) {

const show = data[0].show;

const article = document.createElement('article');
const heading = document.createElement('h2');
heading.textContent = show.name;

const link = document.createElement('a');
link.href = show.url;
link.textContent = 'Show Details';
link.target = '_blank';

const image = document.createElement('img');
image.src = show.image?.medium || 'https://via.placeholder.com/210x295';
image.alt = show.name;

const summary = document.createElement('div');
summary.innerHTML = show.summary;


article.appendChild(heading);
article.appendChild(link);
article.appendChild(image);
article.appendChild(summary);


resultsContainer.appendChild(article);
} else {
resultsContainer.textContent = 'No information found about the searched TV show.';
}
});

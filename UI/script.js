import { fetchArticles } from './http-calls.js';

const articles = await fetchArticles();
const articleGrid = document.querySelector('.article-grid');

console.log(articles);

articles.forEach((article) => {
  const row = document.createElement('div');
  const articleUrl = `//${article.articleUrl}`;
  row.classList.add('grid-item');
  
  row.innerHTML = `
    <div><img class="article-img" src="${article.pictureUrl}" alt="Article image"></div>
    <div><a href="${articleUrl}" target="_blank">${article.title}</a></div>
    <div class="date">${new Date(article.date).toLocaleDateString('ro-RO', { day: 'numeric', month: 'long', year: 'numeric' })}</div>
    <div class="provider">${article.provider}</div>
  `;
  articleGrid.appendChild(row);
});

import { fetchArticles } from './http-calls.js';

const articles = await fetchArticles();
const newsContainer = document.querySelector('.news-container');

console.log(articles);

articles.forEach((article) => {
  const row = document.createElement('div');
  const articleUrl = `//${article.articleUrl}`;
  row.classList.add('row');
  
  row.innerHTML = `
    <div class="col-lg-2"><img class="article-img" src="${article.pictureUrl}" alt="Article image"></div>
    <div class="col-lg-6"><a href="${articleUrl}" target="_blank">${article.title}</a></div>
    <div class="col-lg-2">${new Date(article.date).toLocaleDateString('ro-RO', { day: 'numeric', month: 'long', year: 'numeric' })}</div>
    <div class="col-lg-2">${article.provider}</div>
  `;
  newsContainer.appendChild(row);
});

import { fetchArticles } from './http-calls.js';

const articles = await fetchArticles();

const truncatedArticles = articles.map(article => {
  if (article.title.length > 90) {
    return {...article, title: article.title.slice(0, 90) + '...'};
  } else {
    return article;
  }
});

const articleGrid = document.querySelector('.article-grid');

console.log(articles);

truncatedArticles.forEach((article) => {
  const row = document.createElement('div');
  const articleUrl = `//${article.articleUrl}`;
  row.classList.add('grid-item');
  
  row.innerHTML = `
    <div class="article-box">
      <div><img class="article-img" src="${article.pictureUrl}" alt="Article image"></div>
      <div><a href="${articleUrl}" target="_blank">${article.title}</a></div>
    </div>
    <div class="date">${new Date(article.date).toLocaleDateString('ro-RO', { day: 'numeric', month: 'long', year: 'numeric' })}</div>
    <div class="provider">${article.provider}</div>
  `;
  articleGrid.appendChild(row);
});

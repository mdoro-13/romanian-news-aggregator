import { fetchArticles } from './http-calls.js';
import { getProviderClass } from './utils.js';

let articles = [];
let lastArticleDate = null;
let stopScroll = false;
let keyword = '';

const truncateTitle = (title) => {
  return title.length > 90 ? title.slice(0, 90) + '...' : title;
};

const createArticleElement = (article) => {
  const articleUrl = `//${article.articleUrl}`;
  const row = document.createElement('div');
  const providerClass = getProviderClass(article)
  row.classList.add('grid-item');
  row.innerHTML = `
    <div class="article-box">
      <div><img class="article-img" src="${article.pictureUrl}" alt="Image not found" onerror="this.src='./assets/white.png';"></div>
      <div><a href="${articleUrl}" target="_blank">${truncateTitle(article.title)}</a></div>
    </div>
    <div class="info-box">
      <div class="date-posted">${new Date(article.date).toLocaleDateString('ro-RO', { day: 'numeric', month: 'long', year: 'numeric' })}</div>
      <div class="provider ${providerClass}">${article.provider}</div>
    </div>
  `;
  return row;
};

const loadArticles = async () => {
  if (!stopScroll) {
    let newArticles = [];
    // Load next page
    const datePosted = lastArticleDate;
    newArticles = await fetchArticles({ datePosted, keyword });
    if (newArticles.length > 0) {
      articles = newArticles;
      lastArticleDate = articles[newArticles.length - 1].date;
      const articleElements = newArticles.map(article => createArticleElement(article));
      articleElements.forEach(articleElement => {
        articleGrid.appendChild(articleElement);
      });
    }
    else {
      stopScroll = true;
    }
  }
};

const handleScroll = () => {
  const scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
  const triggerAt = document.documentElement.offsetHeight - window.innerHeight - 100;
  if (scrollPosition > triggerAt) {
    loadArticles();
  }
};

function addSearchByKeyword() {
  let timeoutId;
  const inputElement = document.querySelector('.search-bar');
  inputElement.addEventListener('input', (event) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      keyword = event.target.value;
      console.log(keyword)
      lastArticleDate = null;
      stopScroll = false;
      articles = []
      articleGrid.innerHTML = ''
      loadArticles();
    }, 500); 
  });
}


const articleGrid = document.querySelector('.article-grid');
window.addEventListener('scroll', handleScroll);
loadArticles();
addSearchByKeyword()


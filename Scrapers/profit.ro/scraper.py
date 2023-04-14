from bs4 import BeautifulSoup
import requests
from datetime import date, timedelta
import hashlib

URL = 'https://www.profit.ro/toate'
provider = 'profit.ro'


def get_date(featured_date):
    # we scrape the first page only for news
    # not expecting any results to be before yesterday
    date_added = date.today()
    if 'ieri' in featured_date:
        date_added = date_added - timedelta(days=1)
    return date_added

def get_featured_article(provider, soup):
    featured = soup.find(class_='feature')
    featured_anchor = featured.find('a', href=True)
    featured_url = provider + featured_anchor['href']
    featured_title = featured_anchor.get('title')
    featured_str_date = featured.find(class_='publish-date').text
    date_added = get_date(featured_str_date)
    
    return {
        'title': featured_title,
        'url': featured_url,
        'provider': provider,
        'date': date_added,
    }

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
scraped_articles = []
featured_article = get_featured_article(provider, soup)
scraped_articles.append(featured_article)

articles_section = soup.find(class_='articles')
articles = articles_section.find_all(class_='col-xs-12 col-sm-8 col-md-9')
for article in articles:
    article_anchor = article.find('a', href=True)
    article_url = provider + article_anchor['href']
    article_title = article_anchor.get('title')
    article_str_date = article.find(class_='publish-date').text
    article_date = get_date(article_str_date)

    insert_article = {
        'title': article_title,
        'url': article_url,
        'provider': provider,
        'date': article_date
    }

    scraped_articles.append(insert_article)

for article in scraped_articles:
    for key, value in article.items():
        print(f"{key}: {value}")
    print('\n')
    print('-' * 20)



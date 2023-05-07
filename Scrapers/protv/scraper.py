from datetime import datetime
import uuid
from utils.date_handler import get_date
from utils import response_handler
from utils.fetch_below import scrape_limit



URL = 'https://stirileprotv.ro/ultimele-stiri/'

def get_articles():
    parsed_html = response_handler.parse_response(URL)
    provider = 'protv'

    article_div = parsed_html.find('div', class_='content')
    articles= article_div.find_all('article', class_='grid')
    scraped_articles = []

    count = 0
    for article in articles:
        if (count == scrape_limit):
            break

        article_title = article.find(class_='article-lead').text.strip()
        article_url = article.find('a')['href']
        img_url = article.find('img')['data-src']
        article_str_date = article.find('div', class_='article-date').text
        date = get_date(article_str_date)

        extracted_article = {
            'id': str(uuid.uuid4()),
            'title': article_title,
            'article_url': article_url,
            'provider_id': 5,
            'date': get_date(date),
            'scrape_date': datetime.now(),
            'picture_url': img_url
        }
        
        scraped_articles.append(extracted_article)

    return scraped_articles




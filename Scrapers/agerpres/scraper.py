from utils import date_handler, response_handler, image_handler
import uuid
from datetime import datetime

URL = 'https://www.agerpres.ro/'

def get_articles():
    parsed_html = response_handler.parse_response(URL)
    return get_article_grid(parsed_html)


def get_article_grid(parsed_html):
    grid = parsed_html.find(class_='wrapper_news_articles')
    grid_articles = grid.find_all('article')
    extracted_articles = []

    for article in grid_articles:
        article_title = article.find('h2').text.strip()
        article_url = 'agerpres.ro' + article.find("a")["href"]
        img_url = article.find("img")["src"]
        date = article.find('time')['datetime']

        extracted_article = {
            'id': str(uuid.uuid4()),
            'title': article_title,
            'article_url': article_url,
            'provider_id': 4,
            'date': date,
            'scrape_date': datetime.now(),
            'picture_url': img_url
        }

        extracted_articles.append(extracted_article)

    return extracted_articles
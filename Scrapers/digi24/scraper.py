from utils.date_handler import get_date
from utils import response_handler
import uuid
from datetime import datetime
from utils.fetch_below import scrape_limit


URL = 'https://www.digi24.ro/ultimele-stiri'


def get_articles():
    parsed_html = response_handler.parse_response(URL)
    return get_article_grid(parsed_html)

def get_article_grid(parsed_html):
    grid = parsed_html.find(class_='col-10 col-md-12')
    grid_articles = grid.find_all('article', class_='article brdr')
    extracted_articles = []

    ## the grid is long, take only the first 10
    count = 0
    for article in grid_articles:
        if count == scrape_limit:
            break
        article_title = article.find(class_='article-title').text.strip()
        article_url = 'digi24.ro' + article.find("a")["href"]
        img_url = article.find("img")["src"]
        date = article.find('time')['datetime']

        extracted_article = {
            'id': str(uuid.uuid4()),
            'title': article_title,
            'article_url': article_url,
            'provider_id': 3,
            'date': get_date(date),
            'scrape_date': datetime.now(),
            'picture_url': img_url
        }

        extracted_articles.append(extracted_article)
        count += 1

    return extracted_articles







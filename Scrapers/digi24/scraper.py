from utils import date_handler, response_handler, image_handler
import uuid
from datetime import datetime

URL = 'https://www.digi24.ro/ultimele-stiri'


def get_articles():
    parsed_html = response_handler.parse_response(URL)
    scraped_articles = get_article_grid(parsed_html)

    for article in scraped_articles:
        print(article['title'])
        print(article['article_url'])
        print(article['picture_url'])
        print(article['date'])
        print('-'*100)
    return scraped_articles

def get_article_grid(parsed_html):
    grid = parsed_html.find(class_='col-10 col-md-12')
    grid_articles = grid.find_all('article', class_='article brdr')
    extracted_articles = []

    ## the grid is long, take only the first 10
    count = 0
    for article in grid_articles:
        if count == 10:
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
            'date': date,
            'scrape_date': datetime.now(),
            'picture_url': img_url
        }

        extracted_articles.append(extracted_article)
        count += 1

    return extracted_articles







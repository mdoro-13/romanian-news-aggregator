from utils.image_handler import get_image
from utils import response_handler, image_handler
import uuid
from datetime import datetime, timedelta
from utils.date_handler import get_date
from utils.sanitize import strip_url
from utils.fetch_below import scrape_limit


URL = 'https://www.g4media.ro/'

def get_articles():
    parsed_html = response_handler.parse_response(URL)
    return get_article_grid(parsed_html)


def get_article_grid(parsed_html):
    grid = parsed_html.find(class_='articole-grid')
    grid_articles = grid.find_all(class_='post-review')
    extracted_articles = []

    count = 0
    for article in grid_articles:
        if count == scrape_limit:
            break
        article_title = article.find(class_='post-title').text.strip()
        article_url = article.find('a')['href']
        post_img = article.find(class_='post-img')
        all_img = post_img.find_all('img')
        img_url = ''
        for img in all_img:
            src = img['src']
            if 'cdn.g4media' in src:
                img_url = src
                break
        date = datetime.now()

        extracted_article = {
            'id': str(uuid.uuid4()),
            'title': article_title,
            'article_url': strip_url(article_url),
            'provider_id': 4,
            'date': date,
            'scrape_date': date,
            'picture_url': img_url
        }

        extracted_articles.append(extracted_article)
        count += 1

    return extracted_articles
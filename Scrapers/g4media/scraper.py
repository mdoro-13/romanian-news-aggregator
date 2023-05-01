from utils import response_handler, image_handler
import uuid
from datetime import datetime, timedelta
from utils.date_handler import get_date
from utils.sanitize import strip_url


URL = 'https://www.g4media.ro/'

def get_articles():
    parsed_html = response_handler.parse_response(URL)
    return get_article_grid(parsed_html)


def get_article_grid(parsed_html):
    grid = parsed_html.find(class_='articole-grid')
    grid_articles = grid.find_all(class_='post-review')
    extracted_articles = []

    ## the grid is long, take only the first 10
    count = 0
    for article in grid_articles:
        if count == 10:
            break
        article_title = article.find(class_='post-title').text.strip()
        article_url = article.find('a')['href']
        img_src_all = article.find_all('img')
        img_url = ''
        if len(img_src_all) >=1:
            img_url = img_src_all[1]['src']
        str_date = article.find(class_='entry-date').text.strip()

        ## TODO
        ## g4media always stores their dates as '1 mai 2023' for example which will be parsed to 00:00 + timestamp
        ## will need to generate some hours so that they won't always be at the bottom
        date = get_date(str_date)

        extracted_article = {
            'id': str(uuid.uuid4()),
            'title': article_title,
            'article_url': strip_url(article_url),
            'provider_id': 5,
            'date': date,
            'scrape_date': datetime.now(),
            'picture_url': img_url
        }

        extracted_articles.append(extracted_article)
        count += 1

    return extracted_articles
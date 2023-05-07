from utils import response_handler, image_handler
import uuid
from datetime import datetime
from utils.sanitize import strip_url
from utils.date_handler import get_date
from utils.fetch_below import limit



URL = 'https://www.hotnews.ro/'


def get_articles():
    parsed_html = response_handler.parse_response(URL)
    return get_latest_articles(parsed_html)

def get_latest_articles(parsed_html):
    latest_section = parsed_html.find('div', class_='ultima-ora-dreapta')

    articles = latest_section.find_all('a')
    articles.pop(0)
    extracted_articles = []

    count = 0
    for article in articles:
        if (count == limit):
            break
        article_title = article.find('h1', class_='title').text.strip()
        article_url = article['href']
        img_url = ''
        date_section = get_date_section(article)
        date = parse_date(date_section)

        extracted_article = {
            'id': str(uuid.uuid4()),
            'title': article_title,
            'article_url': strip_url(article_url),
            'provider_id': 2,
            'date': date,
            'scrape_date': datetime.now(),
            'picture_url': img_url
        }

        extracted_articles.append(extracted_article)
        count+=1

    return extracted_articles


def get_date_section(parent_section):
    return parent_section.find(class_='ora')


def parse_date(date_section):
    raw_date = date_section.contents[0].strip().split(' ')[0]
    return get_date(raw_date)




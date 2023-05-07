from datetime import datetime
import uuid

from utils.sanitize import strip_url

from utils.image_handler import get_image
from utils.date_handler import get_date
from utils import response_handler, sanitize
from utils.fetch_below import scrape_limit

URL = 'https://www.libertatea.ro/stiri'

def get_articles():
    parsed_html = response_handler.parse_response(URL)
    articles = parsed_html.find_all('div', class_='news-item')
    scraped_articles = []
    count = 0
    for article in articles:
        if (count == scrape_limit):
            break
        anchor = article.find('a')
        article_title = anchor['title'].strip()
        article_url = anchor['href']

        img_section = article.find('picture')
        img_url = img_section.find('img')['data-src']
        article_str_date = get_str_date(article)
        date = get_date(article_str_date)

        extracted_article = {
            'id': str(uuid.uuid4()),
            'title': article_title,
            'article_url': strip_url(article_url),
            'provider_id': 6,
            'date': get_date(date),
            'scrape_date': datetime.now(),
            'picture_url': img_url
        }

        print(extracted_article['title'])
        print(extracted_article['article_url'])
        print(extracted_article['date'])
        print(extracted_article['picture_url'])
        print('*' * 10)
        scraped_articles.append(extracted_article)
        count+=1

    return scraped_articles

def get_str_date(article):
    time_section = article.find('time')
    if time_section is not None:
        return time_section['datetime']
    
    time_or_date_section = article.find('span', class_='time-or-date')
    if time_or_date_section is not None:
        print ('RETURN  time_or_date_section')
        return time_or_date_section.text

    now_utc = datetime.utcnow()
    return now_utc.strftime('%Y-%m-%d %H:%M:%S.%f UTC')


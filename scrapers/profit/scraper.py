from utils import date_handler, response_handler
import uuid
from datetime import datetime

URL = 'https://www.profit.ro/toate'


def get_image(parsed_html):
    img = parsed_html.find('img')
    return img['src']


def get_featured_article(provider, parsed_html):
    featured = parsed_html.find(class_='feature')
    featured_anchor = featured.find('a', href=True)
    featured_url = provider + featured_anchor['href']
    featured_title = featured_anchor.get('title')
    featured_str_date = featured.find(class_='publish-date').text
    date_added = date_handler.get_date(featured_str_date)
    image = get_image(featured)

    return {
        'id': str(uuid.uuid4()),
        'title': featured_title,
        'article_url': featured_url,
        'provider_id': 1,
        'date': date_added,
        'scrape_date': datetime.now(),
        'picture_url': image
    }


def get_articles():
    parsed_html = response_handler.parse_response(URL)
    provider = 'profit.ro'

    scraped_articles = []
    featured_article = get_featured_article(provider, parsed_html)
    scraped_articles.append(featured_article)
    articles_section = parsed_html.find(class_='articles')
    articles = articles_section.find_all(class_='col-xs-12 col-sm-8 col-md-9')
    images = articles_section.find_all(class_='col-xs-12 col-sm-4 col-md-3')
    count = 0

    for article in articles:
        article_anchor = article.find('a', href=True)
        article_url = provider + article_anchor['href']
        article_title = article_anchor.get('title')
        article_str_date = article.find(class_='publish-date').text
        article_date = date_handler.get_date(article_str_date)
        article_image = get_image(images[count])

        insert_article = {
            'id': str(uuid.uuid4()),
            'title': article_title,
            'article_url': article_url,
            'provider_id': 1,
            'date': article_date,
            'scrape_date': datetime.now(),
            'picture_url': article_image
        }

        scraped_articles.append(insert_article)
        count += 1

    return scraped_articles

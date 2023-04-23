from utils import date_handler, response_handler, image_handler
import uuid
from datetime import datetime

URL = 'https://www.hotnews.ro/'


def get_articles():
    parsed_html = response_handler.parse_response(URL)
    scraped_articles = []
    first_main_article = get_single_article(parsed_html, 'ob-1')
    scraped_articles.append(first_main_article)

    main_grid_articles = get_articles_from_main_grid(parsed_html)
    scraped_articles.extend(main_grid_articles)

    second_main_article = get_single_article(parsed_html, 'ob-2')
    scraped_articles.append(second_main_article)

    third_main_article = get_single_article(parsed_html, 'ob-3')
    scraped_articles.append(third_main_article)

    return scraped_articles


def get_single_article(parsed_html, class_name):
    first_article_section = parsed_html.find('article', {'id': class_name})
    img_section = first_article_section.find(class_='pic poz-1')
    title_section = first_article_section.find(class_='snip poz-1')
    date_section = first_article_section.find(class_='ora')
    article_anchor = title_section.find('a', href=True)

    article_url = article_anchor['href']
    article_title = article_anchor['aria-label'].strip()
    img_url = image_handler.get_image(img_section)
    date = parse_date(date_section)
    return {
        'id': str(uuid.uuid4()),
        'title': article_title,
        'article_url': strip_url(article_url),
        'provider_id': 2,
        'date': date,
        'scrape_date': datetime.now(),
        'picture_url': img_url
    }


def get_articles_from_main_grid(parsed_html):
    main_grid = parsed_html.find(class_='grid-2x3x1')
    articles = main_grid.find_all("article", class_="art")

    extracted_articles = []
    for article in articles:
        article_title = article.find("h1", class_="title").text.strip()
        article_url = article.find("a", class_="snip")["href"]
        img_url = article.find("img")["src"]
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

    return extracted_articles


def get_date_section(parent_section):
    return parent_section.find(class_='ora')


def parse_date(date_section):
    raw_date = date_section.contents[0].strip().split(' ')[0]
    return date_handler.get_date(raw_date)


def strip_url(url):
    return url.split("://")[1]

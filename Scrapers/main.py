from profit import scraper as profit_ro_scraper
from hotnews import scraper as hotnews_scraper
from digi24 import scraper as digi24_scraper
from agerpres import scraper as agerpres_scraper
from g4media import scraper as g4media_scraper
from db_operations import commands


def main():
    profit_ro_articles = profit_ro_scraper.get_articles()
    hotnews_articles = hotnews_scraper.get_articles()
    digi24_articles = digi24_scraper.get_articles()
    g4media_articles = g4media_scraper.get_articles()
    # agerpres_articles = agerpres_scraper.get_articles()

    for article in g4media_articles:
        print(article['title'])
        print(article['article_url'])
        print(article['picture_url'])
        print(article['date'])
        print('-'*100)

    all_articles = profit_ro_articles + hotnews_articles + digi24_articles + g4media_articles

    for article in all_articles:
        if len(article['title']) > 255:
            article['title'] = article['title'][:255]

    commands.insert_articles(all_articles)


if __name__ == '__main__':
    main()

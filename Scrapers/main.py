from profit import scraper as profit_ro_scraper
from hotnews import scraper as hotnews_scraper
from digi24 import scraper as digi24_scraper
from g4media import scraper as g4media_scraper
from protv import scraper as protv_scraper
from libertatea import scraper as liberatatea_scraper
from db_operations import commands

def ensure_unqiue(all_articles):
    unique_urls = {item['article_url'] for item in all_articles}

    return [item for item in all_articles if item['article_url'] in unique_urls]


def main():
    profit_ro_articles = profit_ro_scraper.get_articles()
    hotnews_articles = hotnews_scraper.get_articles()
    digi24_articles = digi24_scraper.get_articles()
    g4media_articles = g4media_scraper.get_articles()
    protv_articles = protv_scraper.get_articles()
    libertatea_articles = liberatatea_scraper.get_articles()

    all_articles = profit_ro_articles + hotnews_articles + digi24_articles + g4media_articles + protv_articles + libertatea_articles
    all_articles = ensure_unqiue(all_articles)

    for article in all_articles:
        if len(article['title']) > 255:
            article['title'] = article['title'][:255]

    commands.insert_articles(all_articles)


if __name__ == '__main__':
    main()



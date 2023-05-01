from profit import scraper as profit_ro_scraper
from hotnews import scraper as hotnews_scraper
from db_operations import commands


def main():
    print ('Fetching articles...')
    profit_ro_articles = profit_ro_scraper.get_articles()
    hotnews_articles = hotnews_scraper.get_articles()

    all_articles = profit_ro_articles + hotnews_articles
    commands.insert_articles(all_articles)


if __name__ == '__main__':
    main()

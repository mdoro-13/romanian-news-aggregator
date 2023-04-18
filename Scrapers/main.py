from profit import scraper
from db_operations import commands


def main():
    profit_ro_articles = scraper.get_articles()
    commands.insert_articles(profit_ro_articles)

if __name__ == '__main__':
    main()

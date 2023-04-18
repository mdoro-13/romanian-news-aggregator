from profit import scraper


def main():
    profit_ro_articles = scraper.get_articles('profit.ro')


if __name__ == '__main__':
    main()

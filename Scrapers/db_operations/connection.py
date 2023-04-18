import os
import psycopg2


def get():
    database = os.environ.get('NEWS_DB_NAME')
    user = os.environ.get('NEWS_DB_USER')
    password = os.environ.get('NEWS_DB_PASSWORD')
    host = os.environ.get('NEWS_DB_HOST')
    port = os.environ.get('NEWS_DB_PORT')
    return psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

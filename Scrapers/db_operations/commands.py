from db_operations import connection
import psycopg2


def insert_articles(articles):
    conn = connection.get()
    cursor = conn.cursor()

    try:
        cursor.executemany("""
            INSERT INTO articles (id, title, date, scrape_date, article_url, picture_url, provider_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s) 
            ON CONFLICT (title, article_url) DO NOTHING
            """, [
            (a['id'], a['title'], a['date'], a['scrape_date'], a['article_url'], a['picture_url'], a['provider_id']) for
            a in articles])
        conn.commit()
    except psycopg2.errors.UniqueViolation:
        print("Skipping duplicate articles")
    finally:
        cursor.close()
        conn.close()

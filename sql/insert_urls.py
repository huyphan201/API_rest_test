from newspaper import Article
import sqlite3
import insert_news

class urls_insert:

    def get_url_crawled(conn,d,url):
        sql = """
                INSERT INTO urlnews(names, urlsnews)
                VALUES (?, ?)
                """
        
        conn.execute(sql, (d,url))
        conn.commit()
        t = insert_news.add_news(conn,url)
        conn.close()

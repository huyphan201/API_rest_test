import sqlite3
import newspaper

def get_all(query):
    conn = sqlite3.connect("data/newsdb")
    dt = conn.execute(query).fetchall()
    conn.close()

    return dt

def get_news_by_id(news_id):
        conn = sqlite3.connect("data/newsdb.news-db.db")
        sql = """
        SELECT N.domain, N.title, N.time, N.description, N.image, N.content, N.author, N.tags, N.meta, U.names, U.urlsnews
        FROM news N INNER JOIN urlnews U on N.url_id=U.id
        WHERE id=?
        """
        news = conn.execute(sql, (news_id, )).fetchone()
        conn.close()

        return news

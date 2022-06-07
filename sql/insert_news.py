from newspaper import Article
import sqlite3


def add_news(conn, url):
    sql = """
                INSERT INTO news(title, time, description, image, content, author)
                VALUES (?, ?, ?, ?, ?, ?)
                """
        #print(url)
    try:
        article = Article(url)
        article.download()
        article.parse()
    except:
        pass

    title = article.title
    time = article.publish_date
    descrip = "".join(article.text.split("\n")[0])
    img  = article.top_image
    content = " ".join(article.text.split("\n")[1:])
    authors = "".join(article.authors)
    #ags = ",".join(article.tags)
    #meta = article.meta_data
    #print(tags)
    conn.execute(sql, (title, time, descrip, img,
                                    content, authors))
    conn.commit()
   # return (title, time, descrip, img,content, authors, url_id)


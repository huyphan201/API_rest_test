from newspaper import Article
import sqlite3
import newspaper

from insert_urls import urls_insert

import sys
sys.path.append("/home/norii/NORII/test/url_news")
from js_url import in_out
sys.path.append("/home/norii/NORII/test/url_news")
from url_up import sosa_file
from js_url import in_out


class sqlite_dt:


    def get_news_urls(d,lik):
        conn = sqlite3.connect("/home/norii/NORII/test/data/newsdb")
        if d in lik:
            t = urls_insert.get_url_crawled(conn,d,lik)

        conn.close()


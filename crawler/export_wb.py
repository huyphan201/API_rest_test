import sys
sys.path.append("/home/norii/NORII/test/crawler")
from crawler_link import crawl_link_web
sys.path.append("/home/norii/NORII/test/url_news")
from js_url import in_out
from url_up import sosa_file
import url_df
sys.path.append("/home/norii/NORII/test/sql")
from sql import sqlite_dt


class export_web:

	def export_link():
		lit = []
		print("1__")
		file = in_out.json_input()
		for f in file:
			d = f["web_name"]
			print("==>",d)
			co = crawl_link_web(f["link_domain"],f["cate_select"],f["links_select"])
			li = tuple(set(co.getcate()))
			ur = tuple(set(co.getlink(li)))
			
			for u in ur[:5]:
				t = sqlite_dt.get_news_urls(d,u)
		
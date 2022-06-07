import json 
import os
from datetime import datetime
import sys
sys.path.append("/home/norii/NORII/test/url_news")
from url_up import sosa_file


class in_out:

	def json_input():
		print("3__")
		
		with open("/home/norii/NORII/test/data/domain.json") as js:
			dt = json.load(js)
			doms = dt["js_web"]
			return doms


	def json_output(url, web_name):

		
		#for ur in url:

			# old = sosa_file.url_up()
			# ss_ur = sosa_file.url_if(ur,old)
			
		with open("/home/norii/NORII/test/data/output/_{}_data.json".format(web_name),'a',encoding="utf-8") as nf:
			json.dump(url, nf, indent=4,ensure_ascii=False)
				#f.write(ss_ur+"\n")

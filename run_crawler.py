# import json
# import os
# import requests
# from lxml.html import fromstring
# from apscheduler.schedulers.blocking import BlockingScheduler
# #############################
import sys  
sys.path.append("/home/norii/NORII/test/crawler")
from export_wb import export_web

if __name__=="__main__":
	export_web.export_link()

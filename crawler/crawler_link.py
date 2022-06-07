import requests
import time
from bs4 import BeautifulSoup



class crawl_link_web:

	def __init__(self, dom, cate, link):

		self.dom = dom
		self.cate = cate
		self.link = link

	def getcate(self):
		print("2__")
		
		req = requests.get(self.dom).text
		soup = BeautifulSoup(req, "html.parser")
		cate =soup.select(self.cate)
		ct = []

		for c in cate[1:]:
			l = c.get("href")
			if l.startswith("https://"):
				ct.append(l)
			
			if l.startswith("/"):
				ct.append(self.dom + l[1:])
				
		return ct 


	def getlink(self,ca):
		li = []
		try:
			for c in ca:
				req = requests.get(c).text
				soup = BeautifulSoup(req, "html.parser")
				link = soup.select(self.link)

				for i in link: 
					l = i.get('href')
					if l.startswith("https://"):	
						li.append(l)

					if l.startswith("/"): 	
						li.append(self.dom + l[1:])
							
			return li
		except :
			pass



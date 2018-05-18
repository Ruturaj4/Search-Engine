# Name: link_finder
# Author: Ruturaj Kiran Vaidya
# Date: 17 May 2018


from urllib import parse
from html.parser import HTMLParser

class LinkFinder(HTMLParser):
	
	#In this function, we will initialize everything
	def __init__(self, base_url, page_url):
		super().__init__()
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()

	def handle_starttag(self, tag, attrs):
		#Check for a
		if tag == 'a':
		#print(tag)
			for(attribute, value) in attrs:
				#Chekc for href
				if attribute == 'href':
					url = parse.urljoin(self.base_url, value)
					self.links.add(url)

	def page_links(self):
		return self.links


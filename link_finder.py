from urllib import parse
from html.parser import HTMLParser

class LinkFinder(HTMLParser):
	
	def __init__(self, base_url, page_url):
		super().__init__()
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()

	def handle_starttag(self, tag, attrs):
		if tag == 'a'
		#print(tag)
		for(attribute, value) in attrs:
			if attribute == 'href':
				url = parse.urljoin(self.base_url, value)
				self.links.add(url)

	deg page_links(self):
		return self.links
		
	def error(self, message):
		pass


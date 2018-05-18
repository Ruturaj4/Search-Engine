# Name: spider
# Author: Ruturaj Kiran Vaidya
# Date: 17 May 2018

from urllib.request import urlopen
from link_finder import LinkFinder
from house_keeping import *
from urllib.parse import urlparse

dec = "utf-8"

#For charmap codec error, use command 'chcp 65001'

class Spider:

#Initializing all the class variables
	base_url = ''
	domain_name = ''
	q_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()

	def __init__(self, base_url, domain_name):
		#Initializing everything
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.q_file = './queue.txt'
		Spider.crawled_file = './crawled.txt'
		self.start()
		#Pass the thread and base url in
		self.crawl_page('Initial thread', Spider.base_url)

	@staticmethod
	def start():
		create_data_files(Spider.base_url)
		Spider.queue = toSet(Spider.q_file)
		Spider.crawled = toSet(Spider.crawled_file)

	@staticmethod
	def crawl_page(thread_name, page_url):
		if page_url not in Spider.crawled:
			print(thread_name + ' crawling '+ page_url)
			print('Queue: '+str(len(Spider.queue)) + ' Crawled: ' + str(len(Spider.crawled)))
			Spider.add_links_q(Spider.collect_links(page_url))
			#print(page_url)
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
			Spider.set_to_file()

	#Urlopen gets all the data as bytes, but as we need strings here we will convert all the binary data into strings
	@staticmethod
	def collect_links(page_url):
		html = ''
		#Check if the page is html only, not in the other format, eg. pdf, ppt, etc.
		try:
			print(page_url)
			response = urlopen(page_url)
			#do a check
			if 'text/html' in response.getheader('content-Type'):
				#if yes then ....
				html_bytes = response.read()
				html = html_bytes.decode(dec)
				#print(html)
				#print("linkfinder")
			finder = LinkFinder(Spider.base_url, page_url)
			finder.feed(html)
		except Exception as e:
			print("Error")
			return set()
		return finder.page_links()

	@staticmethod
	def add_links_q(links):
		for url in links:
			if url in Spider.queue:
				continue
			if url in Spider.crawled:
				continue
			if Spider.domain_name not in url:
				continue
			Spider.queue.add(url)

	@staticmethod
	def set_to_file():
		writeInFile(Spider.queue, Spider.q_file)
		writeInFile(Spider.crawled, Spider.crawled_file)

def get_name(url):
	try:
		try:
		#Now, we will get the domain name, we need to parse
		#To get the url domain name
		#print(urlparse(url).netloc)
			a = urlparse(url).netloc
		except:
			a = ''
		results = a.split('.')
		#print(results)
		return (results[-2]+'.'+results[-1])
	except:
		return ''

#print(get_name('https://stackoverflow.com/jobs?med=site-ui&ref=jobs-tab'))	
	
	
	
	
	
	
	

	
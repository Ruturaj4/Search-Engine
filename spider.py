from urllib.request import urlopen
from link_finder import Linkfinder
from house_keeping import *

class Spider:

#class variables which are shared among all instances
	base_url = ''
	domain_name = ''
	q_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()

	def __init__(self, base_url, domain_name):
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.q_file = './queue.txt'
		Spider.crawled_file = './crawled.txt'
		self.start()
		self.crawl_page('first spider', Spider.base_url)

	def start():
		create_data_files(Spider.base_url)
		Spider.queue = file_to_set(Spider.q_file)
		Spider.crawled = file_to_set(Spider.crawled_file)
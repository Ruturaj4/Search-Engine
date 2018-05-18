# Name: pre-processing.py
# Author: Shaina Krumme
# Date: 12 May 2018

# Inspired by: https://www.harding.edu/fmccown/classes/comp475-s11/python-web-crawler.pdf
# and https://www.youtube.com/playlist?list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q
import os
import urllib.request

#Theading for multiple spiders
import threading
from spider import Spider, get_name
from house_keeping import *

#Queue to store to-be-crawled URLs.
#As we using parallel processing, queue is a better datastructure
from queue import Queue

###############################################
# Folder that will store the crawled webpages #
###############################################

if not os.path.exists('linkedin-pre-processing'):
    os.makedirs('linkedin-pre-processing')

##########################################################
# Multi-threaded spider that fetches and parses webpages #
##########################################################

# Download a webpage.
seed_url = 'https://stackoverflow.com/'
#response = urllib.request.urlopen(seed_url)
domain = get_name(seed_url)
#html = response.read()
# Print for testing purposes.
# Terminal command: print html.split('\n')[0]

# Identify ourselves to be polite.
request = urllib.request.Request(seed_url)
request.add_header("Shaina Krumme and Ruturaj Vaidya", "Mini Search Engine Project")
opener = urllib.request.build_opener()
#response = opener.open(request)
#html = response.read()

# Get the HTTP headers.
response = urllib.request.urlopen(seed_url)
# Print for testing purposes.
# Terminal command: print response.info()

# Find out what content type is being returned.
content_type = response.info().get('Content-Type')
# Print for testing purposes.
# Terminal command: content_type

# Save the content to files that are named after the URL.
#f = open('linkedin-pre-processing/seed-url.htm', 'wb')
#f.write(html)
#f.close()

################################################
# URL frontier which stores to-be-crawled URLs #
################################################
		
# Will only collect 1,000 webpges to be polite to the site.
queue = Queue()
que = './queue.txt'
craw = './crawled.txt'
#Threades depend on the your system
threads = 8
Spider(seed_url, domain)

################################################
# URL frontier which stores to-be-crawled URLs #
################################################

#first spider is completed successfully
#Let's do the multithreading now

#Lets create spiders or workers first
def spiders():
	for _ in range(threads):
		thrd = threading.Thread(target=doCrawling)
		#Daemon process dies when we exit out of main
		thrd.daemon = True
		#Start the thread
		thrd.start()

def doCrawling():
	while 1:
		#Remove from the queue
		url = queue.get()
		#We will use use the name of current thread to see what is going on
		Spider.crawl_page(threading.current_thread().name, url)
		queue.task_done()

def works():
	for link in toSet(que):
		#insert into the queue
		queue.put(link)
	#Join the queue
	queue.join()
	crawler()

def crawler():
	#Convert everything in the que to a set
	set_q = toSet(que)
	#Check if atleast one link is there
	if len(set_q) >=1:
		print(str(len(set_q))) #- print total number of links in the queue
		works()

#First execute the spider
spiders()
#Then start crawling
crawler()		

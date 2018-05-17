# Name: pre-processing.py
# Author: Shaina Krumme
# Date: 12 May 2018

# Inspired by: https://www.harding.edu/fmccown/classes/comp475-s11/python-web-crawler.pdf

import os
import urllib.request


# Queue to store to-be-crawled URLs.
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
seed_url = 'https://business.linkedin.com/'
response = urllib.request.urlopen(seed_url)
html = response.read()
# Print for testing purposes.
# Terminal command: print html.split('\n')[0]

# Identify ourselves to be polite.
request = urllib.request.Request(seed_url)
request.add_header("Shaina Krumme and Ruturaj Vaidya", "Mini Search Engine Project")
opener = urllib.request.build_opener()
response = opener.open(request)
html = response.read()

# Get the HTTP headers.
response = urllib.request.urlopen(seed_url)
# Print for testing purposes.
# Terminal command: print response.info()

# Find out what content type is being returned.
content_type = response.info().get('Content-Type')
# Print for testing purposes.
# Terminal command: content_type

# Save the content to files that are named after the URL.
f = open('linkedin-pre-processing/seed-url.htm', 'wb')
f.write(html)
f.close()

################################################
# URL frontier which stores to-be-crawled URLs #
################################################
		
# Will only collect 1,000 webpges to be polite to the site.
url_frontier = Queue(maxsize = 1000)
urlQueue = './queue.txt'
if not os.path.isfile(urlQueue):
	write_file(urlQueue, seed_url)



###########################################
# URL repository that stores crawled URLs #
###########################################

# This will be a set.

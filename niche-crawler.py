# Name: pre-processing.py
# Author: Shaina Krumme
# Date: 12 May 2018

# Inspired by: https://www.harding.edu/fmccown/classes/comp475-s11/python-web-crawler.pdf

import urllib2
import os

###############################################
# Folder that will store the crawled webpages #
###############################################

if not os.path.exists('linkedin-pre-processing'):
    os.makedirs('linkedin-pre-processing')

##########################################################
# Multi-threaded spider that fetches and parses webpages #
##########################################################

# Will only collect 1,000 webpges to be polite to the site.
# for x in range(1000):

# Download a webpage.
response = urllib2.urlopen('https://business.linkedin.com/')
html = response.read()
# Print for testing purposes.
# Terminal command: print html.split('\n')[0]

# Identify ourselves to be polite.
request = urllib2.Request('https://business.linkedin.com/')
request.add_header("Shaina Krumme and Ruturaj Vaidya", "Mini Search Engine Project")
opener = urllib2.build_opener()
response = opener.open(request)
html = response.read()

# Get the HTTP headers.
response = urllib2.urlopen('https://business.linkedin.com/')
# Print for testing purposes.
# Terminal command: print response.info()

# Find out what content type is being returned.
content_type = response.info().get('Content-Type')
# Print for testing purposes.
# Terminal command: content_type

# Save the content to files that are named after the URL.
f = open('linkedin-pre-processing/seed-url.htm', 'w')
f.write(html)
f.close()

################################################
# URL frontier which stores to-be-crawled URLs #
################################################

###########################################
# URL repository that stores crawled URLs #
###########################################

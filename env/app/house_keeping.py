# Name: house_keeping
# Author: Ruturaj Kiran Vaidya
# Date: 17 May 2018

import os

def create_data_files(base_url):
	#Create two files
	queue = 'queue.txt'
	crawled = 'crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, base_url)

	if not os.path.isfile(crawled):
		write_file(crawled, '')

#We will use this to write in the file
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close

#Read a file and convert each line to set items
def toSet(filename):
	#Using set to save the result
	results = set()
	with open(filename, 'rt') as f:
		for line in f:
			results.add(line.replace('\n',''))
	return results
	
#Iterate through a set, each item will be a new line in the file
def writeInFile(links, file):
	with open(file, 'w'):
		pass
	for link in sorted(links):
		with open(file, 'a') as f:
			f.write(link + '\n')
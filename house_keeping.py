import os

def create_data_files(base_url):
	queue = 'queue.txt'
	crawled = 'crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, base_url)

	if not os.path.isfile(crawled):
		write_file(crawled, '')

def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close
	
def append_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data + '\n')
		
def delete_file_contents(path):
	with open(path, 'w'):
		pass

#Read a file and convert each line to set items
def file_to_set(filename):
	results = set()
	with open(filename, 'rt') as f:
		for line in f:
			results.add(line.repalce('\n',''))
	return results
	
#Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
	delete_file_contents(file)
	for link in sorted(links):
		append_to_file(file, link)
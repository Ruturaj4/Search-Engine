# Name: Preprocessor
# Author: Ruturaj Kiran Vaidya
# Date: 7th May 2018

import os
import re
import string
from lxml import html
from lxml.html.clean import clean_html
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle
from collections import Counter

directory = os.listdir('./docsnew/')
TAG_RE = re.compile(r'<[^>]+>')

stop_words = set(stopwords.words('english'))

def puns(ch):
    if ch.isalpha():
        return ch
    else:
        return ' '
		
def remov_duplicates(input):
	# split input string separated by space
	input = input.split(" ")
	# joins two adjacent elements in iterable way
	for i in range(0, len(input)):
		input[i] = "".join(input[i])
	# now create dictionary using counter method
	# which will have strings as key and their 
	# frequencies as value
	UniqW = Counter(input)
	# joins two adjacent elements in an iterable way
	s = " ".join(UniqW.keys())
	return s

def remove_tags(read_file):
	read_file = clean_html(read_file)
	read_file = ''.join(puns(ch)for ch in read_file)
	read_file = ' '.join(read_file.split())
	var_remove_tags = TAG_RE.sub('', read_file)
	var_remove_tags = re.sub('<script>.*?</script>', '', var_remove_tags)
	var_lower = read_file.lower()
	var_lower = remov_duplicates(var_lower)
	#var_lower = var_lower.replace(r'\n+', '\n')
	word_tokens = word_tokenize(var_lower)
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	filtered_sentence = []
	for w in word_tokens:
		if w not in stop_words:
			filtered_sentence.append(w)
	#print(filtered_sentence)
	return filtered_sentence

def main():
	for file in directory:
		open_file = open("./docsnew/"+file,'r', encoding="utf8")
		read_file = open_file.read()
		tag = []
		tag = remove_tags(read_file)
		#word_list = tag.split()
		#tag = [word for word in word_list if word not in stopwords.words('English')]
		#tag = ''.join(tag)
		base = os.path.splitext(file)[0]
		new_file = base + ".txt"
		#with open("./cleaned_docs/"+new_file,'wb') as write_file:
		#	pickle.dump(tag, write_file)
		#write_file.write(tag)
		write_file = open("./cleaned_docs/"+new_file, 'w', encoding='utf-8')
		write_file.write(" ".join(tag))# ---- to store the file as " " separated list
		#tag = str(tag).split()
		#we'll put the file as it is in ['a','b'] form
		#write_file.write(str(tag))
		write_file.close()


if __name__ == "__main__":
	main()

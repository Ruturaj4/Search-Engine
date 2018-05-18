# Name: Indexing
# Author: Ruturaj Kiran Vaidya
# Date: 4th May 2018

import os
from collections import defaultdict
import pickle

#path,dir and files.
#Default path given is cleaned_docs - YOu can change it to your appropriate directory.
path, dirs, files = next(os.walk("./cleaned_docs"))
#print(files) - prints a list of documents like - [doc1, doc2]
#print(dir) - prints - <built-in function dir> - reason - why not? :-p
#print(path) - prints - ./cleaned_docs

#Empty list, to store keys
keys = []

#Now, keys for each documnet, in short, counting how many documnets are there.
for i in range(0, len(files)):
	keys.append(i)
	#print(keys) - print all the keys for example - [0,1,2,3,4] - If there are five documents

#Empty dictionary, just like keys - used to store the list of files from 0 to n
all_docs = {}

#Now creating a dictionary structure using above empty dictionary
for i in range(0, len(files)):
	(k,v)=(keys[i], "./cleaned_docs/"+files[i])
	all_docs[k] = v
	#print(v) - prints list of all the files

#Setting a dictionary - It contains all of the words in total number of documents
dictionary = set()
#print(dictionary) - prints set()

#This is to store number of postings
postings = {}
postings = defaultdict(dict)
#print(postings) - prints - defaultdict(<class 'dict'>, {})

def main():
	print("Something")
	assign_dict()
	#Store the dictionary structure in pickle file
	afile = open(r'dict.pkl', 'wb')
	pickle.dump(dictionary, afile)
	afile.close()
	#print(dictionary)

	#Store postings in pickle file
	bfile = open(r"postings.pkl", "wb")
	pickle.dump(postings, bfile)
	bfile.close()
	#print(postings)
	
	#Store list of docs in pickle file
	cfile = open(r"all_docs.pkl", "wb")
	pickle.dump(all_docs, cfile)
	cfile.close()
	#print(all_docs)
	
	#Store the keys in pickle file
	dfile = open(r"keys.pkl", "wb")
	pickle.dump(keys, dfile)
	dfile.close()
	#print(keys)

def assign_dict():
	global dictionary, postings
	for id in all_docs:
		#Opening the pickle file
		#print(all_docs[id])
		f = open(all_docs[id], 'r', encoding="utf8")
		document_whole = f.read()
		#print(document_whole)
		f.close()
		document_whole = document_whole.split()
		#Set creates a set of tokens in the documents
		unique_terms = set(document_whole)
		#print(unique_terms)
		#So, in the previous created dictionary, I'm adding all these terms
		dictionary = dictionary.union(unique_terms)
		#print(dictionary)
		# Now we'll set the postings, with the values equal to the frequency of terms in the document
		for term in unique_terms:
			postings[term][id] = document_whole.count(term)

if __name__ == "__main__":
	main()
# Name: Vector space model
# Author: Ruturaj Kiran Vaidya
# Date: 7th May 2018

#For - UnicodeEncodeError: 'charmap' codec can't encode characters in position 149-159: character maps to <undefined> error - use - chcp 65001

import pickle
from collections import defaultdict
import math
from query_processing import remove_tags
from functools import reduce
import sys

#collecting word list using pickle
file2 = open(r'dict.pkl', 'rb')
token_list = pickle.load(file2)
file2.close()
#print(token_list)

#Collecting dictionary structure (specifically postings) using pickle
file3 = open(r'postings.pkl', 'rb')
postings = pickle.load(file3)
file3.close()
#print(postings)

#Collecting dictionary structure (specifically postings) using pickle
file4 = open(r'all_docs.pkl', 'rb')
all_docs = pickle.load(file4)
file3.close()
#print(all_docs) - list of all the documnets in dictionary format
#print(token_list)

#Collecting all the keys using pickle
#file5 = open(r'keys.pkl', 'rb')
#keys = pickle.load(file5)
#print(keys)
#file5.close()

#This is a document frequency
freq = defaultdict(int)
#print(freq) - prints - defaultdict(<class 'int'>, {}) - as it does above

#This gives inverse documnet frequency
inverse_frequency = 0

# This is a dictionary, who's keys are document ids and vlues are Euclidean distance of corresponding documnet vector
euclidean_len = defaultdict(float)
#print(euclidean_len) - prints - defaultdict(<class 'float'>, {})


#cosine_similarity = 0
# Total number of documnets
total_docs = len(all_docs)
#print(total_docs)

def main(que):
	#Initializing term length to frequency
	term_len_to_freq()
	#Initializing Euclidean length
	euclidian_length()
	#Get the query from the user
	query(que)

def term_len_to_freq():
	#Stores the frequency of each token in the global freq structure
	global freq
	for token in token_list:
		freq[token] = len(postings[token])

#Now that we have calculated the frequency, we will find the inverse document frequency
def inverse_freq(token):
	if token in token_list:
		global inverse_frequency
		#Using the formula idf = log10(N/df)
		inverse_frequency = math.log10(total_docs/freq[token])
		#Retutn frequency calulated by the formula
		#print(inverse_frequency)
		return inverse_frequency
	else:
		#Return 0 otherwise
		return inverse_frequency

#Now we will calculate the tf_idf weight of each token
def weight(token, x):
	if x in postings[token]:
		#Calculating weight, which is number tf*idf
		return postings[token][x]*inverse_freq(token)
	else:
		return 0

#Now we will use everything we've calculated before, to calculate the Euclidian length
def euclidian_length():
	global euclidean_len
	for x in all_docs:
		length = 0
		for token in token_list:
			#Now calculating length of each token in the token list
			length = length + (weight(token,x)**2)
		#Now our Euclidean length which is obtained is square root of length we jsut calculated
		euclidean_len[x] = math.sqrt(length)

#Now we'll pass the user query in our query() function to search the right term
def query(que):
	#search_query = input("Enter your query: ")
	search_query = que
	if search_query == "":
		sys.exit()
	
	#while(search_query):
	search_query = remove_tags(search_query)
	search_query = list(filter(('p').__ne__, search_query))
	print(search_query)
	match = []
	for term in search_query:
		match.append(set(postings[term].keys()))
	#Now removing set() from match
	match = list(filter((set()).__ne__, match))
	#print(match)
	#Now intersecting the sub-matches
	try:
		re = reduce(set.intersection, [x for x in match])
	except:
		re = 0
	#print(re)
	#removing set() from re
	#re = list(filter((set()).__ne__, re))
	scores = []
	if not re:
		print("DOcument not found")
	else:
		for id in re:
			cosine_similarity = 0
			for term in search_query:
				if term in token_list:
					cosine_similarity += inverse_freq(term)*weight(term,id)
			#print(euclidean_len)
			cosine_similarity /=euclidean_len[id]
			#print(cosine_similarity)
			scores.append([id, cosine_similarity])
		scores = list(map(tuple, scores))
		scores = sorted(scores, key=lambda tup: tup[1], reverse=True)
		#print(scores)
		#mapping the nested list into the list of tuples
		#scores = sorted(scores, reverse=True)
		#print(scores)
		print("Score: filename")
		for (x,rate) in scores:
			#print(str(rate)+": "+ all_docs[x])
			get.append(str(score)+": "+ prac[x]+"/n")
		print(get)
		thefile = open('templates/results.html', 'w', encoding='utf-8')
		html_body = '<body>'
		thefile.write(html_body)
		for item in get:
			thefile.write("<p>%s</p>" % item)
			thefile.write('</body>')



if __name__ == "__main__":
	main()
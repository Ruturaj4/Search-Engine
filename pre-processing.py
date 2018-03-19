# Name: pre-processing.py
# Author: Shaina Krumme
# Date: 18 March 2018

# Install Natural Language Toolkit (NLTK) using the following command:
# run sudo pip install -U nltk

# Download NLTK stopwords
# nltk.download('stopwords')

# Support for regular expressions.
import re

# Implementing a stop list and stemmer.
from nltk.stem import *
from nltk.stem.porter import *
from nltk.corpus import stopwords
import nltk

import os

# Pre-process the documents by removing all HTML tags and convert everything
# into lower case.

def removeTags(html):
    removetags = re.compile('<.*?>')
    plain = re.sub(removetags, '', html)
    return plain

def toLowercase(text):
    return text.lower()

# Implement a stop list and a stemmer to pre-process the documents (for the stop
# list and stemmer, you are allowed to use third-party open source code).

def filterStopWords(text):
	stopWords = set(stopwords.words('english'))
	filtered =  [i for i in text.split() if i not in stopWords]
	return filtered

def stemmer(text):
    stemmer = PorterStemmer()
    stem = []
    for words in text:
        stem.append(stemmer.stem(words))
    return stem

# Build an inverted index (including dictionary and posting lists) for the
# documents. Please make sure to keep all the frequency information.

# def invertedIndex(documents):
#
#     return index

def main():

    counter = 0
    directory = os.listdir('pre-processing-files')

    for file in directory:
        open_file = open(file, 'r')
        read_file = open_file.read()

        plain = removeTags(read_file)
        lowerCase = toLowercase(plain)
        filtered = filterStopWords(lowerCase)
        stem = stemmer(filtered)
        
        counter += 1
    print "Number of files ", counter

if __name__ == "__main__":
	main()

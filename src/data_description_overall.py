#!/usr/local/lib/python2.7

from __future__ import division
import csv
import nltk
import sys
from nltk.collocations import *

def overall_list(data):
	"""
		This function returns one list with all the reviews from text-cat combined.
		In addition, it also counts the amount of reviews per gender.
	"""
	# Declare the variables and lists where I am going to store the data that I will be acquiring.
	reviews_count_overall = 0
	token_list_overall = []
	# Loop over each row of text in the csv-file.
	for row in data:
		token_list_overall += nltk.word_tokenize(row['text-cat'])
		reviews_count_overall += 1
	return reviews_count_overall, token_list_overall

def corpus_description(tokens):
	"""
		Input is a list of tokens retrieved from unstructured_text. Output contains corpus analysis + frequency plot
	"""
	print("The corpus size is {0}".format(len(tokens)))
	print("The vocabulary size is {0}".format(len(set(tokens))))
	print("The lexical density is {0}".format(len(set(tokens))/len(tokens)))
	# plot a frequency graph with stopwords
	freqdist_1 = nltk.FreqDist(tokens)
	freqdist_1.plot(20)
	# plot a frequency graph without stopwords
	stopwords = nltk.corpus.stopwords.words('english')
	#punctuation = ",.<>;:?[]{}-_+=!@#$%^&*()~`"
	punctuation = [",", ".", "<", ">", ";", ":", "?", "[", "]", "{", "}" ,"-", "_", "+", "=", "!", "@", "#",
	"$", "%", "^", "&", "*", "(", ")", "~", "`", "''", "...", "``"]
	stopwords_and_punctuation = stopwords + punctuation
	# add tokens to list if they are not in the stopwords provided by nltk
	new_tokens = [item for item in tokens if item.lower() not in stopwords_and_punctuation]
	# stopwords and punctuation from the histogram
	freqdist_2 = nltk.FreqDist(new_tokens)
	freqdist_2.plot(20)

def bigrams_extractor(text):
	stopwords = nltk.corpus.stopwords.words('english')
	punctuation = [",", ".", "<", ">", ";", ":", "?", "[", "]", "{", "}" ,"-", "_", "+", "=", "!", "@", "#",
	"$", "%", "^", "&", "*", "(", ")", "~", "`", "''", "...", "``"]
	stopwords_and_punctuation = stopwords + punctuation
	tokens = [item for item in text if item.lower() not in stopwords_and_punctuation]
	bigram_measures = nltk.collocations.BigramAssocMeasures()
	finder = BigramCollocationFinder.from_words(tokens)
	scored = finder.score_ngrams(bigram_measures.raw_freq)
	sorted = (finder.nbest(bigram_measures.raw_freq, 50))
	#scored = finder.score_ngrams(bigram_measures.chi_sq)
	#sorted = (finder.nbest(bigram_measures.chi_sq, 20))
	print sorted

def main():
	# open the file
	reload(sys)
	# Apparently we have decided to store the csv-files in the same folder/directory as the source code.
	file = open('../data/trainset-sentiment.csv')
	sys.setdefaultencoding("utf-8")
	reader = csv.DictReader(file)

	count1, list1 = overall_list(reader) # Extract the raw data sorted by gender by means of calling the function overall_list().
	print '-------- OVERALL CORPUS ANALYTICS ------'
	print "There are", count1, "reviews that have been written in total."
	corpus_description(list1)
	print "These are the 50 most prevalent bigrams of the whole reviews dataset:"
	bigrams_extractor(list1)
	file.close()
if __name__ == "__main__":
    main()

#!/usr/local/lib/python2.7

from __future__ import division
import csv
import nltk
import sys
from nltk.collocations import *

def label_lists(data):
	"""
		This function returns two lists: one list with the tokens from negatives, and one with the tokens from positives.
		In addition, it also counts the amount of reviews per label.
	"""
	# Declare the variables and lists where I am going to store the data that I will be acquiring.
	reviews_count_negative = 0
	reviews_count_positive = 0
	token_list_negative = []
	token_list_positive = []
	# Loop over each row of text in the csv-file.
	for row in data:
		if 'pos' == row['label']:
			# If the review was written by a man, put it in a separate list and add one extra to the positive-review count.
			token_list_positive += nltk.word_tokenize(row['text-cat'])
			reviews_count_positive += 1
			review_length = 0
		if 'neg' == row['label']:
			# If the review was written by a woman, put it in a separate list and add one extra to the negative-review count.
			token_list_negative += nltk.word_tokenize(row['text-cat'])
			reviews_count_negative += 1
	# We have now acquired four sets of data in this function. This raw data I will return to the main() function, so that I can do stuff with it.
	return reviews_count_positive, reviews_count_negative, token_list_positive, token_list_negative

def corpus_description(tokens):
	"""
		Input is a list of tokens retrieved from unstructured_text. Output contains corpus analysis + frequency plot
	"""
	print "The corpus size is {0}".format(len(tokens))
	print "The vocabulary size is {0}".format(len(set(tokens)))
	print "The lexical density is {0}".format(len(set(tokens))/len(tokens))
	stopwords = nltk.corpus.stopwords.words('english')
	punctuation = [",", ".", "<", ">", ";", ":", "?", "[", "]", "{", "}" ,"-", "_", "+", "=", "!", "@", "#",
	"$", "%", "^", "&", "*", "(", ")", "~", "`", "''", "...", "``", "'"]
	stopwords_and_punctuation = stopwords + punctuation
	# add tokens to list if they are not in the stopwords provided by nltk
	new_tokens = [item for item in tokens if item.lower() not in stopwords_and_punctuation]
	# stopwords and punctuation from the histogram
	freqdist_2 = nltk.FreqDist(new_tokens)
	print "These are the 50 most frequently occurring words of this corpus (minus punctuation and stopwords):"
	print freqdist_2.most_common(50)


def bigrams_extractor(text):
	"""
		With this function, we are going to extract the 150 most frequent bigrams from the dataset, but without
		punctuation or stopwords, in order to get as many relevant results as possible and to remove all noise.
	"""
	stopwords = nltk.corpus.stopwords.words('english')
	punctuation = [",", ".", "<", ">", ";", ":", "?", "[", "]", "{", "}" ,"-", "_", "+", "=", "!", "@", "#",
	"$", "%", "^", "&", "*", "(", ")", "~", "`", "''", "...", "``", "'"]
	stopwords_and_punctuation = stopwords + punctuation
	tokens = [item for item in text if item.lower() not in stopwords_and_punctuation]
	bigram_measures = nltk.collocations.BigramAssocMeasures()
	finder = BigramCollocationFinder.from_words(tokens)
	scored = finder.score_ngrams(bigram_measures.raw_freq)
	sorted = (finder.nbest(bigram_measures.raw_freq, 150))
	print sorted


def main():

	reload(sys)
	file = open('../data/trainset-sentiment.csv')
	sys.setdefaultencoding("utf-8")
	reader = csv.DictReader(file)
	count1, count2, list1, list2 = label_lists(reader)
	print '-------- POSITIVE ------'
	print "There are", count1, "reviews that have been reviewed as positives."
	corpus_description(list1)
	print "These are the 150 most prevalent bigrams of the positive reviews:"
	bigrams_extractor(list1)
	print '---------- NEGATIVE -----'
	print "There are", count2, "reviews that have been reviewed as negatives."
	corpus_description(list2)
	print "These are the 150 most prevalent bigrams of the negative reviews:"
	bigrams_extractor(list2)
	file.close()

if __name__ == "__main__":
    main()

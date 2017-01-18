#!/usr/local/lib/python2.7

from __future__ import division
import csv
import nltk
import sys
from nltk.collocations import *

def time_lists(data):
	"""
		This function returns two lists: one list with the tokens from evenings, and one with the tokens from mornings.
		In addition, it also counts the amount of reviews per gtime.
	"""
	# Declare the variables and lists where I am going to store the data that I will be acquiring.
	reviews_count_evening = 0
	reviews_count_morning = 0
	token_list_evening = []
	token_list_morning = []
	# Loop over each row of text in the csv-file.
	for row in data:
		if 'morning' == row['time-cat']:
			# If the review was written by a man, put it in a separate list and add one extra to the morning-review count.
			token_list_morning += nltk.word_tokenize(row['text-cat'])
			reviews_count_morning += 1
		if 'evening' == row['time-cat']:
			# If the review was written by a woman, put it in a separate list and add one extra to the evening-review count.
			token_list_evening += nltk.word_tokenize(row['text-cat'])
			reviews_count_evening += 1
	# We have now acquired four sets of data in this function. This raw data I will return to the main() function, so that I can do stuff with it.
	return reviews_count_morning, reviews_count_evening, token_list_morning, token_list_evening

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
	sorted = (finder.nbest(bigram_measures.raw_freq, 20))
	#scored = finder.score_ngrams(bigram_measures.chi_sq)
	#sorted = (finder.nbest(bigram_measures.chi_sq, 20))
	print sorted
	
def main():
	# open the file
	reload(sys)
	# Apparently we have decided to store the csv-files in the same folder/directory as the source code.
	file = open('trainset-sentiment-extra.csv')
	sys.setdefaultencoding("utf-8")
	reader = csv.DictReader(file)

	count1, count2, list1, list2, = time_lists(reader) # Extract the raw data sorted by time by means of calling the function gender_lists().
	print '-------- MORNING ------'
	print "There are", count1, "reviews that have been written in the morning."
	corpus_description(list1)
	print "These are the 20 most prevalent bigrams in the reviews written in the morning:"
	bigrams_extractor(list1)
	print '---------- EVENING-----'
	print "There are", count2, "reviews that have been written in the evening."
	corpus_description(list2)
	print "These are the 20 most prevalent bigrams in the reviews written in the evening:"
	bigrams_extractor(list2)
	file.close()
if __name__ == "__main__":
    main()
from __future__ import division
import csv
import nltk
import sys
from nltk.collocations import *

def gender_lists(data):
	"""
		This function returns two lists: one list with the tokens from females, and one with the tokens from males.
		In addition, it also counts the amount of reviews per gender.
	"""
	# Declare the variables and lists where I am going to store the data that I will be acquiring.
	reviews_count_female = 0
	reviews_count_male = 0
	token_list_female = []
	token_list_male = []
	# Loop over each row of text in the csv-file.co
	for row in data:
		if 'male' == row['gender-cat']:
			# If the review was written by a man, put it in a separate list and add one extra to the male-review count.
			token_list_male += nltk.word_tokenize(row['text-cat'])
			reviews_count_male += 1
		if 'female' == row['gender-cat']:
			# If the review was written by a woman, put it in a separate list and add one extra to the female-review count.
			token_list_female += nltk.word_tokenize(row['text-cat'])
			reviews_count_female += 1
	# We have now acquired four sets of data in this function. This raw data I will return to the main() function, so that I can do stuff with it.
	return reviews_count_male, reviews_count_female, token_list_male, token_list_female

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

	count1, count2, list1, list2, = gender_lists(reader) # Extract the raw data sorted by gender by means of calling the function gender_lists().
	print '-------- MALE ------'
	print "There are", count1, "reviews that have been written by males."
	corpus_description(list1)
	print "These are the 20 most prevalent bigrams in the reviews written by males:"
	bigrams_extractor(list1)
	print '---------- FEMALE-----'
	print "There are", count2, "reviews that have been written by females."
	corpus_description(list2)
	print "These are the 20 most prevalent bigrams in the reviews that have been written by females:"
	bigrams_extractor(list2)
	file.close()

if __name__ == "__main__":
    main()

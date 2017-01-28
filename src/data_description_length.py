#!/usr/local/lib/python2.7

import csv
import nltk
import sys
import numpy
import pylab

def stats(values):
	"""
		This is a function that calculates some generic descriptive statistics of the set of numbers that it processes.
	"""
	# Calculate the sample size:
	print "The sample size is: " + str(len(values))

	# Calculate the mean:
	print "The mean is: " + str(numpy.mean(values))

	# Calculate the median:
	print "The median is: " + str(numpy.median(values))

	# Calculate the standard deviation:
	print "The standard deviation is: " + str(numpy.std(values))

	# Calculate the minimal value:
	minimum = min(values)
	print "The mininum value is: " + str(minimum)

	# Calculate the maximum value:
	maximum = max(values)
	print "The maximum value is: " + str(maximum)

	# Calculate the mode:
	print "The mode is: " + str(max(set(values), key=values.count))

def review_length_extractor(data):
	"""
		Extracts the lengths of the reviews from each row in the .csv file, both for the file as a whole and
		for each category.
	"""
	list_of_lengths_total = []
	list_of_lengths_positive = []
	list_of_lengths_negative = []
	for row in data:
		string_length = row['length']
		# For some quirky reason, some values in the list are NoneType. I have to get rid of these, or I can't do calculations with it.
		if string_length != None:
			# I know, it's a heckuvalot lists that I'm working with, but it also gives me a precise and fine-grained desription of my data.
			list_of_lengths_total.append(int(string_length))
			if "pos" in row['label']:
				list_of_lengths_positive.append(int(string_length))
			if "neg" in row['label']:
				list_of_lengths_negative.append(int(string_length))
	# Oof! What a lot of values to return to the main()! Still, it is more neast to do this in one function, as otherwise the same dataset
	# has to be looped over several times. This way, it is more efficient, as long as I keep track of which list gets returned where.
	return list_of_lengths_total, list_of_lengths_positive, list_of_lengths_negative

def main():
	# open the file
	reload(sys)
	file = open('../data/trainset-sentiment-extra.csv')
	sys.setdefaultencoding("utf-8")
	reader = csv.DictReader(file)

	# I chose for rather generic list names, as their function is self-evident from the print fucntion in the line immediately before
	# it is being used for processing.
	list1, list2, list3 = review_length_extractor(reader)
	print "Please find below the descriptive statistics for the lengths of all the reviews:"
	stats(list1)
	pylab.hist(list1,bins=10)
	pylab.show()
	file.close()
	print "Please find below the descriptive statistics for the lengths of those reviews that were positive:"
	stats(list2)
	pylab.hist(list2,bins=10)
	pylab.show()
	file.close()
	print "Please find below the descriptive statistics for the lengths of those reviews that were negative:"
	stats(list3)
	pylab.hist(list3,bins=10)
	pylab.show()
	file.close()
	file.close()
if __name__ == "__main__":
    main()

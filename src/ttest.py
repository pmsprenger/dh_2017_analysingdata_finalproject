#!/usr/local/lib/python2.7

from __future__ import division
import csv
import nltk
import sys
import scipy
import numpy
import pylab
import scipy.stats
from scipy import stats

reload(sys)
file = open('../data/new_csvfile_with_counts.csv')
sys.setdefaultencoding("utf-8")
reader = csv.DictReader(file)

def bigram_counter(reader):
    pos_bigr_count = []
    neg_bigr_count = []

    for row in reader:
        pos_row = row['pos_score']
        pos_bigr_count.append(int(pos_row))
        neg_row = row['neg_score']
        neg_bigr_count.append(int(neg_row))
    return pos_bigr_count, neg_bigr_count

def descriptives(name, values):
    """
        Returns the descriptive statistics for a list of values
    """
    sorted_results = sorted(values)
    print "--------DESCRIPTIVE STATISTICS FOR" + " " + name + "----------------"
    print "{0} {1}".format('Mean', numpy.mean(values))
    print "{0} {1}".format('Median', numpy.median(values))
    print "{0} {1}".format('SD', numpy.std(values))
    print "{0} {1}".format('Max', sorted_results[-1])
    print "{0} {1}".format('Min', sorted_results[0])



def t_test(x, y):
    result_t_test = stats.ttest_ind(x,y, equal_var=True)
    print '--------------------'
    print 'INDEPENDENT T-TEST:'
    print '------------------'
    print "t-value = {0}".format(result_t_test[0])
    print "p-value = {0}".format(result_t_test[1])



positive_bigrams, negative_bigrams = bigram_counter(reader)
descriptives("positive bigrams", positive_bigrams)
descriptives("negative bigrams", negative_bigrams)
t_test(positive_bigrams, negative_bigrams)

file.close()

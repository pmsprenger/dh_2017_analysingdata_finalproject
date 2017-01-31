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
file = open('../data/DATA_WITH_COUNTS.csv')
sys.setdefaultencoding("utf-8")
reader = csv.DictReader(file)

def bigram_counter(reader):
    prev_pos_bigr_count = []
    prev_neg_bigr_count = []
    nrev_pos_bigr_count = []
    nrev_neg_bigr_count = []
    for row in reader:
        if row['label'] == 'pos':
            pos_row = row['pos_score']
            if int(pos_row) < 5:
                prev_pos_bigr_count.append(int(pos_row))
                neg_row = row['neg_score']
            if int(neg_row) < 5:
                prev_neg_bigr_count.append(int(neg_row))
        if row['label'] == 'neg':
            pos_row = row['pos_score']
            if int(pos_row) < 5:
                nrev_pos_bigr_count.append(int(pos_row))
                neg_row = row['neg_score']
            if int(neg_row) < 5:
                nrev_neg_bigr_count.append(int(neg_row))
    return prev_neg_bigr_count, prev_pos_bigr_count, nrev_neg_bigr_count, nrev_pos_bigr_count

def descriptives(name, values):
    """
        Returns the descriptive statistics for a list of values
    """
    sorted_results = sorted(values)
    print "--------DESCRIPTIVES----", name
    print "N = {0}".format(len(values))
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

posneg, pospos, negneg, negpos = bigram_counter(reader)

# positive reviews
descriptives("negative bigrams in positive reviews", posneg)
descriptives("positive bigrams in positive reviews", pospos)

#negative reviews
descriptives("negative bigrams in negative reviews", negneg)
descriptives("positive bigrams in negative reviews", negpos)


print "Positive Bigrams appear more in positive reviews then in negative reviews"
t_test(pospos, negpos)
print "Negative bigrams appear more in negative reviews then in positive reviews"
t_test(negpos, posneg)



file.close()


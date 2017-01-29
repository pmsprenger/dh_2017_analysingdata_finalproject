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


def t_test(x, y):
    result_t_test = stats.ttest_ind(x,y, equal_var=True)
    print '--------------------'
    print 'INDEPENDENT T-TEST:'
    print '------------------'
    print "t-value = {0}".format(result_t_test[0])
    print "p-value = {0}".format(result_t_test[1])



values1, values2 = bigram_counter(reader)
t_test(values1, values2)

file.close()

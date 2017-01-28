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
    pos_bigr_count = []
    neg_bigr_count = []

    for row in reader:
        pos_row = row['pos_score']
        pos_bigr_count.append(int(pos_row))
        neg_row = row['neg_score']
        neg_bigr_count.append(int(neg_row))
    return pos_bigr_count, neg_bigr_count

def ttest(pos_bigr_count, neg_bigr_count):
    print "\nThis is the ttest for our data:"
    print scipy.stats.ttest_ind_from_stats(numpy.mean(pos_bigr_count), numpy.std(pos_bigr_count), len(pos_bigr_count), numpy.mean(neg_bigr_count), numpy.std(neg_bigr_count), len(neg_bigr_count))

counter1, counter2 = bigram_counter(reader)
ttest(counter1, counter2)

file.close()

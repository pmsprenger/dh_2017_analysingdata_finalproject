#!/usr/local/lib/python2.7

from __future__ import division
import csv
import nltk
import sys
from nltk.collocations import *

reload(sys)
file = open('DATA_WITH_COUNTS.csv')
sys.setdefaultencoding("utf-8")
reader = csv.DictReader(file)

pos_bigr_count = []
neg_bigr_count = []

for row in reader:
    pos_row = row['pos_score']
    pos_bigr_count.append(pos_row)
    neg_row = row['neg_score']
    neg_bigr_count.append(neg_row)

def ttest(pos_bigr_count, neg_bigr_count):
    print "\nThis is the ttest for our data:"
    print scipy.stats.ttest_ind_from_stats(numpy.mean(pos_bigr_count), numpy.std(pos_bigr_count), len(pos_bigr_count), numpy.mean(neg_bigr_count), numpy.std(neg_bigr_count), len(neg_bigr_count))

ttest()

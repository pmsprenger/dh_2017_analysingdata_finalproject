#!/usr/local/lib/python

from __future__ import division
import sys
import csv
import nltk
import matplotlib
import numpy 
import pylab
import scipy
import string

reload(sys)
sys.setdefaultencoding("utf-8")

mypath = "../data/"
myfile = mypath + "trainset-sentiment-extra.csv"

file = open(myfile)
reader = csv.DictReader(file)

token_list = []
for row in reader:
	if "male" in row['gender-cat']:
		token_list += nltk.word_tokenize(row['text-cat'])
print token_list

from __future__ import division
import csv
import nltk
import sys
import pickle
from collections import*
import operator
from pprint import pprint

def part_of_speech(pos):
    """
        Convert list of POS-tags into frequency dicts
    """
    pos_tag = nltk.pos_tag(pos)
    pos_dict = {}
    for item, key in pos_tag:
        if "JJ" in key:
            key = key[0:2]
        if key not in pos_dict:
            pos_dict[key] = defaultdict(int)
        pos_dict[key][item]+=1
    return pos_dict


def sort_dict(freq_dict):
    """
        Sorts the dictionary per frequency
    """
    sorted_list = sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_list


def count_values(pos_dict):
    """
        Counts POS-tags
    """
    for pos, freq in pos_dict.items():
        if pos=="JJ":
            print '------' + pos + '-------'
            print sort_dict(freq)


def main():
    # open the file
    reload(sys)
    sys.setdefaultencoding("utf-8")

    print "POSITIEF"
    pos_in = open("../data/positive.pickle","rb")
    pos_list = pickle.load(pos_in)
    lijst1 = part_of_speech(pos_list)
    count_values(lijst1)

    print "NEGATIEF"
    neg_in = open("../data/negative.pickle","rb")
    neg_list = pickle.load(neg_in)
    lijst2 = part_of_speech(neg_list)
    count_values(lijst2)

    #pos_in.close()
    neg_in.close()
if __name__ == "__main__":
    main()
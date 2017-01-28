#!/usr/local/lib/python2.7

# please change the interpreter if necessary
# the location of a mac interpreter is always different than the one on a windows

import csv
import nltk
# i removed all things that we did not need yet


def gender_lists(data):
    """
        This function returns two lists: one list with the tokens from females, and one with the tokens from males
    """
    token_list_female = []
    token_list_male = []
    for row in data:
        if 'male' == row['gender-cat']:
            token_list_male += nltk.word_tokenize(row['text-cat'])
        if 'female' == row['gender-cat']:
            token_list_female += nltk.word_tokenize(row['text-cat'])
    return token_list_female, token_list_male


def main():
    # open the file (sys.reload is totally unneccesary)
    file = open('../data/trainset-sentiment-extra.csv')
    sys.setdefaultencoding("utf-8")
    reader = csv.DictReader(file)

    list1, list2 = gender_lists(reader)
    print '-------- MALE ------'
    print list1[0:50] # only print the first 50 characters
    print '---------- FEMALE-----'
    print list2[0:50] # only print the first 50 characters
main()

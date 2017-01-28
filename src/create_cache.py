import pickle
import nltk
import sys
import csv


def main():
        # open the file
    reload(sys)
    file = open('../data/trainset-sentiment-extra.csv')
    sys.setdefaultencoding("utf-8")

    # make a dictionary
    d = [row for row in csv.DictReader(file)]

    # initialize different lists
    pos_list, neg_list = label_lists(d)

    pos_out = open("positive.pickle","wb")
    pickle.dump(pos_list, pos_out)

    neg_out = open("negative.pickle","wb")
    pickle.dump(neg_list, neg_out)

def label_lists(data):
    """
        This function returns two lists: one list with the tokens from negatives, and one with the tokens from positives.
        In addition, it also counts the amount of reviews per label.
    """
    token_list_negative = []
    token_list_positive = []
    for row in data:
        if 'pos' == row['label']:
            token_list_positive += nltk.word_tokenize(row['text-cat'])
        if 'neg' == row['label']:
            token_list_negative += nltk.word_tokenize(row['text-cat'])
    return token_list_positive, token_list_negative

if __name__ == "__main__":
    main()

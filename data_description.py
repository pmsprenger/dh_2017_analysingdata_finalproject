#!/usr/local/lib/python3.5

import csv
import nltk
import matplotlib


def unstructured_text(file):
    """
        Returns text and label separately
    """
    labels = []
    token_list = []
    for row in file:
        labels.append(row['label'])
        # use word_tokenizer for nltk (what about word_punct)
        token_list += nltk.word_tokenize(row['text-cat'])
    return labels, token_list


def labels_descriptives(labels):
    """
        Input is a list of labels retrieved from unstructured_text. Output contains statistical information about the
        labels.
    """
    pos_labels= []
    neg_labels = []
    for label in labels:
        if label == 'pos':
            pos_labels.append(label)
        if label == 'neg':
            neg_labels.append(label)
    print "-------------- LABELS ---------------------------------------"
    print "The number of positive labels is {0}".format(len(pos_labels))
    print "The number of negative labels is {0}.format(len(neg_labels))"
    print "--------------------------------------------------------------"


def corpus_description(tokens):
    """
        Input is a list of tokens retrieved from unstructured_text. Output contains corpus analysis + frequency plot
    """

    print("The corpus size is {0}".format(len(tokens)))
    print("The vocabulary size is {0}".format(len(set(tokens))))
    # plot a frequency graph with stopwords
    freqdist_1 = nltk.FreqDist(tokens)
    freqdist_1.plot(20)
    # plot a frequency graph without stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    # add tokens to list if they are not in the stopwords provided by nltk
    new_tokens = [item for item in tokens if item.lower() not in stopwords]
    freqdist_2 = nltk.FreqDist(new_tokens)
    freqdist_2.plot(20)


def main():
    # open the file, in this case trainset-sentiment
    data = open("../data/trainset-sentiment.csv", 'r')
    reader = csv.DictReader(data)
    # unlabel the data
    labels, tokens = unstructured_text(reader)

    # do things with the data
    labels_descriptives(labels)
    corpus_description(tokens)

    # close the file
    data.close()

main()

# -------------------------------------- NOTES --------------------------------------------------------------
# possible question 1: the length correlates with the label of the text?
# possible question 2: for the extra-sentiment set: is there a correlation between gender and labels? interesting for
# the literature section as well, as I read that man ten to use more negative words in language especially swearwords.
# possible question 3: we can add a new feature and think about something else which might correlate. Maybe there is a
# correlation between intensifiers and negative words? Do not know
# possible question 4: correlation between punctuation and label?
# we can use that answer to prove our model
# ----------------------------------------------------------------------------------------

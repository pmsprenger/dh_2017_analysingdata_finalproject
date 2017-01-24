import csv
import sys


positive_words = ["Don't", "I", "That", "she"]
negative_words = ["Forced", "after", "most"]


def extract_text(data):
    for row in data:
        text = row['text-cat']
        for positive_bigrams in positive_words:
            if positive_bigrams in text:
                print('yes, positive')
        for negative_bigrams in negative_words:
            if negative_bigrams in text:
                print('yes, negative')

def remove_things(file):
    for line in file:
        line = line.strip()
        print("".join(line))

def main():
    reload(sys)
    file = open('trainset-sentiment.csv')
    sys.setdefaultencoding("utf-8")
    reader = csv.DictReader(file)
    extract_text(reader)
    file.close()

    neg = open('neg_bigrams.txt')
    remove_things(neg)
    neg.close()

    #pos = open('pos_bigrams.txt')
    #pos.close()

main()



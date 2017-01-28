import csv
import sys
from nltk import bigrams, word_tokenize
from pprint import pprint


def make_list(text):
    """
        A function to sort lists in order to search faster
    """
    word_list = []
    for words in text:
        words = words.replace("\n","").split(" ")
        word_list.append((words[0], words[1]))
    return sorted(word_list)


def row_to_bigrams(row):
    sentence_bigrams = [bigram for bigram in bigrams(word_tokenize(row["text-cat"])) if bigram]
    return sentence_bigrams


def score_text(p_sentiment_list, n_sentiment_list, lines):
    scores = []
    for line in lines:
        bigram_list = row_to_bigrams(line)
        p_score_line = intersection(p_sentiment_list, bigram_list)
        n_score_line = intersection(n_sentiment_list, bigram_list)
        scores.append(
            {
                "label": line["label"],
                "text-cat": line["text-cat"],
                "pos_score": p_score_line,
                "neg_score": n_score_line
            }
        )
    return scores

def intersection(sentiment_list, sentence_bigrams):
    score = 0
    for sentiment_bigram in sentiment_list:
        score_delta = sentence_bigrams.count(sentiment_bigram)
        score += score_delta
    return score


def main():
    # open all the files
    reload(sys)
    file = open('../data/trainset-sentiment-test.csv')
    sys.setdefaultencoding("utf-8")
    reader = csv.DictReader(file)

    positive_file = open('../output/pos-150-bigrams.txt')
    negative_file = open('../output/neg-150-bigrams.txt')

    list1 = make_list(positive_file)
    list2 = make_list(negative_file)
    scores = score_text(list1, list2, reader)

    headers = ["label","text-cat","pos_score","neg_score"]
    out_file = open("../output/out.csv", 'w')
    csv_out = csv.DictWriter(f=out_file, fieldnames=headers)
    csv_out.writeheader()
    for score in scores:
        csv_out.writerow(score)

    file.close()
    positive_file.close()
    negative_file.close()
    out_file.close()

main()

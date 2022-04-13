from english_words import english_words_set as ews
import unittest


class Spellchecker:
    def __init__(self, word):
        self.word = word

    def english_word(self):
        if self.word not in ews:
            print('nice')


def open_file(filename):
    word_set = []
    with open(filename) as f:
        for word in f:
            word = word.strip()
            word_set.append(word)
    return word_set





from english_words import english_words_set as ews
import string
import unittest


def open_file(filename='englishwords.txt'):
    """
    Opens a text file and gets its word
    :param filename: string
    :return: words in the text file
    """
    word_set = []
    with open(filename, encoding='utf8') as f:
        for line in f:
            # Remove spaces, punctuations, \n, and make all the words lowercase
            line = line.strip().lower().split()
            for word in line:
                if word in string.punctuation:
                    line = line.replace(word, '')
            word_set += line
    return word_set


class Spellchecker:
    """
    Checks spelling of all words and returns suggestions of corrected word
    """
    def __init__(self, word):
        self.word_list = word
        self.wrong_words = []
        self.corrected_words = []

    def check_word(self):
        for word in self.word_list:
            if word not in ews:
                self.wrong_words.append(word)

        for word in self.wrong_words:
            temp_word = []
            for i in range(len(word) + 1):
                temp_word += [(word[:i], word[i:])]

            transpose = [L + R[1] + R[0] + R[2:] for L, R in temp_word if len(R) > 1]

            for transpose_corrected_word in transpose:
                if transpose_corrected_word in ews:
                    self.corrected_words.append(transpose_corrected_word)
                    continue

        return self.corrected_words

    def single_transposition(self):
        pass

    def __str__(self):
        return f'{self.wrong_words}, {self.corrected_words}'


a = Spellchecker(open_file())
print(a.check_word())


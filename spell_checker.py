from english_words import english_words_set as ews
import test


class Spellchecker:
    def __init__(self, word):
        self.word = word

    def english_word(self):
        if self.word in ews:
            print('nice')



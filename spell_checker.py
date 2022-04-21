from english_words import english_words_set as ews
import string


def open_file(filename='englishwords.txt'):
    """
    Opens a text file and gets its word
    :param filename: name of the file
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
    """Checks spelling of all words and returns suggestions of corrected word"""
    def __init__(self):
        self.wrong_words = []
        self.corrected_words = {}

    def single_transposition(self):
        """
        Performs single transposition on the incorrect words
        :return: The transposed words
        """
        for word in self.wrong_words:
            temp_word = []
            for i in range(len(word) + 1):
                temp_word += [(word[:i], word[i:])]

            # Takes the tuple of the left and right side of the word and by swapping the first and second element of the
            # second index, it creates a single transposition of the words
            transpose = [left + right[1] + right[0] + right[2:] for left, right in temp_word if len(right) > 1]

            for transposed_word in transpose:
                if transposed_word in ews:
                    if word in self.corrected_words:
                        self.corrected_words[word].append(transposed_word)
                    else:
                        self.corrected_words[word] = [transposed_word]
                    continue
        return self.corrected_words

    def delete_duplicates(self):
        """

        :return:
        """
        for word in self.wrong_words:
            changed_word = [letter for letter in word]

            # Finds if the letter in front of the current letter is the same which is therefore a double letter
            for length_word in range(len(word)-1):
                if word[length_word] == word[length_word + 1]:
                    changed_word.remove(word[length_word])
            changed_word = ''.join(changed_word)

            if changed_word in ews:
                if changed_word in self.corrected_words:
                    self.corrected_words[word].append(changed_word)
                else:
                    self.corrected_words[word] = [changed_word]
                continue

        return self.corrected_words

    def add_extra_word(self):
        """

        :return:
        """
        for word in self.wrong_words:
            temp_word = []

            for i in range(len(word) + 1):
                temp_word += [(word[:i], word[i:])]

            added_letter_words = [left + right[0] + right for left, right in temp_word if len(right) > 0]

            for added_words in added_letter_words:
                if added_words in ews:
                    if added_words in self.corrected_words:
                        self.corrected_words[word].append(added_words)
                    else:
                        self.corrected_words[word] = [added_words]
                    continue
        return self.corrected_words

    def find_incorrect_word(self, words):
        for word in words:
            if word not in ews:
                self.wrong_words.append(word)
        Spellchecker.single_transposition(self)
        Spellchecker.delete_duplicates(self)
        Spellchecker.add_extra_word(self)
        return self.corrected_words

    def __str__(self):
        return f'{self.wrong_words}, {self.corrected_words}'


a = Spellchecker()
print(a.find_incorrect_word(open_file()))


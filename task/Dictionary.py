import string

from config import logger


class Dictionary:
    def __init__(self, content: str) -> None:
        self.content = content

        self.count_of_symbols = 0
        self.count_of_words = 0
        self.words_frequency = {}

        self.dictionary_filling()

    def dictionary_filling(self) -> None:

        """
        Determining the number of characters, words and word frequency
        """

        for symbol in self.content:
            if symbol != ' ' and symbol != '\n':
                self.count_of_symbols += 1

        words = self.content.translate(str.maketrans('', '', string.punctuation)).split()
        self.count_of_words = len(words)

        for word in words:
            if word in self.words_frequency:
                self.words_frequency[word] += 1
            else:
                self.words_frequency[word] = 1
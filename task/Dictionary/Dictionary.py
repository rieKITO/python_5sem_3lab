import string

from config import logger
from task.Dictionary.config import punctuation, space_symbols

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

        content_len = len(self.content)
        new_content = ""
        for index in range(content_len):
            if self.content[index] not in space_symbols:
                self.count_of_symbols += 1
            if self.content[index] in punctuation:
                if 0 < index < content_len - 1:
                    if self.content[index - 1] not in punctuation and self.content[index + 1] not in punctuation or \
                       self.content[index] in space_symbols:
                        new_content += self.content[index]
            else:
                new_content += self.content[index]

        words = new_content.lower().split()
        self.count_of_words = len(words)

        for word in words:
            if word in self.words_frequency:
                self.words_frequency[word] += 1
            else:
                self.words_frequency[word] = 1

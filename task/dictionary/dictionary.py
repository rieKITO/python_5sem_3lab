from task.dictionary.dictionary_config import punctuation, space_symbols


class Dictionary:
    def __init__(self, content: str) -> None:
        if content and type(content) is not str:
            raise TypeError

        self.content = content
        self.count_of_symbols = 0
        self.count_of_words = 0
        self.words_frequency = {}

        self.dictionary_filling(self.content)

    def dictionary_filling(self, content: str) -> None:
        """
        Determining the number of characters, words and word frequency
        """
        self.count_of_symbols = 0
        self.count_of_words = 0
        self.words_frequency = {}
        self.content = content

        if type(self.content) is not str:
            raise TypeError

        content_len = len(self.content)
        new_content = ""

        for index in range(content_len):
            if self.content[index] not in space_symbols:
                self.count_of_symbols += 1
            if self.content[index] in punctuation:
                if 0 < index < content_len - 2:
                    left_symbol = self.content[index - 1]
                    right_symbol = self.content[index + 1]
                    if left_symbol not in punctuation and right_symbol not in punctuation or \
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

    def sort_dictionary(self, reverse: bool = None) -> list:
        if reverse and type(reverse) is not bool:
            raise TypeError

        if reverse:
            sorted_dictionary = sorted(self.words_frequency.items(), key=lambda x: x[1], reverse=True)
        else:
            sorted_dictionary = sorted(self.words_frequency.items(), key=lambda x: x[1], reverse=False)

        return sorted_dictionary

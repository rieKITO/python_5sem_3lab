import unittest
from task.dictionary.dictionary import Dictionary


class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = Dictionary("Sample sample sample sample content content content for for testing")
        self.empty_dictionary = Dictionary("")

    def test_init(self):
        self.assertEqual(self.dictionary.content,
                         "Sample sample sample sample content content content for for testing")
        self.assertEqual(self.dictionary.count_of_symbols, 58)
        self.assertEqual(self.dictionary.count_of_words, 10)
        self.assertEqual(self.dictionary.words_frequency,
                         {'sample': 4, 'content': 3, 'for': 2, 'testing': 1})

        self.assertEqual(self.empty_dictionary.content, "")
        self.assertEqual(self.empty_dictionary.count_of_symbols, 0)
        self.assertEqual(self.empty_dictionary.count_of_words, 0)
        self.assertEqual(self.empty_dictionary.words_frequency, {})

    def test_init_with_invalid_values(self):
        with self.assertRaises(TypeError):
            Dictionary(123)
            Dictionary([4])
            Dictionary(None)
            Dictionary(5.2)
            Dictionary({4, 8})

    def test_sort_dictionary_with_valid_values(self):
        self.assertEqual(self.dictionary.sort_dictionary(True),
                         [('sample', 4), ('content', 3), ('for', 2), ('testing', 1)])
        self.assertEqual(self.dictionary.sort_dictionary(),
                         [('testing', 1), ('for', 2), ('content', 3), ('sample', 4)])

        self.assertEqual(self.empty_dictionary.sort_dictionary(True), [])
        self.assertEqual(self.empty_dictionary.sort_dictionary(), [])

    def test_sort_dictionary_with_invalid_values(self):
        with self.assertRaises(TypeError):
            self.dictionary.sort_dictionary(123)
            self.dictionary.sort_dictionary([4])
            self.dictionary.sort_dictionary(None)
            self.dictionary.sort_dictionary(5.2)
            self.dictionary.sort_dictionary({4, 8})



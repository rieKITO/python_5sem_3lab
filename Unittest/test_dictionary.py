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
        self.assertRaises(TypeError, Dictionary.__init__, 123)
        self.assertRaises(TypeError, Dictionary.__init__, [4])
        self.assertRaises(TypeError, Dictionary.__init__, None)
        self.assertRaises(TypeError, Dictionary.__init__, 5.2)
        self.assertRaises(TypeError, Dictionary.__init__, {4, 8})

    def test_dictionary_filling(self):
        self.dictionary.dictionary_filling("      ! \ # $ % & ' ( )  * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~ ")
        self.assertEqual(self.dictionary.count_of_symbols, 32)
        self.assertEqual(self.dictionary.words_frequency, {})

        self.dictionary.dictionary_filling("!?abc-cba .hhh. - da")
        self.assertEqual(self.dictionary.words_frequency, {'abc-cba': 1, 'hhh': 1, 'da': 1})

    def test_dictionary_filling_with_invalid_values(self):
        self.assertRaises(TypeError, self.dictionary.dictionary_filling, 4)
        self.assertRaises(TypeError, self.dictionary.dictionary_filling)
        self.assertRaises(TypeError, self.dictionary.dictionary_filling, None)
        self.assertRaises(TypeError, self.dictionary.dictionary_filling, 5.2)
        self.assertRaises(TypeError, self.dictionary.dictionary_filling, {4, 8})
        self.assertRaises(TypeError, self.dictionary.dictionary_filling, [4])

    def test_sort_dictionary_with_valid_values(self):
        self.assertEqual(self.dictionary.sort_dictionary(True),
                         [('sample', 4), ('content', 3), ('for', 2), ('testing', 1)])
        self.assertEqual(self.dictionary.sort_dictionary(),
                         [('testing', 1), ('for', 2), ('content', 3), ('sample', 4)])

        self.assertEqual(self.empty_dictionary.sort_dictionary(True), [])
        self.assertEqual(self.empty_dictionary.sort_dictionary(), [])

    def test_sort_dictionary_with_invalid_values(self):
        self.assertRaises(TypeError, self.dictionary.sort_dictionary, 123)
        self.assertRaises(TypeError, self.dictionary.sort_dictionary, [4])
        self.assertRaises(TypeError, self.dictionary.sort_dictionary, 5.2)
        self.assertRaises(TypeError, self.dictionary.sort_dictionary, {4, 8})
        self.assertRaises(TypeError, self.dictionary.sort_dictionary, "adc")

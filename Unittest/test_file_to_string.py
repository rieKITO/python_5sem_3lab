import os
import unittest
from utils.file_to_string import file_to_string
from unittest.mock import patch, mock_open


class TestFileToString(unittest.TestCase):
    def test_file_to_string_with_valid_file(self):
        expected_result = "bb aaa b b a a aaa aaa"
        with patch('builtins.open', mock_open(read_data=expected_result)):
            actual_result = file_to_string("../test_1.txt")
            self.assertEqual(actual_result, expected_result)

        expected_result = ""
        with patch('builtins.open', mock_open(read_data=expected_result)):
            actual_result = file_to_string("../empty.txt")
            self.assertEqual(actual_result, expected_result)

    def test_file_to_string_with_invalid_file(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                file_to_string('../invalid_file.txt')

    def test_file_to_string_with_invalid_values(self):
        with self.assertRaises(TypeError):
            file_to_string(123)
            file_to_string([4])
            file_to_string(None)
            file_to_string(5.2)
            file_to_string({4, 8})

    def test_large_file(self):
        with open('../large.txt', 'w') as file:
            for i in range(10000):
                file.write('This is a line\n')
        self.assertEqual(len(file_to_string('../large.txt')), 150000)

    def test_different_encodings(self):
        with open('../utf8.txt', 'w', encoding='utf-8') as file:
            file.write('UTF-8 encoding')

        with open('../ascii.txt', 'w', encoding='ascii') as file:
            file.write('ASCII encoding')

        self.assertEqual(file_to_string('../utf8.txt'), 'UTF-8 encoding')
        self.assertEqual(file_to_string('../ascii.txt'), 'ASCII encoding')

    def test_no_read_permission(self):
        with self.assertRaises(PermissionError):
            file_to_string('../unreadable_file.txt')

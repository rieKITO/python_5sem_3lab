import unittest
from utils.file_to_string import file_to_string
import unittest.mock


class TestFileToString(unittest.TestCase):
    def test_file_to_string_returns_file_content(self):
        file_content = "First line \n Second line    \n third line"
        with unittest.mock.patch(
            'builtins.open',
            new=unittest.mock.mock_open(read_data=file_content),
            create=True
        ):
            self.assertEqual(file_content, file_to_string("test_path"))

    def test_file_to_string_on_empty_file_return_empty_string(self):
        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=""),
            create=True
        ):
            self.assertEqual("", file_to_string("test_path"))

    def test_file_to_string_with_nonexistent_file(self):
        self.assertRaises(FileNotFoundError, file_to_string, '../invalid_file.txt')

    def test_file_to_string_with_invalid_values(self):
        self.assertRaises(TypeError, file_to_string, 123)
        self.assertRaises(TypeError, file_to_string, [4])
        self.assertRaises(TypeError, file_to_string, None)
        self.assertRaises(TypeError, file_to_string, 5.2)
        self.assertRaises(TypeError, file_to_string, {4, 8})

    def test_file_to_string_with_large_file(self):
        file_content = ""
        for i in range(10000):
            file_content += "This is a line\n"
        with unittest.mock.patch(
            'builtins.open',
            new=unittest.mock.mock_open(read_data=file_content),
            create=True
        ):
            self.assertEqual(len(file_content), len(file_to_string("test_path")))

    def test_file_to_string_with_different_encodings(self):
        file_content = "UTF-8 encoding".encode("utf-8")
        file_content = file_content.decode("utf-8")
        with unittest.mock.patch(
            'builtins.open',
            new=unittest.mock.mock_open(read_data=file_content),
            create=True,

        ):
            self.assertEqual(file_content, file_to_string("test_path"))

        file_content = "ASCII encoding".encode("ascii")
        file_content = file_content.decode("ascii")
        with unittest.mock.patch(
                'builtins.open',
                new=unittest.mock.mock_open(read_data=file_content),
                create=True
        ):
            self.assertEqual(file_content, file_to_string("test_path"))

    def test_file_to_string_with_no_read_permission_file(self):
        with unittest.mock.patch(
                'builtins.open',
                side_effect=PermissionError
        ):
            self.assertRaises(PermissionError, file_to_string, "test_path")

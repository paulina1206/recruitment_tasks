import unittest
from task2 import scan_directory
from unittest.mock import patch


class TestScanDirectory(unittest.TestCase):

    @patch("os.path.getsize")
    @patch('os.walk')
    def test_scan_directory(self, mock_walk, getsize):
        mock_walk.return_value = [('/usr/share/doc', ('',), ('file.txt',)),
                                  ('/usr/share/doc', ('',), ('file2.txt',)),
                                  ('/usr/share/doc', ('',), ('abaaba2.txt',))]
        getsize.return_value = 1024 ** 2 + 4
        dir_path = '/usr/share/doc'
        actual = scan_directory(dir_path)
        expected = {'aba': [(1048580, 'abaaba2.txt')], 'fil': [(1048580, 'file.txt'), (1048580, 'file2.txt')]}
        self.assertEqual(actual, expected)

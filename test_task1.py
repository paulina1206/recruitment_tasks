import unittest
from task1 import new_list


class TestNewList(unittest.TestCase):
    def test_new_list(self):
        # first test scenario
        a = ['test', 'customer', 'democratic', 'exist', 'evening',
             'often', 'outside', 'weight']
        b = ['weapon', 'western', 'test', 'guess', 'customer', 'exist',
             'democratic', 'Congress', 'finish', 'executive']
        actual = new_list(a, b)
        # expected returned list
        expected = ['test', 'exist', 'customer', 'democratic']
        self.assertEqual(actual, expected)
        # bad ordered list
        bad_order = ['test', 'democratic', 'exist', 'customer']
        self.assertNotEqual(actual, bad_order)
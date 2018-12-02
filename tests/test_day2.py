import unittest
from advent.day2 import checksum

class TestDay2(unittest.TestCase):

    def test_checksum(self):
        test_data = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        expected = 12
        actual = checksum(test_data)
        self.assertEqual(expected, actual)

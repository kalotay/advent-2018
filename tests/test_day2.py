import unittest
from advent.day2 import checksum, commonletters

class TestDay2(unittest.TestCase):

    def test_checksum(self):
        test_data = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        expected = 12
        actual = checksum(test_data)
        self.assertEqual(expected, actual)

    def test_commonletters(self):
        test_data = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
        expected = "fgij"
        actual = commonletters(test_data)
        self.assertEqual(expected, actual)

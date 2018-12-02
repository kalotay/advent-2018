import unittest
from advent.day1 import frequency, firstduplicatefreq

class TestDay1(unittest.TestCase):

    def test_frequency(self):
        self.assertEqual(frequency([+1, -2, +3, +1]), 3)
        self.assertEqual(frequency([+1, +1, +1]), 3)
        self.assertEqual(frequency([+1, +1, -2]), 0)
        self.assertEqual(frequency([-1, -2, -3]), -6)
    
    def test_firstduplicatefreq(self):
        self.assertEqual(firstduplicatefreq([+1, -2, +3, +1]), 2)
        self.assertEqual(firstduplicatefreq([+1, -1]), 0)
        self.assertEqual(firstduplicatefreq([+3, +3, +4, -2, -4]), 10)
        self.assertEqual(firstduplicatefreq([-6, +3, +8, +5, -6]), 5)
        self.assertEqual(firstduplicatefreq([+7, +7, -2, -7, -4]), 14)

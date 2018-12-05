import unittest
from advent.day3 import overlaparea, parseclaim, Claim, findunique

class TestDay2(unittest.TestCase):

    def test_overlaparea(self):
        test_data = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        expected = 4
        actual = overlaparea(test_data)
        self.assertEqual(expected, actual)

    def test_parseclaim(self):
        expected = Claim(id='2', left=3, top=1, width=4, height=4)
        actual = parseclaim("#2 @ 3,1: 4x4")
        self.assertEqual(expected, actual)

    def test_findunique(self):
        test_data = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        expected = frozenset('3')
        actual = findunique(test_data)
        self.assertEqual(expected, actual)

"""tdd: test driven development
1. write test
2. run test - fail
3. write code
4. re-run test - pass
"""

from unittest import TestCase
import simple as s


class TestSimple(TestCase):
    def test_add1(self):
        result = s.add1(3)
        answer = 4
        self.assertEqual(result, answer)

    def test_square(self):
        result = s.square(3)
        answer = 9
        self.assertEqual(result, answer)

    def test_is_even(self):
        result = s.is_even(2)
        self.assertTrue(result)
        result = s.is_even(3)
        self.assertFalse(result)

    def test_get_odds(self):
        nums = range(3, 20)
        odds = s.get_odds(nums)
        self.assertIsInstance(odds, list)
        self.assertEqual(len(odds), 9)
        self.assertIn(5, odds)
        self.assertNotIn(6, odds)

    def test_dot_product(self):
        v1 = [1, 2]
        v2 = [4, 5]
        result = s.dot_product(v1, v2)
        answer = 14
        self.assertEqual(result, answer)
        self.assertIsInstance(result, int)

import unittest
from ..functions import (count_characters, invert_dictionary, max_lists,
                         merge_dictionaries, matrix_multiplication, get_diagonal,
                         get_min, get_max)


class TestFunctions(unittest.TestCase):
    def test_count_characters(self):
        string = "abafdcggfaabe"
        answer = {"a": 4, "b": 2, "c": 1, "d": 1, "e": 1, "f": 2, "g": 2}
        result = count_characters(string)
        self.assertEqual(result, answer)

    def test_invert_dictionary(self):
        d = {"a": 4, "b": 2, "c": 1, "d": 1, "e": 1, "f": 2, "g": 2}
        result = {4: {'a'}, 2: {'b', 'f', 'g'}, 1: {'c', 'd', 'e'}}
        self.assertEqual(invert_dictionary(d), result)


class TestMinMax(unittest.TestCase):
    def test_get_min_without_arguments(self):
        with self.assertRaises(ValueError):
            get_min()

    def test_get_min_with_one_argument(self):
        # write your test here
        result = get_min(3)
        answer = 3
        self.assertEqual(
            answer, result, 'the result is not equal the answer, ERR(:')

    def test_get_min_with_many_arguments(self):
        # write your test here
        self.assertEqual(3, get_min(3, 5))

    def test_get_max_without_arguments(self):
        # write your test here
        with self.assertRaises(ValueError):
            get_max()

    def test_get_max_with_one_argument(self):
        # write your test here
        self.assertEqual(3, get_max(3))

    def test_get_max_with_many_arguments(self):
        # write your test here
        self.assertEqual(5, get_max(3, 5))

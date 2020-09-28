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

    def test_max_lists(self):
        result = max_lists([5, 7, 2, 3, 6], [3, 9, 1, 2, 8])
        self.assertEqual(result, [5, 9, 2, 3, 8])

    def test_get_diagonal(self):
        result = get_diagonal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        self.assertEqual(result, [1, 6, 11])

    def test_merge_dictionaries(self):
        result = merge_dictionaries({"a": 1, "b": 5, "c": 1, "e": 8},
                                    {"b": 2, "c": 5, "d": 10, "f": 6})
        self.assertEqual(result, {"a": 1, "b": 7, "c": 6, "d": 10, "e": 8, "f": 6})

    def test_matrix_multiplication(self):
        A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]]
        B = [[8, -3, 1], [-7, 3, 2], [0, 3, 3]]
        answer = [[-5, 15, 20], [20, 0, 20], [-22, 9, 3]]
        self.assertEqual(matrix_multiplication(A, B), answer)


class TestMinMax(unittest.TestCase):
    def test_get_min_without_arguments(self):
        with self.assertRaises(ValueError):
            get_min()

    def test_get_min_with_one_argument(self):
        # write your test here
        assert False

    def test_get_min_with_many_arguments(self):
        # write your test here
        assert False

    def test_get_max_without_arguments(self):
        # write your test here
        assert False

    def test_get_max_with_one_argument(self):
        # write your test here
        assert False

    def test_get_max_with_many_arguments(self):
        # write your test here
        assert False

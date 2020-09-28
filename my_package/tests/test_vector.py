from vector import Vector
from unittest import TestCase


class TestVector(TestCase):
    def test_make_vector(self):
        v = Vector()
        self.assertIsInstance(v, Vector)

    def test_create_vector_from_list(self):
        v = Vector([1, 2, 3])
        self.assertEqual(len(v.__nums), 3)

    def test_create_vector_from_list(self):
        v = Vector([1, 2, 3, 4])
        self.assertEqual(len(v), 4)

    def test_create_vector_from_file(self):
        filename = 'vectors.csv'
        vectors = Vector.from_file(filename)
        self.assertEqual(len(vectors), 5)

    def test_add_vectors(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v3 = v1 + v2
        self.assertIsInstance(v3, Vector)
        self.assertEqual(v3._nums, [5, 7, 9])

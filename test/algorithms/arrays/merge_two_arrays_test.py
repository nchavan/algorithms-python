import unittest

from src.main.algorithms.arrays.merge_two_arrays import mergeArrays

class TestMergeTwoArrays(unittest.TestCase):

    def test_merge_two_arrays(self):
        arr1 = [10, 20, 3, 4, 5, 6, 7]
        arr2 = [11, 2, 30, 4, 5, 6, 7]

        result = mergeArrays(arr1, arr2)
        self.assertEqual(result, [2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 10, 11, 20, 30])

    def test_merge_two_empty_arrays(self):
        arr1 = []
        arr2 = []

        result = mergeArrays(arr1, arr2)
        self.assertEqual(result, [])

    def test_merge_two_undefined_arrays(self):
        arr1 = None
        arr2 = None

        result = mergeArrays(arr1, arr2)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
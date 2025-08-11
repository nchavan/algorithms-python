import unittest

from src.main.algorithms.arrays.rotate_array import rotate_array

class TestRotateArrays(unittest.TestCase):

    def test_rotate_arrays(self):
        arr1 = [1, 4, 5, 8, 12, 111]
        expArr2 = [111, 1, 4, 5, 8, 12]

        result = rotate_array(arr1, 1)
        self.assertEqual(result, expArr2)


if __name__ == '__main__':
    unittest.main()
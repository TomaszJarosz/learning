from unittest import TestCase

from python.algorithms.freeCodeCamp.kth_largest_element import kth_largest_element_hepq


class Test(TestCase):
    def test_kth_largest_element_0(self):
        arr = [1, 3, 2, 6, 4, 4, 6, 4, 9]
        k = 2
        result = kth_largest_element_hepq(arr, k)
        self.assertEqual(6, result, 'Should return 2')

    def test_kth_largest_element_1(self):
        arr = [1, 3, 2, 6, 4, 4, 6, 4, 9]
        k = 6
        result = kth_largest_element_hepq(arr, k)
        self.assertEqual(4, result, 'Should return 4')

    def test_kth_largest_element_2(self):
        arr = [1, 3, 2, 6, 4, 4, 6, 4, 9]
        k = -1
        with self.assertRaises(Exception) as context:
            kth_largest_element_hepq(arr, k)
        self.assertEqual('k should be in range: 1<= k <= len(given_array)', str(context.exception))

from unittest import TestCase

from python.algorithms.sorting.quicksort import quicksort


class QuickSortTest(TestCase):
    def test_quicksort0(self):
        unsorted_list = [3, 6, 3, 1, 3, 1, 2, 4, 8]
        result = quicksort(unsorted_list)
        self.assertListEqual([1, 1, 2, 3, 3, 3, 4, 6, 8], result, "Should be equals [1, 1, 2, 3, 3, 3, 4, 6, 8]")

    def test_quicksort1(self):
        unsorted_list = []
        result = quicksort(unsorted_list)
        self.assertListEqual([], result, "Should return empty list")

    def test_quicksort2(self):
        unsorted_list = [1]
        result = quicksort(unsorted_list)
        self.assertListEqual([1], result, "Should be equals [1]")

    def test_quicksort3(self):
        unsorted_list = [1, 1]
        result = quicksort(unsorted_list)
        self.assertListEqual([1, 1], result, "Should be equals [1,1]")

    def test_quicksort4(self):
        unsorted_list = [2, 1]
        result = quicksort(unsorted_list)
        self.assertListEqual([1, 2], result, "Should be equals [1,2]")

    def test_quicksort5(self):
        unsorted_list = None
        with self.assertRaises(Exception) as context:
            quicksort(unsorted_list)
        self.assertEqual(str(context.exception), "object of type 'NoneType' has no len()")

from unittest import TestCase

from python.algorithms.sorting.bubblesort import bubble_sort


class BubbleSort(TestCase):
    def test_bubble_sort(self):
        unsorted_list = [10, 4, 3, 7, 5]
        result = bubble_sort(unsorted_list)

        self.assertListEqual([3, 4, 5, 7, 10], result, 'list should be sorted: [3, 4, 5, 7, 10]')

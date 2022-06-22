from unittest import TestCase

from python.algorithms.sorting.selectionsort import selection_sort


class TestSelectionSort(TestCase):
    def test_selection_sort0(self):
        list_to_sort = [4, 1, 5, 3, 2]
        result = selection_sort(list_to_sort)
        self.assertEqual([1, 2, 3, 4, 5], result), "Should be [1, 2, 3, 4, 5]"

    def test_selection_sort1(self):
        list_to_sort = [1, 2, 3, 4, 5]
        result = selection_sort(list_to_sort)
        assert result == [1, 2, 3, 4, 5], "Should be [1, 2, 3, 4, 5]"

    def test_selection_sort2(self):
        list_to_sort = [4, 1]
        result = selection_sort(list_to_sort)
        assert result == [1, 4], "Should be [1, 4]"

    def test_selection_sort3(self):
        list_to_sort = [1]
        result = selection_sort(list_to_sort)
        assert result == [1], "Should be [1]"

    def test_selection_sort_empty_list(self):
        list_to_sort = []
        result = selection_sort(list_to_sort)
        assert result == [], "Should be []"

    def test_selection_sort_none_value(self):
        list_to_sort = None
        with self.assertRaises(Exception) as context:
            selection_sort(list_to_sort)

        self.assertTrue('object of type \'NoneType\' has no len()' in str(context.exception))

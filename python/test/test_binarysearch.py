from unittest import TestCase

from python.algorithms.search.binarysearch import binary_search_sam


class Test(TestCase):
    def test_binary_iterative_search(self):
        list_to_search = [1, 2, 3, 4, 5]
        result = binary_search_sam(list_to_search, 4)
        self.assertEqual(3, result, 'Should return index 3')

    # def test_binary_recursive_search(self):
    #     list_to_search = [1, 2, 3, 4, 5]
    #     result = binary_search_recursive(list_to_search, 4, 0, len(list_to_search) - 1)
    #     self.assertEqual(3, result, 'Should return index 3')

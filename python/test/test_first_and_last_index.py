from unittest import TestCase

from python.algorithms.freeCodeCamp.first_and_last_index import first_last_index


class Test(TestCase):
    def test_first_last_index_1(self):
        # given
        arr = [1, 2, 3, 3, 3, 5, 5, 6, 8]
        target = 3
        # when
        result = first_last_index(arr, target)
        # then
        self.assertEqual([2, 4], result, 'Should return first index = 2, last index = 4')

    def test_first_last_index_2(self):
        # given
        arr = [1, 2, 3, 3, 3, 5, 5, 6, 8]
        target = 4
        # when
        result = first_last_index(arr, target)
        # then
        self.assertEqual([-1, -1], result, 'When target not found then return [-1,-1]')

    def test_first_last_index_3(self):
        # given
        arr = [1, 2]
        target = 4
        # when
        result = first_last_index(arr, target)
        # then
        self.assertEqual([-1, -1], result, 'When target not found then return [-1,-1]')

    def test_first_last_index_4(self):
        # given
        arr = [1]
        target = 4
        # when
        result = first_last_index(arr, target)
        # then
        self.assertEqual([-1, -1], result, 'When target not found then return [-1,-1]')

    def test_first_last_index_5(self):
        # given
        arr = None
        target = 4
        # when
        with self.assertRaises(Exception) as context:
            first_last_index(arr, target)
        # then
        self.assertEqual('object of type \'NoneType\' has no len()', str(context.exception))

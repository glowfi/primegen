import unittest
import algo


class MultiplyTestCase(unittest.TestCase):

    # Lower limit > upper should return []
    def test_if_lower_greater_than_upper(self):
        result = algo.algo_V1(100, 10)
        self.assertEqual(result, [])

    # negative range should return []
    def test_negative_range_2(self):
        result = algo.algo_V1(-1, -10)
        self.assertEqual(result, [])

    # Test algov1
    def test_algo_V1(self):
        result = algo.algo_V1(2, 10)
        self.assertEqual(result, [2, 3, 5, 7])

    # Test algov2
    def test_algo_V2(self):
        result = algo.algo_V2(2, 10)
        self.assertEqual(result, [2, 3, 5, 7])

    # Test algov3
    def test_algo_V3(self):
        result = algo.algo_V3(2, 10)
        self.assertEqual(result, [2, 3, 5, 7])

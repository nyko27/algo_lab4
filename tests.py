import unittest
from util import algorithm


class AlgorithmTester(unittest.TestCase):

    def test_algorithm_on_first_data_example(self):
        self.assertEqual(algorithm('input_1.txt'), 3)

    def test_algorithm_on_second_data_example(self):
        self.assertEqual(algorithm('input_2.txt'), 1)

    def test_algorithm_on_third_data_example(self):
        self.assertEqual(algorithm('input_3.txt'), 3)

    def test_algorithm_on_third_data_example(self):
        self.assertEqual(algorithm('input_4.txt'), 5)


if __name__ == '__main__':
    unittest.main()

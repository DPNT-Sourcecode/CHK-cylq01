import unittest

from solutions.SUM import sum_solution


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_solution.compute(1, 2), 3)

    def test_notequal(self):
        self.assertNotEqual(sum_solution.compute(1,1), 3)


if __name__ == '__main__':
    unittest.main()

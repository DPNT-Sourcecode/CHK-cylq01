import unittest

from solutions.CHK import checkout_solution


class TestSum(unittest.TestCase):
    def test_invalid(self):
        self.assertEqual(checkout_solution.checkout('ABCa'), -1)

    def test_empty_checkout(self):
        self.assertEqual(checkout_solution.checkout(''), 0)

    def test_one_of_each(self):
        self.assertEqual(checkout_solution.checkout('ABCD'), 50 + 30 +20 + 15)

    def test_special_offer(self):
        self.assertEqual(checkout_solution.checkout('AAABBB'), 130 + 75)

    def test_multi_special_offers(self):
        self.assertEqual(checkout_solution.checkout('AAAAAAAAA'), 200 + 130 + 50)

    def test_buy_2E_get_B_free(self):
        self.assertEqual(checkout_solution.checkout('BBBBEE'), 45+30+80)

if __name__ == '__main__':
    unittest.main()

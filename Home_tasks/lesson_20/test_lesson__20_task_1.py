"""Testing store Veselka"""


import unittest
from lec_20_Тестирование import Product, ProductStore


class TestProductStore(unittest.TestCase):
    def setUp(self):
        self.prod1 = Product('Ball', 'Abibas', 1000)
        self.prod2 = Product('Coca Cola', 'Nestle', 20)
        self.veselka = ProductStore()

    def test_add(self):
        self.veselka.add(self.prod1, 10)
        self.veselka.add(self.prod2, 15)
        self.assertEqual(self.veselka.products, {self.prod1: 10, self.prod2: 15})

    def test_set_discount(self):
        self.veselka.add(self.prod1, 10)
        self.veselka.set_discount('Abibas', 30)
        self.assertEqual(round(self.prod1.price), 910, 'No discount for losers')

    def test_sell_product(self):
        self.prod1 = Product('Ball', 'Abibas', 1000)
        self.assertRaises(Exception, self.veselka.sell_product('Ball', 1000), 'Hello')

    def test_get_income(self):
        self.veselka.get_income()
        self.assertEqual(self.veselka.cash, 0, 'Low money')

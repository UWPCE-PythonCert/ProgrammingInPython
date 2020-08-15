import unittest

import calculator_functions as calc


def setUpModule():
    print("running setup module")


class TestCalculatorFunctions(unittest.TestCase):

    def setUp(self):
        print("running setup")
        self.x = 2
        self.y = 3

    def tearDown(self):
        print("running teardown")

    def test_add(self):
        print("running test_add")
        self.assertEqual(calc.add(self.x, self.y), 5)

    def test_add2(self):
        print("running test_add2")
        self.assertEqual(calc.add(7, 8), 15)


# class TestCalculatorFunctions2(unittest.TestCase):

#     def setUp(self):
#         self.x = 2
#         self.y = 3

#     def test_add(self):
#         self.assertEqual(calc.subtract(self.y, self.x), 1)

if __name__ == "__main__":
    unittest.main()

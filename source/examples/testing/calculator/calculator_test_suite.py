import unittest

from test_calculator import TestCalculatorFunctions

suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)

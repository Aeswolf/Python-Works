"""
This file helps to understand unit testing  in python.
In order to perform a unit test in python, the module unittest must first be imported
This module comes with the python standard library and as such does not require any installation
To be able to perform a unit test, a class must first be created which inherits from unittest.TestCase

"""

import unittest
from Applications import NotPrimeNumbers


# function to be tested
def add(x, y):
    return x + y


# function to test the output of the not_prime_numbers method


# class required to perform unit test
class TestAddFunction(unittest.TestCase):
    def test_add_function(self):
        self.assertEqual(add(30, 10), 40)
        self.assertEqual(add(-1, -1), -2)
        self.assertTrue(add(-1, 5), 4)

    def test_not_prime_numbers(self):
        self.assertEqual(NotPrimeNumbers.not_prime_number(2, 30), [22, 25, 27])


if __name__ == '__main__':
    unittest.main()


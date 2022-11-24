#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Subtraction import subtraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to subtract two numbers
        """
        a=30
        b=30
        result = subtraction(a,b)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()

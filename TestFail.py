#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from SUbtraction import subtraction

class TestSubtract(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to subtract two numbers
        """
        a=30
        b=30
        result = subtraction(a,b)
        self.assertEqual(result, 500)

if __name__ == '__main__':
    unittest.main()

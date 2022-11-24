#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Subtraction import subtraction

class TestSubtract(unittest.TestCase):
    def test_case1_int(self):
        """
        Test case to subtract two numbers
        """
        a=30
        b=30
        result1 = subtraction(a,b)
        self.assertEqual(result1, 0)
        
    def test_case2_int(self):
        """
        Test case to subtract two numbers
        """
        c=60
        d=30
        result2 = subtraction(c,d)
        self.assertEqual(result2, 30)
    
    def test_case3_int(self):
        """
        Test case to subtract two numbers
        """
        e=100
        f=40
        result3 = subtraction(e,f)
        self.assertEqual(result3, 60)

if __name__ == '__main__':
    unittest.main()

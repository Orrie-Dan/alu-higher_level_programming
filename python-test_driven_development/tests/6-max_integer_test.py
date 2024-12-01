# tests/6-max_integer_test.py

import unittest
from max_integer import max_integer  # Import the function to test

class TestMaxInteger(unittest.TestCase):
    
    # Test case 1: Test a normal list with multiple integers
    def test_normal_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
    
    # Test case 2: Test a list with negative integers
    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
    
    # Test case 3: Test a list with a single integer
    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)
    
    # Test case 4: Test an empty list
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))  # We expect None since the list is empty
    
    # Test case 5: Test a list with all identical integers
    def test_identical_integers(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
    
    # Test case 6: Test a list with mix of positive and negative integers
    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 0, 3, 2, -5]), 3)

    # Test case 7: Test an empty list (using default argument)
    def test_default_empty_list(self):
        self.assertIsNone(max_integer())  # Since the default list is empty, it should return None

if __name__ == "__main__":
    unittest.main()


import unittest
from max_in_list import max_in_list  # Import the function

class TestMaxInList(unittest.TestCase):
    
    def test_max_at_the_end(self):
        """Test case where the maximum value is at the end of the list"""
        result = max_in_list([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)
    
    def test_max_at_the_beginning(self):
        """Test case where the maximum value is at the beginning of the list"""
        result = max_in_list([5, 4, 3, 2, 1])
        self.assertEqual(result, 5)
    
    def test_max_in_the_middle(self):
        """Test case where the maximum value is in the middle of the list"""
        result = max_in_list([1, 5, 3, 2, 4])
        self.assertEqual(result, 5)
    
    def test_one_negative_number(self):
        """Test case where there is one negative number in the list"""
        result = max_in_list([1, -1, 2])
        self.assertEqual(result, 2)
    
    def test_only_negative_numbers(self):
        """Test case where the list contains only negative numbers"""
        result = max_in_list([-1, -2, -3])
        self.assertEqual(result, -1)
    
    def test_list_of_one_element(self):
        """Test case where the list contains only one element"""
        result = max_in_list([42])
        self.assertEqual(result, 42)
    
    def test_empty_list(self):
        """Test case where the list is empty"""
        with self.assertRaises(ValueError):
            max_in_list([])

    def test_invalid_input_type(self):
        """Test case where input is not a list"""
        with self.assertRaises(TypeError):
            max_in_list("not a list")
    
    def test_non_numeric_elements(self):
        """Test case where the list contains non-numeric elements"""
        with self.assertRaises(TypeError):
            max_in_list([1, 2, 'a', 4])

if __name__ == '__main__':
    unittest.main()


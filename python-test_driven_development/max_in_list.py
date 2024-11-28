# max_in_list.py
def max_in_list(numbers):
    """Find the maximum number in a list of numbers"""
    
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    
    # Check if all elements are integers or floats
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be integers or floats")
    
    return max(numbers)


#!/usr/bin/python3

"""
This function takes an instance of a class and returns a dictionary representation
of the object, making all attributes serializable for JSON serialization.
"""

def class_to_json(obj):
    """
    Convert the instance of a class to a dictionary representation for JSON serialization.
    
    Args:
        obj: An instance of a class.
        
    Returns:
        A dictionary representation of the object, where all attributes are serializable.
    """
    # Create an empty dictionary to store the attributes of the object
    result = {}

    # Iterate over the attributes of the object (using the __dict__ of the object)
    for attr, value in obj.__dict__.items():
        # Only add attributes that are of simple, JSON-serializable types
        if isinstance(value, (str, int, float, bool, list, dict)):
            result[attr] = value
    
    # Return the dictionary representation
    return result

# Example class to demonstrate functionality
class MyClass:
    def __init__(self, name, age, is_active, tags):
        self.name = name       # string
        self.age = age         # integer
        self.is_active = is_active # boolean
        self.tags = tags       # list

# Create an instance of MyClass
obj = MyClass("John", 30, True, ["developer", "python"])

# Convert the object to a dictionary using class_to_json function
json_compatible = class_to_json(obj)
print(json_compatible)


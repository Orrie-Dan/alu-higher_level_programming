#!/usr/bin/python3
Square = __import__('3-square').Square

# Creating a Square instance with a valid size
my_square = Square(5)
print(type(my_square))  # <class '__main__.Square'>
print(my_square.__dict__)  # {'_Square__size': 5}
print(my_square.area())  # 25 (5 * 5)

# Creating a Square instance with the default size (0)
default_square = Square()
print(default_square.area())  # 0 (0 * 0)

# Testing with invalid values
try:
    invalid_square = Square(-5)  # This should raise a ValueError
except Exception as e:
    print(e)  # Output: size must be >= 0

try:
    invalid_square = Square("5")  # This should raise a TypeError
except Exception as e:
    print(e)  # Output: size must be an integer

# Testing setter with invalid size
try:
    my_square.size = -3  # This should raise a ValueError
except Exception as e:
    print(e)  # Output: size must be >= 0

try:
    my_square.size = "10"  # This should raise a TypeError
except Exception as e:
    print(e)  # Output: size must be an integer

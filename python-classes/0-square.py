#!/usr/bin/python3
class Square:
    """Represents a square."""

    def __init__(self):
        """Initialize a new Square instance."""
        self.dict_ = {}

# Usage example
if __name__ == "__main__":
mysquare = Square()
print(type(mysquare))  # Output: <class '__main__.Square'>
print(mysquare.dict_)  # Output: {}

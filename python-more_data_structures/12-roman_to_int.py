#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    # Mapping of Roman numerals to integers
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Iterate over the string in reverse
    for char in reversed(roman_string):
        value = roman_map.get(char, 0)
        if value < prev_value:
            total -= value  # Subtract if the current value is less than the previous one
        else:
            total += value  # Add if the current value is greater or equal to the previous one
        prev_value = value

    return total

# Example usage
if __name__ == "__main__":
    print(roman_to_int("III"))        # Output: 3
    print(roman_to_int("IV"))         # Output: 4
    print(roman_to_int("IX"))         # Output: 9
    print(roman_to_int("LVIII"))      # Output: 58
    print(roman_to_int("MCMXCIV"))    # Output: 1994
    print(roman_to_int(None))         # Output: 0
    print(roman_to_int(123))          # Output: 0


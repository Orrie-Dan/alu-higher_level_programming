#!/usr/bin/python3
def islower(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')

# Test cases for checking the function
def main():
    test_cases = ['a', 'z', 'A', 'Z', '4', '!']
    
    for char in test_cases:
        if islower(char):
            print(f"{char} => lower")
        else:
            print(f"{char} => upper")

if __name__ == "__main__":
    main()


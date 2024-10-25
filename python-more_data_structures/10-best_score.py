#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Initialize variables to track the best score and corresponding key
    best_key = None
    max_value = float('-inf')

    # Iterate over the dictionary items
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            best_key = key

    return best_key

# Example usage
if __name__ == "__main__":
    scores = {'Alice': 90, 'Bob': 85, 'Charlie': 95}
    result = best_score(scores)
    print(result)  # Output: Charlie

    # Test with an empty dictionary
    empty_scores = {}
    print(best_score(empty_scores))  # Output: None


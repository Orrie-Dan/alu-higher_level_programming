#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            # Check if the current index is valid for both lists
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result.append(0)  # Append 0 for out of range cases
                continue

            # Attempt to divide the elements
            num1 = my_list_1[i]
            num2 = my_list_2[i]

            if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                print("wrong type")
                result.append(0)  # Append 0 for wrong type cases
                continue

            # Perform the division
            result.append(num1 / num2)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)  # Append 0 for division by zero
        except Exception as e:
            print("wrong type")  # Catch any other unforeseen exceptions
            result.append(0)  # Append 0 for any other type issues
        finally:
            # Optionally could be used for any cleanup, but not necessary here
            pass

    return result

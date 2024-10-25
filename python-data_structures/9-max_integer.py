#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)  # If the sentence is empty
    else:
        return (len(sentence), sentence[0])  # Length and first character


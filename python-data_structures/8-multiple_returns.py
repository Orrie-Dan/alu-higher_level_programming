#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)  # Length is 0 and first character is None
    else:
        return (len(sentence), sentence[0])  # Length and first character


#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')
if __name__ == "__main__":
    print("a => {}".format("lower" if islower("a") else "upper"))

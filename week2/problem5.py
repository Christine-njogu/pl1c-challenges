import os
import sys
import math

"""
Traceback (most recent call last):
  File "/Users/paulkorir/sci2pro/cnjogu/Week2/problem5.py", line 22, in <module>
    sys.exit(main())
  File "/Users/paulkorir/sci2pro/cnjogu/Week2/problem5.py", line 9, in main
    x, y, z = input("Enter the three co-efficients: ")
ValueError: too many values to unpack (expected 3)
"""


def main():
    # the user needs to be informed about the \t to separate values
    # the question asked you to use ','
    string_y = input("Enter the three co-efficients separating them with a ',': ")
    x, y, z = string_y.split(",")
    print(x, y, z)
    a = float(x)
    b = float(y)
    c = float(z)
    x1 = float(2 * c) / (-b + (math.sqrt(b ** 2 - (4 * a * c))))
    x2 = float(2 * c) / (-b - (math.sqrt(b ** 2 - (4 * a * c))))
    print(f"x1: {x1}")
    print(f"x2: {x2}")


if __name__ == "__main__":
    sys.exit(main())

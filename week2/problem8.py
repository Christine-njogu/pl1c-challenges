import os
import sys
import random


def main():
    x = int(input("Enter a number that is from 0 to 9: "))
    w = random.randint(0, 9)
    print(f"Random number: {w}")
    print(x < w)

    return None


if __name__ == "__main__":
    sys.exit(main())

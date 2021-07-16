import os
import sys
import random


def main():
    # excellent!
    x = float(input("Enter x (number between 0 and 1): "))
    y = float(input("Enter y (number between 0 and 1): "))
    X1 = random.random()
    Y1 = random.random()
    print(f"Random X: {X1} Random Y: {Y1}")
    print(f"Ace: {x < X1 and y > Y1}")
    print(f"King: {x > X1 and y > Y1}")
    print(f"Judge: {x < X1 and y < Y1}")
    print(f"Queen: {x > X1 and y < Y1}")


if __name__ == "__main__":
    sys.exit(main())

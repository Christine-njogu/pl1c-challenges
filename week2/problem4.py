import sys
import math


def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    # very good
    x1 = float(2 * c) / (-b + (math.sqrt(b ** 2 - (4 * a * c))))
    x2 = float(2 * c) / (-b - (math.sqrt(b ** 2 - (4 * a * c))))

    print(f"x1: {x1}")
    print(f"x2: {x2}")


if __name__ == "__main__":
    sys.exit(main())

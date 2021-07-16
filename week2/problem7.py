import os
import sys
import math

# the library does the work for you so you lose the points you could have gained


def calculate(a, b, c):
    discriminant = (b ** 2 - 4 * a * c)
    if discriminant < 0:
        discriminant *= -1

    z = float(math.sqrt(discriminant))
    x1 = float((-b + z) / (2 * a))
    x2 = float((-b - z) / (2 * a))
    return x1, x2


def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x1, x2 = calculate(a, b, c)
    print(f"x1={x1}, x2={x2}")
    z1 = complex(x1)
    z2 = complex(x2)
    print(z1, z2)

    return None


if __name__ == "__main__":
    sys.exit(main())

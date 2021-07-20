import sys
import math


def main():
    a = list(input("Enter x, y, z, coordinates of point A: "))
    b = list(input("Enter x, y, z, coordinates of point B: "))
    a0 = int(a[0])
    a1 = int(a[1])
    a2 = int(a[2])
    a = [a0, a1, a2]
    b0 = int(b[0])
    b1 = int(b[1])
    b2 = int(b[2])
    b = [b0, b1, b2]
    print(f"Point A: {a}")
    print(f"Point B: {b}")
    distance = float(math.sqrt(pow((a0 - b0), 2) + pow((a1 - b1), 2) + pow((a2 - b2), 2)))
    print(f"Distance between point A and B: {distance}")
    c = [0, 0, 0]
    distance2 = float(math.sqrt(pow((a0 - c[0]), 2) + pow((a1 - c[1]), 2) + pow((a2 - c[2]), 2)))
    print(f"Distance between point A and the origin: {distance2}")
    distance3 = float(math.sqrt(pow((b0 - c[0]), 2) + pow((b1 - c[1]), 2) + pow((b2 - c[2]), 2)))
    print(f"Distance between point B and the origin: {distance3}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

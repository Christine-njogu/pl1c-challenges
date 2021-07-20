import sys
import random


def main():
    a = list(range(5))
    b = random.choices(a, k=10)
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"Number of 0's in list: {b.count(0)}")
    print(f"Number of 1's in list: {b.count(1)}")
    print(f"Number of 2's in list: {b.count(2)}")
    print(f"Number of 3's in list: {b.count(3)}")
    print(f"Number of 4's in list: {b.count(4)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

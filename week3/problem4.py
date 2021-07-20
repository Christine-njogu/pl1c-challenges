import random
import sys


def main():
    a = list(range(100))
    b = a[51:75]
    c = random.choices(b, k=100)
    print(f"Random List: {c}")
    d = sorted(c)
    print(f"Sorted list: {d}")
    print(f"Minimum value of list: {min(d)}  First value of list: {d[0]} {min(d) == d[0]}")
    print(f"Maximum value of list: {max(d)}  Last value of list: {d[-1]}  {max(d) == d[-1]}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

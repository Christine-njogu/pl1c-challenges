import random
import sys
import random


def main():
    m = list(range(40, 100, 1))
    n = random.choices(m, k=5)
    x = input("Enter your subject1: ")
    y = input("Enter your subject2: ")
    z = input("Enter year subject3: ")
    v = input("Enter your subject4: ")
    w = input("Enter your subject5: ")
    try:
        assert len(x) > 5
    except AssertionError:
        print(f"Argument is too short {x}")
    print(f"{x}: {n[0]}, {y}: {n[1]}, {z}: {n[2]}, {v}: {n[3]}, {w}: {n[4]}")




if __name__ == "__main__":
    sys.exit(main())

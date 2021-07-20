import sys
import random


def main():
    x = int(input("Enter a number between 0 and 9 (inclusive): "))
    y = list(range(10))
    z = random.choices(y, k=5)
    print(f"Computer generated values: {z}")
    if x not in z:
        print("You win")
    if x in z:
        print("You lose")

    return 0


if __name__ == "__main__":
    sys.exit(main())

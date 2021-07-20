import sys


def main():
    x = float(input("Enter the value of x: "))

    try:
        y = float(pow(x, 3) - 9 * x) / (pow(x, 2) - 2 * x + 1)
        print(f"The value of y: {y}")
    except ZeroDivisionError as ie:
        print(f"Warning: {ie}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

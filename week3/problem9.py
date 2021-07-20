import sys


def main():
    x = int(input("Enter lower limit: "))
    y = int(input("Enter upper limit: "))
    a = list(reversed(range(x, (y + 1), 1)))
    print(a)


if __name__ == "__main__":
    sys.exit(main())

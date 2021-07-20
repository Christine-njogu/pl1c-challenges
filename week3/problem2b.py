import sys


def main():
    a = list(input(f"Enter the 4 elements of matrix1: "))
    a0 = int(a[0])
    a1 = int(a[1])
    a2 = int(a[2])
    a3 = int(a[3])
    a = [a0, a1, a2, a3]
    print(f"a: {a}")
    b = list(input(f"Enter the 4 elements of matrix2: "))
    b0 = int(b[0])
    b1 = int(b[1])
    b2 = int(b[2])
    b3 = int(b[3])
    b = [b0, b1, b2, b3]
    print(f"b: {b}")
    c = [(a[0] * b[0] + a[1] * b[2]), (a[0] * b[1] + a[1] * b[3]), (a[2] * b[0] + a[3] * b[2]),
         (a[2] * b[1] + a[3] * b[3])]
    print(f"Product matrix: {c}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

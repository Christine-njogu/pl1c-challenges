import sys


def main():
    rows1_a = [2, 3]
    rows2_a = [4, 1]
    a = rows1_a + rows2_a
    rows1_b = [5, 7]
    rows2_b = [3, 8]
    b = rows1_b + rows2_b
    print(f"Matrix 1: {a}")
    print(f"Matrix 2: {b}")
    c = [(a[0] * b[0] + a[1] * b[2]), (a[0] * b[1] + a[1] * b[3]), (a[2] * b[0] + a[3] * b[2]),
         (a[2] * b[1] + a[3] * b[3])]
    print(f"Product matrix: {c}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

import sys


def main():
    rows1_a = [2, 3, 7]
    rows2_a = [4, 1, 8]
    rows3_a = [3, 4, 5]
    a = rows1_a + rows2_a + rows3_a
    rows1_b = [5, 7, 1]
    rows2_b = [3, 8, 2]
    rows3_b = [5, 8, 4]
    b = rows1_b + rows2_b + rows3_b
    print(f"Matrix 1: {a}")
    print(f"Matrix 2: {b}")
    c = [(a[0] * b[0] + a[1] * b[3] + a[2] * b[6]), (a[0] * b[1] + a[1] * b[4]) + a[2] * b[7],
         (a[0] * b[2] + a[1] * b[5] + a[2] * b[8]),
         (a[3] * b[0] + a[4] * b[3] + a[5] * b[6]), (a[3] * b[1] + a[4] * b[4] + a[5] * b[7]),
         (a[3] * b[2] + a[4] * b[5] + a[5] * b[8]),
         (a[6] * b[0] + a[7] * b[3] + a[8] * b[6]), (a[6] * b[1] + a[7] * b[4] + a[8] * b[7]),
         (a[6] * b[2] + a[7] * b[5] + a[8] * b[8])]
    print(f"Product matrix: {c}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

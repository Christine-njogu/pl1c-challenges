import math
import random
import sys

"""
Notes:
- Very good work!
"""


def calculate_distance(a, b):
    # todo: add a docstring; see class notes on how to do this
    distance = float(math.sqrt(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2) + pow((a[2] - b[2]), 2)))
    return distance


def main():
    point_a = random.choices(range(10), k=3)
    point_b = random.choices(range(10), k=3)
    dist_btn_points = calculate_distance(point_a, point_b)
    print(f"Point A: {point_a}, Point B: {point_b}")
    print(f"Distance between point A and B: {dist_btn_points}")
    pentagon_a = [1, 3, 2]
    pentagon_b = [3, 1, 5]
    pentagon_c = [5, 2, 1]
    pentagon_d = [4, 5, 4]
    pentagon_e = [2, 4, 3]
    dist_a_to_b = calculate_distance(pentagon_a, pentagon_b)
    dist_b_to_c = calculate_distance(pentagon_b, pentagon_c)
    dist_c_to_d = calculate_distance(pentagon_c, pentagon_d)
    dist_d_to_e = calculate_distance(pentagon_d, pentagon_e)
    dist_e_to_a = calculate_distance(pentagon_e, pentagon_a)
    perimeter = dist_a_to_b + dist_b_to_c + dist_c_to_d + dist_d_to_e + dist_e_to_a
    print(f"Perimeter of pentagon: {perimeter}")
    # sanity check: perimeter of a 1-square is 4
    print(
        calculate_distance((0, 0, 0), (1, 0, 0)) +
        calculate_distance((1, 0, 0), (1, 1, 0)) +
        calculate_distance((1, 1, 0), (0, 1, 0)) +
        calculate_distance((0, 1, 0), (0, 0, 0)) == 4
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())

import sys


def main():
    one = set(range(2, 101))
    two = set(range(4, 101, 2))
    three = set(range(6, 101, 3))
    four = set(range(8, 101, 4))
    five = set(range(10, 101, 5))
    six = set(range(12, 101, 6))
    seven = set(range(14, 101, 7))
    diff = one - two - three - four - five - six - seven
    diff_list = list(diff)
    print(f"Prime numbers: {sorted(diff_list)}")
    one_t = set(range(2, 1001))
    two_t = set(range(4, 1001, 2))
    three_t = set(range(6, 1001, 3))
    four_t = set(range(8, 1001, 4))
    five_t = set(range(10, 1001, 5))
    six_t = set(range(12, 1001, 6))
    seven_t = set(range(14, 1001, 7))
    diff_t = one_t - two_t - three_t - four_t - five_t - six_t - seven_t
    diff_t_list = list(diff_t)
    print(f"Prime numbers: {sorted(diff_t_list)}")



if __name__ == "__main__":
    sys.exit(main())

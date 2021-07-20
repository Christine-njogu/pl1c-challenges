import sys
import random


def max_and_min(list_l):
    # fixme: try writing your own routine instead of relying on the builtin functions min() and max()
    maximum_value = max(list_l)
    minimum_value = min(list_l)
    return maximum_value, minimum_value


def main():
    my_list = random.choices(range(100), k=15)
    print(my_list)
    max_value, min_value = max_and_min(my_list)
    print(f"Maximum value = {max_value}, Minimum value = {min_value}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

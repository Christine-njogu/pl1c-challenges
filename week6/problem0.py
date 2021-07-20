import sys
import random


def sum_of_list(this_list):
    # todo: add a docstring; see class notes on how to do this
    list_sum = 0
    for items in this_list:
        list_sum += items
    return list_sum


def main():
    my_list = random.choices(range(50), k=10)
    new_list = sum_of_list(my_list)
    print(f"My list: {my_list}")
    print(f"Sum of list: {new_list}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

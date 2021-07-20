import sys
import random
import string


def main():
    letters = string.ascii_lowercase
    assorted_letters1 = random.choices(letters, k=10)
    assorted_letters2 = random.choices(letters, k=10)
    numbers_list1 = random.choices(list(range(100)), k=100)
    numbers_list2 = random.choices(list(range(100)), k=100)
    d1 = dict(zip(assorted_letters1, numbers_list1))
    d2 = dict(zip(assorted_letters2, numbers_list2))
    print(f"d1: {d1}, {len(d1)}")
    print(f"d2: {d2}, {len(d2)}")
    d3sum = {**d1, **d2}
    for key, value in d3sum.items():
        if key in d1 and key in d2:
            d3sum[key] = [value + d1[key]]
    print(f"d3: {d3sum}")


if __name__ == "__main__":
    sys.exit(main())
import random
import sys


def main():
    random_floats = []
    for i in range(0, 15):
        float_num = random.uniform(0, 100)
        random_floats.append(float_num)
    print(f"Float: {random_floats}")
    double_floats = list(map(lambda x: x * 2, random_floats))
    print(f"Doubled: {double_floats}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

import random
import sys


def main():
    l = random.choices(range(101), k=100)
    length_l = len(l)
    new_l_cumulative_sum = [sum(l[0:x:1]) for x in range(1, length_l+1)]
    print(f"Random list l: {l}")
    print(f"Cumulative  l: {new_l_cumulative_sum}")
    print(len(new_l_cumulative_sum))
    new_l_adjoining_sum = [sum(l[x:x+2:1]) for x in range(0, length_l-1)]
    print(f"Adjoining sum: {new_l_adjoining_sum}")
    print(len(new_l_adjoining_sum))
    new_l_alternate_sum = [sum(l[x:x+5:2]) for x in range(0, length_l-4)]
    print(f"Alternate sum: {new_l_alternate_sum}")
    print(len(new_l_alternate_sum))
    return 0


if __name__ == "__main__":
    sys.exit(main())


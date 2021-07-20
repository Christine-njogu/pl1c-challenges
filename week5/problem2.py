import sys
import random


def main():
    l = random.choices(range(101), k=100)
    length_l = len(l)
    print(f"Random list gen: {l}")
    new_l_cumulative_sum = []
    x = 0
    sums1 = 0
    while x <= (length_l-1):
        sums1 += l[x]
        new_l_cumulative_sum.append(sums1)
        x += 1
    print(f"Cumulative sum: {new_l_cumulative_sum}")
    print(len(new_l_cumulative_sum))
    new_l_adjoining_sum = []
    y = 0
    counter = 1
    while y < (length_l-1):
        sums2 = l[y] + l[counter]
        new_l_adjoining_sum.append(sums2)
        y += 1
        counter += 1
    print(f" Adjoining sum: {new_l_adjoining_sum}")
    print(len(new_l_adjoining_sum))
    new_l_alternate_sum = []
    z = 0
    while z < (length_l-4):
        sums3 = l[z] + l[z+2] + l[z+4]
        new_l_alternate_sum.append(sums3)
        z += 1
    print(f"Alternate sum: {new_l_alternate_sum}")
    print(len(new_l_alternate_sum))
    return 0


if __name__ == "__main__":
    sys.exit(main())
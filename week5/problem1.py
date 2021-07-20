import sys
import random


def main():
    L1 = random.choices(range(101), k=100)
    L2 = random.choices(range(101), k=100)
    length = len(L1)
    pairwise_sum = []
    cumulative_product = []
    even_odd_sum = []
    for x in range(length):
        pairwise_sum.append(L1[x] + L2[x])
    print(f"Random list1: {L1}")
    print(f"Random list2: {L2}")
    print(f"Pairwise sum: {pairwise_sum}")
    for y in range(length):
        cumulative_product.append(L1[y] * L2[y])
    print(f"Cumltve prod: {cumulative_product}")
    cumulative_product_sum = sum(cumulative_product)
    print(f"Cumulative product sum: {cumulative_product_sum}")
    for z in range(length):
        if (L1[z] % 2 == 0 and L2[z] % 2 == 0) or (L1[z] % 2 == 1 and L2[z] % 2 == 1):
            even_odd_sum.append(L1[z] + L2[z])
    print(f"Even/Odd sum: {even_odd_sum}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
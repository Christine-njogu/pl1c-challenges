import sys
import random


def main():
    L1 = random.choices(range(101), k=100)
    L2 = random.choices(range(101), k=100)
    length = len(L1)
    print(f"Random list1: {L1}")
    print(f"Random list2: {L2}")
    pairwise_sum = []
    x = 0
    while x < length:
        pairwise_sum.append(L1[x] + L2[x])
        x += 1
    print(f"Pairwise sums: {pairwise_sum}")
    # print(len(pairwise_sum))
    pairwise_product = []
    y = 0
    while y < length:
        pairwise_product.append(L1[y] * L2[y])
        y += 1
    print(f"Pairwise prod: {pairwise_product}")
    # print(len(pairwise_product))
    z = 0
    product_sum = 0
    while z < len(pairwise_product):
        product_sum += pairwise_product[z]
        z += 1
    print(f"Cumulative product sum: {product_sum}")
    even_odd_sum = []
    v = 0
    while v < length:
        if L1[v] % 2 == 0 and L2[v] % 2 == 0 or (L1[v] % 2 == 1 and L2[v] % 2 == 1):
            even_odd_sum.append(L1[v] + L2[v])
        v += 1
    print(f"Even/Odd sum: {even_odd_sum}")
    # print(len(even_odd_sum))
    return 0


if __name__ == "__main__":
    sys.exit(main())

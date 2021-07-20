import sys
import random


def main():
    matrix_size1 = input("Enter the size of the first matrix (i.e. 2x3): ")
    matrix_size2 = input("Enter the size of the second matrix (i.e 3x2): ")
    matrix_size1_list = matrix_size1.split("x")
    matrix_size2_list = matrix_size2.split("x")
    num_of_rows1 = int(matrix_size1_list[0])
    num_of_cols1 = int(matrix_size1_list[1])
    num_of_rows2 = int(matrix_size2_list[0])
    num_of_cols2 = int(matrix_size2_list[1])
    if num_of_cols1 != num_of_rows2:
        print("Invalid matrix size, cannot perform multiplication")
    x = 0
    matrix_list = []
    while x < num_of_rows1:
        rows_matrix1 = random.choices(range(-10, 11), k=num_of_cols1)
        matrix_list.append(rows_matrix1)
        x += 1
    print("Matrix1:")
    v = 0
    while v < len(matrix_list):
        print(matrix_list[v])
        v += 1
    y = 0
    matrix_list2 = []
    while y < num_of_rows2:
        rows_matrix2 = random.choices(range(-10, 11), k=num_of_cols2)
        matrix_list2.append(rows_matrix2)
        y += 1
    print("Matrix2:")
    z = 0
    while z < len(matrix_list2):
        print(matrix_list2[z])
        z += 1
    product = 0
    result = []
    for i in range(len(matrix_list)):
        for j in range(len(matrix_list2[0])):
            for k in range(len(matrix_list2)):
                product += matrix_list[i][k] * matrix_list2[k][j]
                result.append(product)
    print(result)



if __name__ == "__main__":
    sys.exit(main())

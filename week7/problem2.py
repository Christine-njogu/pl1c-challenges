import sys


def main():
    product_matrix = []
    with open('input_matrices.txt') as f:
        extracted_data = f.readlines()
        count2 = 0
        while count2 < len(extracted_data):
            data = str(extracted_data[count2])
            data_list = data.replace("\n", "").split("\t")
            list_with_integers = []
            for items in data_list:
                x = int(items)
                list_with_integers.append(x)
            print(list_with_integers)
            n = 3
            matrix1 = [list_with_integers[x * n: (x + 1) * n] for x in range(0, len(list_with_integers) - 15)]
            matrix2 = [list_with_integers[x * n: (x + 1) * n] for x in range(3, len(list_with_integers) - 12)]
            result = [[0, 0, 0, ], [0, 0, 0], [0, 0, 0]]
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        result[i][j] += (matrix1[i][k] * matrix2[k][j])
            string_result = []
            for i in range(len(result)):
                for j in range(len(result)):
                    items = str(result[i][j])
                    string_result.append(items)
            # print(string_result)
            product_matrix.append(string_result)
            count2 += 1
    with open('matrix_products.txt', 'w') as f:
        count2 = 0
        while count2 < len(product_matrix):
            my_result = product_matrix[count2]
            for i in range(len(my_result)):
                f.write(my_result[i])
                f.write("\t")
            f.write("\n")
            count2 += 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

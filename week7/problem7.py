import sys


def main():
    my_list = []
    with open('AAPL.csv') as f:
        stock_data = f.readlines()
        count = 0
        stock_data.pop(0)
        stock_list = []
        while count < len(stock_data):
            data = str(stock_data[count])
            data_list = data.replace("\n", "").split(",")
            my_list.append(data_list[-1])
            stock_list.append(data_list[0])
            # stock_dict[data_list[0]] = data_list[-1]
            count += 1
        volumes_integers = []
        for items in my_list:
            volumes_integers.append(int(items))
        stock_dict = dict(zip(stock_list, volumes_integers))
        stocks = sorted(stock_dict.items(), key=lambda x: x[1], reverse=True)
        print(f"Date with highest sales: {stocks[0]}")
        stock_differences = []
        count1 = 0
        count2 = 1
        while count1 < len(volumes_integers) - 1:
            difference = volumes_integers[count2] - volumes_integers[count1]
            stock_differences.append(difference)
            count1 += 1
            count2 += 1
        stock_list.pop(0)
        stock_diff_dict = dict(zip(stock_list, stock_differences))
        stock_diff_list = sorted(stock_diff_dict.items(), key=lambda x: x[1])
        print(f"Day with the biggest inter-day rise: {stock_diff_list[-1]}")
        print(f"Day with the biggest inter-day fall: {stock_diff_list[0]}")

        return 0


if __name__ == "__main__":
    sys.exit(main())

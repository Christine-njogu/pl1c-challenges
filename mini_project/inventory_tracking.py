import datetime
import pathlib
import random
import sys

"""A module to track the stock levels of different input types in a factory against the units produced. The input 
types are used to produce different products """


def generate_input_types():
    """
    Define the different input types that are used in the factory
    :return: list of items
    """
    input_types = ["Angle_irons", "Tubes", "Channels", "Mig_wire", "Argon_gas", "Galvanised_sheets", "Budget_locks",
                   "Welding_rods", "Body_filler", "Grinding_discs", "Drill_bits", "Primer", "Paints", "Thinner",
                   "Sand_paper", "Masking_tapes", "Carpet", "Pop_rivets", "Electrical_wires", "Bulbs", "Switch",
                   "Insulation_tapes", "Fasteners", "Adhesives", "Reflectors", "Accessories", "Rubbers",
                   "Aluminum_mouldings", "Glasses", "Window_locks"]

    return input_types


def create_stock():
    """
    Creates the stock from different consignment arriving at the factory
    :return: stock - input_type and its quantity
    """
    input_items = generate_input_types()
    consignment = set(random.choices(input_items, k=random.randint(1, 5)))
    consignment_dict = {}
    for inputs in consignment:
        consignment_dict[inputs] = random.choice(range(0, 101))

    return consignment_dict


def write_stock_to_file():
    """
    Write created stock into the directory stock with a date-time stamp as the filename
    :return: parent folder
    """
    parent_folder = pathlib.Path("./stock")
    if not parent_folder.exists():
        parent_folder.mkdir()
    else:
        print("Folder already exists")
    current_date = datetime.datetime.now()
    current_date_string = str(current_date)
    file_name = current_date_string.replace(":", "-") + ".txt"
    stock_path = parent_folder / file_name
    created_stock_dictionary = create_stock()
    with open(stock_path, 'w') as f:
        created_stock_dict_strings = {}
        for key, value in created_stock_dictionary.items():
            value_string = str(value)
            created_stock_dict_strings[key] = value_string
        for key, value in created_stock_dict_strings.items():
            f.write(key)
            f.write("\t")
            f.write(value)
            f.write("\n")

    return parent_folder


def create_products():
    """
    Create products at random and in random quantities
    :return: products created and their quantities
    """
    # product_types = generate_product_types()
    product_types = ["Frame_prod", "Paint_prod", "Electric_prod", "Glass_prod", "Finishings"]
    products_created = random.choices(product_types, k=random.randint(1, 3))
    product_dict = {}
    for items in products_created:
        product_dict[items] = random.choice(range(1, 10))

    return product_dict


def write_product_to_file():
    """
    Write the created products into file in product directory
    :return:
    """
    created_product_dict = create_products()
    product_parent_folder = pathlib.Path("./product")
    if not product_parent_folder.exists():
        product_parent_folder.mkdir()
    else:
        print("This folder already exists")
    current_date = datetime.datetime.now()
    current_date_string = str(current_date)
    file_name = current_date_string.replace(":", "-") + ".txt"
    product_path = product_parent_folder / file_name
    with product_path.open('w') as f:
        product_dict_str = {}
        for key, value in created_product_dict.items():
            value_str = str(value)
            product_dict_str[key] = value_str
        for key, value in product_dict_str.items():
            f.write(key)
            f.write("\t")
            f.write(value)
            f.write("\n")

    return product_parent_folder


def read_stock_files():
    """
    Read the stock files and merge them
    :return: merged_stock_list
    """
    stock_merged_list = []
    parent_folder = write_stock_to_file()
    for items in parent_folder.iterdir():
        with open(items) as f:
            stock_data = f.readlines()
            new_list = []
            count = 0
            while count < len(stock_data):
                stock_data_str = stock_data[count]
                my_list = stock_data_str.replace("\n", "").split("\t")
                new_list.append(my_list)
                count += 1
            major_dict = {x[0]: x[1] for x in new_list}
            for key, value in major_dict.items():
                major_dict[key] = int(value)
            stock_merged_list.append(major_dict)

    return stock_merged_list


def read_product_files():
    """
    Read product items from files and merge them
    :return: product_merged_list
    """
    product_merged_list = []
    product_folder = write_product_to_file()
    for items in product_folder.iterdir():
        with open(items) as f:
            product_data = f.readlines()
            new_list = []
            count = 0
            while count < len(product_data):
                product_data_str = product_data[count]
                my_product_list = product_data_str.replace("\n", "").split("\t")
                new_list.append(my_product_list)
                count += 1
            major_prod_dict = {x[0]: x[1] for x in new_list}
            for key, value in major_prod_dict.items():
                major_prod_dict[key] = int(value)
            product_merged_list.append(major_prod_dict)

    return product_merged_list


def calculate_stock_levels():
    """
    Collect data from all stock files and calculate aggregate stock for the different input types
    :return: aggregate stock values
    """
    merged_prod_list = read_product_files()
    stocks_list = read_stock_files()
    stock_merged_dict = {}
    for dictionary in stocks_list:
        for keys in dictionary.keys():
            stock_merged_dict[keys] = stock_merged_dict.get(keys, 0) + dictionary[keys]
    for dictionary in merged_prod_list:
        for keys, values in dictionary.items():
            if keys == "Frame_prod":
                stock_merged_dict["Angle_irons"] -= (values * 6)
                stock_merged_dict["Tubes"] -= (values * 3)
                stock_merged_dict["Channels"] -= (values * 4)
                stock_merged_dict["Mig_wire"] -= (values * 2)
                stock_merged_dict["Argon_gas"] -= (values * 2)
                stock_merged_dict["Welding_rods"] -= (values * 3)
                stock_merged_dict["Drill_bits"] -= (values * 5)
            elif keys == "Paint_prod":
                stock_merged_dict["Primer"] -= (values * 4)
                stock_merged_dict["Body_filler"] -= (values * 2)
                stock_merged_dict["Thinner"] -= (values * 3)
                stock_merged_dict["Paints"] -= (values * 4)
                stock_merged_dict["Sand_paper"] -= (values * 5)
                stock_merged_dict["Masking_tapes"] -= (values * 5)
            elif keys == "Electric_prod":
                stock_merged_dict["Electrical_wires"] -= (values * 5)
                stock_merged_dict["Insulation_tapes"] -= (values * 4)
                stock_merged_dict["Bulbs"] -= (values * 3)
                stock_merged_dict["Switch"] -= (values * 2)
            elif keys == "Glass_prod":
                stock_merged_dict["Glasses"] -= (values * 2)
                stock_merged_dict["Adhesives"] -= (values * 5)
                stock_merged_dict["Window_locks"] -= (values * 3)
                stock_merged_dict["Pop_rivets"] -= (values * 10)
                stock_merged_dict["Aluminum_mouldings"] -= (values * 3)
                stock_merged_dict["Welding_rods"] -= (values * 2)
            elif keys == "Finishings":
                stock_merged_dict["Adhesives"] -= (values * 4)
                stock_merged_dict["Aluminum_mouldings"] -= (values * 2)
                stock_merged_dict["Reflectors"] -= (values * 2)
                stock_merged_dict["Accessories"] -= (values * 3)
                stock_merged_dict["Fasteners"] -= (values * 6)
                stock_merged_dict["Rubbers"] -= (values * 5)
            else:
                pass
    print("Stock levels")
    print("-" * 70)
    for key, value in stock_merged_dict.items():
        print(f"{key}\t {value}")

    return stock_merged_dict


def calculate_products_aggregate():
    """
    Calculates the sum of products created by reading the product files
    :return:
    """
    product_list = read_product_files()
    merged_prod_dict = {}
    for dictionary in product_list:
        for keys in dictionary.keys():
            merged_prod_dict[keys] = merged_prod_dict.get(keys, 0) + dictionary[keys]
    print("Total of products created")
    print("-" * 70)
    for key, value in merged_prod_dict.items():
        print(key, value)

    return merged_prod_dict


def consume_stock():
    stock_data = read_stock_files()
    stock_data_dict = {}
    for dictionary in stock_data:
        for keys in dictionary.keys():
            stock_data_dict[keys] = stock_data_dict.get(keys, 0) + dictionary[keys]
    for keys, value in stock_data_dict.items():
        if (keys == "Angle_irons" and value > 6) or (keys == "Tubes" and value > 3) or (
                keys == "Channels" and value > 4) or (keys == "Mig_wire" and value > 2) or (
                keys == "Argon_gas" and value > 2) or (keys == "Welding_rods" and value > 3) or (
                keys == "Drill_bits" and value > 5):
            create_products()
        if (keys == "Primer" and value > 4) or (keys == "Body_filler" and value > 2) or (
                keys == "Thinner" and value > 3) or (keys == "Paints" and value > 4) or (
                keys == "Sand_paper" and value > 5) or (keys == "Masking_tapes" and value > 5):
            create_products()
        if (keys == "Electrical_wires" and value > 5) or (keys == "Insulation_tapes" and value > 4) or (
                (keys == "Bulbs" and value > 3) or (keys == "Switch" and value > 2)):
            create_products()
        if (keys == "Glasses" and value > 2) or (keys == "Adhesives" and value > 5) or (
                keys == "Window_locks" and value > 3) or (keys == "Pop_rivets" and value > 10) or (
                keys == "Aluminum_mouldings" and value > 3) or (keys == "Welding_rods" and value > 2):
            create_products()
        if (keys == "Adhesives" and value > 4) or (keys == "Aluminum_mouldings" and value > 2) or (
                keys == "Reflectors" and value > 2) or (keys == "Accessories" and value > 3) or (
                keys == "Fasteners" and value > 6) or (keys == "Rubbers" and value > 5):
            create_products()

    return stock_data


def main():
    probability_num = random.random()
    print(probability_num)
    if probability_num < 0.6:
        write_stock_to_file()
    else:
        consume_stock()
    calculate_stock_levels()
    calculate_products_aggregate()

    return 0


if __name__ == "__main__":
    sys.exit(main())

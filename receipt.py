# An invitation is printed after the receipt, requesting the customer to complete an online survey

import csv
from datetime import datetime

PRODUCT_NUMBER_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRICE_INDEX = 2


def read_dictionary(csv_file, PRODUCT_NUMBER_INDEX):

# """Read the contents of a CSV file into a compound
#     dictionary and return the dictionary.
#     Parameters
#         filename: the name of the CSV file to read.
#         key_column_index: the index of the column
#             to use as the keys in the dictionary.
#     Return: a compound dictionary that contains
#         the contents of the CSV file.
#     """
    dictionary = {}

    with open("products.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[PRODUCT_NUMBER_INDEX]
                dictionary[key] = row_list
    return dictionary


def main():
    try:
        products_dict = read_dictionary("products.csv", PRODUCT_NUMBER_INDEX)

        # print("All Products")

        # print(product_dictionary)

        print()

        print("Lord's Errand Enterprise")
        print()
        print("Requested Items: ")
        with open("request.csv","rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)

            total_items = 0
            total_cost = 0
            sales_tax = 0.06

            current_date_and_time = datetime.now()

            for request in reader:
            
                quantity = int(request[1])
                value = products_dict[request[0]]
                product_name = value[PRODUCT_NAME_INDEX]
                product_price = float(value[PRICE_INDEX])   

                total_items += quantity

                subtotal = product_price * quantity
                total_cost += subtotal
            
                total = total_cost + sales_tax
            
                print(f"{product_name}: {quantity} @ {product_price}")    

            print(f"Number of Item: {total_items}")

            print(f"Subtotal: {total_cost:.2f}")

            print(f"Sales Tax: {sales_tax}")

            print(f'Total: {total:.2f}')

            print("Thank You for shopping at the Lord's Errand Enterprise")

            print(f"{current_date_and_time: %c}")
            print()
            
            print("Thank you for shopping with us!")
            print("We value your feedback and would love to hear about your experience.")
            print("Please take a few minutes to complete our online survey at:")
            print("Online survey link")
            print("Your input will help us improve our services and products.")



    except FileNotFoundError as file_err:
        print(f"{file_err}")

    except PermissionError as permission_err:
        print(f"{permission_err}")
        

    except KeyError as key_err:
        print(f"{key_err}: unknown product ID in the request.csv file")
    

    


if __name__ == "__main__":
    main()

"""
A local grocery store subscribes to an online service that enables its customers 
to order groceries online. After a customer completes an order, the online service 
sends a CSV file that contains the customer’s requests to the grocery store. 
The store needs you to write a program that reads the CSV file and prints to the 
terminal window a receipt that lists the purchased items and shows the subtotal, 
the sales tax amount, and the total.
"""
import csv

def main():
    # Declare index of the dictionary
    PRODUCT_KEY_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2

    # Call the read_dictionary function and store the data in 
    # products.csv file into a variable named products_dict
    products_dict = read_dictionary('products.csv', PRODUCT_KEY_INDEX)

    # Print the entire products dictionary
    print('All Products')
    print(products_dict)

    # Open de request.csv file for read
    with open('request.csv', 'rt') as csv_file:
        reader = csv.reader(csv_file)

        # Skip the first row (Header row)
        next(reader)

        print()
        print('Requested Items')

        # Processes each row from the request.csv file
        # Use the requested product number to find the corresponding item in the products_dict.
        for row_list in reader:

            PRODUCT_ID_INDEX = 0
            QUANTITY_INDEX = 1

            quantity = 0
            price = 0

            # For the current row, retrieve the
            # values in columns 0 and 1.
            product_id = row_list[PRODUCT_ID_INDEX]
            quantity = int(row_list[QUANTITY_INDEX])

            # Use the requested product id to find the corresponding item in the products_dict.
            if product_id in products_dict:
                list = products_dict[product_id]
                name = list[PRODUCT_NAME_INDEX]
                price = list[PRODUCT_PRICE_INDEX]
        
            # Print the product name, requested quantity, and product price.
            print(f'{name}: {quantity} @ {price}')
            

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that store the products data
    products_dict = {}

    # Open the text file for reading and store a reference
    # to the opened file in a variable named products.
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)

        # Skip the first row (Header row)
        next(reader)

        # Add every row to the products dictionary
        for row_list in reader:
            key_product = row_list[key_column_index]
            products_dict[key_product] = row_list

    return products_dict


# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
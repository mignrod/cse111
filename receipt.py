"""
A local grocery store called 'Inkom Emporium'subscribes to an online service that enables its customers 
to order groceries online. After a customer completes an order, the online service 
sends a CSV file that contains the customer’s requests to the grocery store. 
The store needs you to write a program that reads the CSV file and prints to the 
terminal window a receipt that lists the purchased items and shows the subtotal, 
the sales tax amount, and the total.
"""
import csv
from datetime import datetime

def main():
    # Declare index of the dictionary
    PRODUCT_KEY_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2

    try:
        # Call the read_dictionary function and store the data in 
        # products.csv file into a variable named products_dict
        products_dict = read_dictionary('products.csv', PRODUCT_KEY_INDEX)

        # Print the header for store company name
        print('Inkom Emporium Store')
        print()

        # Open de request.csv file for read
        filename = 'request.csv'
        with open(filename, 'rt') as csv_file:
            reader = csv.reader(csv_file)

            # Skip the first row (Header row)
            next(reader)

            # Declare variables
            items = 0
            subtotal = 0

            # Print a brief opening to the request list
            print('Requested Items')
            
            # Processes each row from the request.csv file
            # Use the requested product number to find the corresponding item in the products_dict.
            for row_list in reader:

                PRODUCT_ID_INDEX = 0
                QUANTITY_INDEX = 1

                # For the current row, retrieve the
                # values in columns 0 and 1.
                product_id = row_list[PRODUCT_ID_INDEX]
                quantity = int(row_list[QUANTITY_INDEX])

                # Compute the total number of items in the list
                items += quantity             
                
                # Use the requested product id to find the corresponding item in the products_dict.
                if product_id in products_dict:
                    list = products_dict[product_id]
                    name = list[PRODUCT_NAME_INDEX]
                    price = float(list[PRODUCT_PRICE_INDEX])

                    # Compute the subtotal amount 
                    subtotal += (price * quantity)

                    # Print the product name, requested quantity, and product price.
                    print(f'{name}: {quantity} @ {price}')
            
            # Compute the sales tax according to the subtotal amount
            sales_tax = subtotal * 0.06

            # Compute the total amount in $ of the request list items
            total = sales_tax + subtotal

            # Print all the information to the client
            print()
            print(f'Number of Items: {items}')
            print(f'Subtotal: {subtotal:.2f}')
            print(f'Sales Tax: {sales_tax:.2f}')
            print(f'Total: {total:.2f}')

            # Compute a discount the product prices by 10% if today is Tuesday or Wednesday, and if hour of day is lees than 11am.
            today = datetime.now()
            hour_of_day = today.hour

            if today.weekday() == 1 or today.weekday() == 2 and hour_of_day < 11:
                discount = 0.20
                discount_amount = total * discount
                new_total = total - discount_amount
                print()
                print(f'Discount for Today: {discount*100:.0f}% =  {discount_amount:.2f}')
                print(f'Total after Discount: {new_total:.2f}')
            elif today.weekday() == 1 or today.weekday() == 2:
                day_discount = 0.10
                discount_amount = total * day_discount
                new_total = total - discount_amount
                print()
                print(f'Discount for Today: {day_discount*100:.0f}% =  {discount_amount:.2f}')
                print(f'Total after Discount: {new_total:.2f}')
            elif hour_of_day < 11:
                hour_discount = 0.10
                discount_amount = total * hour_discount
                new_total = total - discount_amount
                print()
                print(f'Discount for Today: {hour_discount*100:.0f}% =  {discount_amount:.2f}')
                print(f'Total after Discount: {new_total:.2f}')
            else:
                pass

            # Print the thank you message, time and date
            print()
            print('Thank you for shopping at the Inkom Emporium Store.')
            print(f'{today:%a %b %d  %H:%M:%S %Y}')

    except FileNotFoundError as not_found:
        print('Error: missing file')
        print(not_found)
    
    except KeyError as key_err:
        print(f'Error: unknown product ID in the {filename} file')
        print(key_err)

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
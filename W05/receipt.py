import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

PRODUCT_NUMBER_INDEX = 0
QUANTITY_INDEX = 1

PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

sales_tax_rate = .06

def main():
    try:
        # Print the store name at the top of the receipt.
        print('Inkom Emporium')
        print()

        products_dict = read_dict("products.csv", 0)
        # print('All Products')
        # print(products_dict)
        # print()

        # Open a file named request.csv and store a reference
        # to the opened file in a variable named request_file.
        with open("request.csv", mode="rt") as request_file:

            # Use the csv module to create a reader
            # object that will read from the opened file.
            reader = csv.reader(request_file)

            # The first row of the CSV file contains column
            # headings so this statement skips the first row 
            # of the CSV file.
            next(reader)

            # initiate value of variable: number_of_items
            number_of_items = 0
            subtotal_due = 0

            # Read each row in the CSV file one at a time.
            # The reader object returns each row as a list.
            for row_list in reader:
                product_number = row_list[PRODUCT_NUMBER_INDEX]
                quantity = int(row_list[QUANTITY_INDEX])
                # sum number of items
                number_of_items += int(quantity)

                # if product_number is in products_dict, 
                # print the product_number, requested quantity, and product price
                # if product_number in products_dict:
                print(f'{products_dict[product_number][PRODUCT_NAME_INDEX]}: {quantity} @ {products_dict[product_number][PRODUCT_PRICE_INDEX]}')

                # sum subtotal_due
                subtotal_due += quantity * float(products_dict[product_number][PRODUCT_PRICE_INDEX])
            
            # print the number of ordered items.
            print()
            print(f'Number of items: {number_of_items}')
            
            # print the subtotal due.
            print(f'Subtotal: {subtotal_due:.2f}')
            
            # compute and print the sales tax amount
            sales_tax = subtotal_due * sales_tax_rate
            print(f'Sales Tax: {sales_tax:.2f}')

            # compute and print the total amount due
            total_amount_due = subtotal_due + sales_tax
            print(f'Total: {total_amount_due:.2f}')

            # print a thank you message
            print()
            print('Thank you for shopping at the Inkom Emporium.')

            # Use an f-string to print the current
            # day of the week and the current time.
            print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")

            # exceeding requirements
            if current_date_and_time.strftime('%a') == 'Tue' or current_date_and_time.strftime('%a') == 'Wed':
                print()
                print('CONGRATULATIONS! You got a 10% DISCOUNT from all product prices!')
                discount = 0.1 * subtotal_due
                discounted_sales_tax = sales_tax_rate * (subtotal_due - discount)
                new_total = (subtotal_due - discount) + discounted_sales_tax
                print(f'Your discount: {discount:.2f}')
                print(f"Your new total is: {new_total:.2f}")
            else:
                print()
                print('Come back on Tue or Wed and get a discount for your order!')

    except FileNotFoundError as not_found_err:
        print('Error: missing file')
        print(not_found_err)

    except PermissionError as perm_err:
        print(perm_err)
    
    except KeyError as key_err:
        print('Error: unknown product ID in the request.csv file')
        print(key_err)

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
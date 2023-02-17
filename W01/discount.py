# Your program asks the user for the subtotal but does not ask the user for the day of the week. Your program gets the day of the week from your computer's operating system.
# Your program correctly computes and prints the discount amount if applicable.
# Your program correctly computes and prints the sales tax amount and the total amount due.

from datetime import datetime



subtotal =0
price = -1
print('Please enter the price and quantity of each item. (enter a quantity of 0 to finish)')
while price != 0:
    price = float(input('What is your items price? $'))
    if(price == 0):
        break
    quantity = int(input('How many of this item? '))
    subtotal += (price * quantity)

print(f'Your subtotal is ${subtotal:.2f}')

day_of_the_week = datetime.now().strftime("%A")
sub_discount = 0
if ( day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday'):

    if subtotal > 50 :
        discount = 0.1
        sub_discount = subtotal * discount
        print(f'Discount is ${sub_discount:.2f}')
    else:
        additional_amount = 50-subtotal

        print(f'To recive a 10% discount please spend an additional ${additional_amount:.2f}')

sales_tax = 0.06
tax_total = (subtotal - sub_discount) * sales_tax
print(f'Sales tax is ${tax_total:.2f}')
total_amount = subtotal - sub_discount+tax_total

print(f'Your total amount due is ${total_amount:.2f}')
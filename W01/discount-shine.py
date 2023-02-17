from datetime import datetime

subtotal = 0
price = -1

print('Please enter the price and quantity of each item. (enter a quantity of 0 to finish)')

while price != 0:
    price = float(input'What is your item price? $')
    if price == 0:
        break
    quantity = input('How many of this item? ')
    subtotal += price * quantity

subtotal = float(input('What is your subtotal? '))

day_of_the_week = datetime.now().strftime("%A")
sub_discount = 0
if subtotal > 50 and (day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday"):
    if subtotal > 50:
        discount = 0.1
        sub_discount = subtotal * discount
        print(f'Discount is ${sub_discount:.2f}')
    else:
        additional_amount = 50 - subtotal
        print(f'To receive a 10% discount please spend an additional ${additional_amount:.2f}')
sales_tax = 0.06
tax_total = (subtotal - sub_discount) * sales_tax
print(f'Sales tax is ${tax_total:.2f}')
total_amount = subtotal - sub_discount + tax_total

print(f'Your total amount due is ${total_amount:.2f}')
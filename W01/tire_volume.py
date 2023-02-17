# CSE 111 Bro. P
# Sunseehray Tirazona

# 01/02 Prove

import math
from datetime import datetime


current_date = datetime.now()
current_date = f'{current_date:%Y-%m-%d}'

# get user input
w = int(input('Enter the width of the tire in mm (ex 205): '))
a = int(input('Enter the aspect ratio of the tire (ex 60): '))
d = int(input('Enter the diameter of the wheel in inches (ex 15): '))

# calculate results

v = (math.pi * (w ** 2) * a * (w * a + 2540 * d)) / (10000000000)
v = round(v, 2)

print()
print(f'The approximate volume is {v} liters')
print()

with open("volumes.txt", mode="at") as f:
    print(current_date,w,a,d,v,sep=" ",end="\n",file=f,flush=False)
    print('The file, volumes.txt, has been updated.')

# creativity
display = input('Would you like to display its contents? (YES/NO) ')

if display.lower() == 'yes':
    with open("volumes.txt") as read_f:
        for i in read_f:
            print(i.strip())
elif display.lower() == 'no':
    print('Thank you. Goodbye.')
else:
    print('Sorry, I do not know that. Goodbye.')
# 02 Individual Checkpoint
# CSE 111
# Sunseehray Tirazona

import math

items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

boxes = math.ceil(items / items_per_box)

print()
print(f'For {items} items, packing {items_per_box} items in each box, you will need {boxes} boxes.')
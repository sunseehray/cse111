import csv
from datetime import datetime
from datetime import timedelta
import random

MEAL_INDEX = 0
CATEGORY_INDEX = 1
current_date = datetime.now()
current_date = datetime.strftime(current_date,"%a")

print(current_date)
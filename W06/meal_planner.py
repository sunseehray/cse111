""" Meal Planner is a program that helps create a meal plan
    for 7 days from a list of meals generated from the file,
    meals.csv
"""
import csv
from datetime import datetime
from datetime import timedelta
import random

MEAL_INDEX = 0
CATEGORY_INDEX = 1
DATE_INDEX = 0
current_date = datetime.now()
def main():
    try:
        meal_plan = []
        # create a list from the csv file
        meals_list = read_compound_list("meals.csv")

        # separate list into different meal categories
        
        # breakfast
        breakfast_list = filter_list(meals_list, CATEGORY_INDEX, "breakfast")
        
        # lunch
        lunch_list = filter_list(meals_list,CATEGORY_INDEX, "lunch")
        
        # dinner
        dinner_list = filter_list(meals_list,CATEGORY_INDEX, "dinner")
        
        # schedule by meal category
        breakfast_plan = scheduled_list(current_date,breakfast_list,1)
        lunch_plan = scheduled_list(current_date,lunch_list,2)
        dinner_plan = scheduled_list(current_date,dinner_list,3)

        # combine schedules inside meal_plan
        append_list(meal_plan, breakfast_plan)
        append_list(meal_plan, lunch_plan)
        append_list(meal_plan, dinner_plan)
        
        meal_plan.sort()
        write_file("meal_plan.txt",meal_plan)

    except FileNotFoundError as file_error:
        print(file_error)

# def write_file(information):
#     """ Generate a file that will show the final meal plan
#     Parameter:
#         information: the data that will be placed in the file
#     Return:
#         none
#     """
#     with open("meal_plan.csv", "w",newline='') as f:
#         writer = csv.writer(f)
#         writer.writerows(information)

def write_file(filename, lines):
    """Create a file and write lines of text to it.
    Parameter
        lines: a list of strings.
    Return: nothing
    """
    with open(filename, "wt") as outfile:
        for text in lines:
            print(text, file=outfile)

def append_list(main_list, append_list):
    """ Append a list inside a compound list

    Parameter:
        main_list: the compound list where a list will be appended
        append_list: the list that will be appended to the main_list
    Return:
        None
    """
    for i in append_list:
        main_list.append(i)

def scheduled_list(start_date, list_name, index):
    """ Generate the meal plan by category and day

    Parameters:
        start_date: the day the plan starts
        list_name: the list of meals to be planned, say breakfast, lunch, or dinner

    Return:
        meal_plan_list: the list of meals in each scheduled day
    """
    meal_plan_list = []
    temp_list = list_name
    days = seven_days(start_date)

    for i in days:
        meal = random.choice(temp_list)
        meal_list = [i, index, meal]
        meal_plan_list.append(meal_list)
        # remove from the temp_list what was already planned
        temp_list.remove(meal)

    return meal_plan_list

def seven_days(start_date):
    """ Get the days of the week for 7 days a day after the start_date
    Parameters:
        start_date: Day 0
    Return:
        seven_days: a list of the days a day after the start_date
    """
    seven_days = []
    count = 0
    while count < 7:
        count += 1
        day = start_date + timedelta(days=count)
        day = datetime.strftime(day,"%Y-%m-%d")
        seven_days.append(day)
    
    return seven_days

def filter_list(list_name, filter_index, filter_value=any):
    """ Filter a list based on a filter index

    Parameters:
        list_name: the list to be filtered
        filter_index: the index in the list in which
        the filter will be based on
        filter_value: the value of the filter
    Return:
        filtered_list: the filtered list
    """
    filtered_list = []
    for i in list_name:
        if i[filter_index] == filter_value:
            filtered_list.append(i)
    
    return filtered_list

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(some_list):
    """Print each element of the list on a separate line.

    Parameter
        some_list: the list to be printed
    Return: none
    """
    for i in some_list:
        print(i)

if __name__ == "__main__":
    main()
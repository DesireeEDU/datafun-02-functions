# user_math.py
"""
Desiree Thompson - Module 2 - January 23, 2023

Utilization of built-in functions and functions from the math module to illustrate the ability to call functions and display useful results to the user. 

Always start with a docstring that describes what the module does.
Include your name and the date.

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = length * width  # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None

# define more functions here (see instuctions)

# calculates the total price spent at the doggy daycare.


def get_doggy_daycare_total_price(daily_amount, total_days):
    try:
        total_cost = daily_amount * total_days
        return total_cost
    except Exception as ex:
        print(f"Error: {ex}")
        return None

# calculates the cost to buy the essential items for a new dog


def get_new_dog_essentials_total(food, bowls, leash, collar):
    try:
        total_cost = food + bowls + leash + collar
        return total_cost
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# list the total number of dags at the daycare for the past three months

doggy_daycare_monthly_totals = [105, 115, 111]


# -------------------------------------------------------------
# Call some functions and execute code!
# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print(f"get_area_of_alot(5, 1) = {get_area_of_lot(5, 1)}")
    print(f"get_area_of_alot(5, 5) = {get_area_of_lot(5, 5)}")
    print(f"get_area_of_alot(0, 5) = {get_area_of_lot(0, 5)}")
    print(f"get_area_of_alot(-5, 5) = {get_area_of_lot(-5, 5)}")
    print(f"get_area_of_alot(3, 8) = {get_area_of_lot(3, 8)}")
    print(f"get_area_of_alot(23, 45) = {get_area_of_lot(23, 45)}")
    print(f"get_area_of_alot(321, 654) = {get_area_of_lot(321, 654)}")
    print(f"get_area_of_alot(6, 2) = {get_area_of_lot(6, 2)}")
    print()
    print("Custom functions related to my domain of dogs")
    print(
        f"get_doggy_daycare_total_price(25, 3) = {get_doggy_daycare_total_price(25, 3)}")
    print(
        f"get_new_dog_essentials_total(10, 10, 20, 15) = {get_new_dog_essentials_total(10, 10, 20, 15)}")
    print(
        f"math.fsum(doggy_daycare_monthly_total) = {math.fsum(doggy_daycare_monthly_totals)}")

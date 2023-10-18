# Square Roots
# Brayden Towner
# 10/17/2023

import math, os
#Clear Screen
os.system("cls")

# Get the input from user
def get_user_input():

    # Check if user input is an integer
    try:
        global user_input
        user_input = int(input("What number do you want to find the square root of? >  "))
    except:
        os.system("cls")
        print(f"The input must be an integer")
        get_user_input()
    # Check if number is positive
    if user_input < 0:
        os.system("cls")
        print("The input MUST be a positive number")
        get_user_input()

get_user_input()

# Sets the Square Root of the users input
square_rooted_input = math.sqrt(user_input)

# Show the user the result of the square rooted number
print(f"The Square Root of {user_input} is {square_rooted_input}!")
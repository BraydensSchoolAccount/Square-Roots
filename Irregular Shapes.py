# Irregular Shapes
# Brayden Towner
# 10/18/2023

import os

# Clear the screen before the code runs
os.system("cls")

# Get the length of every side from the user, not idiot-proofed
side_A_length = float(input("What is the length of side 'A'? >  "))
side_B_length = float(input("What is the length of side 'B'? >  "))
side_C_length = float(input("What is the length of side 'C'? >  "))
side_D_length = float(input("What is the length of side 'D'? >  "))
side_E_length = float(input("What is the length of side 'E'? >  "))

os.system("cls")

# Calculate the area of the shape in one line
# ad - 1/2ae + bc - dc + 1/2ec
area_of_shape = (side_A_length * side_D_length) - (0.5 * side_A_length * side_E_length) + (side_B_length * side_C_length) - (side_D_length * side_C_length) + (0.5 * side_E_length * side_C_length)

# The shape needed to print, where each item is one line of the shape
# It also formats all the numbers into it
shape_to_print = [
    f"|---------------{side_D_length}--------------|",
    f"___________________________|_{side_E_length}_",
    "|                                /",
    "|                               /",
    f"{side_A_length}           _________________/",
    "|            |",
    f"|         {side_C_length}|",
    "|____________|",
    f"     {side_B_length}",

]

# Print the whole shape line by line
for i in shape_to_print:
    print(i)

# Finishes by putting the area of the shape
print(f"The area of the shape is {area_of_shape}")
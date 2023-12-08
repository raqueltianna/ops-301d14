#!/usr/bin/env python3 

# Script Name:                          collections_ops.py
# Author name:                          Tianna Farrow
# Date of latest revision:              12/07/2023
# Purpose:                              Using "if statements" in Python. 
# Execution:                            python3 conditionals09.py
# Additional Resources:                 https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/; https://www.geeksforgeeks.org/python-os-remove-method/; https://github.com/codefellows/seattle-ops-301d14/tree/main/class-10/challenges; https://github.com/codefellows/seattle-ops-301d14/blob/main/class-10/challenges/DEMO.md


# Decleration of Variables
file_name="testfile.txt"

# Imports
import os 

# Decleration of Functions

# Create a new .txt file 
with open(file_name, "w") as file:
    # Append three lines 
    file.write("This is the first line!\n")
    file.write("This is the second line!\n")
    file.write("This is the third line!\n")

# Print the first line
with open(file_name, "r") as file:
    first_line = file.readline()
    print("Here's the first line of your text file!:", first_line)

# Delete the file 
os.remove(file_name)
print(f"Your file is deleted!")

# End
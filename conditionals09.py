#!/usr/bin/env python3 

# Script Name:                          collections_ops.py
# Author name:                          Tianna Farrow
# Date of latest revision:              12/07/2023
# Purpose:                              Using "if statements" in Python. 
# Execution:                            python3 conditionals09.py
# Additional Resources:                 https://github.com/codefellows/seattle-ops-301d14/tree/main/class-09/challenges; https://docs.python.org/3/tutorial/controlflow.html; https://www.geeksforgeeks.org/check-multiple-conditions-in-if-statement-python/; https://www.tutorialspoint.com/python/nested_if_statements_in_python.htm; https://www.geeksforgeeks.org/nested-if-statement-in-python/; https://ioflood.com/blog/python-pass/

# Decleration of Variables
optimaltemp = 30
zermatt = 31
stmoritz = 20
aspen = 37
laketahoe = 33
jacksonhole = 30

# Decleration of Functions

# Equals
if jacksonhole == optimaltemp:
    print('Jackson Hole is at the optimal temp for skiing!')

# Less than or equal to; Greater than; elif; else
if aspen <= optimaltemp:
    print("Aspen is at a a good temp to go skiing!")
elif aspen > optimaltemp: 
    print("Aspen might not be the best choice for skiing!")
else:
    print("Unknown Weather?")

# Less than; greater than; elif; else
if stmoritz < optimaltemp:
    print("St. Moritz might be a little too cold but still a good temp for skiing! ")
elif stmoritz > optimaltemp:
    print("St. Moritz might not be the best choice for skiing!")
else:
    print("Unknown Weather?")

# Not equal, equal, elif, else 

if laketahoe != optimaltemp:
    print("Lake Tahoe might not be the optimal temp for skiing!")
elif laketahoe == optimaltemp:
    print("Lake Tahoe is at the optimal temp for skiing!")
else:
    print("Unknown Weather?")


# Stretch Goals

# If statement with 'and' in between
if aspen > optimaltemp and laketahoe >= optimaltemp:
    print("Aspen and Lake Tahoe might both be too warm for skiing!")

# If statement with 'or' in between
if jacksonhole == optimaltemp or stmoritz >= optimaltemp:
    print("Either Jackson Hole is the optimal temp for skiing or St. Moritz is too warm.")

# Nested if statement
if jacksonhole == optimaltemp:
    if zermatt <= optimaltemp:
        print("Jackson Hole is at the optimal temp for skiing, and Zermatt is also at a good temp.")
    else:
        print("Jackson Hole is at the optimal temp for skiing, but Zermat may be too warm.")

# If statement with "Pass"
try:
    pass
except Error as e:
    pass
else:
    print("No Errors! Yay!")
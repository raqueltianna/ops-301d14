#!/usr/bin/env python3 

# Script Name:                          collections_ops.py
# Author name:                          Tianna Farrow
# Date of latest revision:              12/07/2023
# Purpose:                              working with list in python
# Execution:                            python3 collections.py
# Additional Resources:                 https://github.com/codefellows/seattle-ops-301d14/blob/main/class-08/challenges/DEMO.md; https://www.programiz.com/python-programming/methods/list/append; 



# Decleration of Variables 
my_list = ['apple', 'bread', 'eggs', 'peppers', 'shrimp', 'pears', 'chicken', 'rice', 'icecream', 'juice']
appended_element = 'bananas'
extended_list = ['pineapples', 'steak']
index_egg = my_list.index('eggs')
popped_element = my_list.pop(2)
original_list = my_list
copied_list = original_list.copy

# Decleration of Variables 

# Print fourth element of the list 
print("Fourth Element:", my_list[3])

# Print the sixth through tenth element of the list.
print("\nSixth through Tenth Elements:", my_list[5:10])

# Change the value of the seventh element to "onion"
my_list[6] = 'onion'
print("\nNew List:", my_list)

# Stretch Goals

# append ()
my_list.append(appended_element)
print(f"\nUpdated List: {my_list[:-1]} \033[91m{appended_element}\033[0m")

# clear()
my_list.clear()
print("\nList after clear:", my_list)

# copy 
print("\nOriginal List:", original_list)
print("Copied List:", copied_list)

# count


# extend ()
my_list.extend(extended_list)
print("\nExtended List:", my_list)

# index()
print("\nIndex of 'eggs' in the list:", index_egg)

# insert()
my_list.insert(1, "grapes")
print("\nList after insert:", my_list)

# pop()
print("\nPopped Element:", popped_element)
print("List after pop:", my_list)

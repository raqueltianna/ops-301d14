# Script Name:                          directorycreation.py
# Author name:                          Tianna Farrow
# Date of latest revision:              12/04/2023
# Purpose:                              utilize bash prompts in python
# Execution:                            python3 bashinpython3 
# Additional Resources:                 https://github.com/codefellows/seattle-ops-301d14/blob/main/class-07/demo.py


#!/usr/bin/env python3

# Import libraries

import os

# Declaration of variables

### Read user input here into a variable
user_input_path = input("Enter the file path: ")

# Declaration of functions
def generate_directory_structure(user_path):
    for (root, dirs, files) in os.walk(user_path):
    ### Add a print command here to print ==root==
        print("==root==")
        print(root)
    ### Add a print command here to print ==dirs==
        print("==dirs==")
        print(dirs)
    ### Add a print command here to print ==files==
        print("==files==")
        print(files)

# Main

### Pass the variable into the function here
generate_directory_structure(user_input_path)
# End
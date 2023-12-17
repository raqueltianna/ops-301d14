#!/bin/bash

# Script Name:                          conditionalmenus.sh
# Author name:                          Tianna Farrow
# Date of latest revision:              12/17/23
# Purpose:                              create a bash script that launches a menu system
# Execution:                            bash conditionalmenus.sh
# Additional Resources:                 https://linuxhint.com/bash_conditional_statement/; https://phoenixnap.com/kb/bash-case-statement;https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php 

# For the menu
while true; do
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    # User input
    read -p "Enter your choice (1-4): " choice

    # Read user input
    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1
            ;;
        3)
            ifconfig
            ;;
        4)
            echo "Exiting. Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 4."
            ;;
    esac

    echo

done
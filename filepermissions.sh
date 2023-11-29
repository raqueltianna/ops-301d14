#!/bin/bash
# manipulate a varibale in bash to apply today's date to a log

# Script Name:                          filepermissions.sh
# Author name:                          Tianna Farrow
# Date of latest revision:              11/28/2023
# Purpose:                              change the permission for files in a directory
# Execution:                            bash filepermissions.sh or ./filepermissions.sh chmod -x filepermissions.sh
# Additional Resources                  https://www.geeksforgeeks.org/bash-script-file-permissions/; https://www.youtube.com/watch?v=lOX2iKTMWWA; https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/#7_8211_FILE_PERMISSIONS; https://github.com/codefellows/seattle-ops-301d14/blob/main/class-03/challenges/README.md; 


# Decleration of Variables 

#Decleration of Functions 

# Function to change permissions and display information
change_permissions() {
    directory="$1"
    permissions="$2"
    
    # Change permission for all files in the directory
    chmod "$permissions" "$directory"/*

    #Display directory contents and permissions
    ls -l "$directory"
}

# Main

# Prompt user for input directory path
read -p "Enter the directory path: " input_directory

# Prompt user for input permissions
read -p "Enter the permissions number you want to use: " input_permissions

# Change permissions from above function
change_permissions "$input_directory" "$input_permissions"

# End 

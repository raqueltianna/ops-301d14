#!/bin/bash
# manipulate a varibale in bash to apply today's date to a log

# Script Name:                          dateandtimeappend.sh
# Author name:                          Tianna Farrow
# Date of latest revision:              10/27/2023
# Purpose:                              Copies /var/log/syslog to the current working directory and appends the current date and time to the filename
# Execution:                            bash dateandtimeappend.sh or ./dateandtimeappend.sh chmod -x dateandtimeappend.sh
# Additional resources:                 https://intellipaat.com/community/62286/create-timestamp-variable-in-bash-script#:~:text=timestamp%3D%22%24(date%20%2B%22,when%20the%20variable%20was%20initialized; https://crunchify.com/shell-script-append-timestamp-to-file-name/; Ian Bennet; Hector Cordova; https://stackoverflow.com/questions/19181466/powershell-simply-checking-if-a-function-completed-successfully-or-not-times


# Make the script executable using sudo
sudo chmod +x "$0"


# Declaration of the variables
source_file="/var/log/syslog"

destination_file="systemlog_$(date +'%Y%m%d-%H:%M::%W')"

# Print the current date
echo $(date)

# Declaration of the functions
timestamp() {
  date +"%Y%m%d_%H%M%S"
}

# Print source file information
echo "Source file: $source_file"

# Copy syslog to the current directory
echo "$(timestamp) - Copying system log to your directory :)"
cp "${source_file}" "${destination_file}"

# Append the current date and time to the file
echo "$(timestamp) - Appending the current date and time to the file systemlog.log"
echo "Your new string with date: $(date)" >> systemlog_$(date +'%Y%m%d-%H:%M::%W')

#Check if done successfully 
if [ $? -eq 0 ]; then
  echo "$(timestamp) - Copy successful!"
else
  echo "$(timestamp) - Copy failed. Exiting..."
  exit 1
fi

# Completion Message
echo $(timestamp) - Backup completed! 

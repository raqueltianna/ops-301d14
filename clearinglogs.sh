#!/bin/bash

# Script Name:                          clearinglogs.sh
# Author name:                          Tianna Farrow
# Date of latest revision:              12/5/23
# Purpose:                              create a bash script that clears log files for you
# Execution:                            sudo bash clearinglogs.sh 
# Additional Resources                  https://unix.stackexchange.com/questions/16640/how-can-i-get-the-size-of-a-file-in-a-bash-script; https://www.cyberciti.biz/faq/howto-bash-check-file-size-in-linux-unix-scripting/; https://github.com/codefellows/seattle-ops-301d14/blob/main/class-05/challenges/DEMO.md; https://github.com/codefellows/seattle-ops-301d14/tree/main/class-05/challenges; 

# Decleration of Variables 
backup_dir="/var/log/backups"

# Needs to be as sudo
if [ "$EUID" -ne 0 ]; then
    echo "This script needs to be ran using sudo."
    exit 1 
fi

#Decleration of Functions 


# Does back dir exist? 
mkdir -p "$backup_dir"

# Print File Size 
print_file_size(){
    echo "File Size of $1: $(du -h $1 | cut -f1)"
}

# Clear log file
clear_log_file(){
    truncate -s 0 $1
}

# Compress and backup log file
compress_and_backup() {
    log_file=$1
    timestamp=$(date "+%Y%m%d%H%M%S")
    backup_file="$backup_dir/$(basename $log_file)-$timestamp.zip"

    gzip -c $log_file > $backup_file
    print_file_size $backup_file
}

# print original file size
print_file_size "/var/log/syslog"
print_file_size "/var/log/wtmp"

# compress and backup log files
compress_and_backup "/var/log/syslog"
compress_and_backup "/var/log/wtmp"

# clear log files
clear_log_file "/var/log/syslog"
clear_log_file "/var/log/wtmp"

# print compressed file sizes and compare 
print_file_size "$backup_dir/syslog-*.zip"
print_file_size "$backup_dir/wtmp-*.zip"

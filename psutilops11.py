#!/usr/bin/env python3 

# Script Name:                          psutilops11.py
# Author name:                          Tianna Farrow
# Date of latest revision:              12/07/2023
# Purpose:                              Using Psutil to fetch system information
# Execution:                            python3 psutilops11.py
# Additional Resources:                 https://readthedocs.org/projects/giamptest/downloads/pdf/latest/; https://www.educative.io/answers/what-is-the-psutilcputimes-method-in-python; https://ioflood.com/blog/python-create-file/#:~:text=To%20create%20a%20file%20in,if%20it%20does%20not%20exist; https://github.com/codefellows/seattle-ops-301d14/tree/main/class-11/challenges; https://github.com/codefellows/seattle-ops-301d14/blob/main/class-11/challenges/DEMO.md

# Imports 
import psutil

# Decleration of Variables 


# Decleration of Functions

# Main function to get and print cpu times

def print_cpu_time(metric_name, metric_value, file):
    print(f"{metric_name}: {metric_value} seconds", file=file)
    
          
def get_cpu_times():
    with open("currenttimes.txt", "w") as file:
        print_cpu_time("Time spent by normal processes executing in user mode", psutil.cpu_times().user, file)
        print_cpu_time("Time spent by processes executing in kernel mode", psutil.cpu_times().system, file)
        print_cpu_time("Time when system was idle", psutil.cpu_times().idle, file)
        print_cpu_time("Time spent by priority processes executing in user mode", psutil.cpu_times().nice, file)
        print_cpu_time("Time spent waiting for I/O to complete", psutil.cpu_times().iowait, file)
        print_cpu_time("Time spent for servicing hardware interrupts", psutil.cpu_times().irq, file)
        print_cpu_time("Time spent for servicing software interrupts", psutil.cpu_times().softirq, file)
        print_cpu_time("Time spent by other operating systems running in a virtualized environment", psutil.cpu_times().steal, file)
        print_cpu_time("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel", psutil.cpu_times().guest, file)
        print_cpu_time("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel (including time spent in userspace)", psutil.cpu_times().guest_nice, file)

if __name__ == "__main__":
        get_cpu_times()
        print("CPU times have been saved to currenttimes.txt")




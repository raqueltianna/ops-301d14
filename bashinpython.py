# Script Name:                          bashinpython.py
# Author name:                          Tianna Farrow
# Date of latest revision:              12/04/2023
# Purpose:                              utilize bash prompts in python
# Execution:                            python3 bashinpython3 
# Additional Resources                  https://stackoverflow.com/questions/58402900/how-to-run-bash-commands-using-subprocess-run-on-windows; https://stackoverflow.com/questions/11248224/python-subprocess-popen-result-stored-in-a-variable, https://docs.python.org/3/library/subprocess.html#module-subprocess, https://peps.python.org/pep-0008/, https://docs.python.org/3/library/os.html, https://github.com/codefellows/seattle-ops-301d14/tree/main/class-06/challenges, https://github.com/codefellows/seattle-ops-301d14/blob/main/class-06/challenges/DEMO.md


# Imports 
import subprocess 

# Variables 
whoami = subprocess.check_output(['whoami'], text=True).strip()
ip_a = subprocess.check_output(['ip', 'a'], text=True)
lshw = subprocess.check_output(['lshw', '-short'], text=True)

# Input 


# Output
print ("This is the Current user:", whoami)

print ("This is the Current Network Interface" + ip_a)

print ("This is the current Hardware Information" + lshw)



# Functions 




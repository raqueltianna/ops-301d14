#!/usr/bin/env python3 

# Script Name:                          adautomation.sh
# Author name:                          Tianna Farrow
# Date of latest revision:              12/13/23
# Purpose:                              Create a powershell script to add a new user to AD. 
# Execution:                            bash adautomation.sh
# Additional Resources:                 https://lazyadmin.nl/powershell/add-user-to-group-add-adgroupmember/; https://lazyadmin.nl/powershell/add-user-to-group-add-adgroupmember/; 
 
 # User Info
$firstName = "Franz"
$lastName = "Ferdinand"
$username = "ferdi"
$jobTitle = "TPS Reporting Lead"
$department = "TPS Department"
$email = "ferdi@GlobeXpower.com"
$office = "Springfield, OR"

# User in AD
New-ADUser -SamAccountName $username -GivenName $firstName -Surname $lastName `
    -DisplayName "$firstName $lastName" -Title $jobTitle -Department $department `
    -EmailAddress $email -Office $office -Enabled $true `
    -UserPrincipalName "$username@corp.globex.com" -AccountPassword (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force)

# Output
Write-Host "User $username added successfully."

# Remove-ADUser -Identity $username -Confirm:$false (if you need to remove user.)
#!/usr/bin/env python3 

# Script Name:                          requestlib.py
# Author name:                          Tianna Farrow
# Date of latest revision:              12/12/2023
# Purpose:                              Performing HTTP GET requests using the requests Python library. 
# Execution:                            python3 requestlib.py
# Additional Resources:                 https://realpython.com/python-requests/; https://docs.python.org/3/reference/compound_stmts.html#the-try-statement; https://codepal.ai/code-generator/query/lts1CYWu/python-function-get-user-input; https://docs.python.org/3/reference/simple_stmts.html#the-return-statement; https://docs.python.org/3/library/functions.html#input; https://docs.python.org/3/library/functions.html#print; https://docs.python.org/3/tutorial/datastructures.html#dictionaries



# Imports 
import requests

# Get User Input (Prompt)
def get_user_input(prompt):
    return input(prompt)

# HTTP method from the user
def get_http_method():
    #  HTTP methods
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']
    # choose an HTTP method 
    method_prompt = f"Choose an HTTP Method ({', '.join(methods)}): "
    
    
    while True:
        user_input = get_user_input(method_prompt).upper()
        if user_input in methods:
            return user_input
        else:
            print("Invalid HTTP Method. Please choose from the provided options.")

# translate HTTP status codes
def translate_status_code(status_code):
    # Dictionary mapping status codes 
    status_codes = {
        200: 'OK',
        201: 'Created',
        204: 'No Content',
        400: 'Bad Request',
        401: 'Unauthorized',
        404: 'Site not found',
        500: 'Internal Server Error'
    }
    # 'Unknown Status Code'
    return status_codes.get(status_code, 'Unknown Status Code')

# print response information, including status code and headers
def print_response_info(response):
    print(f"\nResponse Status Code: {response.status_code} - {translate_status_code(response.status_code)}")
    print("Response Headers:")
    # Print each header key and value
    for key, value in response.headers.items():
        print(f"{key}: {value}")

# main function
def main():
    # destination URL from the user
    destination_url = get_user_input("Enter the destination URL: ")
    # HTTP method from the user
    http_method = get_http_method()

    # upcoming request
    print(f"\nPreparing to send a {http_method} request to: {destination_url}")
    
    # Ask the user for confirmation
    confirmation = get_user_input("Do you want to proceed? (yes/no): ").lower()
    # If the user doesn't confirm, exit
    if confirmation != 'yes':
        print("Request canceled.")
        return

    try:
        # Make the HTTP request using the specified method and URL
        response = requests.request(http_method, destination_url)
        # Print information
        print_response_info(response)
    except requests.exceptions.RequestException as e:
        # Handle exceptions that may occur during the request
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
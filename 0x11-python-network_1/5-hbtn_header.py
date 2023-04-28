#!/usr/bin/python3
""" sends a request to the URL and displays the value of
the variable X-Request-Id in the response header"""
import requests
import sys

# Get the URL from the command-line arguments
url = sys.argv[1]

# Send a GET request to the URL
response = requests.get(url)

# Read the value of the X-Request-Id header from the response
x_request_id = response.headers.get('X-Request-Id')

# Print the value of the X-Request-Id header to the terminal
print(x_request_id)

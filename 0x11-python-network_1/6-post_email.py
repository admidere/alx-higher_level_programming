#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
nd finally displays the body of the response.
"""

import requests
import sys


if __name__ == '__main__':
    # Get URL and email address from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Send POST request with email as parameter
    response = requests.post(url, data={'email': email})

    # Display response body
    print(response.text)

#!/usr/bin/python3
"""ends a POST request to the passed URL with the email"""
import requests
import sys

if __name__ == '__main__':
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary of the data to be sent in the POST request
    data = {'email': email}

    # Send a POST request to the URL with the data
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)

#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import requests
import sys

if __name__ == '__main__':
    # Get the URL from command-line arguments
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check the status code of the response
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        # Display the body of the response
        print(response.text)

#!/usr/bin/python3
"""ends a POST request to the passed URL with the email"""
import urllib.request
import sys

if __name__ == '__main__':
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = "email={}".format(email).encode('utf-8')

    # Send the POST request
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        # Read the response and decode it in utf-8
        body = response.read().decode('utf-8')

    # Print the response body
    print(body)

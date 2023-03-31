#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    params = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send the POST request
    with urllib.request.urlopen(url, data=params) as response:
        # Decode and print the response body
        print(response.read().decode('utf-8'))

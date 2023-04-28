#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response"""
import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    # Get the URL from the command line argument
    url = sys.argv[1]

    try:
        # Send the request and read the response
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)

    except urllib.error.HTTPError as e:
        # If there's an HTTP error, print the error code
        print("Error code: {}".format(e.code))

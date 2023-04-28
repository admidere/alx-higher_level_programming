#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the
header of the response."""
import urllib.request
import sys

# Get URL from command line argument
url = sys.argv[1]

# Send request to URL and get response
with urllib.request.urlopen(url) as response:
    # Get the value of the X-Request-Id variable from the response header
    x_request_id = response.headers.get('X-Request-Id')

    # Display the value of the X-Request-Id variable
    print(x_request_id)

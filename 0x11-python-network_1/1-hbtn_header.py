#!/usr/bin/python3
import urllib.request
import sys
"""Response header value"""

# Get the URL from the command-line argument
url = sys.argv[1]

if __name__ == '__main__':
    # Send a request to the URL and get the response
    with urllib.request.urlopen(url) as response:
        # Get the value of the X-Request-Id header
        X_request_id = response.headers.get('X-Request-Id')
        # Display the value of the X-Request-Id header
        print(X_request_id)

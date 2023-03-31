#!/usr/bin/python3
"""Response header value"""
import urllib.request
import sys

# Get the URL from the command-line argument
url = sys.argv[1]

if __name__ == '__main__':
    with urllib.request.urlopen(url) as response:
        X_request_id = response.headers.get('X-Request-Id')
    print(X_request_id)

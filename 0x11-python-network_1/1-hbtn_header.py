#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the
header of the response."""
from sys import argv
import urllib.request

# get a url from CLA
url = argv[1]

# use with statment for open request url and get response the header id
with urllib.request.urlopen(url) as response:
    # get the value of requested id and store at id variable
    id = response.headers.get('X-Request-Id')
    print(id)

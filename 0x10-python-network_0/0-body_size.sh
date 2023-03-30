#!/bin/bash
# takes in a URL, sends a request to that URL using curl, and
# displays the size of the response body in bytes

curl -Is -L "$1" | grep -w 'Content-Length' | cut -d ' ' -f2

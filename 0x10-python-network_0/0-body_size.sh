#!/bin/bash
# Check if a URL was provided as an argument
if [ -z "$1" ]; then
	  echo "Usage: $0 <url>"
	    exit 1
fi

# Send a request to the URL and get the size of the body
size=$(curl -sI "$1" | awk '/Content-Length/ { print $2 }')

# Display the size of the body in bytes
echo "${size}"

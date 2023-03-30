#!/bin/bash
# takes in a URL, sends a request to that URL using curl, and
# displays the size of the response body in bytes

# Check if URL is provided
if [ $# -eq 0 ]; then
	  echo "Please provide a URL as an argument"
	    exit 1
fi

url="$1"

# Send request using curl and get the size of the response body in bytes
size=$(curl -s -o /dev/null -w '%{size_download}' "$url")

# Display the size of the response body in bytes
echo "$size"

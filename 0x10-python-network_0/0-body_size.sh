#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL
# band displays the size of the body of the response

# Check that an argument was provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a request to the URL and save the response body
response=$(curl -s $1)

# Get the size of the response body in bytes
size=$(echo -n $response | wc -c)

# Display the size of the response body
echo "$size"

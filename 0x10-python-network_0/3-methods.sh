#!/bin/bash

# Get the URL from the command line argument
url=$1

# Use curl to send a request to the server and get the response headers
headers=$(curl -I -X OPTIONS $url 2>/dev/null)

# Extract the Allow header from the response headers
allow_header=$(echo "$headers" | grep -i allow)

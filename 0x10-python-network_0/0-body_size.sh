#!/bin/bash
# takes in a URL, sends a request to that URL using curl, and
# displays the size of the response body in bytes

#!/bin/bash

# get URL from command line argument
url=$1

# send request to URL and get response body size in bytes
response_size=$(curl -s -o /dev/null -w '%{size_download}' $url)

# display response body size
echo "$response_size"

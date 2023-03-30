#!/bin/bash
# takes in a URL, sends a request to that URL using curl, and
# displays the size of the response body in bytes

curl -so /dev/null -w '%{size_download}\n' $1

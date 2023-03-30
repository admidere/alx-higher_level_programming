#!/bin/bash
# sends a DELETE request to the URL
URL=$1
curl -s -X DELETE $URL
echo "I'm a DELETE request"

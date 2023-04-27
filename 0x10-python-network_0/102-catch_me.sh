#!/bin/bash
# Bash script to make a request to 0.0.0.0:5000/catch_me
curl -s -X PUT -H "Content-Type: text/plain" -d "You got me!" 0.0.0.0:5000/catch_me --output /dev/null -w "%{http_code}\n"

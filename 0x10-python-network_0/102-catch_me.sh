#!/bin/bash
# This script makes a request to catch_me endpoint and causes the server to respond with "You got me!" message.
curl -s -X PUT -H "Content-Type: text/plain" -d "user_id=42" 0.0.0.0:5000/catch_me --output /dev/null

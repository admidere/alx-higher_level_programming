#!/bin/bash
# Makes a request to the server and causes it to respond with "You got me!"
curl -s -X PUT -H "Content-Type: text/plain" -d "You got me!" "0.0.0.0:5000/catch_me" -w "\n"

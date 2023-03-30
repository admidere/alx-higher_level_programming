#!/bin/bash
# Set the URL and variables

email="test@gmail.com"
subject="I will always be here for PLD"

# Send POST request with curl and save response to variable
curl -s -X POST -d "email=$email&subject=$subject" "$1"

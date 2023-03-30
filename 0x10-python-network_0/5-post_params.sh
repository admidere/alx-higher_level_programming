#!/bin/bash
# Set the URL and variables

email="test@gmail.com"
subject="I will always be here for PLD"

# Send the POST request with the variables
curl -s -X POST -d "email=$email&subject=$subject" "$1"

#!/bin/bash
# Get the URL from the command line argu
curl -sI -L -X OPTIONS -i "$1" 2>/dev/null | grep "Allow" | tr -d '\r\n'

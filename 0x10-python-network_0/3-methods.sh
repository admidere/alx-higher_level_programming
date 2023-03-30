#!/bin/bash
# Get the URL from the command line argu
curl -sI -L -X OPTIONS "$1" | grep -w 'Allow' | cut -d ' ' -f2-

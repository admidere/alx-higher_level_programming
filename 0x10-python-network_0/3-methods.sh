#!/bin/bash
# Get the URL from the command line argu
curl -X OPTIONS -i $1 2>/dev/null | grep "Allow" | tr -d '\r\n'

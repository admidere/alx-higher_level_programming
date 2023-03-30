#!/bin/bash
# Check if a URL was provided as an argument
curl -sI "$1" | awk '/Content-Length/ { print $2 }'

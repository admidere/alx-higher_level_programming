#!/bin/bash
# This script takes a URL and displays all HTTP methods the server will accept
curl -I -X OPTIONS "$1" | grep "Allow" | cut -d " " -f2-

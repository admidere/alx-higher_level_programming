#!/bin/bash
# This script isplays only the status code of the response form the requested URL
curl -s -X HEAD --write-out "%{http_code}" "$1"

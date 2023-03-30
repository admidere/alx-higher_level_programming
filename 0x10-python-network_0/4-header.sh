#!/bin/bash
# ends a GET request to the URL
url="$1"
curl -H "X-School-User-Id: 98" -X GET "$url"

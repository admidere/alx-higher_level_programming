#!/bin/bash
# Display HTTP methods accepted by server
curl -s -I -X OPTIONS $1 | grep "Allow" | awk '{print $2}'

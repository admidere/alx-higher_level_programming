#!/bin/bash
# Send GET request and display body of response
curl -sL $1 | sed '/^$/d'

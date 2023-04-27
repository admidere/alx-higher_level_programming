#!/bin/bash
# This script sends a POST request to 0.0.0.0:5000/catch_me
curl -s -X POST 0.0.0.0:5000/catch_me -d "user_id=42" -H "Origin:HolbertonSchool"

#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys


if __name__ == '__main__':
username = sys.argv[1]
pat = sys.argv[2]

# Construct the API endpoint URL
url = f"https://api.github.com/users/{username}"

# Set the Authorization header with the Basic Authentication token
headers = {"Authorization": f"Basic {username}:{pat}"}

# Make the API request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Extract the user ID from the response JSON
    user_id = response.json()["id"]
    print(f"Your user ID is {user_id}")
else:
    print("Error:", response.status_code)

#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys


if __name__ == '__main__':

# Replace with your GitHub username and personal access token
username = sys.argv[1]
password = sys.argv[2]

# Set up the API endpoint and headers
api_endpoint = 'https://api.github.com/user'
headers = {'Accept': 'application/vnd.github.v3+json'}

# Make the API request using Basic Authentication
response = requests.get(api_endpoint, auth=(username, password), headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Extract and display the user id
    user_id = response.json()['id']
    print(f"Your GitHub user id is {user_id}.")
else:
    print("Failed to retrieve your user id.")

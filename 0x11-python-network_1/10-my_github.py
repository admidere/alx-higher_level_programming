#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
import sys

if __name__ == '__main__':
    # The first argument is the GitHub username, the second argument is the personal access token
    username = sys.argv[1]
    token = sys.argv[2]

    # Define the URL for the API request
    url = f"https://api.github.com/user"

    # Define the headers for the API request
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Basic {username}:{token}"
    }

    # Send the API request
    response = requests.get(url, headers=headers)

    # If the request was successful, print the user ID
    if response.status_code == 200:
        user_id = response.json()["id"]
        print("{}".format(user_id)
    else:
        print("None")

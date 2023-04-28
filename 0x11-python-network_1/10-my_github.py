#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
import sys

if __name__ == '__main__':
    # Set the GitHub API endpoint
    endpoint = "https://api.github.com/user"

    # Get the username and password from the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Send a GET request to the endpoint with the Basic Authentication header
    response = requests.get(endpoint, auth=(username, password))

    # If the response is successful, print the user id
    if response.status_code == 200:
        user_id = response.json()["id"]
        print("{}".format(user_id))
    else:
        print("None")

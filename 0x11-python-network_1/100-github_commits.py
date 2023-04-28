#!/usr/bin/python3
"""The Holberton School staff evaluates candidates applying for
a back-end position with multiple technical challenges"""
import requests
import sys

if __name__ = '__main__':
    # Set the GitHub API endpoint
    endpoint = "https://api.github.com/repos/{}/{}/commits"

    # Get the repository name and owner name from the command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Send a GET request to the endpoint with the repository and owner names
    response = requests.get(endpoint.format(owner_name, repo_name))

    # If the response is successful, print the last 10 commits
    if response.status_code == 200:
        commits = response.json()[:10]  # Get the last 10 commits
        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    else:
        print("Error")

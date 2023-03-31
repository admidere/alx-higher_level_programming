#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == '__main__':
    # Set the URL to send the POST request to
    url = "http://0.0.0.0:5000/search_user"

    # Get the letter as input, default to empty string if no argument is given
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Create the data payload for the POST request
    payload = {"q": q}

    # Send the POST request with the data payload
    response = requests.post(url, data=payload)

    try:
        # Try to parse the response body as JSON
        json_response = response.json()

        # If the JSON is properly formatted and not emptty
        if json_response:
            print("[{}] {}".format(json_response.get("id"),
                  json_response.get("name")))
        else:
            print("No result")
    except ValueError:
        # If the response body is not properly formatted JSon
        print("Not a valid JSON")

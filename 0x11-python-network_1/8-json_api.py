#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys

if __name__ == '__main__':
    # Get the letter from command-line arguments or set it to ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    # Set the URL and data for the POST request
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}

    # Send the POST request
    response = requests.post(url, data=data)

    # Check if the response body is JSON formatted and not empty
    try:
        json_response = response.json()
        if json_response:
            # Display the id and name from the JSON response
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            # Display a message if the JSON response is empty
            print("No result")
    except ValueError:
        # Display a message if the response is not valid JSON
        print("Not a valid JSON")

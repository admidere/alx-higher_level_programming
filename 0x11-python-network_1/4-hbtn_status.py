#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)

    content = response.content.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

# define url to fetch
url = 'https://alx-intranet.hbtn.io/status'

# use with statmentr for open url and fetch response
with urllib.request.urlopen(url) as response:
    # read the reponse and store it in the variable res
    res = response.read()

# print the body of response that is requird format
print("Body response:")
print("\t- type: {}".format(type(res)))
print("\t- content: {}".format(res))
print("\t- utf8 content: {}".format(res.decode('utf-8')))

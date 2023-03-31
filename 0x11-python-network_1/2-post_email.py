#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import urllib.request
import sys
if __name__ == '__main__':
  # Get the URL and email from the command-line arguments
  url = sys.argv[1]
  email = sys.argv[2]

  # Encode the email in utf-8
  email_bytes = email.encode('utf-8')

  # Make the POST request with the email as a parameter
  with urllib.request.urlopen(url, data=email_bytes) as response:
      # Decode the body of the response in utf-8 and print it
      body = response.read().decode('utf-8')
  print(body)

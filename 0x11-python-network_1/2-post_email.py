#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST request to the
URL with the email as a parameter, and displays the body of the
response decoded
in utf-8.
"""


import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """
    Sends a POST request to the specified URL with the provided
    email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to include in the POST request.
    """
    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    # Send the POST request
    with urllib.request.urlopen(url, data) as response:
        # Read and decode the response
        body = response.read().decode('utf-8')

    # Print the response body
    print(body)


if __name__ == "__main__":
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Call the function to send the POST request
    post_email(url, email)

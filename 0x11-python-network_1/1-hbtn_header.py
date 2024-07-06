#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the
header of the response.
"""


import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Fetches and prints the X-Request-Id header from the response of the URL.

    Args:
        url (str): The URL to send the request to.
    """
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    # Get the URL from the command line arguments
    url = sys.argv[1]
    fetch_x_request_id(url)

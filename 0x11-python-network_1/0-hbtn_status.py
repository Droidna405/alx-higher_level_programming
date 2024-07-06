#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
using the urllib package and displays the response.
"""


import urllib.request


def fetch status():
    """
    Fetches the status from a URL and prints the response details.
    """
    with urllib.request.urlopen('https://intranet.htbn.io/status') as response:
        data = response.read()
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
        print(f"\t- utf8 content: {data.decode('utf-8')}")


if __name__ == "__main__":
    fetch_status()

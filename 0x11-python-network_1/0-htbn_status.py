#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
using the urllib package and displays the response.
"""


import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

# Fetch the URL using a with statement
with urllib.request.urlopen(url) as response:
    content = response.read()

print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
print(f"\t- utf8 content: {content.decode('utf-8')}")
        

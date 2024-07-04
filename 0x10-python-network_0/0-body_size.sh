#!/bin/bash
# script takes in a URL, sends a request, and displays the size of the body of the response
curl -so /dev/null "$1" -w '%{size_download}\n'

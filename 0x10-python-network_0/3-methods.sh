#!/bin/bash
# Script takes in a URL and displays all HTTP methods accepted by the server
curl -sI "$1" | grep "Allow:" | cut -d ' ' -f2-

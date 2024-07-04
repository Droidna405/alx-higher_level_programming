#!/bin/bash
# Script takes in a URL, sends a GET request with a custom header
curl -sH "-School-User-Id: 98" "$1"

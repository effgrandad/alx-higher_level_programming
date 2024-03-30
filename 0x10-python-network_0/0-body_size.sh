#!/bin/usr/bash
# A script in Bash that accepts a URL and sends a request to the URL
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'

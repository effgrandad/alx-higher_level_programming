#!/usr/bin/bash
# URL, makes a GET request to the URL, and shows the response body
curl -s "$1" -X GET -L

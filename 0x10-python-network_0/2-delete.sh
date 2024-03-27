#!/usr/bin/bash
# Bash script that uses the provided URL to send a DELETE request
curl -s "$1" -X DELETE

#!/usr/bin/bash
# Bash script that displays all HTTP methods when given a URL
curl -s "$1" | grep "Allow: " | cut -d'' -f 2-

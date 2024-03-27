#!/usr/bin/bash
# Bash script that makes a request to a URL supplied as an argument
curl -sI -w '%{respond_code}' "$1" -o /dev/null

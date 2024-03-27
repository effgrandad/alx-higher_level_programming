#!/usr/bin/bash
# Bash script that receives a URL, sends a POST request to a supplied URL
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

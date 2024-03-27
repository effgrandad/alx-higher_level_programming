#!/usr/bin/bash
# Bash script that send JSON POST quest
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"

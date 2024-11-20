#!/bin/bash
# Check if the URL is provided, else show usage message and exit
[ -z "$1" ] && echo "Usage: $0 <URL>" && exit 1
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'

#!/bin/bash
# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi
# Send the request and extract the size of the body
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'

#!/bin/bash
# Check if a URL argument is provided
[ -z "$1" ] && echo "Usage: $0 <URL>" && exit 1 curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'

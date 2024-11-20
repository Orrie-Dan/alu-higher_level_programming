#!/bin/bash
# Check if URL argument is provided
[ -z "$1" ] && echo "Usage: $0 <URL>" && exit 1; curl -sI "$1" | awk '/Content-Length/ {print $2}'

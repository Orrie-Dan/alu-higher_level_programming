#!/bin/bash
# Send GET request, check for 200 status code, and display body if 200
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q "^200$" && curl -s "$1"

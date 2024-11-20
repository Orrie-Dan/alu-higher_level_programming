#!/bin/bash
# Send GET request and display the body if status code is 200
curl -s -o response_body.txt -w "%{http_code}" "$1" | grep -q "200" && cat response_body.txt

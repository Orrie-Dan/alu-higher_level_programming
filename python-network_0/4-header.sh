#!/bin/bash
# Send GET request with custom header and display the body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1" | grep -i "OK"

#!/bin/bash
# Send GET request with custom header and display the body of the response
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"

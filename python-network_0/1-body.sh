#!/bin/bash
# Send GET request, follow redirections, and count how many redirects occurred
curl -s -L -w "%{num_redirects}" -o /dev/null "$1" 

#!/bin/bash
# Send GET request, follow redirections, and count how many redirects occurred
redirects=$(curl -s -L -w "%{num_redirects}" -o /dev/null "$1"); [ "$redirects" -eq 0 ] && echo "Direct access" || echo "With $redirects redirections" 

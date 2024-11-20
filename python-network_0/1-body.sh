#!/bin/bash
# Send GET request and handle redirections
redirects=$(curl -s -L -w "%{num_redirects}" -o /dev/null "$1"); [ "$redirects" -eq 0 ] && echo "Direct access" || { [ "$redirects" -eq 1 ] && echo "With one redirection" || echo "With $redirects redirections"; } 

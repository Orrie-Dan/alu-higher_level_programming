#!/bin/bash
# Get allowed HTTP methods for the URL
curl -s -I "$1" | grep -i Allow | sed 's/Allow: //'

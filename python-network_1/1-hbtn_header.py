#!/usr/bin/python3
"""A script that takes in a URL,
Sends a request to the URL,
And displays the value of the X-Request-Id
variable found in the header of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    # Get URL from the command line argument
    url = sys.argv[1]

    # Create the request object
    request = urllib.request.Request(url)

    # Open the URL and follow redirections automatically
    with urllib.request.urlopen(request) as resp:
        # Retrieve the X-Request-Id from the response headers, if it exists
        x_request_id = resp.headers.get("X-Request-Id")

        # If the X-Request-Id header is not found, print None (or handle it differently)
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id not found")


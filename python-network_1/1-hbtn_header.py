#!/usr/bin/python3
import urllib.request
import sys

"""
This script takes in a URL, sends a request to the URL, and displays the value of
the X-Request-Id variable found in the header of the response. It uses the urllib
and sys packages, and ensures proper handling of the response using a with statement.
"""

def fetch_x_request_id(url):
    """
    Fetches and displays the value of the X-Request-Id header from the given URL.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        None
    """
    with urllib.request.urlopen(url) as response:
        # Retrieve the value of the X-Request-Id from the response headers
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

if __name__ == "__main__":
    # Take URL from the command line argument
    url = sys.argv[1]

    # Fetch and display the X-Request-Id value
    fetch_x_request_id(url)


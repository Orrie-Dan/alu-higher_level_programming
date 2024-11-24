#!/usr/bin/python3
import urllib.request
"""
This script fetches the content from a given URL using the urllib.request module.
It reads the body of the response and displays it with a tabulation before the content.

The URL being accessed is: https://alu-intranet.hbtn.io/status

Modules Used:
    - urllib.request: To open the URL and read the response.

The output is the body content of the response displayed with a tabulation as required.
"""
# URL to fetch
url = "https://alu-intranet.hbtn.io/status"

def fetch_status(url):
    """
    Fetches the content from the provided URL and displays the body response.

    This function uses urllib to open the provided URL, reads the body of the response,
    and prints it with a tabulation prefix as specified.

    Parameters:
        url (str): The URL to fetch content from.

    Returns:
        None
    """
    with urllib.request.urlopen(url) as response:
        body = response.read()  # Read the body of the response
        print("Body response:")
        print(f"\t- {body.decode('utf-8')}")  # Decode and print the body content

# Calling the function to fetch and display the status page
fetch_status(url)


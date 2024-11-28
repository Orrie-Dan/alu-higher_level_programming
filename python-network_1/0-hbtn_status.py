#!/usr/bin/python3
import urllib.request

"""
This script fetches the content from a given URL using the urllib.request module.

The main function fetch_status(url) opens the specified URL and prints the body of the
response with a tabulation before it.

The script can be run as a standalone program and will fetch content from the URL
'https://intranet.hbtn.io/status' by default.
"""

def fetch_status(url):
    """
    Fetches and prints the response body from the given URL.
    
    Args:
        url (str): The URL to fetch the content from.
        
    Returns:
        None
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(f"Body response:\n\t{body}")
    except Exception as e:
        print(f"Error fetching URL: {e}")


if __name__ == "__main__":
    # URL for fetching status
    url = "https://intranet.hbtn.io/status"
    
    # Fetch and display status for the given URL
    fetch_status(url)


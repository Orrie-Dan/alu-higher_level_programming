#!/usr/bin/python3
import urllib.request

url = "https://alu-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print(f"\t- {body.decode('utf-8')}")


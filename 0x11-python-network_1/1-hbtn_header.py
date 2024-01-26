#!/usr/bin/python3
"""
the script takes in as URL, sends the request and displays
value of X-Request-Id variable found in header
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))

#!/usr/bin/python3
"""
the script sends request to URL and
displays:
- body of response if there's no errors
- error code when there is HTTP error.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)

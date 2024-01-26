#!/usr/bin/python3
"""
the script that takes in URL, sends request and displays 
value of X-Request-Id variable found in header
(handling HTTP errors)
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))

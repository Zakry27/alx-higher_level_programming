#!/usr/bin/python3
"""
the script takes in URL and email, sends POST
request to passed URL with email as parameter, and
displays body of response
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))

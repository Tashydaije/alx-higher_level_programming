#!/usr/bin/python3

"""
Script that makes a POST request to a URL passed as an argument
and displays the decoded body response in utf-8
"""
import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)

#!/usr/bin/python3

"""
script that fetches https://alx-intranet.hbtn.io/status
using urllib packkage
"""

if __name__ == '__main__':
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(page)))
        print('\t- content: {}'.format(page))
        print('\t- utf8 content: {}'.format(page.decode('utf-8')))

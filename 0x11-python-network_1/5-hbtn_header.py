#!/usr/bin/python3
"""accepts a URL, makes a request to the URL, and shows the value
of the response header's variable X-Request-Id
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))

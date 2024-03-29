#!/usr/bin/python3
"""receives a URL, makes a request to it, and then shows the value
of the X-Request-Id variable that can be found in the response header
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))

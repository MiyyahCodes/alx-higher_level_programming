#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    from sys import argv

    url = argv[1]
    val = {'email': argv[2]}
    data = urllib.parse.urlencode(val).encode('ascii')

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))

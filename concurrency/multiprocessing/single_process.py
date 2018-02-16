import urllib.request

sites = [
    'https://www.yahoo.com/',
    'http://www.cnn.com',
    'http://www.python.org',
    'http://www.jython.org',
    'http://www.pypy.org',
    'http://www.perl.org',
    'http://www.cisco.com',
    'http://www.facebook.com',
    'http://www.twitter.com',
    'http://www.macrumors.com/',
    'http://arstechnica.com/',
    'http://www.reuters.com/',
    'http://abcnews.go.com/',
    'http://www.cnbc.com/',
]


# for url in sites:
#     with urllib.request.urlopen(url) as u:
#         page = u.read()
#         print(url, len(page))

# with functions
def sitesize(url):
    ''' Determine the size of a website '''
    with urllib.request.urlopen(url) as u:
        page = u.read()
        return url, len(page)

for result in map(sitesize, sites):
    print(result)

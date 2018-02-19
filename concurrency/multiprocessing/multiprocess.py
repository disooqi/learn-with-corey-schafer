# http://pybay.com/site_media/slides/raymond2017-keynote/process.html
# only option when you have multiple cores

#fully independent of eath other i.e. no shared memory

# lack of communication (need for IPC and object pickling )

# Never run a multi-processing example from within an IDE that runs in the same process as the code you are developing.
# Otherwise, the forking step will fork the IDE itself as well as your code.

# Setting the number of processes is a bit of an art. If the code is CPU bound, the number of cores times two is a
# reasonable starting point. If the code is IO bound, the number of cores can be much higher. Experimentation is the key.

import urllib.request
from multiprocessing.pool import ThreadPool as Pool
# from multiprocessing.pool import Pool

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
    'http://www.cnbc.com/',
]

def sitesize(url):
    ''' Determine the size of a website '''
    with urllib.request.urlopen(url) as u:
        page = u.read()
        return url, len(page)



###########################################################################################
# Too many trips back and forth
# If the input iterable to map is very large, it suggests you're making too many trips

# def sitesize(url, start):
#     req = urllib.request.Request(url)
#     req.add_header('Range:%d-%d' % (start, start+1000))
#     u = urllib.request.urlopen(url, req)
#     block = u.read()
#     return url, len(block)


###########################################################################################
# Not doing enough work relative to the travel time
# Once you get to a process, be sure to do enough work to make the trip worthwhile

# def sitesize(url, results):
#     with urllib.request.urlopen(url) as u:
#         while True:
#             line = u.readline()
#             results.put((url, len(line)))


###########################################################################################
# Taking too much with you or bringing too much back

# def sitesize(url):
#     u = urllib.request.urlopen(url)
#     page = u.read()
#     return url, page

pool = Pool(10)
for result in pool.imap_unordered(sitesize, sites):
    print(result)
# single-threaded (No computational concurrency - that is ok because we have the problem of
# GIL anyway)
# but it can do I/O concurrency
# they use non-blocking sockets to acheive I/O concurrency
# epoll/kqueue
# Examples of Python Async Frameworks are Tornado, Asyncio, Twisted
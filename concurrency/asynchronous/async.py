# A style of concurrent programming in which tasks release the CPU during waiting periods, so the other tasks can use it.
# 01. single-threaded (No computational concurrency - that is ok because we have the problem of
# GIL anyway)
# 02. No OS intervention
# but it can do I/O concurrency
# they use non-blocking sockets to acheive I/O concurrency
# epoll/kqueue
# Examples of Python Async Frameworks are Tornado, Asyncio, Twisted
##############################################################################################
# https://gist.github.com/miguelgrinberg/f15bc03471f610cfebeba62438435508
# https://www.youtube.com/watch?v=iG6fr81xHKA&index=3&list=PL3MKc3R0Ff6jmkYQ_BTmAQK0rOO1Y7vKo&t=107s
# https://speakerd.s3.amazonaws.com/presentations/5f2ae4479d8c44ff840d4cbba71d79c9/13h50_-_Miguel_Grinberg_-_Asynchronous_Python_for_the_Complete_Beginner-1crap5avmsmqe.pdf

# Two things are needed
# 1. Async functions need the ability to suspend and resume
#      A function that enters a waiing period is suspended, and only resumed when the wait is over. There are 4 ways
# 2. We need a thing that knows how the CPU is shared and which function takes the CPU next (a scheduler)
#    the scheduler is usually called "event loop" and it keep track of all the running tasks
#    when the func is suspended, return controls to the loop , which then finds another function to start or resume.
#    This is called "cooperative multi-tasking"

##############################################################################################

'''
Long CPU-intensive tasks must routinely release the CPU to avoid starving other tasks. This can be done by “sleeping”
periodically (such as once per loop iteration) for (0) sec.

Asyncio: await asyncio.sleep(0)
Twisted: reactor.callWhenRunning(do_something)
Gevent:  gevent.sleep(0)
Eventlet:eventlet.sleep(0)
'''
'''
Blocking library functions are incompatible with async frameworks:
socket.*, select.*
subprocess.*, os.waitpid
threading.*
time.sleep
'''

# Standard (Synchronous) Python
from time import sleep

def hello():
    sleep(3)
    print('Hello!')

if __name__ == '__main__':
    hello()
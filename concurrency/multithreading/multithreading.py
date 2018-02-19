# what is the difference between
# import thread
# import threading
# In Python 3, thread has been renamed to _thread. It is infrastructure code that is used to implement threading, and
# normal Python code shouldn't be going anywhere near it.

# PROS: threads have a shared state
# CONS: race condition

# Testing cannot prove the absence of errors. It is still useful, don’t rely on it. Many interest racing conditions
# don’t reveal themselves in test environments.

# very important blocks (critical code) of code that needs to be executed in one piece should
# be marked with locks or queues
# The concept of thread safe is simply that the program state (fields/objects/variables) behaves correctly when
# multiple simultaneous threads are using a resource.

import threading

counter = 0

def worker():
    'My job is to increment the counter and print the current count'
    global counter

    counter += 1
    print('The count is %d' % counter)
    print('---------------')

print('Starting up')
for i in range(10):
    # worker()
    threading.Thread(target=worker).start()
print('Finishing up')
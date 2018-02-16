# what is the difference between
# import thread
# import threading
# threads have a shared state
# race condition
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
    threading.Thread(target=worker).start()
print('Finishing up')
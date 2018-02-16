import threading, time, random

##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible

FUZZ = True

def fuzz():
    if FUZZ:
        time.sleep(random.random())

###########################################################################################

counter = 0

def worker():
    'My job is to increment the counter and print the current count'
    global counter

    fuzz()
    oldcnt = counter
    fuzz()
    counter = oldcnt + 1
    fuzz()
    print('The count is %d' % counter, end='')
    fuzz()
    print()
    fuzz()
    print('---------------', end='')
    fuzz()
    print()
    fuzz()

print('Starting up')
fuzz()
for i in range(10):
    threading.Thread(target=worker).start()
    fuzz()
print('Finishing up')
fuzz()
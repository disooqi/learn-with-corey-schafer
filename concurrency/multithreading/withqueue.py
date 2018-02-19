import threading, time, random, queue

##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible

FUZZ = True

def fuzz():
    if FUZZ:
        time.sleep(random.random())

###########################################################################################

counter = 0

counter_queue = queue.Queue()

def counter_manager():
    'I have EXCLUSIVE rights to update the counter variable'
    global counter

    while True:
        increment = counter_queue.get()
        fuzz()
        oldcnt = counter
        fuzz()
        counter = oldcnt + increment
        fuzz()

        fuzz()
        counter_queue.task_done()
        print_queue.put([
            'The count is %d' % counter,
            '---------------'])

t = threading.Thread(target=counter_manager)
t.daemon = True
t.start()
del t

###########################################################################################

print_queue = queue.Queue()

def print_manager():
    'I have EXCLUSIVE rights to call the "print" keyword'
    while True:
        job = print_queue.get()
        fuzz()
        for line in job:
            print(line, end='')
            fuzz()
            print()
            fuzz()
        print_queue.task_done()
        fuzz()

t = threading.Thread(target=print_manager)
t.daemon = True
t.start()
del t

###########################################################################################

def worker():
    'My job is to increment the counter and print the current count'
    counter_queue.put(1)
    fuzz()

print_queue.put(['Starting up'])
fuzz()

worker_threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    worker_threads.append(t)
    t.start()
    fuzz()
for t in worker_threads:
    fuzz()
    t.join()

counter_queue.join()
fuzz()
print_queue.put(['Finishing up'])
fuzz()
print_queue.join()
fuzz()
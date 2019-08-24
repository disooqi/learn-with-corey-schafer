# [book] the pragmatic programmer

# Combining Coroutines with Threads and Processes
# https://pymotw.com/3/asyncio/executors.html
# one core
# http://pybay.com/site_media/slides/raymond2017-keynote/index.html
counter = 0

print('Starting up')
for i in range(10):
    counter += 1
    print('The count is %d' % counter)
    print('---------------')
print('Finishing up')


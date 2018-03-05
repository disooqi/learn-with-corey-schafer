# https://stackoverflow.com/questions/35127520/asyncio-queue-consumer-coroutine
import asyncio
import random

count = 0
async def consume(queue):
    global count
    while True:
        await asyncio.sleep(random.random())
        item = await queue.get()
        oldcnt = count
        await asyncio.sleep(random.random())
        count = oldcnt + item
        await asyncio.sleep(random.random())
        queue.task_done()
        return count

async def worker(queue, i):
    'My job is to increment the counter and print the current count'
    print('worker', i)
    await asyncio.sleep(random.random())
    # put_nowait
    await queue.put(1)
    await asyncio.sleep(random.random())
    # fuzz()


loop = asyncio.get_event_loop()
queue = asyncio.Queue()
# Connection coroutine
# factory = lambda: StreamProtocol(loop, queue)
# connection = loop.create_connection(factory, '127.0.0.1', '42')

tasks = [loop.create_task(worker(queue, i)) for i in range(10)]
# Consumer task
consumer = asyncio.ensure_future(consume(queue))
# Set up connection
# loop.run_until_complete(connection)
# Wait until the connection is closed
# loop.run_forever()
loop.run_until_complete(asyncio.wait(tasks))
# Wait until the queue is empty
# loop.run_until_complete(queue.join())
# Cancel the consumer
consumer.cancel()
# Let the consumer terminate
loop.run_until_complete(consumer)

# Close the loop
loop.close()
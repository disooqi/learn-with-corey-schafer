# Python 3.5+

# https://www.youtube.com/watch?v=iG6fr81xHKA&list=PL3MKc3R0Ff6jmkYQ_BTmAQK0rOO1Y7vKo&index=3&t=1505s
import asyncio
import time
import random
#loop = asyncio.get_event_loop()

# async def hello():
#     print('Hello!')
#     await asyncio.sleep(3)
#     print('diooqi!')
#
#
# if __name__ == '__main__':
#     loop.run_until_complete(hello())


# https://www.youtube.com/watch?v=l4Nn-y9ktd4&list=PL3MKc3R0Ff6jmkYQ_BTmAQK0rOO1Y7vKo&index=19&t=0s
# fuzzing = True
# asyncio_fuzzing = True
# async def fuzz():
#     if fuzzing:
#         if asyncio_fuzzing:
#             asyncio.sleep(random.random())
#         else:
#             time.sleep(random.random())
#
# count = 0
# # not coroutine function
# def increment_over_avariable(itr):
#     fuzz()
#     global count
#     fuzz()
#     tmp = count
#     fuzz()
#     count = tmp + 1
#     fuzz()
#     print(count, time.time())
#     fuzz()
#
# # coroutine function
# async def coroutine_func(itr):
#
#     await asyncio.sleep(random.random())
#     global count
#     try:
#         await asyncio.sleep(random.random())
#         tmp = count
#         await asyncio.sleep(random.random())
#         count = tmp + itr
#     except TypeError:
#         pass
#     await asyncio.sleep(random.random())
#     return count, time.time()
#
# if __name__ == '__main__':
#     t = (1, 1, 'g', 1, 1, 1, 1, 1, 1, 1)
#     loop = asyncio.get_event_loop()
#     #loop.call_later(2, loop.stop)
#     tasks = [loop.create_task(coroutine_func(i)) for i in t]
#         # TypeError: coroutines cannot be used with call_soon() use create_task
#         # loop.call_soon(coroutine_increment_over_avariable, i)
#     atask = loop.create_task(coroutine_func(10))
#
#     try:
#         # for a single task
#         result = loop.run_until_complete(atask)
#         #loop.run_forever()
#         loop.run_until_complete(asyncio.wait(tasks))
#
#         print(result)
#     except TypeError:
#         print('Type error:', result.exception())
#     else:
#         for task in tasks:
#             print(task.result())
#     finally:
#         loop.close()


'''
Generator-based coroutines should be decorated with @asyncio.coroutine, although this is not strictly enforced. The
decorator enables compatibility with async def coroutines, and also serves as documentation. Generator-based coroutines
use the yield from syntax introduced in PEP 380, instead of the original yield syntax.
'''

import asyncio

loop = asyncio.get_event_loop()


@asyncio.coroutine
def hello():
    print('Hello!')
    yield from asyncio.sleep(3)
    print('diooqi!')


if __name__ == '__main__':
    loop.run_until_complete(hello())


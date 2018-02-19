# Python 3.5+
import asyncio

loop = asyncio.get_event_loop()


async def hello():
    print('Hello!')
    await asyncio.sleep(3)
    print('diooqi!')



if __name__ == '__main__':
    loop.run_until_complete(hello())

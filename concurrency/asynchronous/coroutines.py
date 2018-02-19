import asyncio

loop = asyncio.get_event_loop()


@asyncio.coroutine
def hello():
    print(f'Hello')
    yield from asyncio.sleep(3)
    print('diooqi!')


if __name__ == '__main__':
    loop.run_until_complete(hello())

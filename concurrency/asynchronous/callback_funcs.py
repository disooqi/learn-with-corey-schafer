# Miguel Grinberg: Gross
# https://gist.github.com/miguelgrinberg/f15bc03471f610cfebeba62438435508
import asyncio

loop = asyncio.get_event_loop()


def hello():
    loop.call_later(3, print_hello)


def print_hello():
    print('Hello!')
    loop.stop()


if __name__ == '__main__':
    loop.call_soon(hello)
    loop.run_forever()


# with twisted
from twisted.internet import reactor


def hello():
    reactor.callLater(3, print_hello)


def print_hello():
    print('Hello!')
    reactor.stop()


if __name__ == '__main__':
    reactor.callWhenRunning(hello)
    reactor.run()

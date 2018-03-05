# https://gist.github.com/miguelgrinberg/f15bc03471f610cfebeba62438435508
import asyncio

loop = asyncio.get_event_loop()


@asyncio.coroutine
def hello():
    print(f'Hello')
    yield from asyncio.sleep(3)
    print('diooqi!')

#twisted
# from twisted.internet import reactor
# from twisted.internet.defer import inlineCallbacks, Deferred
#
#
# def sleep(secs):
#     d = Deferred()
#     reactor.callLater(secs, d.callback, None)
#     return d
#
# @inlineCallbacks
# def hello():
#     yield sleep(3)
#     print('Hello!')
#     reactor.stop()




if __name__ == '__main__':
    loop.run_until_complete(hello())
    #twisted
    reactor.callWhenRunning(hello)
    reactor.run()

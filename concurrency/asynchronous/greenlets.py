# Makes asynchronous programming transparent
# gevent (pip install gevent)
import gevent

def hello1():
    print('Hello!')
    gevent.sleep(3)
    print('disooqi!')



# eventlet (pip install eventlet)
import eventlet

def hello2():
    print('Hello!')
    eventlet.sleep(3)
    print('disooqi!')

if __name__ == '__main__':
    hello1()
    hello2()
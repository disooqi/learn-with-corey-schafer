# https://stackoverflow.com/questions/3211292/two-processes-reading-writing-to-the-same-file-python
from threading import Thread
import os
import time
import itertools

def write_every_3_sec():

    f = open('2.txt', 'a', os.O_NONBLOCK)
    abc = itertools.cycle('abcdefghijklmnopqrstuvwxyz')

    while True:
        char= abc.__next__()
        f.write(char)
        print('Writing:', char)
        f.flush()
        time.sleep(3)



def read_every_5_sec():
    f = open('2.txt', 'r', os.O_NONBLOCK)
    while True:
        time.sleep(1)
        print('reading byte %s :' % f.tell(), f.read(1))


if __name__ == '__main__':
    Thread(target=write_every_3_sec).start()
    Thread(target=read_every_5_sec).start()
import logging

logger = logging.getLogger(__name__)
fr = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
sh = logging.StreamHandler()
sh.setFormatter(fr)
logger.addHandler(sh)
logger.setLevel(logging.DEBUG)

cache = dict()

def expensive_func(num):
    if num in cache:
        return cache[num]

    logger.info('Computing extremely expensive func with "{}" ...'.format(num))

    result = num**num**num

    cache[num] = result

    return result

if __name__ == '__main__':
    print(expensive_func(7))

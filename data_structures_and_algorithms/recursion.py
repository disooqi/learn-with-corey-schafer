import sys
import resource
sys.setrecursionlimit(1001)
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))


def fibonacci(n):
    """Calculate the value of nth element in fibonacci sequence

    :param n: nth element in fibonacci sequence
    :return: the value of nth element in fibonacci sequence
    """
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


fib = [0, 1]


def fibonacci_with_mem(n):
    global fib
    if n < 0:
        raise ValueError
    if n == 0:
        return fib[0]
    if n == 1:
        return fib[1]

    # I added one because n is index starting from 0
    if len(fib)-1 < n:
        fib.append(fibonacci_with_mem(n - 1) + fibonacci_with_mem(n - 2))

    return fib[n]


def number_of_ways_for_the_frog_to_jump_n_feet(n):
    """number of ways for the frog to jump n feet

    :param n: num of feets
    :return:
    """
    global total
    if n == 0:
        return 1
    if n < 0:
        return 0

    return number_of_ways_for_the_frog_to_jump_n_feet(n - 1) + number_of_ways_for_the_frog_to_jump_n_feet(n - 2)


print(number_of_ways_for_the_frog_to_jump_n_feet(11))
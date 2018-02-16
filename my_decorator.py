# First-class function; treating function like any other object
# Assign func to variable, pass func as argument and return func

# Closure
def outer_func(msg):
    # free variable
    # message = msg
    def inner_func():
        print(msg)
    return inner_func

func = outer_func('Hello disooqi!')
func()

# Decorator
from functools import wraps

def decorator_func_w_parameter(para):
    def decorator_func(original_func):
        # free variable
        # message = msg
        @wraps(original_func)
        def wrapper(*args, **kwargs):
            # Add extra functionality here
            result = original_func(*args, **kwargs)
            # Add extra functionality here
            return result
        return wrapper
    return decorator_func


class Decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        # Add extra functionality here
        result = self.original_func(*args, **kwargs)
        # Add extra functionality here
        return result

# solution = decorator_func(solution([1,2,3,4], 3))
#solution()

@decorator_func_w_parameter('hello')
def solution(A, K):
    n = len(A)
    for i in range(n - 1):
        if not ((A[i] == A[i + 1]) or (A[i + 1] == A[i] + 1)):
            return False
    if (A[0] != 1 or A[n - 1] != K):
        return False
    else:
        return True
print(solution([1,2,3,4], 4))


@Decorator_class
def nothing_func():
    pass

nothing_func()
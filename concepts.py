# Idenpotant

# Closure

def outer_function(tag):
    pass


def add(x, y):
    return x + y


def deco(orig_func):

    def wrapper(*args, **kwargs):
        print("That is to know that I ran the deco func")
        return orig_func(*args, **kwargs)

    return wrapper

add = deco(add)

print(add(3, 5))

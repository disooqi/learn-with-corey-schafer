# https://www.youtube.com/watch?v=6uAvHOKofws

data = [1, 2, 3, 4, 5]
def f(x):
    return x-1

# Case 2
results = [f(x) for x in data if f(x)%2] # instead of
results = [y for x in data if (y := f(x)%2)] # instead of

print(results)
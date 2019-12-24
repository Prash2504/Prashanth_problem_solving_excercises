#! /usr/bin/python
import timeit


def fib(n):
    x, y = 0, 1

    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        for _ in range(2, n+1):
            y, x = x + y, y
        return y


# Brute force mechanisum
def fib_brute_force(n):
    x, y = 0, 1
    for _ in range(0, n):
        y, x = x+y, y
    return x



# Memory optimised code using recursion
def fib_memory_opts(n):
    # When we have recursion tree for f(5), than it would be smaller iterations
    # but, when we have larger number we have more iterations, so its always better
    # to the data into a data structure and check if f(n) already present, we 
    # return the data from list instead of computing, by this we avoid lot of compute

    if f[n] != -1: 
        return f[n]

    f[n] = fib_memory_opts(n-1) + fib_memory_opts(n-2)
    return f[n]

f  = list()
for _ in range(0, 51):
    f.append(-1)
f[0] = 0
f[1] = 1

print(fib_memory_opts(9))
print(timeit.timeit("fib_memory_opts(9)", setup="from __main__ import fib_memory_opts", number=1))


print(fib(9))
print(timeit.timeit("fib(9)", setup="from __main__ import fib", number=1))

# print(fib_brute_force(9))
# print(timeit.timeit("fib_brute_force(9)", setup="from __main__ import fib_brute_force", number=1))




import timeit

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(timeit.timeit('fib(35)', globals=globals(), number=1))

memoized_fib = memoize(fib)
print(timeit.timeit('memoized_fib(35)', globals=globals(), number=1))
print(timeit.timeit('memoized_fib(35)', globals=globals(), number=1))

from timeit import timeit
from functools import cache


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


@cache
def fib_memoise(n):
    if n <= 1:
        return n
    return fib_memoise(n - 1) + fib_memoise(n - 2)


def fib_non_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def timeit_function():
    round_to = 10
    print('First version:', round(timeit('fib(25)', globals=globals(), number=1000), round_to))
    print('Second version:', round(timeit('fib_memoise(25)', globals=globals(), number=1000), round_to))
    print('Third version:', round(timeit('fib_non_recursive(25)', globals=globals(), number=1000), round_to))


if __name__ == '__main__':
    timeit_function()

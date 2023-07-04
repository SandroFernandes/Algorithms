# Improving performance

## Use memoization to show how to improve performance in algorithms 

example: Fibonacci

Exponential time O(c^n)

'''python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
'''

'''python
def fib(n):
    if n <= 1:
        return n
    return memoize(fib(n-1)) + memoize(fib(n-2))
'''


Is there a way to improve this algorithm?

Factorial time O(n!)




# function to return the nth fibonacci number using recursion

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for f in range(0, 11):
    print(fibonacci(f))

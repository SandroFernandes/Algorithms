# recursive function to find factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


for f in range(0, 11):
    print(factorial(f))


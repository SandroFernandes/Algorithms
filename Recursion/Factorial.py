from fractions import Fraction
from math import gamma


def halp_factorial(n):
    return gamma(n + 1)


# recursive function to find factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def double_factorial(n):
    # skips every second number
    if n == 0 or n == 1:
        return 1
    else:
        return n * double_factorial(n - 2)


if __name__ == '__main__':
    print(factorial(5))
    print(double_factorial(9))

    number = 3 / 2
    result = halp_factorial(number)
    print(f"The factorial of {number} is: {result}")

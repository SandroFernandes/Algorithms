# https://en.wikipedia.org/wiki/AKS_primality_test
# does not use random numbers, but it's alluring and powerful
from math import gcd


def aks_primality_test(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Compute r such that r^2 > n
    r = 1
    while r ** 2 < n:
        r += 1

    # Check if n is a perfect square
    if r ** 2 == n:
        return False

    # Check if n is prime using the AKS algorithm
    for a in range(2, r + 1):
        if gcd(a, n) != 1:
            return False
        if pow(a, n - 1, n) != 1:
            return False

    return True


if __name__ == '__main__':
    p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    for v in p:
        print(f'{v:>5,} is prime? ', aks_primality_test(v))

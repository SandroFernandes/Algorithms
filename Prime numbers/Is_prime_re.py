# Check if a number is prime or not using regular expression

import re


def is_prime_re(n):
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) is None


if __name__ == '__main__':
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]:
        print(f'{x} is {"prime " if is_prime_re(x) else "not prime"}')

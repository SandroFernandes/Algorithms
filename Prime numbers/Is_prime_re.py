# Check if a number is prime or not using regular expression

import re


def is_prime_re(n):
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) is None


if __name__ == '__main__':
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]:
        print(f'{x} is {"prime " if is_prime_re(x) else "not prime"}')
"""
The function `is_prime_re(n)` uses a regular expression to check if a number `n` is a prime number.

Here's how it works:

- It takes an integer `n` as input and creates a string of `n` '1's. 

- It then uses the `re.match()` function with the regular expression `r'^1?$|^(11+?)\1+$'`. 

This regular expression uses two patterns separated by a '|', which means "or" in regex:

1. `^1?$`: This matches either an empty string or a string with a single '1'. This would correspond to `n` being 0 or 1, neither of which are prime numbers.

2. `^(11+?)\1+$`: This is a bit more complex. The `(11+?)` matches one or more '11' in the string (but as few as possible due to the '?'). The `\1` is a backreference which matches the same text as most recently matched by the 1st capturing group `(11+?)`. So `(11+?)\1+$` will match if the string of 1's can be expressed as a multiple of a smaller string of 1's, which would mean that `n` is not a prime number.

If `re.match()` doesn't find a match for either of these patterns, then `n` must be a prime number, and the function returns `True`. Otherwise, it returns `False`.

However, note that this is not a practical method for prime number checking. It is more of a curiosity showing a connection between number theory and regular expressions. The function will perform poorly and will fail to work at all for large inputs due to the length of the string '1' * n and limitations of the regex engine. In actual applications, other methods such as trial division or the Sieve of Eratosthenes would be used for prime checking."""

""" This is one of the simplest methods to understand conceptually,
    but it converges to π very slowly, meaning it's not very practical
     for computing π to a high degree of precision. Here is the formula and a Python implementation:
    Formula: π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
"""


def calculate_pi_leibniz(n_terms):
    pi = 0
    for i in range(n_terms):
        term = (-1) ** i / (2 * i + 1)
        pi += term
    pi *= 4
    return pi


if __name__ == '__main__':
    print(calculate_pi_leibniz(1000000))

""" The Nilakantha Series is a little more complex than the Leibniz formula,
    but it converges to π much more quickly:
    Formula: π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + ...
"""


def calculate_pi_nilakantha(n_terms):
    pi = 3
    for i in range(1, n_terms + 1):
        term = 4 / ((2 * i) * (2 * i + 1) * (2 * i + 2))
        if i % 2 == 0:  # Subtract term for even i
            pi -= term
        else:  # Add term for odd i
            pi += term
    return pi


print(calculate_pi_nilakantha(1000000))

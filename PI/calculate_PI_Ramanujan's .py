from mpmath import mp


def compute_pi(digits):
    mp.dps = digits  # set number of decimal places
    pi = mp.mpf(0)  # initialize pi as a multiple precision float
    fact = mp.mpf(1)  # factorial term
    term = mp.mpf(0)  # term in the series
    for k in range(digits):
        fact *= k  # compute factorial
        numerator = mp.mpf(((-1) ** k) * fact * (2 * k + 1))
        denominator = mp.mpf((2 * mp.power(2, k) * mp.power(fact, 2)))
        term = numerator / denominator
        pi += term
    pi = pi * 2 / mp.sqrt(2)
    return pi


if __name__ == '__main__':
    print(compute_pi(10))

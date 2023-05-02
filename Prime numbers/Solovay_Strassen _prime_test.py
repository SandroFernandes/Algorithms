# https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test
import random


def jacobi_symbol(base, number):
    """
    Computes the Jacobi symbol (a/number).
    """
    if number % 2 == 0:
        raise ValueError("number must be odd")
    base %= number
    sign = 1
    while base != 0:
        while base % 2 == 0:
            base //= 2
            if number % 8 == 3 or number % 8 == 5:
                sign = -sign
        base, number = number, base
        if base % 4 == number % 4 == 3:
            sign = -sign
        base %= number
    if number == 1:
        return sign
    else:
        return 0


def solovay_strassen_primality_test(number, num_trials=5):
    """
    Performs the Solovay-Strassen primality test on number.
    Returns True if number is likely to be prime, False otherwise.
    """
    if number == 2 or number == 3:
        return True
    if number <= 1 or number % 2 == 0:
        return False

    for i in range(num_trials):
        witness = random.randint(2, number - 1)
        jacobi_val = jacobi_symbol(witness, number)
        euler_criterion_val = pow(witness, (number - 1) // 2, number)
        if jacobi_val == 0 or euler_criterion_val != jacobi_val % number:
            return False
    return True


if __name__ == '__main__':
    p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    for v in p:
        print(f'{v:>5,} is prime? ', solovay_strassen_primality_test(v))

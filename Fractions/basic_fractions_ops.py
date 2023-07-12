from fractions import Fraction


def add_fractions(fraction1, fraction2):
    """Add two fractions."""
    return fraction1 + fraction2


def subtract_fractions(fraction1, fraction2):
    """Subtract two fractions."""
    return fraction1 - fraction2


def multiply_fractions(fraction1, fraction2):
    return fraction1 * fraction2


def divide_fractions(fraction1, fraction2):
    return fraction1 / fraction2


def power_fractions(fraction1, fraction2):
    return fraction1 ** fraction2


def root_fractions(fraction1, fraction2):
    return fraction1 ** (1 / fraction2)


def reciprocal_fractions(fraction1):
    return 1 / fraction1


if __name__ == '__main__':

    print('Add fractions:', add_fractions(Fraction(1, 2), Fraction(1, 2)))
    print('Subtract fractions:', subtract_fractions(Fraction(1, 2), Fraction(1, 2)))
    print('Multiply fractions:', multiply_fractions(Fraction(1, 2), Fraction(1, 2)))
    print('Divide fractions:', divide_fractions(Fraction(1, 2), Fraction(1, 2)))
    print('Power fractions:', power_fractions(Fraction(1, 2), Fraction(1, 2)))
    print('Root fractions:', root_fractions(Fraction(1, 2), Fraction(1, 2)))
    print('Reciprocal fractions:', reciprocal_fractions(Fraction(1, 2)))

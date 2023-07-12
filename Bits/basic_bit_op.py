# Basic bit operations


def show_binary(n):
    """Print the binary representation of a number."""
    print(f'{n} in binary is {n:08b}')


def bit_add(a, b):
    """Add two bits and return the sum and carry."""
    return a ^ b, a & b


def bit_subtract(a, b):
    """Subtract two bits and return the difference and borrow."""
    return a ^ b, (a ^ 1) & b


def bit_multiply(a, b):
    """Multiply two bits and return the product and carry."""
    return a & b, a | b


def bit_divide(a, b):
    """Divide two bits and return the quotient and remainder."""
    return a ^ b, a & (b ^ 1)


def bit_exponentiation(a, b):
    """Raise a to the power of b and return the result and carry."""
    return a ^ b, a & b


def bit_shift_left(a, b):
    """Shift a left by b bits and return the result and carry."""
    return a << b, a & (1 << b)


def bit_shift_right(a, b):
    """Shift a right by b bits and return the result and carry."""
    return a >> b, a & (1 << b)


def bit_complement(a):
    """Return the complement of a"""
    return a ^ 1


def bit_and(a, b):
    """Return the bitwise and of a and b."""
    return a & b


def bit_or(a, b):
    """Return the bitwise or of a and b."""
    return a | b


def bit_xor(a, b):
    """Return the bitwise xor of a and b."""
    return a ^ b


def bit_not(a):
    """Return the bitwise not of a"""
    return ~a


def bit_rotate_left(a, b):
    """Rotate a left by b bits and return the result and carry."""
    return (a << b) | (a >> (8 - b)), a & (1 << (8 - b))


def bit_rotate_right(a, b):
    """Rotate a right by b bits and return the result and carry."""
    return (a >> b) | (a << (8 - b)), a & (1 << (8 - b))

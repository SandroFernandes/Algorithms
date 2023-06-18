# sum all digits in a number

def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


def sum_digits2(n):
    # iterative version
    return sum(map(int, str(n)))


print(sum_digits(1234))

print(sum_digits2(123456789))

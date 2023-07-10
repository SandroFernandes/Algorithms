# the inf in python
import math


# So infinity is endless, think about it, it is a number, but it is endless
# to infinity you can add 1, and it will still be infinity
# you can multiply it by 2, and it will still be infinity
# you can divide it by 2, and it will still be infinity
# logical operations with infinity
# is bigger than any number
# infinity is equal to infinity, and this one mathematically is not true because there are different types of infinity
# example map the numbers from 0 to 1 to the numbers from 0 to 2, and you will see that there are more numbers in the
# interval from 0 to 1 than in the interval from 0 to 2


inf = float('inf')

print(f'Infinity is endless, think about it, it is am idea, but it is endless...{inf}')
print(f'Infinity is the idea that you can always add 1 to a number and it will never end')
print(f'To infinity you can add 1, and it will still be infinity: {inf + 1}')
print(f'You can multiply it by 2, and it will still be infinity: {inf * 2}')
print(f'You can divide it by 2, and it will still be infinity: {inf / 2}')
print('-' * 80)
print(f'Logical operations with infinity')
print(f'Infinity is bigger than any number inf > 10000000: {inf > 100000000}')
print(f'Infinity is equal to infinity: {inf == inf}')
print('The IEEE 754 standard specifies that positive infinity should be equal to itself.'
      'Therefore, in programming languages that follow this standard, including Python, inf == inf returns True.')
print(f'This one mathematically is not true because there are different types of infinity')
# when float('inf') specify the type of infinity like set of real numbers, or set of natural numbers
# this creates  different types of infinity

print(f'in')

print(inf == inf)
print(inf + 1 == inf)
print(inf + 1 == inf + 2)
print(inf - 1 == inf)

print(inf + inf == inf)
print(inf * inf == inf)
print(inf / inf == inf)
try:
    print(inf / 0)
except ZeroDivisionError:
    print('inf / 0 is not defined')

print(inf * 0)
print(math.sqrt(inf))
print(math.log(inf))
print(math.exp(-inf))
print(math.exp(inf))

print(inf + 1e308)

print(max([1, inf]))
print(min([-1, -inf]))
print(-inf + (-inf))
print(-inf - (-inf))
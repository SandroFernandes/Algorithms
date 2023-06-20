# constant time O(1) algorithms, just some examples


def access_element(array, index):
    # no mater how big the array is, it will always take the same time to access an element
    return array[index]


def add_elements(array, element):
    # no mater how big the array is, it will always take the same time to add all elements
    return array.append(element)


def is_even(number):
    # no mater how big the number is, it will always take the same time to check if it is even
    return number % 2 == 0


def is_odd(number):
    # no mater how big the number is, it will always take the same time to check if it is odd
    return number % 2 != 0


def add(a, b):
    # if a and be are simple numbers, it will always take the same time to add them
    return a + b


def subtract(a, b):
    # if a and be are simple numbers, it will always take the same time to add them
    return a - b


def multiply(a, b):
    # if a and be are simple numbers, it will always take the same time to add them
    return a * b


def divide(a, b):
    # if a and be are simple numbers, it will always take the same time to add them
    return a / b


def change_variable_value(value):
    # it will always take the same time to change the value of a variable
    a = value
    return a


def insert_key_value(dictionary, key, value):
    # it will always take the same time to insert a key value pair in a dictionary
    dictionary[key] = value
    return dictionary

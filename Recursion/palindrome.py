# palindrome checker using recursion

def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and is_palindrome(string[1:-1])


def is_palindrome2(string):
    # a must shorter and iterative way to check palindrome
    return string == string[::-1]


print(is_palindrome('racecar'))

print(is_palindrome2('racecar'))

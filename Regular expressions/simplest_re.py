# A very simple regular expression engine

def match_char(pattern, text):
    if not text:
        return False
    if not pattern:
        return False
    if pattern == '.':
        return True
    return pattern == text


def match(pattern, text):
    # If the pattern is empty, return True
    if not pattern:
        return True
    # If the second char in the pattern is '*', then check the rest of the string
    if len(pattern) >= 2 and pattern[1] == '*':
        # First, check for zero occurrences (skip the current character)
        if match(pattern[2:], text):
            return True
        # Then, check if the first character matches
        # If so, check the rest of the string (without skipping the current character)
        if match_char(pattern[0], text[0]) and match(pattern, text[1:]):
            return True
        return False
    # If the first character matches, continue with the rest of the pattern and the string
    elif match_char(pattern[0], text[0]) and match(pattern[1:], text[1:]):
        return True
    # If nothing else matches, return False
    return False


if __name__ == '__main__':
    match_list = [
        ("a", "a"),
        ("a", "b"),
        ("a*", "aaaa"),
        (".*", "Hello, World!"),
        ("H.*d", "Hello, World!")
    ]
    for pattern, text in match_list:
        print(f'pattern: {pattern}, text: {text}, match: {match(pattern, text)}')

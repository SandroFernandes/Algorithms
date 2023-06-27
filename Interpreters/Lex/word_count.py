import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'WORD',
)

# A string containing ignored characters (spaces and tabs)
t_ignore = '\t.,?!;:'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_space(t):
    r'\s+'
    t.lexer.space_count = t.lexer.space_count + len(t.value)
    pass


def t_WORD(t):
    r'\b\w+\b'
    t.value = t.value.lower()
    t.lexer.word_count = t.lexer.word_count + 1
    t.lexer.char_count = t.lexer.char_count + len(t.value)
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.'''

# Give the lexer some input
lexer.input(data)
lexer.word_count = 0
lexer.char_count = 0
lexer.space_count = 0

# Tokenize and count
word_counts = {}

# Tokenize
for tok in lexer:
    # If the word is already a key in the dictionary, increment its value
    if tok.value in word_counts:
        word_counts[tok.value] += 1
    # If the word is not a key in the dictionary, add it with a value of 1
    else:
        word_counts[tok.value] = 1

print(f'Word count:{word_counts}')
print(f'Number of lines:{lexer.lineno}')
print(f'Total words:{lexer.word_count}')
print(f'Total characters:{lexer.char_count}')
print(f'Total spaces:{lexer.space_count}')

import ply.lex as lex
import math

# Define the token names
tokens = [
    'NUMBER',
    'POWER',
    'MULTIPLY',
    'DIVIDE',
    'PLUS',
    'MINUS',
    'LPAREN',
    'RPAREN',
    'SQRT',
    'LOG',
    'LN',
]

# Define the regular expressions for each token
t_POWER = r'\^'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_PLUS = r'\+'
t_MINUS = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t\n\r'  # Ignore spaces, tabs, line feeds, and newlines

# Function names
function_names = {
    'sqrt': math.sqrt,
    'log': math.log10,
    'ln': math.log,
    'sin': math.sin,
}


# Define a rule to handle numbers
def t_NUMBER(t):
    r'[+-]?\d+(\.\d+)?([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t


# Define a rule to handle functions
def t_FUNCTION(t):
    r'sqrt|log|ln'
    t.type = t.value.upper()
    return t


# Error handling rule
def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test the lexer
expression = "sqrt(16) + log(100) - ln(1) + 100 - 10^2 * -5 / 5 + 2^3^2 +sin(0)"
lexer.input(expression)

# Print the tokens
while True:
    token = lexer.token()
    if not token:
        break
    print(token)

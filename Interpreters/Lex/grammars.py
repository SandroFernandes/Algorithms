import ply.lex as lex
import ply.yacc as yacc

# token names
tokens = ['ARTICLE', 'NOUN', 'ADJECTIVE', 'VERB', 'ADVERB', 'PREPOSITION']


# token definitions
def t_ARTICLE(t):
    r'\b(a|an|the)\b'
    return t


def t_NOUN(t):
    r'\b(cat|dog|man|woman|boy|girl)\b'
    return t


def t_ADJECTIVE(t):
    r'\b(lazy|happy|sad|tall|short|fat|thin)\b'
    return t


def t_VERB(t):
    r'\b(is|was|jumped|ran|walked|talked|ate|slept|saw|loved|hated|eat)\b'  # I've added 'eat'
    return t


def t_ADVERB(t):
    r'\b(slowly|quickly|well|badly|loudly|quietly|suddenly|never|always)\b'
    return t


def t_PREPOSITION(t):
    r'\b(to|from|over|under|on|in|with|without|about|into|onto|of|for|by|at|after|before|during|against|among|around|behind|below|beneath|beside|between|beyond|despite|except|inside|near|off|since|through|throughout|toward|towards|upon|within|without)\b'
    return t


# Ignore spaces
t_ignore = ' \t'


# Error handling
def t_error(t):
    print("Invalid sentence")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


# Parser rules
def p_sentence(p):
    '''sentence : noun_phrase verb_phrase'''
    p[0] = p[1:]


def p_noun_phrase(p):
    '''noun_phrase : ARTICLE NOUN
                   | ARTICLE ADJECTIVE NOUN'''
    p[0] = p[1:]


def p_verb_phrase(p):
    '''verb_phrase : VERB
                   | VERB noun_phrase
                   | VERB ADVERB noun_phrase
                   | VERB PREPOSITION noun_phrase'''
    p[0] = p[1:]


# Error rule for syntax errors
def p_error(p):
    if p:
        print("Invalid sentence")
    else:
        print("Valid sentence")


# Build the parser
parser = yacc.yacc()

# Test the parser
while True:
    try:
        s = input('Enter a sentence: ')
        if s == 'exit':
            break

    except EOFError:
        break
    result = parser.parse(s)

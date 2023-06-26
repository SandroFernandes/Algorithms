# simple lexer for sentences
# this lexer is not complete, it is just an example of how to use ply.lex
# to tokenize a sentence
# the order is not considered, so the sentence "the cat is lazy" will be tokenized,
# as well as "lazy cat is the" or "is the cat lazy"

import ply.lex as lex

# List of token names
tokens = (
    'VERB',
    'ADVERB',
    'PREPOSITION',
    'ARTICLE',
    'NOUN',
    'ADJECTIVE',
    'OTHER',
)

verbs = ['ask', 'be', 'begin', 'call', 'can', 'come', 'do', 'feel', 'find', 'get',
         'give', 'go', 'have', 'is', 'jump', 'keep', 'know', 'leave', 'let', 'make', 'provide',
         'say', 'see', 'seem', 'show', 'take', 'tell', 'think', 'try', 'use', 'want', 'work']

adverbs = [
    'up',
    'so',
    'out',
    'just',
    'now',
    'how',
    'then',
    'more',
    'also',
    'here',
    'well',
    'only',
    'very',
    'even',
    'back',
    'there',
    'down',
    'still',
    'in',
    'as',
    'too',
    'when',
    'never',
    'really',
    'most',
]

prepositions = [
    'of',
    'in',
    'to',
    'for',
    'with',
    'on',
    'at',
    'from',
    'by',
    'about',
    'as',
    'into',
    'like',
    'through',
    'after',
    'over',
    'between',
    'out',
    'against',
    'during',
    'without',
    'before',
    'under',
    'around',
    'among',
]

articles = [
    'a',
    'an',
    'the',
]

nouns = [
    'cat',
    'dog',
]

adjectives = [
    'good',
    'new',
    'first',
    'last',
    'long',
    'lazy',
    'little',
    'own',
    'other',
]


# Regular expression rule for word
def t_WORD(t):
    r'\b[A-Za-z]+\b'  # Matches any word consisting of alphabetical characters
    match t.value:
        case t.value if t.value in verbs:
            t.type = 'VERB'
        case t.value if t.value in adverbs:
            t.type = 'ADVERB'
        case t.value if t.value in prepositions:
            t.type = 'PREPOSITION'
        case t.value if t.value in articles:
            t.type = 'ARTICLE'
        case t.value if t.value in nouns:
            t.type = 'NOUN'
        case t.value if t.value in adjectives:
            t.type = 'ADJECTIVE'
        case _:
            t.type = 'OTHER'
    return t


# Ignored characters (spaces and punctuation)
t_ignore = ' \t,.?!;:'


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

while True:
    print()
    print("Type 'exit' to exit")
    data = input("Write a sentence: ")

    if data == "exit":
        break

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input

        print(f'token:{tok.type} -> {tok.value}')

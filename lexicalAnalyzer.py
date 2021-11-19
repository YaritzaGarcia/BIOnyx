import ply.lex as lex
import re

# BIOnyx Tokens
# This is a list with all the token names of BIOnyx

# F_INVOCATION =
tokens = [
    'STRING',
    'FINISHER',
    'FINVOCATION',
    'LBRACKET',
    'RBRACKET',
    'QMARKS',
    'COMMA',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE'
]

# BIOnyx Reserved Words
reserved = {
    'infoId': 'INFOID',
    'model': 'MODEL',
    'getFile': 'GETFILE'
}

tokens = tokens + list(reserved.values())

# BIOnyx Regular expressions
t_FINISHER = r'\;'
t_FINVOCATION = r'\->'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_QMARKS = r'\"'
t_COMMA = r'\,'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# Rule for turn string into numbers


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# # Defining rules for reserved words

def t_STRING(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'

    # Verifying if the string is a reserve word
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# Define a rule to track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Define a rule for error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the BIOnyx lexer
lexer = lex.lex()

# Test it out
data = '''
infoId -> "holi", ["wiii"]
3+4,
"3+4"
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

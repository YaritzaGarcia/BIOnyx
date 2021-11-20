import ply.lex as lex

# BIOnyx Tokens
# This is a list with all the token names of BIOnyx

tokens = [
    'STRING',
    'FINISHER',
    'FINVOCATION',
    'COMMA',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ID'
]

# BIOnyx Reserved Words
reserved = {
    'infoID': 'INFOID',
    'model': 'MODEL',
    'getFile': 'GETFILE',
    'getPolypeptides': 'GETPOLYPEPTIDES',
    'getAminoAcidsInfo' : 'GETAMINOACIDSINFO'
}

tokens = tokens + list(reserved.values())

# BIOnyx Regular expressions
t_FINISHER = r'\;'
t_FINVOCATION = r'\->'
t_COMMA = r'\,'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# Rule for turn string into numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'(\"([^"]*)\")'
    t.value = t.value[1:-1]

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


# Build the lexer
lexer = lex.lex()


def codeFile(file):
    # read the code in the file
    file = open(file, "r")
    lines = file.read()
    file.close()
    return(lines)

lexer.input(codeFile("BIOnyxCode.bx"))

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    # print(tok)
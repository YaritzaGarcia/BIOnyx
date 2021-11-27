import ply.yacc as yacc
from lexicalAnalyzer import tokens
from utilities import getPolypeptides, model, infoID, getFile, getAminoAcidsInfo

def p_expression_infoID(p):
    # infoID -> "1atp", ["name", "sequence", "aminoAcids"];"
    'expression : INFOID FINVOCATION STRING FINISHER'
    print(infoID(p[3]))

def p_expression_model(p):
    # model -> "1atp";
    'expression : MODEL FINVOCATION STRING FINISHER'
    return(model(p[4]))

def p_expression_getFile(p):
    # getFile -> "1atp", "C:\Users\User\Desktop";
    'expression : GETFILE FINVOCATION STRING COMMA STRING FINISHER'
    print(getFile(p[3], p[5]))

def p_expression_getPolypeptides(p):
    # getPolypeptides -> "1atp";
    'expression : GETPOLYPEPTIDES FINVOCATION STRING FINISHER'
    getPolypeptides(p[3])

def p_expression_getAminoAcidsInfo(p):
    # getPolypeptides -> "1atp";
    'expression : GETAMINOACIDSINFO FINVOCATION STRING FINISHER'
    getAminoAcidsInfo(p[3])

def p_expression_plus(p):
    'expression : NUMBER PLUS NUMBER'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : NUMBER MINUS NUMBER'
    p[0] = p[1] - p[3]

def p_expression_times(p):
    'expression : NUMBER TIMES NUMBER'
    p[0] = p[1] * p[3]

def p_expression_divide(p):
    'expression : NUMBER DIVIDE NUMBER'
    p[0] = p[1] / p[3]

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

print('''Welcome to BIOnyx! 
Click here https://github.com/YaritzaGarcia/BIOnyx to learn more about us.''')
while True:
    try:
        s = input('BIOnyx > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    if result != None:
        print(result)
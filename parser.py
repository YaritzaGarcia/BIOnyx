import ply.yacc as yacc
from lexicalAnalyzer import tokens
from utilities import model, infoID, getFile

def p_expression_infoID(p):
    # infoID -> "1atp", ["name", "sequence", "aminoAcids"];"
    'expression : INFOID FINVOCATION STRING COMMA LBRACKET RBRACKET FINISHER'
    print(infoID(p[4]))

def p_expression_model(p):
    # model -> "1atp";
    'expression : MODEL FINVOCATION STRING FINISHER'
    return(model(p[4]))

def p_expression_getfile(p):
    # getFile -> "1atp", "C:\Users\User\Desktop";
    'expression : GETFILE FINVOCATION STRING COMMA STRING FINISHER'
    getFile(p[3], p[5])

def p_expression_plus(p):
    'expression : NUMBER PLUS NUMBER'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : NUMBER MINUS NUMBER'
    p[0] = p[1] - p[3]

def p_expression_times(p):
    'expression : NUMBER TIMES NUMBER'
    p[0] = p[1] + p[3]

def p_expression_divide(p):
    'expression : NUMBER DIVIDE NUMBER'
    p[0] = p[1] + p[3]

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
   if not s: continue
   result = parser.parse(s)
   print(result)
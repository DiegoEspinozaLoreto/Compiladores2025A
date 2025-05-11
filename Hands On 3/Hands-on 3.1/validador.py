import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

def p_expr_binop(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr'''
    pass

def p_expr_uminus(p):
    'expr : MINUS expr %prec UMINUS'
    pass

def p_expr_group(p):
    'expr : LPAREN expr RPAREN'
    pass

def p_expr_number(p):
    'expr : NUMBER'
    pass

def p_error(p):
    raise SyntaxError("Expresión inválida")

parser = yacc.yacc()

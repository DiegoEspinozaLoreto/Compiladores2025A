import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', 'AND', 'OR'),
    ('right', 'NOT'),
)

def p_expr_binop(p):
    '''expr : expr AND term
            | expr OR term'''
    pass

def p_expr_term(p):
    'expr : term'
    pass

def p_term_not(p):
    'term : NOT factor'
    pass

def p_term_factor(p):
    'term : factor'
    pass

def p_factor_group(p):
    'factor : LPAREN expr RPAREN'
    pass

def p_factor_boolean(p):
    'factor : BOOLEAN'
    pass

def p_error(p):
    raise SyntaxError("Expresión inválida")

parser = yacc.yacc()

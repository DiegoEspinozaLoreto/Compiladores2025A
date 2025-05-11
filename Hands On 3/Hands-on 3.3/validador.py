import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_expr_binop(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr'''
    p[0] = (p[2], p[1], p[3])  # (operador, operando1, operando2)

def p_expr_logical(p):
    '''expr : expr AND expr
            | expr OR expr'''
    p[0] = (p[2], p[1], p[3])  # (operador, operando1, operando2)

def p_expr_not(p):
    'expr : NOT expr'
    p[0] = ('NOT', p[2])  # (operador, operando)

def p_expr_group(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]  # El valor es la expresión dentro de los paréntesis

def p_expr_number(p):
    'expr : NUMBER'
    p[0] = p[1]  # El valor es el número, válido en lógicas y aritméticas

def p_expr_bool(p):
    'expr : BOOL'
    p[0] = p[1]  # El valor es el booleano (TRUE/FALSE)

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' en la línea {p.lineno}")
    else:
        print("Error de sintaxis: entrada incompleta o inválida")
    raise SyntaxError("Expresión inválida")

parser = yacc.yacc()
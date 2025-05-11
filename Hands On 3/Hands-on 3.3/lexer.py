import ply.lex as lex

tokens = (
    'NUMBER',
    'AND',
    'OR',
    'NOT',
    'BOOL',
    'LPAREN',
    'RPAREN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
)

t_ignore = ' \t'

t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_BOOL = r'TRUE|FALSE'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
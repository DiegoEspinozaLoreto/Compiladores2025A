import ply.lex as lex

tokens = (
    'BOOLEAN',
    'AND',
    'OR',
    'NOT',
    'LPAREN',
    'RPAREN',
)

t_ignore = ' \t'

t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_BOOLEAN(t):
    r'0|1'
    t.value = bool(int(t.value))
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

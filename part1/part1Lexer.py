import ply.lex as lex

# Token list
tokens = [
    'ID', 'INT', 'FLOAT',
    'PLUS', 'MINUS', 'MULT', 'DIV',
    'EQ', 'ASSIGN', 'LT',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMI',
    'INTTYPE', 'FLOATTYPE',
    'IF', 'ELSE', 'FOR'
]

# Regex rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULT    = r'\*'
t_DIV     = r'/'
t_EQ      = r'=='
t_ASSIGN  = r'='
t_LT      = r'<'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMI    = r';'

# Reserved words mapping
reserved = {
    'int': 'INTTYPE',
    'float': 'FLOATTYPE',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR'
}

# Floating point numbers
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Integers
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identifiers and keywords
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Ignore whitespace and tabs
t_ignore = ' \t\r\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

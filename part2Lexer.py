import ply.lex as lex

# Todo: Add all the tokens here
tokens = [
    'PLUS', 'ID', 'SEMI',
    'NUM',
    'MULT',
    'DIV',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'ASSIGN',
    'IF',
    'ELSE',
    'INT',
    'FLOAT',
    'EQ',
    'LT',
    'FLOATTYPE',
    'FOR',
    'MINUS',
]

keywords = {
        "if": 'IF',
        "else": 'ELSE',
        "int": 'INT',
        "float": 'FLOATTYPE',
        "for": 'FOR',
    }

# Todo: Add all the requied regular expression rules here
t_SEMI = r';'
t_PLUS = r'\+'
t_MULT = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'='
t_EQ = r'=='
t_LT = r'<'

t_ignore = ' \t\r\n'  # Ignore spaces and tabs

# Todo: Write all the required regular expression rule with action code
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID') 
    return t

def t_FLOAT(t): 
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t



# Todo: Fix the error function 
def t_error(t):
    print(f"Illegal character")

# Build the lexer
lexer = lex.lex()


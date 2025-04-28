import argparse
import ply.yacc as yacc
from part1Lexer import lexer, tokens

def p_program(p):
    'program : statement_list'

def p_statement_list(p):
    '''statement_list : statement statement_list
                      | '''

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | if_stmt
                 | for_stmt
                 | block'''

def p_declaration(p):
    '''declaration : INTTYPE ID SEMI
                   | FLOATTYPE ID SEMI'''

def p_assignment(p):
    'assignment : ID ASSIGN expression SEMI'

def p_assignment_no_semi(p):
    'assignment_no_semi : ID ASSIGN expression'

def p_if_stmt(p):
    'if_stmt : IF LPAREN expression RPAREN statement ELSE statement'

def p_for_stmt(p):
    'for_stmt : FOR LPAREN assignment expression SEMI assignment_no_semi RPAREN statement'

def p_block(p):
    'block : LBRACE statement_list RBRACE'

# Expression grammar encoded with precedence by hierarchy
def p_expression_eq(p):
    'expression : expression EQ relation'

def p_expression_rel(p):
    'expression : relation'

def p_relation_lt(p):
    'relation : relation LT term'

def p_relation_term(p):
    'relation : term'

def p_term_add(p):
    'term : term PLUS factor'

def p_term_sub(p):
    'term : term MINUS factor'

def p_term_factor(p):
    'term : factor'

def p_factor_mult(p):
    'factor : factor MULT unit'

def p_factor_div(p):
    'factor : factor DIV unit'

def p_factor_unit(p):
    'factor : unit'

def p_unit_group(p):
    'unit : LPAREN expression RPAREN'

def p_unit_id(p):
    'unit : ID'

def p_unit_int(p):
    'unit : INT'

def p_unit_float(p):
    'unit : FLOAT'

def p_error(p):
    if p:
        print(f"Syntax error at {p.value}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file_name', type=str, help="Input file containing the text to parse.")
    args = arg_parser.parse_args()

    try:
        with open(args.file_name, 'r') as file:
            f_contents = file.read()
    except FileNotFoundError:
        print(f"Error: File '{args.file_name}' not found.")
        exit()

    try:
        result = parser.parse(f_contents, lexer=lexer)
        if result is None:
            print("Input matches the grammar.")
        else:
            print("Input does not match the grammar.")
    except Exception as e:
        print(f"Error during parsing: {e}")

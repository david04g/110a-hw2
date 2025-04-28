import argparse
import ply.yacc as yacc

# Importing tokens map from part1Lexer
from part2Lexer import lexer, tokens

# Todo: Define all the required grammar and actions
def p_program(p):
    'program : statement_list'

def p_statement_list(p):
    '''statement_list : statement statement_list
                      | '''

def p_statement(p):
    '''statement : variables
                  | assignment
                  | if_statement
                  | for_statement
                  | block'''
    

def p_variables(p):
    '''variables : INT ID SEMI
                  | FLOATTYPE ID SEMI'''

def p_assignment(p):
    'assignment : ID ASSIGN expression SEMI'

def p_if_statement(p):
    'if_statement : IF LPAREN expression RPAREN statement ELSE statement'

def p_for_statement(p):
    'for_statement : FOR LPAREN assignment expression SEMI ID ASSIGN expression RPAREN statement'

def p_block(p):
    'block : LBRACE statement_list RBRACE'

def p_expression(p):
    'expression : equality'

def p_equality(p):
    'equality : less_than equality_tail'

def p_equality_tail(p):
    '''equality_tail : EQ less_than equality_tail
                    | '''

def p_less_than(p):
    '''less_than : addition less_than_tail'''

def p_less_than_tail(p):
    '''less_than_tail : LT addition less_than_tail
                    | '''



def p_addition(p):
    '''addition : multiplication addition_tail'''

def p_addition_tail(p):
    '''addition_tail : PLUS multiplication addition_tail
                     | MINUS multiplication addition_tail
                     | '''

def p_multiplication(p):
    '''multiplication : term multiplication_tail'''

def p_multiplication_tail(p):
    '''multiplication_tail : MULT term multiplication_tail
                           | DIV term multiplication_tail
                           | '''
                           
def p_term(p):
    '''term : LPAREN expression RPAREN
            | ID
            | NUM
            | FLOAT'''

def p_error(p):
    if p:
        print(f"Syntax error at {p.value}")
    else:
        print("Syntax error at EOF")

def test_parser(input_string):
    result = parser.parse(input_string, lexer=lexer)
    if result is None:
        print("Input matches the grammar.")
    else:
        print("Input does not match the grammar.")

# Build the parser
ply_parser = yacc.yacc(debug=True)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file_name', type=str, help="Input file containing the text to parse.")
    args = arg_parser.parse_args()
    
    try:
        with open(args.file_name, 'r') as file:
            f_contents = file.read()
            #print("File contents read successfully:")
            #print(f_contents)
    except FileNotFoundError:
        print(f"Error: File '{args.file_name}' not found.")
        exit()

    try:
        result = ply_parser.parse(f_contents, lexer=lexer)
        if result is None:
            print("Input matches the grammar.")
        else:
            print("Input does not match the grammar.")
    except Exception as e:
        print(f"Error during parsing: {e}")


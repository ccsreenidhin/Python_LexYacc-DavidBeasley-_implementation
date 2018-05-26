# -----------------------------------------------------------------------------
# File          :parser.py
#
# Author        :Sreenidhin C C.
# Date          :6-June-2018.
# Description   :Dynamic  Binder Implementation using python PLY package
#                (Parser using PLY)
# -----------------------------------------------------------------------------

#       -------------------------- Imports  ---------------------------

import ply.yacc as yacc

from .lexer import tokens


#       ------------------------ Grammer Rules  -----------------------

def p_statement(p):
    '''statement : statement_if
                | expression
                | return
    '''
    p[0] = p[1]


def p_expression(p):
    '''expression : expression_bracket
                  | expression_bin
                  | expression_uni
                  | term
    '''
    p[0] = p[1]


def p_expression_bin(p):
    '''expression_bin : expression IN term
                  | expression EQUAL term
                  | expression GREATER term
                  | expression LESSER term
                  | expression AND term
                  | expression OR term
    '''
    if p[2]=='in':
        p[0] = 1 if p[1] in p[3] else 0
    elif p[2] == '==':
        p[0] = 1 if p[1] == p[3] else 0
    elif p[2] == '>':
        p[0] = 1 if p[1] > p[3] else 0
    elif p[2] == '<':
        p[0] = 1 if p[1] < p[3] else 0
    elif p[2] == 'and':
        p[0] = 1 if p[1] and p[3] else 0
    elif p[2] == 'or':
        p[0] = 1 if p[1] or p[3] else 0


def p_expression_uni(p):
    '''expression_uni : NOT term
    '''
    if p[1] == 'not':
        p[0] = not p[2]
    elif p[1] == 'return':
        p[0] = p[2]


def p_expression_bracket(p):
    '''expression_bracket : LPAREN expression RPAREN
    '''
    p[0] = p[2]


def p_return(p):
    '''return : RETURN expression
    '''
    p[0] = p[2]


def p_term(p):
    '''term : factor
    '''    
    p[0] = p[1]


def p_factor(p):
    '''factor : VARIABLE
              | NUMBER
              | STRING
    '''
    p[0] = p[1]

def p_statement_if(p):
    '''statement_if : IF expression statement ELSE statement
    '''
    if p[2] == 1:
      p[0] = p[3]
    else:
      p[0] = p[5]


def p_error(p):
    print("Syntax error in input!")



#      -------------------Function to build Parser  ------------------

def build_parser():
    return yacc.yacc()


#      ------------------------------ End  -----------------------------

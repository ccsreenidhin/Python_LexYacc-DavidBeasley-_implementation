# -----------------------------------------------------------------------------
# File          :lexer.py
#
# Author        :Sreenidhin C C.
# Date          :6-June-2018.
# Description   :Dynamic  Binder Implementation using python PLY package
#                (Lexer using PLY)
# -----------------------------------------------------------------------------

#       -------------------------- Imports  ---------------------------

import ply.lex as lex
from data import *


#       ----------------------- List of tokens  -----------------------

tokens = [
   'VARIABLE',
   'NUMBER',
   'STRING',
   'GREATER',
   'LESSER',
   'LPAREN',
   'RPAREN',
   'ID',
   'SEMICOLON',
   'EQUAL',
]

reserved={
    'else' : 'ELSE',
    'if' : 'IF',
    'return' : 'RETURN',
    'in' : 'IN',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',
}

tokens += reserved.values()


#   ----------------- Regular expressions for tokens  -----------------

t_ELSE = r'else'
t_EQUAL = r'=='
t_GREATER = r'>'
t_LESSER   = r'<'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SEMICOLON = r';'
t_RETURN = r'return'
t_IF = r'if'
t_AND = r'and'
t_OR = r'or'
t_NOT = r'not'
t_IN = r'in'


literals = ['+','-','*','/' ]

#ignored characters (spaces and tabs)
t_ignore  = ' \t'


#   ----------- Regular expression with actions for tokens  -----------

def t_STRING(t):
    r'[\'|\"][a-zA-Z0-9_]*[\'|\"]'
    try:
         t.value = t.value[1:-1]
    except ValueError:
         print("Line {}: String {} is not valid!" .format(t.lineno, t.value))
         t.value = ""
    return t


def t_NUMBER(t) :
    r'\d+'
    try:
         t.value = int(t.value)
    except ValueError:
         print("Line {}: Number {} is too large!" .format(t.lineno, t.value))
         t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t


def t_VARIABLE(t):
  r'@[a-zA-Z0-9_\[\]\.]*'
  
  li=None
  dat = data
  temp = t.value[1::]
  if temp[-1]=="]":
    li = temp[-3:]
    temp = temp[:-3]
  temp = temp.split('.')

  if li:
    i=int(li[1])
    temp.append(i)
  for i in temp:
    if isinstance(dat, dict) and i in dat:
        dat = dat[i]
    elif isinstance(dat, (list, tuple)) and isinstance(i, int):
        try:
            dat = dat[i]
            dat = next(iter(dat.values()))
            dat = int(dat)
        except:
            dat = dat[i]
  try:
    t.value = dat
  except:
    print("Line {}: Number {} is too large!".format(t.lineno,t.value))
    t.value = 0
  return t



def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
  print ("Illegal character {}" .format(t.value[0]))
  t.lexer.skip(1)


lex.lex()

#       -------------------------- End  ---------------------------

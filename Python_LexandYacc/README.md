# The Dynamic Binder

A parser to parse the basic instructions AND, OR, NOT, ==, <, >, if, else and in built in python 3.6 using PLY(Python Lex-Yacc)- (http://www.dabeaz.com/ply/).

This parser was built to parse the following inputs as part of a programming challenge.

## INPUTS
operation_a = "
	if (@a > @b) return 1
	else if (@a < @b) return 2
	else return 3"

operation_b = "
	if (@name == 'test') return 1
	else return 2"

operation_c = "
	if (@name in @list) return 1
	else return 2"
	
*@key is any variable.

The value of variables are given as dictionary(given bllow)

## Dictionary(data)

data = {
	"a": "5",
	"b": "6",
	"name": "test",
	"value": "a",
	"list": ["a", "b", "c"]
}


## Running on your machine
Simply run: `pip install -r requirements.txt`
run: main.py

The main.py is used for parsing the operations described in data.py file.



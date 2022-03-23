grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
	

//Main Program
program 		: (var_declare | func_declare)+ EOF;

//Function, Variable, Parameter Declaration
var_declare 	: TYPE id_list SM
				;
func_declare 	: TYPE ID param_declare body
				;
param_declare 	: LRB (param_list (SM param_list)*)? RRB
				;
body			: LCB (var_declare |stm_declare)+ RCB
				;
//Statement Declaration
stm_declare		: (assign_stm | call_stm | retrn_stm) SM;

assign_stm	: ID EQ expr; 
call_stm	: ID LRB exp_list RRB;
retrn_stm	: RETURN expr;

//Expression Declaration
expr		: expr1 (ADDOP) expr 	| expr1;
expr1		: expr2 (SUBOP) expr2 	| expr2;
expr2		: expr2	(MULOP | DIVOP) sub_expr | sub_expr;
sub_expr	: LCB expr RCB 
			| INTLIT
			| FLOATLIT 
			| ID 
			| call_stm 
			;

//Expression Declaration

//Sub Parser rule

id_list		: ID (CM ID)*;
param_list 	: TYPE id_list;
exp_list	: expr (CM expr)*;
//Lexer

TYPE: 'int'|'float' 
	; 
RETURN	: 'return'
	;
ID	: [a-zA-Z]+
	;
INTLIT: [0-9]+
	;
FLOATLIT: INTLIT '.' INTLIT
	;
ADDOP	: '+'
	;
SUBOP	: '-'
	;
MULOP	: '*'
	;
DIVOP	: '/'
	;
LRB	: '('
	;
RRB	: ')'
	;
LCB	: '{'
	;
RCB	: '}'
	;
CM	: ','
	;
SM	: ';'
	;
EQ	: '='
	;

	
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
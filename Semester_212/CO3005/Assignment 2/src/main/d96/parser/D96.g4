grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
start: program EOF;
program: class_decl+ EOF;

//2.1 Class declaration
class_decl	: CLASS ID (CL ID)? LP mem_list RP ;
mem_list	: (attri_decl | method_decl)*;

// 2.2 Attribute declaration
attri_decl	: (VAL | VAR) (id_list CL data_type | attri_recurse) SEMI ;
attri_recurse
			: ident CM attri_recurse CM expr
			| ident CL data_type ASSIGN expr
			;
// attri_decl	: (VAL | VAR) attri_body SEMI;

// attri_body	: (ID | STATIC_ID) CM attri_body CM expr 
// 			| (ID | STATIC_ID) CL data_type (ASSIGN expr)?;

id_list		: ident (CM ident)*;

//2.3 Method Declaration
method_decl	: ident LB param_list? RB block_stmt
			| CONSTRUCTOR LB param_list? RB block_stmt
			| DESTRUCTOR LB RB block_stmt
			;
param_list	: id_list CL data_type (SEMI id_list CL data_type)*;

//5 Expression
expr	: literal | idx_arr | mul_dim_arr | SELF | NULL 
		| ID | func_call
		| LB expr RB
		| NEW ID LB expr_list? RB
		| ID STATIC_ACC STATIC_ID (LB expr_list? RB)?
		| expr DOT ID (LB expr_list? RB)?
		| expr (LSB expr RSB)+
		| SUB expr
		| NOT expr
		| expr (MUL | DIV | PRCNT) expr
		| expr (ADD | SUB) expr
		| expr (AND | OR) expr
		| expr (EQ | NOT_EQ | LESS | GREAT | LESS_EQ | GREAT_EQ) expr
		| expr (EQ_STR | CONCAT_STR) expr
		;
expr_list: expr (CM expr)*;
func_call : ID LB expr_list? RB;

//6 Statements
stmt	: varval_const_stmt
		| if_stmt
		| for_in_stmt
		| break_stmt
		| cont_stmt
		| rtrn_stmt
		| method_invoc_stmt
		| assign_stmt
		| block_stmt
		;

//6.1 Variable, Constant Declare Statement
varval_const_stmt
		: (VAR | VAL) (ID (CM ID)* CL data_type | const_recurse) SEMI;

const_recurse
		: ID CM const_recurse CM expr
		| ID CL data_type ASSIGN expr
		; 
//6.2 Assignment Statement
assign_stmt : lhs ASSIGN expr SEMI;
lhs		: ID | SELF | lhs (LSB expr RSB)+ | lhs DOT expr;

//6.3 If Statement
if_stmt 	: 	
			IF LB expr RB block_stmt 
			(ELSEIF LB expr RB block_stmt)*
			(ELSE block_stmt)?
			;

//6.4 For/In Statement
for_in_stmt
			: FOREACH LB IN expr DOTDOT expr (LSB BY expr RSB)? block_stmt;

//6.5 Break Statement
break_stmt 	: BREAK SEMI;

//6.6 Continue statement
cont_stmt 	: CONTINUE SEMI;

//6.7 Return statement
rtrn_stmt 	: RETURN (expr)? SEMI;

//6.8 Method Invocation Statement
method_invoc_stmt 
			: expr DOT ID LB expr_list? RB SEMI
			| ID STATIC_ACC STATIC_ID LB expr_list? RB SEMI
			;

//6.9
block_stmt	: LP stmt* RP;

//3.2 Program comment

BLOCK_CMT : CMT .*? CMT -> skip;
fragment CMT: '##';

//3.7 Literals
literal
	:	FLOAT_LIT 	{self.text = self.text.replace('_','')}
	|	INT_LIT		{self.text = self.text.replace('_','')}
	|	BOOL_LIT
	|	STR_LIT		{self.text = self.text[1:-1]}
	;

INT_LIT
	: 	OCTAL	
	| 	DECIMAL	
	| 	HEX		
	| 	BINARY	
	;
fragment OCTAL		: '0' ( [0-7] | [1-7]('_'?[0-7])* );
fragment DECIMAL 	: [0-9] | [1-9]('_'?[0-9])*;
fragment HEX		: '0'[xX] ([0-9A-F] | [1-9A-F]('_'?[0-9A-F])* );
fragment BINARY		: '0'[bB] ([01] | '1'('_'?[01])* );

FLOAT_LIT
	: 	DECIMAL? (DOT DIGIT*) EXPONENT
	|	DECIMAL (DOT (DIGIT*))? EXPONENT
	|	DECIMAL (DOT DIGIT*) EXPONENT?
	;

BOOL_LIT: TRUE | FALSE;

STR_LIT: DOUBLEQUOTE (STR_CHAR | '\'"')* DOUBLEQUOTE
	;

idx_arr	: ARRAY LB expr_list? RB ; 

mul_dim_arr	: ARRAY LB ((idx_arr (CM idx_arr)*) | mul_dim_arr)+ RB;

DIGIT : [0-9];
fragment EXPONENT : [eE] (ADD | SUB)? (DIGIT)+;

//4 Data Types
data_type 
	: primitive_type	//4.1
	| array_type		//4.2
	| ID				//4.3
	;

//4.1 Primitive types
primitive_type: INT | FLOAT | BOOLEAN | STRING;

//4.2 Array type
array_type: ARRAY LSB (primitive_type | array_type) CM literal RSB;

//4.3 Class type
//CLASS_TYPE: ID;
//3.4 Keywords

BREAK		: 'Break';
CONTINUE	: 'Continue';
IF			: 'If';
ELSEIF		: 'Elseif';
ELSE		: 'Else';
FOREACH		: 'Foreach';
TRUE		: 'True';
FALSE		: 'False';
ARRAY		: 'Array';
IN			: 'In';
INT			: 'Int'; 
FLOAT		: 'Float';
BOOLEAN		: 'Boolean';
STRING		: 'String';
RETURN		: 'Return';
NULL		: 'Null';
CLASS		: 'Class';
VAL			: 'Val';
VAR			: 'Var';
SELF		: 'Self';
CONSTRUCTOR	: 'Constructor';
DESTRUCTOR	: 'Destructor';
NEW			: 'New';
BY			: 'By';

//3.5 Operators
ADD			: '+';
SUB			: '-';
MUL			: '*';
DIV			: '/';
PRCNT		: '%';
NOT			: '!';
AND			: '&&';
OR			: '||';
EQ			: '==';
ASSIGN		: '=';
NOT_EQ		: '!=';
LESS		: '<';
LESS_EQ		: '<=';
GREAT		: '>';
GREAT_EQ	: '>=';
EQ_STR		: '==.';
CONCAT_STR	: '+.';
STATIC_ACC	: '::';

//3.6 Seperators

LB: '(';
RB: ')';
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';
DOTDOT: '..';
DOT: '.';
CM: ',';
SEMI: ';';
CL: ':';
DOUBLEQUOTE: '"';

//3.3 Identifiers
//Keywords are put before ID so Lexer 
//can prioritze Keywords before Identifiers

ident: ID | STATIC_ID;
ID: [_a-zA-Z][_0-9a-zA-Z]*;
STATIC_ID: '$'[0-9a-zA-Z_]+;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .	
	{	
		raise ErrorToken(self.text)	
	}
	;

UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		raise UncloseString(self.text[1:])
	}
	;
	
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		raise IllegalEscape(self.text[1:])
	}
	;

fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;
fragment ESC_SEQ: '\\' [btnfr"'\\] ;
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;
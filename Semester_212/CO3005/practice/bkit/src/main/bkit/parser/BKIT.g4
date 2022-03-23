grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program : EOF ;

IPv4: ('0'|([1-9][0-9]?[0-9])?)'.'('0'|([1-9][0-9]?[0-9]?))'.'('0'|([1-9][0-9]?[0-9]?))'.'('0'|([1-9][0-9]?[0-9]?));

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
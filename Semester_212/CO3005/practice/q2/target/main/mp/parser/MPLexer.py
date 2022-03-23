# Generated from main/mp/parser/MP.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("-\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\6\6!\n\6\r\6\16\6\"\3\7\6\7&\n\7\r\7\16")
        buf.write("\7\'\3\7\3\7\3\b\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\3\2\4\3\2c|\5\2\13\f\17\17\"\"\2.\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\3\21\3\2\2\2\5\25\3\2\2\2\7\33\3\2\2\2")
        buf.write("\t\35\3\2\2\2\13 \3\2\2\2\r%\3\2\2\2\17+\3\2\2\2\21\22")
        buf.write("\7k\2\2\22\23\7p\2\2\23\24\7v\2\2\24\4\3\2\2\2\25\26\7")
        buf.write("h\2\2\26\27\7n\2\2\27\30\7q\2\2\30\31\7c\2\2\31\32\7v")
        buf.write("\2\2\32\6\3\2\2\2\33\34\7=\2\2\34\b\3\2\2\2\35\36\7.\2")
        buf.write("\2\36\n\3\2\2\2\37!\t\2\2\2 \37\3\2\2\2!\"\3\2\2\2\" ")
        buf.write("\3\2\2\2\"#\3\2\2\2#\f\3\2\2\2$&\t\3\2\2%$\3\2\2\2&\'")
        buf.write("\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\b\7\2\2*\16")
        buf.write("\3\2\2\2+,\13\2\2\2,\20\3\2\2\2\5\2\"\'\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    FLOATTYPE = 2
    SEMI = 3
    COMMA = 4
    ID = 5
    WS = 6
    ERROR_CHAR = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "SEMI", "COMMA", "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "INTTYPE", "FLOATTYPE", "SEMI", "COMMA", "ID", "WS", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



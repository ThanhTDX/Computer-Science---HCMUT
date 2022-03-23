# Generated from /home/thanh792001/Computer-Science---HCMUT/Semester_212/CO3005/practice/bkit/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("(\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\6\2\21\n\2\r\2\16\2\22\3\3\3\3\6\3\27\n\3\r\3\16")
        buf.write("\3\30\3\4\6\4\34\n\4\r\4\16\4\35\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\2\2\b\3\2\5\3\7\4\t\5\13\6\r\7\3\2\6\3")
        buf.write("\2\62;\3\2c|\5\2\62;C\\c|\5\2\13\f\17\17\"\"\2)\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\3\20\3\2\2\2\5\24\3\2\2\2\7\33\3\2\2\2\t!\3\2\2\2\13")
        buf.write("$\3\2\2\2\r&\3\2\2\2\17\21\t\2\2\2\20\17\3\2\2\2\21\22")
        buf.write("\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23\4\3\2\2\2\24\26")
        buf.write("\t\3\2\2\25\27\t\4\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30")
        buf.write("\26\3\2\2\2\30\31\3\2\2\2\31\6\3\2\2\2\32\34\t\5\2\2\33")
        buf.write("\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2")
        buf.write("\36\37\3\2\2\2\37 \b\4\2\2 \b\3\2\2\2!\"\13\2\2\2\"#\b")
        buf.write("\5\3\2#\n\3\2\2\2$%\13\2\2\2%\f\3\2\2\2&\'\13\2\2\2\'")
        buf.write("\16\3\2\2\2\6\2\22\30\35\4\b\2\2\3\5\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "NUM", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[3] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		raise ErrorToken(self.text)
            	
     



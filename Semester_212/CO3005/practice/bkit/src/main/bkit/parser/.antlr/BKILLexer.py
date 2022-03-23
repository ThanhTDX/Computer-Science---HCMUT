# Generated from /home/thanh792001/Computer-Science---HCMUT/Semester_212/CO3005/practice/bkit/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("\31\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\r\n\2")
        buf.write("\r\2\16\2\16\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\2\2\6")
        buf.write("\3\3\5\4\7\5\t\6\3\2\3\5\2\13\f\17\17\"\"\2\31\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\f\3\2\2\2\5")
        buf.write("\22\3\2\2\2\7\25\3\2\2\2\t\27\3\2\2\2\13\r\t\2\2\2\f\13")
        buf.write("\3\2\2\2\r\16\3\2\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17\20")
        buf.write("\3\2\2\2\20\21\b\2\2\2\21\4\3\2\2\2\22\23\13\2\2\2\23")
        buf.write("\24\b\3\3\2\24\6\3\2\2\2\25\26\13\2\2\2\26\b\3\2\2\2\27")
        buf.write("\30\13\2\2\2\30\n\3\2\2\2\4\2\16\4\b\2\2\3\3\2")
        return buf.getvalue()


class BKILLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    ERROR_CHAR = 2
    UNCLOSE_STRING = 3
    ILLEGAL_ESCAPE = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[1] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		raise ErrorToken(self.text)
            	
     



# Generated from /home/thanh792001/Computer-Science---HCMUT/Semester_212/CO3005/practice/bkit/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("F\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\2\5\2\21\n\2\3\2\5\2\24\n\2\5\2\26\n\2\3\2\3\2\3\2")
        buf.write("\3\2\5\2\34\n\2\3\2\5\2\37\n\2\5\2!\n\2\3\2\3\2\3\2\3")
        buf.write("\2\5\2\'\n\2\3\2\5\2*\n\2\5\2,\n\2\3\2\3\2\3\2\3\2\5\2")
        buf.write("\62\n\2\3\2\5\2\65\n\2\5\2\67\n\2\3\3\6\3:\n\3\r\3\16")
        buf.write("\3;\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\2\2\7\3\3\5\4")
        buf.write("\7\5\t\6\13\7\3\2\5\3\2\63;\3\2\62;\5\2\13\f\17\17\"\"")
        buf.write("\2R\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\3\25\3\2\2\2\59\3\2\2\2\7?\3\2\2\2\tB\3\2")
        buf.write("\2\2\13D\3\2\2\2\r\26\7\62\2\2\16\20\t\2\2\2\17\21\t\3")
        buf.write("\2\2\20\17\3\2\2\2\20\21\3\2\2\2\21\22\3\2\2\2\22\24\t")
        buf.write("\3\2\2\23\16\3\2\2\2\23\24\3\2\2\2\24\26\3\2\2\2\25\r")
        buf.write("\3\2\2\2\25\23\3\2\2\2\26\27\3\2\2\2\27 \7\60\2\2\30!")
        buf.write("\7\62\2\2\31\33\t\2\2\2\32\34\t\3\2\2\33\32\3\2\2\2\33")
        buf.write("\34\3\2\2\2\34\36\3\2\2\2\35\37\t\3\2\2\36\35\3\2\2\2")
        buf.write("\36\37\3\2\2\2\37!\3\2\2\2 \30\3\2\2\2 \31\3\2\2\2!\"")
        buf.write("\3\2\2\2\"+\7\60\2\2#,\7\62\2\2$&\t\2\2\2%\'\t\3\2\2&")
        buf.write("%\3\2\2\2&\'\3\2\2\2\')\3\2\2\2(*\t\3\2\2)(\3\2\2\2)*")
        buf.write("\3\2\2\2*,\3\2\2\2+#\3\2\2\2+$\3\2\2\2,-\3\2\2\2-\66\7")
        buf.write("\60\2\2.\67\7\62\2\2/\61\t\2\2\2\60\62\t\3\2\2\61\60\3")
        buf.write("\2\2\2\61\62\3\2\2\2\62\64\3\2\2\2\63\65\t\3\2\2\64\63")
        buf.write("\3\2\2\2\64\65\3\2\2\2\65\67\3\2\2\2\66.\3\2\2\2\66/\3")
        buf.write("\2\2\2\67\4\3\2\2\28:\t\4\2\298\3\2\2\2:;\3\2\2\2;9\3")
        buf.write("\2\2\2;<\3\2\2\2<=\3\2\2\2=>\b\3\2\2>\6\3\2\2\2?@\13\2")
        buf.write("\2\2@A\b\4\3\2A\b\3\2\2\2BC\13\2\2\2C\n\3\2\2\2DE\13\2")
        buf.write("\2\2E\f\3\2\2\2\20\2\20\23\25\33\36 &)+\61\64\66;\4\b")
        buf.write("\2\2\3\4\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IPv4 = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "IPv4", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IPv4", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[2] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		raise ErrorToken(self.text)
            	
     



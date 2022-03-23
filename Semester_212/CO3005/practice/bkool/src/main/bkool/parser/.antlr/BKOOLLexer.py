# Generated from /home/thanh792001/Computer-Science---HCMUT/Semester_212/CO3005/practice/bkool/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("n\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5")
        buf.write("\2\64\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\6\4>\n\4\r\4")
        buf.write("\16\4?\3\5\6\5C\n\5\r\5\16\5D\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\6\22b\n\22\r")
        buf.write("\22\16\22c\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\2\2\26\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26\3\2")
        buf.write("\5\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2q\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\3\63\3\2\2\2\5\65\3\2\2\2\7=\3\2\2")
        buf.write("\2\tB\3\2\2\2\13F\3\2\2\2\rJ\3\2\2\2\17L\3\2\2\2\21N\3")
        buf.write("\2\2\2\23P\3\2\2\2\25R\3\2\2\2\27T\3\2\2\2\31V\3\2\2\2")
        buf.write("\33X\3\2\2\2\35Z\3\2\2\2\37\\\3\2\2\2!^\3\2\2\2#a\3\2")
        buf.write("\2\2%g\3\2\2\2\'j\3\2\2\2)l\3\2\2\2+,\7k\2\2,-\7p\2\2")
        buf.write("-\64\7v\2\2./\7h\2\2/\60\7n\2\2\60\61\7q\2\2\61\62\7c")
        buf.write("\2\2\62\64\7v\2\2\63+\3\2\2\2\63.\3\2\2\2\64\4\3\2\2\2")
        buf.write("\65\66\7t\2\2\66\67\7g\2\2\678\7v\2\289\7w\2\29:\7t\2")
        buf.write("\2:;\7p\2\2;\6\3\2\2\2<>\t\2\2\2=<\3\2\2\2>?\3\2\2\2?")
        buf.write("=\3\2\2\2?@\3\2\2\2@\b\3\2\2\2AC\t\3\2\2BA\3\2\2\2CD\3")
        buf.write("\2\2\2DB\3\2\2\2DE\3\2\2\2E\n\3\2\2\2FG\5\t\5\2GH\7\60")
        buf.write("\2\2HI\5\t\5\2I\f\3\2\2\2JK\7-\2\2K\16\3\2\2\2LM\7/\2")
        buf.write("\2M\20\3\2\2\2NO\7,\2\2O\22\3\2\2\2PQ\7\61\2\2Q\24\3\2")
        buf.write("\2\2RS\7*\2\2S\26\3\2\2\2TU\7+\2\2U\30\3\2\2\2VW\7}\2")
        buf.write("\2W\32\3\2\2\2XY\7\177\2\2Y\34\3\2\2\2Z[\7.\2\2[\36\3")
        buf.write("\2\2\2\\]\7=\2\2] \3\2\2\2^_\7?\2\2_\"\3\2\2\2`b\t\4\2")
        buf.write("\2a`\3\2\2\2bc\3\2\2\2ca\3\2\2\2cd\3\2\2\2de\3\2\2\2e")
        buf.write("f\b\22\2\2f$\3\2\2\2gh\13\2\2\2hi\b\23\3\2i&\3\2\2\2j")
        buf.write("k\13\2\2\2k(\3\2\2\2lm\13\2\2\2m*\3\2\2\2\7\2\63?Dc\4")
        buf.write("\b\2\2\3\23\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TYPE = 1
    RETURN = 2
    ID = 3
    INTLIT = 4
    FLOATLIT = 5
    ADDOP = 6
    SUBOP = 7
    MULOP = 8
    DIVOP = 9
    LRB = 10
    RRB = 11
    LCB = 12
    RCB = 13
    CM = 14
    SM = 15
    EQ = 16
    WS = 17
    ERROR_CHAR = 18
    UNCLOSE_STRING = 19
    ILLEGAL_ESCAPE = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'{'", 
            "'}'", "','", "';'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "RETURN", "ID", "INTLIT", "FLOATLIT", "ADDOP", "SUBOP", 
            "MULOP", "DIVOP", "LRB", "RRB", "LCB", "RCB", "CM", "SM", "EQ", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TYPE", "RETURN", "ID", "INTLIT", "FLOATLIT", "ADDOP", 
                  "SUBOP", "MULOP", "DIVOP", "LRB", "RRB", "LCB", "RCB", 
                  "CM", "SM", "EQ", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[17] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		raise ErrorToken(self.text)
            	
     



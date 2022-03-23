# Generated from /home/thanh792001/Computer-Science---HCMUT/Semester_212/CO3005/practice/q2/src/main/mp/parser/MP.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("%\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\6\3\21\n\3\r\3\16\3\22\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\6\7\6 \n\6\f\6\16\6#\13\6\3\6\2\2\7\2")
        buf.write("\4\6\b\n\2\3\3\2\3\4\2!\2\f\3\2\2\2\4\20\3\2\2\2\6\26")
        buf.write("\3\2\2\2\b\32\3\2\2\2\n\34\3\2\2\2\f\r\5\4\3\2\r\16\7")
        buf.write("\2\2\3\16\3\3\2\2\2\17\21\5\6\4\2\20\17\3\2\2\2\21\22")
        buf.write("\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2\2\24")
        buf.write("\25\7\2\2\3\25\5\3\2\2\2\26\27\5\b\5\2\27\30\5\n\6\2\30")
        buf.write("\31\7\5\2\2\31\7\3\2\2\2\32\33\t\2\2\2\33\t\3\2\2\2\34")
        buf.write("!\7\7\2\2\35\36\7\6\2\2\36 \7\7\2\2\37\35\3\2\2\2 #\3")
        buf.write("\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\13\3\2\2\2#!\3\2\2\2\4")
        buf.write("\22!")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "INTTYPE", "FLOATTYPE", "SEMI", "COMMA", 
                      "ID", "WS", "ERROR_CHAR" ]

    RULE_start = 0
    RULE_program = 1
    RULE_vardecl = 2
    RULE_mptype = 3
    RULE_ids = 4

    ruleNames =  [ "start", "program", "vardecl", "mptype", "ids" ]

    EOF = Token.EOF
    INTTYPE=1
    FLOATTYPE=2
    SEMI=3
    COMMA=4
    ID=5
    WS=6
    ERROR_CHAR=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(MPParser.ProgramContext,0)


        def EOF(self):
            return self.getToken(MPParser.EOF, 0)

        def getRuleIndex(self):
            return MPParser.RULE_start




    def start(self):

        localctx = MPParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.program()
            self.state = 11
            self.match(MPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MPParser.EOF, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.VardeclContext)
            else:
                return self.getTypedRuleContext(MPParser.VardeclContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_program




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 13
                self.vardecl()
                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MPParser.INTTYPE or _la==MPParser.FLOATTYPE):
                    break

            self.state = 18
            self.match(MPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(MPParser.MptypeContext,0)


        def ids(self):
            return self.getTypedRuleContext(MPParser.IdsContext,0)


        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def getRuleIndex(self):
            return MPParser.RULE_vardecl




    def vardecl(self):

        localctx = MPParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.mptype()
            self.state = 21
            self.ids()
            self.state = 22
            self.match(MPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MPParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MPParser.FLOATTYPE, 0)

        def getRuleIndex(self):
            return MPParser.RULE_mptype




    def mptype(self):

        localctx = MPParser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            _la = self._input.LA(1)
            if not(_la==MPParser.INTTYPE or _la==MPParser.FLOATTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.ID)
            else:
                return self.getToken(MPParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.COMMA)
            else:
                return self.getToken(MPParser.COMMA, i)

        def getRuleIndex(self):
            return MPParser.RULE_ids




    def ids(self):

        localctx = MPParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ids)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(MPParser.ID)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MPParser.COMMA:
                self.state = 27
                self.match(MPParser.COMMA)
                self.state = 28
                self.match(MPParser.ID)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






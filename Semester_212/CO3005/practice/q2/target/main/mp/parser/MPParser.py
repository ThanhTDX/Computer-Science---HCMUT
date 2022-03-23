# Generated from main/mp/parser/MP.g4 by ANTLR 4.9.3
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
        buf.write(" \4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\7\5\33")
        buf.write("\n\5\f\5\16\5\36\13\5\3\5\2\2\6\2\4\6\b\2\3\3\2\3\4\2")
        buf.write("\35\2\13\3\2\2\2\4\21\3\2\2\2\6\25\3\2\2\2\b\27\3\2\2")
        buf.write("\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r\13\3\2\2\2\r")
        buf.write("\16\3\2\2\2\16\17\3\2\2\2\17\20\7\2\2\3\20\3\3\2\2\2\21")
        buf.write("\22\5\6\4\2\22\23\5\b\5\2\23\24\7\5\2\2\24\5\3\2\2\2\25")
        buf.write("\26\t\2\2\2\26\7\3\2\2\2\27\34\7\7\2\2\30\31\7\6\2\2\31")
        buf.write("\33\7\7\2\2\32\30\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2")
        buf.write("\34\35\3\2\2\2\35\t\3\2\2\2\36\34\3\2\2\2\4\r\34")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "INTTYPE", "FLOATTYPE", "SEMI", "COMMA", 
                      "ID", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_vardecl = 1
    RULE_mptype = 2
    RULE_ids = 3

    ruleNames =  [ "program", "vardecl", "mptype", "ids" ]

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
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.vardecl()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MPParser.INTTYPE or _la==MPParser.FLOATTYPE):
                    break

            self.state = 13
            self.match(MPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MPParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.mptype()
            self.state = 16
            self.ids()
            self.state = 17
            self.match(MPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MPParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MPParser.FLOATTYPE, 0)

        def getRuleIndex(self):
            return MPParser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = MPParser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = MPParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ids)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(MPParser.ID)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MPParser.COMMA:
                self.state = 22
                self.match(MPParser.COMMA)
                self.state = 23
                self.match(MPParser.ID)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






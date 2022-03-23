# Generated from /home/thanh792001/Computer-Science---HCMUT/Semester_212/CO3005/practice/bkool/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("\u0093\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\6\2%\n\2\r")
        buf.write("\2\16\2&\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\7\58\n\5\f\5\16\5;\13\5\5\5=\n\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\6\6D\n\6\r\6\16\6E\3\6\3\6\3\7\3\7\3\7")
        buf.write("\5\7M\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\5\13b\n\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\5\fi\n\f\3\r\3\r\3\r\3\r\3\r\3\r\7\rq\n")
        buf.write("\r\f\r\16\rt\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16~\n\16\3\17\3\17\3\17\7\17\u0083\n\17\f\17\16")
        buf.write("\17\u0086\13\17\3\20\3\20\3\20\3\21\3\21\3\21\7\21\u008e")
        buf.write("\n\21\f\21\16\21\u0091\13\21\3\21\2\3\30\22\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \2\3\3\2\n\13\2\u0093\2")
        buf.write("$\3\2\2\2\4*\3\2\2\2\6.\3\2\2\2\b\63\3\2\2\2\n@\3\2\2")
        buf.write("\2\fL\3\2\2\2\16P\3\2\2\2\20T\3\2\2\2\22Y\3\2\2\2\24a")
        buf.write("\3\2\2\2\26h\3\2\2\2\30j\3\2\2\2\32}\3\2\2\2\34\177\3")
        buf.write("\2\2\2\36\u0087\3\2\2\2 \u008a\3\2\2\2\"%\5\4\3\2#%\5")
        buf.write("\6\4\2$\"\3\2\2\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2")
        buf.write("\2\2\'(\3\2\2\2()\7\2\2\3)\3\3\2\2\2*+\7\3\2\2+,\5\34")
        buf.write("\17\2,-\7\21\2\2-\5\3\2\2\2./\7\3\2\2/\60\7\5\2\2\60\61")
        buf.write("\5\b\5\2\61\62\5\n\6\2\62\7\3\2\2\2\63<\7\f\2\2\649\5")
        buf.write("\36\20\2\65\66\7\21\2\2\668\5\36\20\2\67\65\3\2\2\28;")
        buf.write("\3\2\2\29\67\3\2\2\29:\3\2\2\2:=\3\2\2\2;9\3\2\2\2<\64")
        buf.write("\3\2\2\2<=\3\2\2\2=>\3\2\2\2>?\7\r\2\2?\t\3\2\2\2@C\7")
        buf.write("\16\2\2AD\5\4\3\2BD\5\f\7\2CA\3\2\2\2CB\3\2\2\2DE\3\2")
        buf.write("\2\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\7\17\2\2H\13\3\2")
        buf.write("\2\2IM\5\16\b\2JM\5\20\t\2KM\5\22\n\2LI\3\2\2\2LJ\3\2")
        buf.write("\2\2LK\3\2\2\2MN\3\2\2\2NO\7\21\2\2O\r\3\2\2\2PQ\7\5\2")
        buf.write("\2QR\7\22\2\2RS\5\24\13\2S\17\3\2\2\2TU\7\5\2\2UV\7\f")
        buf.write("\2\2VW\5 \21\2WX\7\r\2\2X\21\3\2\2\2YZ\7\4\2\2Z[\5\24")
        buf.write("\13\2[\23\3\2\2\2\\]\5\26\f\2]^\7\b\2\2^_\5\24\13\2_b")
        buf.write("\3\2\2\2`b\5\26\f\2a\\\3\2\2\2a`\3\2\2\2b\25\3\2\2\2c")
        buf.write("d\5\30\r\2de\7\t\2\2ef\5\30\r\2fi\3\2\2\2gi\5\30\r\2h")
        buf.write("c\3\2\2\2hg\3\2\2\2i\27\3\2\2\2jk\b\r\1\2kl\5\32\16\2")
        buf.write("lr\3\2\2\2mn\f\4\2\2no\t\2\2\2oq\5\32\16\2pm\3\2\2\2q")
        buf.write("t\3\2\2\2rp\3\2\2\2rs\3\2\2\2s\31\3\2\2\2tr\3\2\2\2uv")
        buf.write("\7\16\2\2vw\5\24\13\2wx\7\17\2\2x~\3\2\2\2y~\7\6\2\2z")
        buf.write("~\7\7\2\2{~\7\5\2\2|~\5\20\t\2}u\3\2\2\2}y\3\2\2\2}z\3")
        buf.write("\2\2\2}{\3\2\2\2}|\3\2\2\2~\33\3\2\2\2\177\u0084\7\5\2")
        buf.write("\2\u0080\u0081\7\20\2\2\u0081\u0083\7\5\2\2\u0082\u0080")
        buf.write("\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\35\3\2\2\2\u0086\u0084\3\2\2\2\u0087")
        buf.write("\u0088\7\3\2\2\u0088\u0089\5\34\17\2\u0089\37\3\2\2\2")
        buf.write("\u008a\u008f\5\24\13\2\u008b\u008c\7\20\2\2\u008c\u008e")
        buf.write("\5\24\13\2\u008d\u008b\3\2\2\2\u008e\u0091\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090!\3\2\2\2\u0091")
        buf.write("\u008f\3\2\2\2\17$&9<CELahr}\u0084\u008f")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'return'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'", "'{'", "'}'", "','", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "TYPE", "RETURN", "ID", "INTLIT", "FLOATLIT", 
                      "ADDOP", "SUBOP", "MULOP", "DIVOP", "LRB", "RRB", 
                      "LCB", "RCB", "CM", "SM", "EQ", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_var_declare = 1
    RULE_func_declare = 2
    RULE_param_declare = 3
    RULE_body = 4
    RULE_stm_declare = 5
    RULE_assign_stm = 6
    RULE_call_stm = 7
    RULE_retrn_stm = 8
    RULE_expr = 9
    RULE_expr1 = 10
    RULE_expr2 = 11
    RULE_sub_expr = 12
    RULE_id_list = 13
    RULE_param_list = 14
    RULE_exp_list = 15

    ruleNames =  [ "program", "var_declare", "func_declare", "param_declare", 
                   "body", "stm_declare", "assign_stm", "call_stm", "retrn_stm", 
                   "expr", "expr1", "expr2", "sub_expr", "id_list", "param_list", 
                   "exp_list" ]

    EOF = Token.EOF
    TYPE=1
    RETURN=2
    ID=3
    INTLIT=4
    FLOATLIT=5
    ADDOP=6
    SUBOP=7
    MULOP=8
    DIVOP=9
    LRB=10
    RRB=11
    LCB=12
    RCB=13
    CM=14
    SM=15
    EQ=16
    WS=17
    ERROR_CHAR=18
    UNCLOSE_STRING=19
    ILLEGAL_ESCAPE=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declareContext,i)


        def func_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Func_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Func_declareContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 32
                    self.var_declare()
                    pass

                elif la_ == 2:
                    self.state = 33
                    self.func_declare()
                    pass


                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.TYPE):
                    break

            self.state = 38
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(BKOOLParser.TYPE, 0)

        def id_list(self):
            return self.getTypedRuleContext(BKOOLParser.Id_listContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_declare




    def var_declare(self):

        localctx = BKOOLParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(BKOOLParser.TYPE)
            self.state = 41
            self.id_list()
            self.state = 42
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(BKOOLParser.TYPE, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def param_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Param_declareContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_func_declare




    def func_declare(self):

        localctx = BKOOLParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(BKOOLParser.TYPE)
            self.state = 45
            self.match(BKOOLParser.ID)
            self.state = 46
            self.param_declare()
            self.state = 47
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(BKOOLParser.LRB, 0)

        def RRB(self):
            return self.getToken(BKOOLParser.RRB, 0)

        def param_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Param_listContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Param_listContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SM)
            else:
                return self.getToken(BKOOLParser.SM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_param_declare




    def param_declare(self):

        localctx = BKOOLParser.Param_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(BKOOLParser.LRB)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.TYPE:
                self.state = 50
                self.param_list()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.SM:
                    self.state = 51
                    self.match(BKOOLParser.SM)
                    self.state = 52
                    self.param_list()
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 60
            self.match(BKOOLParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declareContext,i)


        def stm_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Stm_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Stm_declareContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_body




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(BKOOLParser.LCB)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.TYPE]:
                    self.state = 63
                    self.var_declare()
                    pass
                elif token in [BKOOLParser.RETURN, BKOOLParser.ID]:
                    self.state = 64
                    self.stm_declare()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.TYPE) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.ID))) != 0)):
                    break

            self.state = 69
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stm_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def assign_stm(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmContext,0)


        def call_stm(self):
            return self.getTypedRuleContext(BKOOLParser.Call_stmContext,0)


        def retrn_stm(self):
            return self.getTypedRuleContext(BKOOLParser.Retrn_stmContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stm_declare




    def stm_declare(self):

        localctx = BKOOLParser.Stm_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stm_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 71
                self.assign_stm()
                pass

            elif la_ == 2:
                self.state = 72
                self.call_stm()
                pass

            elif la_ == 3:
                self.state = 73
                self.retrn_stm()
                pass


            self.state = 76
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stm




    def assign_stm(self):

        localctx = BKOOLParser.Assign_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assign_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(BKOOLParser.ID)
            self.state = 79
            self.match(BKOOLParser.EQ)
            self.state = 80
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LRB(self):
            return self.getToken(BKOOLParser.LRB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_listContext,0)


        def RRB(self):
            return self.getToken(BKOOLParser.RRB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_call_stm




    def call_stm(self):

        localctx = BKOOLParser.Call_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_call_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(BKOOLParser.ID)
            self.state = 83
            self.match(BKOOLParser.LRB)
            self.state = 84
            self.exp_list()
            self.state = 85
            self.match(BKOOLParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Retrn_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_retrn_stm




    def retrn_stm(self):

        localctx = BKOOLParser.Retrn_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_retrn_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(BKOOLParser.RETURN)
            self.state = 88
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def ADDOP(self):
            return self.getToken(BKOOLParser.ADDOP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.expr1()

                self.state = 91
                self.match(BKOOLParser.ADDOP)
                self.state = 92
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr2Context,i)


        def SUBOP(self):
            return self.getToken(BKOOLParser.SUBOP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr1)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.expr2(0)

                self.state = 98
                self.match(BKOOLParser.SUBOP)
                self.state = 99
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sub_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Sub_exprContext,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def MULOP(self):
            return self.getToken(BKOOLParser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(BKOOLParser.DIVOP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.sub_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 107
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 108
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.MULOP or _la==BKOOLParser.DIVOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 109
                    self.sub_expr() 
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Sub_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def call_stm(self):
            return self.getTypedRuleContext(BKOOLParser.Call_stmContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_sub_expr




    def sub_expr(self):

        localctx = BKOOLParser.Sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_sub_expr)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(BKOOLParser.LCB)
                self.state = 116
                self.expr()
                self.state = 117
                self.match(BKOOLParser.RCB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(BKOOLParser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.match(BKOOLParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 122
                self.call_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_id_list




    def id_list(self):

        localctx = BKOOLParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(BKOOLParser.ID)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CM:
                self.state = 126
                self.match(BKOOLParser.CM)
                self.state = 127
                self.match(BKOOLParser.ID)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(BKOOLParser.TYPE, 0)

        def id_list(self):
            return self.getTypedRuleContext(BKOOLParser.Id_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param_list




    def param_list(self):

        localctx = BKOOLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(BKOOLParser.TYPE)
            self.state = 134
            self.id_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp_list




    def exp_list(self):

        localctx = BKOOLParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.expr()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CM:
                self.state = 137
                self.match(BKOOLParser.CM)
                self.state = 138
                self.expr()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expr2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         





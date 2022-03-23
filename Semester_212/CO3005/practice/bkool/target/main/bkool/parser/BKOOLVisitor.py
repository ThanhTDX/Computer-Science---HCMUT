# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_declare.
    def visitVar_declare(self, ctx:BKOOLParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#func_declare.
    def visitFunc_declare(self, ctx:BKOOLParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param_declare.
    def visitParam_declare(self, ctx:BKOOLParser.Param_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stm_declare.
    def visitStm_declare(self, ctx:BKOOLParser.Stm_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_stm.
    def visitAssign_stm(self, ctx:BKOOLParser.Assign_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#call_stm.
    def visitCall_stm(self, ctx:BKOOLParser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#retrn_stm.
    def visitRetrn_stm(self, ctx:BKOOLParser.Retrn_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#sub_expr.
    def visitSub_expr(self, ctx:BKOOLParser.Sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#id_list.
    def visitId_list(self, ctx:BKOOLParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param_list.
    def visitParam_list(self, ctx:BKOOLParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp_list.
    def visitExp_list(self, ctx:BKOOLParser.Exp_listContext):
        return self.visitChildren(ctx)



del BKOOLParser
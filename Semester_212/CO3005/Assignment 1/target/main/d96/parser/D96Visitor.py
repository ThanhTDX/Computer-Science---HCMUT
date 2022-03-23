# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#start.
    def visitStart(self, ctx:D96Parser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mem_list.
    def visitMem_list(self, ctx:D96Parser.Mem_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attri_decl.
    def visitAttri_decl(self, ctx:D96Parser.Attri_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attri_body.
    def visitAttri_body(self, ctx:D96Parser.Attri_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attri_recurse.
    def visitAttri_recurse(self, ctx:D96Parser.Attri_recurseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_list.
    def visitId_list(self, ctx:D96Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx:D96Parser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param_list.
    def visitParam_list(self, ctx:D96Parser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idx_expr.
    def visitIdx_expr(self, ctx:D96Parser.Idx_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ctx:D96Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#func_call.
    def visitFunc_call(self, ctx:D96Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varval_const_stmt.
    def visitVarval_const_stmt(self, ctx:D96Parser.Varval_const_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#const_body.
    def visitConst_body(self, ctx:D96Parser.Const_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#const_recurse.
    def visitConst_recurse(self, ctx:D96Parser.Const_recurseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_stmt.
    def visitFor_in_stmt(self, ctx:D96Parser.For_in_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#cont_stmt.
    def visitCont_stmt(self, ctx:D96Parser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#rtrn_stmt.
    def visitRtrn_stmt(self, ctx:D96Parser.Rtrn_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invoc_stmt.
    def visitMethod_invoc_stmt(self, ctx:D96Parser.Method_invoc_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idx_arr.
    def visitIdx_arr(self, ctx:D96Parser.Idx_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mul_dim_arr.
    def visitMul_dim_arr(self, ctx:D96Parser.Mul_dim_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data_type.
    def visitData_type(self, ctx:D96Parser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)



del D96Parser
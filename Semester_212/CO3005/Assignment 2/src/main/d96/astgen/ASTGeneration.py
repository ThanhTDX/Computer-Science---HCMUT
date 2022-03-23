from ast import Return, UnaryOp

from numpy import format_float_positional
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        res = []
        for x in ctx.class_decl():
            if isinstance(x, list):
                res.extend(x if x else [])
            else:
                res.append(x)
        return Program(res)
    
    #class ClassDecl
    def visitClass_decl(self, ctx: D96Parser.Class_declContext):
        class_name = ctx.ID(0)
        if ctx.CL(): 
            parent_name = ctx.ID(1)
            cl = ctx.CL().getText()
        mem_list = self.visit(ctx.mem_list())
        return ClassDecl(class_name, parent_name if parent_name else None, mem_list)
    
    def visitMem_list(self,ctx: D96Parser.Mem_listContext):
        res = []
        for decl in ctx.mem_decl():
            res += self.visit(decl)
        return res
    
    #class AttributeDecl
    def visitAtrri_decl(self, ctx:D96Parser.Attri_declContext):
        decl = VarDecl if ctx.VAR() else ConstDecl
        if ctx.attri_recurse():
            id, expr, mptype = self.visit(ctx.attri_recurse())
            id = id.reverse()
        else:
            id = self.visit(ctx.id_list())
            mptype = self.visit(ctx.data_type)
        return [(AttributeDecl(Static() if id[i].name[0] == '$' else Instance(), decl(id[i], mptype, expr[i]))) for i in range(len(id))]
    
    def visitAttri_recurse(self, ctx: D96Parser.Attri_recurseContext):
        id, expr, mptype = None, None, None
        if ctx.attri_recurse():
            id, expr, mptype = self.visit(ctx.attri_recurse())
            id.append(self.visit(ctx.ident()))
            expr.append(self.visit(ctx.expr()))
        else:
            id = [self.visit(ctx.ident())]
            expr = [self.visit(ctx.expr())]
            mptype = self.visit(ctx.data_type)
        return id, expr, mptype

    
    def visitId_list(self, ctx: D96Parser.Id_listContext):
        return [self.visit(i) for i in ctx.ident()]
    
    def visitIdent(self, ctx: D96Parser.IdentContext):
        return Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.STATIC_ID().getText())
    
    def visitMethod_decl(self, ctx: D96Parser.Method_declContext):
        param = self.visit(ctx.param_list())
        block_stmt = self.visit(ctx.block_stmt())
        if ctx.CONSTRUCTOR():
            return MethodDecl(Id("Constructor"), None, param, block_stmt)
        elif ctx.DESTRUCTOR():
            return MethodDecl(Id("Destructor"), None, param, block_stmt)
        else:
            id = self.visit(ctx.ident())
            mptype = Static() if id.STATIC_ID() else Instance()
            return MethodDecl(id, mptype, param, block_stmt)
    
    def visitParam_list(self, ctx: D96Parser.Param_listContext):
        res = []
        for i in ctx.id_list():
            id_list = self.visit(i)
            mptype = self.visit(ctx.data_type())
            res += [id_list, mptype]
        return res
    
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if ctx.getChildCount() == 1:
            if ctx.literal(): return self.visit(ctx.literal())
            if ctx.idx_arr(): return self.visit(ctx.idx_arr())
            if ctx.mul_dim_arr(): return self.visit(ctx.mul_dim_arr())
            if ctx.SELF(): return NullLiteral()
            if ctx.NULL(): return SelfLiteral()
            if ctx.ID(): return Id(ctx.ID().getText())
            if ctx.func_call(): return self.visit(ctx.func_call())
            
        elif ctx.NEW(): 
            name = Id(ctx.ID().getText())
            expr = self.visit(ctx.expr_list()) 
            return NewExpr(name, expr_list)
        
        elif ctx.STATIC_ACC():
            id = Id(ctx.ID().getText())
            sta_id = Id(ctx.STATIC_ID().getText())
            expr_list = self.visit(ctx.expr_list()) 
            return CallExpr(id, sta_id, expr_list)
        
        elif ctx.DOT():
            id = Id(ctx.ID().getText())
            expr = self.visit(ctx.expr())
            expr_list = self.visit(ctx.expr_list())
            return CallExpr(expr, id, expr_list)
        
        elif ctx.LSB() or ctx.RSB():
            expr_list = []
            for i in ctx.expr():
                expr_list.append(self.visit(i))
            return ArrayCell(expr_list[:1], expr_list[1:])
        
        elif ctx.SUB():
            return UnaryOp("-", self.visit(ctx.expr()))
        
        elif ctx.NOT():
            return UnaryOp("!", self.visit(ctx.expr()))
        
        elif ctx.MUL() or ctx.DIV() or ctx.PRCNT():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if ctx.MUL(): return BinaryOp("*", left, right)
            elif ctx.DIV(): return BinaryOp("/", left, right)
            else: return BinaryOp("%", left, right)
            
        elif ctx.ADD() or ctx.SUB():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if ctx.ADD(): return BinaryOp("+", left, right)
            else: return BinaryOp("-", left, right)
            
        elif ctx.AND() or ctx.OR():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if ctx.AND(): return BinaryOp("&&", left, right)
            else: return BinaryOp("||", left, right)
            
        elif ctx.EQ() or ctx.NOT_EQ() or ctx.LESS() or ctx.GREAT() or ctx.LESS_EQ() or ctx.GREAT_EQ():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if ctx.EQ(): return BinaryOp("==", left, right)
            elif ctx.NOT_EQ(): return BinaryOp("!=", left, right)
            elif ctx.LESS(): return BinaryOp("<", left, right)
            elif ctx.GREAT(): return BinaryOp(">", left, right)
            elif ctx.LESS_EQ(): return BinaryOp("<=", left, right)
            else: return BinaryOp(">=", left, right)
        elif ctx.EQ_STR() or ctx.CONCAT_STR():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if ctx.EQ_STR(): return Binary("==.",left, right)
            else: return Binary("++.", left, right)
        
        else:
            return self.visit(ctx.expr())
        
    def visitExpr_list(self, ctx: D96Parser.Expr_listContext):
        return [self.visit(i) for i in ctx.expr()]
    
    def visitFunc_call(self, ctx: D96Parser.Func_callContext):
        id = Id(ctx.ID().getText())
        return CallStmt(self.visit(ctx.expr_list()), id)
    
    def visitStmt(self, ctx: D96Parser.StmtContext):
        if ctx.varval_const_stmt():
            return self.visit(ctx.varval_const_stmt())
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.for_in_stmt():
            return self.visit(ctx.for_in_stmt())
        if ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        if ctx.cont_stmt():
            return self.visit(ctx.cont_stmt())
        if ctx.rtrn_stmt():
            return self.visit(ctx.rtrn_stmt())
        if ctx.method_invoc_stmt():
            return self.visit(ctx.method_invoc_stmt())
        if ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())
    
    def visitVarval_const_stmt(self, ctx: D96Parser.Varval_const_stmtContext):
        decl = VarDecl if ctx.VAR() else ConstDecl
        if ctx.attri_recurse():
            id, expr, mptype = self.visit(ctx.const_recurse())
            id = id.reverse()
        else:
            id = self.visit(Id(ctx.ID().getText()))
            mptype = self.visit(ctx.data_type)
        return [(AttributeDecl(Static() if id[i].name[0] == '$' else Instance(), decl(id[i], mptype, expr[i]))) for i in range(len(id))]
    
    def visitConst_recurse(self, ctx: D96Parser.Const_recurseContext):
        id, expr, mptype = None, None, None
        if ctx.const_recurse():
            id, expr, mptype = self.visit(ctx.const_recurse())
            id.append(Id(ctx.ID().getText()))
            expr.append(self.visit(ctx.expr()))
        else:
            id = [Id(ctx.ID().getText())]
            expr = [self.visit(ctx.expr())]
            mptype = self.visit(ctx.data_type)
        return id, expr, mptype
    
    def visitAssign_stmt(self, ctx: D96Parser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        expr = self.visit(ctx.expr())
        return Assign(lhs, expr)
    
    def visitLhs(self, ctx: D96Parser.LhsContext):
        if ctx.ID(): return Id(ctx.ID().getText())
        elif ctx.SELF(): return SelfLiteral()
        elif ctx.DOT(): 
            lhs = self.visit(ctx.lhs())
            expr = self.visit(ctx.expr())
            return FieldAccess(lhs, expr)
        else:
            lhs = self.visit(ctx.lhs())
            expr_list = [self.visit(i) for i in ctx.expr()]
            return ArrayCell(lhs, expr_list)
    
    #class If
    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        if_expr = self.visit(ctx.expr()) if ctx.expr() else None
        block = self.visit(ctx.block_stmt())
        return If(if_expr, block, self.visit(ctx.if_stmt()) if ctx_stmt else None)
    
    #class For
    def visitFor_in_stmt(self, ctx: D96Parser.For_in_stmtContext):
        Expr = [self.visit(x) for x in ctx.expr()]
        loop = self.visit(ctx.block_stmt())
        return For(Expr[0], Expr[1], Expr[2], loop)
    
    def visitBreak_stmt(self, ctx: D96Parser.Break_stmtContext):
        return Break()  
    
    def visitCont_stmt(self, ctx: D96Parser.Cont_stmtContext):
        return Continue()
    
    def visitRtrn_stmt(self, ctx: D96Parser.Rtrn_stmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return()
    
    def visitMethod_invoc_stmt(self, ctx: D96Parser.Method_invoc_stmtContext):
        if ctx.STATIC_ACC():
            id = Id(ctx.ID().getText())
            sta_id = Id(ctx.STATIC_ID().getText())
            expr_list = self.visit(ctx.expr_list()) 
            return CallStmt(id, sta_id, expr_list)
        else:
            id = Id(ctx.ID().getText())
            expr = self.visit(ctx.expr())
            expr_list = self.visit(ctx.expr_list())
            return CallStmt(expr, id, expr_list)
    
    def visitBlock_stmt(self, ctx: D96Parser.Block_stmtContext):
        stmt_list = []
        for stmt in ctx.stmt():
            self.visit(stmt)
        if isinstance(block, list):
            stmt_list.extend(stmt if stmt else [])
        else:
            stmt_list.append(stmt)
        return stmt_list
    
    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.BOOL_LIT():
            return BooleanLiteral(ctx.BOOL_LIT().getText() == "True")
        else:
            return StringLiteral(ctx.STR_LIT().getText())
    
    def visitIdx_arr(self, ctx: D96Parser.Idx_arrContext):
        return ArrayLiteral(self.visit(ctx.expr_list()))
    
    def visitMul_dim_arr(self, ctx: D96Parser.Mul_dim_arrContext):
        return None
    
    #class Id
    def visitData_type(self, ctx: D96Parser.Data_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        else:
            return Id(ctx.ID().getText())
    
    #class IntType
    #class FloatType
    #class BoolType
    #class StringType
    def visitPrimitive_type(self, ctx: D96Parser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        else:
            return StringType()
    
    #class ArrayType
    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        if ctx.primitive_type():
            type = self.visit(ctx.primitive_type())
        else:
            type = self.visit(ctx.array_type())
        value = self.visit(ctx.literal())
        return ArrayType(value, type)
    

    # def visitMptype(self, ctx: D96Parser.MptypeContext):
    #     if ctx.INTTYPE():
    #         return IntType()
    #     else:
    #         return VoidType()

    # def visitBody(self, ctx: D96Parser.BodyContext):
    #     return self.visit(ctx.funcall())

    # def visitFuncall(self, ctx: D96Parser.FuncallContext):
    #     return CallExpr(Id(ctx.ID().getText()), [self.visit(ctx.exp())] if ctx.exp() else [])

    # def visitExp(self, ctx: D96Parser.ExpContext):
    #     if (ctx.funcall()):
    #         return self.visit(ctx.funcall())
    #     else:
    #         return IntLiteral(int(ctx.INTLIT().getText()))

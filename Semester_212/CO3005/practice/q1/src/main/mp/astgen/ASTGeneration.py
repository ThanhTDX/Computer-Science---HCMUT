from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    def toBool(self,x):
        return x == "True"

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.ASSIGN():
            op = ctx.ASSIGN().getText()
            left = self.visit( ctx.term() )
            right = self.visit( ctx.exp() )
            return Binary(op, left, right)
        else:
            return self.visit( ctx.term() )

    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.COMPARE():
            op = ctx.COMPARE().getText()
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            return Binary(op, left, right)
        else:
            return self.visit(ctx.factor(0))

    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.ANDOR():
            op = ctx.ANDOR().getText()
            left = self.visit(ctx.factor())
            right = self.visit(ctx.operand())
            return Binary(op, left, right)
        else:
            return self.visit(ctx.operand())
  
    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(self.toBool(ctx.BOOLIT().getText()))
        else:
            return self.visit(ctx.exp()) 

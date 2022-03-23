from functools import reduce
from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        res = []
        for x in ctx.vardecl():
            res += self.visit(x)
        return Program(res)

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        mptype = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        res = []
        for i in ids:
            res += [VarDecl(i, mptype)]
        return res

    def visitMptype(self,ctx:MPParser.MptypeContext):

        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        res = []
        for i in ctx.ID():
            res += [Id(i.getText())]
        return res

# class ASTGeneration(MPVisitor):

#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         return Program(reduce(lambda prev, curr: prev + self.visit(curr), ctx.vardecl(), []))
    
#     def visitVardecl(self,ctx:MPParser.VardeclContext): 
#         return list(map(lambda x: VarDecl(x, self.visit(ctx.mptype())), self.visit(ctx.ids())))

#     def visitMptype(self,ctx:MPParser.MptypeContext):
#         return IntType() if ctx.INTTYPE() else FloatType()

#     def visitIds(self,ctx:MPParser.IdsContext):
#         return list(map(lambda x: Id(x.getText()), ctx.ID()))
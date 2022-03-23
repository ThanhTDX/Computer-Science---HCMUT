# class ASTGeneration(MPVisitor):
#     def visitProgram(self,ctx:MPParser.ProgramContext):
        
#         return self.visit(ctx.vardecls())

#     def visitVardecls(self,ctx:MPParser.VardeclsContext):
#         vardecl = self.visit(ctx.vardecl())
#         vardecltail = self.visit(ctx.vardecltail())
        
#         return vardecl + vardecltail

#     def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
#         res = []
#         if ctx.vardecltail():
#             vardecl = self.visit(ctx.vardecl())
#             res += vardecl + self.visit(ctx.vardecltail())
#             return res

#     def visitVardecl(self,ctx:MPParser.VardeclContext): 
#         mptype = self.visit(ctx.mptype())
#         ids = self.visit(ctx.ids())
#         res = []
#         for i in ids:
#             res += [VarDecl(i, mptype)]
#         return res

#     def visitMptype(self,ctx:MPParser.MptypeContext):
#         if ctx.INTTYPE():
#             return IntType()
#         if ctx.FLOATTYPE():    
#             return FloatType()               
#         return None

#     def visitIds(self,ctx:MPParser.IdsContext):
#         if ctx.getChildCount() != 1:
#             res = []
#             id = [Id(ctx.ID().getText())]
#             list_id = self.visit(ctx.ids())
#             res += id + list_id
#             return res
#         else: return [Id(ctx.ID().getText())]
from functools import reduce
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(reduce(lambda prev, curr: prev + self.visit(curr), ctx.vardecl(), []))
    
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return list(map(lambda x: VarDecl(x, self.visit(ctx.mptype())), self.visit(ctx.ids())))

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        return list(map(lambda x: Id(x.getText()), ctx.ID()))
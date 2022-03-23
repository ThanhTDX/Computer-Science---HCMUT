# Generated from main/mp/parser/MP.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vardecl.
    def visitVardecl(self, ctx:MPParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#mptype.
    def visitMptype(self, ctx:MPParser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ids.
    def visitIds(self, ctx:MPParser.IdsContext):
        return self.visitChildren(ctx)



del MPParser
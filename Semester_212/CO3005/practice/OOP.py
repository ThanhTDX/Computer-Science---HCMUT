# from abc import ABC, abstractmethod
# from doctest import UnexpectedException

# class Exp(ABC):
#     def eval(self):
#         pass
#     def printPrefix(self):
#         pass
    
# class BinExp(Exp):
#     def __init__(self, leftExp, op, rightExp) -> None:
#         self.left = leftExp
#         self.right = rightExp
#         self.op = op
            
#     def eval(self):
#         if isinstance(self.left, (int, float)) == False:
#             self.left = self.left.eval()
#         if isinstance(self.right, (int, float)) == False:
#             self.right = self.right.eval()
            
#         if self.op == "+":
#             self.val = self.left + self.right
#         if self.op == "-":
#             self.val = self.left - self.right
#         if self.op == "*":
#             self.val = self.left * self.right
#         if self.op == "/":
#             self.val = self.left / self.right
#         return self.val
    
#     def printPrefix(self):
#         if isinstance(self.left, (int, float)) == False:
#             leftPrint = self.left.printPrefix()
#         else:
#             leftPrint = str(self.left)
#         if isinstance(self.right, (int, float)) == False:
#             rightPrint = self.right.printPrefix()
#         else:
#             rightPrint = str(self.right)
#         return self.op + ' ' + leftPrint + ' ' + rightPrint
        
    
# class UnExp(Exp):
#     def __init__(self, op, exp) -> None:
#         self.val = exp
#         self.op = op
            
#     def eval(self):
#         if isinstance(self.val, (int, float)) == False:
#             self.val = self.val.eval()
#         if self.op == "-":
#             self.val = -self.val
#         return self.val
    
#     def printPrefix(self):
#         if isinstance(self.val, (int, float)) == False:
#             expPrint = self.val.printPrefix()
#         else:
#             expPrint = str(self.val)
#         return self.op + ". " + expPrint
    
    
# class IntLit(Exp):
#     def __init__(self, num) -> None:
#         self.val = int(num)
#     def eval(self):
#         return self.val
#     def printPrefix(self):
#         return str(self.val)
    
# class FloatLit(Exp):
#     def __init__(self, num) -> None:
#         self.val = float(num)
#     def eval(self):
#         return self.val
#     def printPrefix(self):
#         return str(self.val)

from abc import ABC, abstractmethod

class Exp(ABC):
    def eval(self):
        pass
    def printPrefix(self):
        pass
    
class BinExp(Exp):
    def __init__(self, leftExp, op, rightExp) -> None:
        self.left = leftExp
        self.right = rightExp
        self.op = op
    
class UnExp(Exp):
    def __init__(self, op, exp) -> None:
        self.val = exp
        self.op = op
    
class IntLit(Exp):
    def __init__(self, num) -> None:
        self.val = int(num)
    
class FloatLit(Exp):
    def __init__(self, num) -> None:
        self.val = float(num)

class Visitor(ABC):
    @abstractmethod
    def visit(self):
        pass
    
    @abstractmethod
    def visitEval(self):
        pass
    
    @abstractmethod
    def visitPrintPrefix(self):
        pass
    
    @abstractmethod
    def visitPrintPostfix(self):
        pass
    
class defaultVisitor(Visitor):
    def visitEval(self, obj):
        pass
    
    def visitPrintPrefix(self, obj):
        pass
    
    def visitPrintPostfix(self, obj):
        pass

class AST(ABC): #Visitable
    @abstractmethod
    def accept(self, visitor):
        return visitor.visit(self)
    
class Eval(AST):
    def __init__(self) -> None:
        pass
    def accept(self, visitor):
        return visitor.visitEval(self)
        
class PrintPrefix(AST):
    def __init__(self) -> None:
        pass
    def accept(self, visitor):
        return visitor.visitPrintPrefix(self)
    
class PrintPostfix(AST):
    def __init__(self) -> None:
        pass
    def accept(self, visitor):
        return visitor.visitPrintPostfix(self)
    

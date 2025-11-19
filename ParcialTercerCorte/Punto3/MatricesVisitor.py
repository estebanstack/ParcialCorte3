# Generated from Matrices.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MatricesParser import MatricesParser
else:
    from MatricesParser import MatricesParser

# This class defines a complete generic visitor for a parse tree produced by MatricesParser.

class MatricesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MatricesParser#program.
    def visitProgram(self, ctx:MatricesParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#stmt.
    def visitStmt(self, ctx:MatricesParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#matrixDecl.
    def visitMatrixDecl(self, ctx:MatricesParser.MatrixDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#assign.
    def visitAssign(self, ctx:MatricesParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#expr.
    def visitExpr(self, ctx:MatricesParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#matrixLiteral.
    def visitMatrixLiteral(self, ctx:MatricesParser.MatrixLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatricesParser#row.
    def visitRow(self, ctx:MatricesParser.RowContext):
        return self.visitChildren(ctx)



del MatricesParser
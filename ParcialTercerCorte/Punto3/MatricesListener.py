# Generated from Matrices.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MatricesParser import MatricesParser
else:
    from MatricesParser import MatricesParser

# This class defines a complete listener for a parse tree produced by MatricesParser.
class MatricesListener(ParseTreeListener):

    # Enter a parse tree produced by MatricesParser#program.
    def enterProgram(self, ctx:MatricesParser.ProgramContext):
        pass

    # Exit a parse tree produced by MatricesParser#program.
    def exitProgram(self, ctx:MatricesParser.ProgramContext):
        pass


    # Enter a parse tree produced by MatricesParser#stmt.
    def enterStmt(self, ctx:MatricesParser.StmtContext):
        pass

    # Exit a parse tree produced by MatricesParser#stmt.
    def exitStmt(self, ctx:MatricesParser.StmtContext):
        pass


    # Enter a parse tree produced by MatricesParser#matrixDecl.
    def enterMatrixDecl(self, ctx:MatricesParser.MatrixDeclContext):
        pass

    # Exit a parse tree produced by MatricesParser#matrixDecl.
    def exitMatrixDecl(self, ctx:MatricesParser.MatrixDeclContext):
        pass


    # Enter a parse tree produced by MatricesParser#assign.
    def enterAssign(self, ctx:MatricesParser.AssignContext):
        pass

    # Exit a parse tree produced by MatricesParser#assign.
    def exitAssign(self, ctx:MatricesParser.AssignContext):
        pass


    # Enter a parse tree produced by MatricesParser#expr.
    def enterExpr(self, ctx:MatricesParser.ExprContext):
        pass

    # Exit a parse tree produced by MatricesParser#expr.
    def exitExpr(self, ctx:MatricesParser.ExprContext):
        pass


    # Enter a parse tree produced by MatricesParser#matrixLiteral.
    def enterMatrixLiteral(self, ctx:MatricesParser.MatrixLiteralContext):
        pass

    # Exit a parse tree produced by MatricesParser#matrixLiteral.
    def exitMatrixLiteral(self, ctx:MatricesParser.MatrixLiteralContext):
        pass


    # Enter a parse tree produced by MatricesParser#row.
    def enterRow(self, ctx:MatricesParser.RowContext):
        pass

    # Exit a parse tree produced by MatricesParser#row.
    def exitRow(self, ctx:MatricesParser.RowContext):
        pass



del MatricesParser
# Generated from Matrices.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,39,8,2,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,3,4,48,8,4,1,4,1,4,1,4,5,4,53,8,4,10,4,12,4,
        56,9,4,1,5,1,5,1,5,1,5,5,5,62,8,5,10,5,12,5,65,9,5,1,5,1,5,1,6,1,
        6,1,6,1,6,5,6,73,8,6,10,6,12,6,76,9,6,1,6,1,6,1,6,0,1,8,7,0,2,4,
        6,8,10,12,0,0,79,0,17,1,0,0,0,2,28,1,0,0,0,4,38,1,0,0,0,6,40,1,0,
        0,0,8,47,1,0,0,0,10,57,1,0,0,0,12,68,1,0,0,0,14,16,3,2,1,0,15,14,
        1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,
        19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,23,3,4,2,0,23,24,5,1,
        0,0,24,29,1,0,0,0,25,26,3,6,3,0,26,27,5,1,0,0,27,29,1,0,0,0,28,22,
        1,0,0,0,28,25,1,0,0,0,29,3,1,0,0,0,30,31,5,2,0,0,31,32,5,8,0,0,32,
        33,5,3,0,0,33,39,3,10,5,0,34,35,5,2,0,0,35,36,5,8,0,0,36,37,5,3,
        0,0,37,39,3,8,4,0,38,30,1,0,0,0,38,34,1,0,0,0,39,5,1,0,0,0,40,41,
        5,8,0,0,41,42,5,3,0,0,42,43,3,8,4,0,43,7,1,0,0,0,44,45,6,4,-1,0,
        45,48,5,8,0,0,46,48,3,10,5,0,47,44,1,0,0,0,47,46,1,0,0,0,48,54,1,
        0,0,0,49,50,10,1,0,0,50,51,5,4,0,0,51,53,3,8,4,2,52,49,1,0,0,0,53,
        56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,9,1,0,0,0,56,54,1,0,0,
        0,57,58,5,5,0,0,58,63,3,12,6,0,59,60,5,6,0,0,60,62,3,12,6,0,61,59,
        1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,
        65,63,1,0,0,0,66,67,5,7,0,0,67,11,1,0,0,0,68,69,5,5,0,0,69,74,5,
        9,0,0,70,71,5,6,0,0,71,73,5,9,0,0,72,70,1,0,0,0,73,76,1,0,0,0,74,
        72,1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,78,5,7,0,
        0,78,13,1,0,0,0,7,17,28,38,47,54,63,74
    ]

class MatricesParser ( Parser ):

    grammarFileName = "Matrices.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'matrix'", "'='", "'*'", "'['", 
                     "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_matrixDecl = 2
    RULE_assign = 3
    RULE_expr = 4
    RULE_matrixLiteral = 5
    RULE_row = 6

    ruleNames =  [ "program", "stmt", "matrixDecl", "assign", "expr", "matrixLiteral", 
                   "row" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    ID=8
    NUMBER=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MatricesParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatricesParser.StmtContext)
            else:
                return self.getTypedRuleContext(MatricesParser.StmtContext,i)


        def getRuleIndex(self):
            return MatricesParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MatricesParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==8:
                self.state = 14
                self.stmt()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(MatricesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matrixDecl(self):
            return self.getTypedRuleContext(MatricesParser.MatrixDeclContext,0)


        def assign(self):
            return self.getTypedRuleContext(MatricesParser.AssignContext,0)


        def getRuleIndex(self):
            return MatricesParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MatricesParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.matrixDecl()
                self.state = 23
                self.match(MatricesParser.T__0)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.assign()
                self.state = 26
                self.match(MatricesParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MatricesParser.ID, 0)

        def matrixLiteral(self):
            return self.getTypedRuleContext(MatricesParser.MatrixLiteralContext,0)


        def expr(self):
            return self.getTypedRuleContext(MatricesParser.ExprContext,0)


        def getRuleIndex(self):
            return MatricesParser.RULE_matrixDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixDecl" ):
                listener.enterMatrixDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixDecl" ):
                listener.exitMatrixDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixDecl" ):
                return visitor.visitMatrixDecl(self)
            else:
                return visitor.visitChildren(self)




    def matrixDecl(self):

        localctx = MatricesParser.MatrixDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_matrixDecl)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(MatricesParser.T__1)
                self.state = 31
                self.match(MatricesParser.ID)
                self.state = 32
                self.match(MatricesParser.T__2)
                self.state = 33
                self.matrixLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(MatricesParser.T__1)
                self.state = 35
                self.match(MatricesParser.ID)
                self.state = 36
                self.match(MatricesParser.T__2)
                self.state = 37
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MatricesParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MatricesParser.ExprContext,0)


        def getRuleIndex(self):
            return MatricesParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MatricesParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(MatricesParser.ID)
            self.state = 41
            self.match(MatricesParser.T__2)
            self.state = 42
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MatricesParser.ID, 0)

        def matrixLiteral(self):
            return self.getTypedRuleContext(MatricesParser.MatrixLiteralContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatricesParser.ExprContext)
            else:
                return self.getTypedRuleContext(MatricesParser.ExprContext,i)


        def getRuleIndex(self):
            return MatricesParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatricesParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 45
                self.match(MatricesParser.ID)
                pass
            elif token in [5]:
                self.state = 46
                self.matrixLiteral()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatricesParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 49
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 50
                    self.match(MatricesParser.T__3)
                    self.state = 51
                    self.expr(2) 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MatrixLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatricesParser.RowContext)
            else:
                return self.getTypedRuleContext(MatricesParser.RowContext,i)


        def getRuleIndex(self):
            return MatricesParser.RULE_matrixLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixLiteral" ):
                listener.enterMatrixLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixLiteral" ):
                listener.exitMatrixLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixLiteral" ):
                return visitor.visitMatrixLiteral(self)
            else:
                return visitor.visitChildren(self)




    def matrixLiteral(self):

        localctx = MatricesParser.MatrixLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_matrixLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MatricesParser.T__4)
            self.state = 58
            self.row()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 59
                self.match(MatricesParser.T__5)
                self.state = 60
                self.row()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(MatricesParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(MatricesParser.NUMBER)
            else:
                return self.getToken(MatricesParser.NUMBER, i)

        def getRuleIndex(self):
            return MatricesParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRow" ):
                return visitor.visitRow(self)
            else:
                return visitor.visitChildren(self)




    def row(self):

        localctx = MatricesParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(MatricesParser.T__4)
            self.state = 69
            self.match(MatricesParser.NUMBER)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 70
                self.match(MatricesParser.T__5)
                self.state = 71
                self.match(MatricesParser.NUMBER)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.match(MatricesParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         





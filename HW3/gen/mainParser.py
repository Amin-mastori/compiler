# Generated from C:/Users/silver/Desktop/comp/compiler/HW2/gen/main.g4 by ANTLR 4.13.1
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
        4,1,11,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,9,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,2,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,48,8,3,1,3,0,2,2,4,4,0,2,4,6,0,0,51,0,
        8,1,0,0,0,2,13,1,0,0,0,4,27,1,0,0,0,6,47,1,0,0,0,8,9,5,8,0,0,9,10,
        5,7,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,6,1,-1,0,
        14,15,3,4,2,0,15,24,1,0,0,0,16,17,10,3,0,0,17,18,5,3,0,0,18,23,3,
        4,2,0,19,20,10,2,0,0,20,21,5,4,0,0,21,23,3,4,2,0,22,16,1,0,0,0,22,
        19,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,1,0,0,
        0,26,24,1,0,0,0,27,28,6,2,-1,0,28,29,3,6,3,0,29,38,1,0,0,0,30,31,
        10,3,0,0,31,32,5,5,0,0,32,37,3,6,3,0,33,34,10,2,0,0,34,35,5,6,0,
        0,35,37,3,6,3,0,36,30,1,0,0,0,36,33,1,0,0,0,37,40,1,0,0,0,38,36,
        1,0,0,0,38,39,1,0,0,0,39,5,1,0,0,0,40,38,1,0,0,0,41,48,5,8,0,0,42,
        48,5,9,0,0,43,44,5,1,0,0,44,45,3,2,1,0,45,46,5,2,0,0,46,48,1,0,0,
        0,47,41,1,0,0,0,47,42,1,0,0,0,47,43,1,0,0,0,48,7,1,0,0,0,5,22,24,
        36,38,47
    ]

class mainParser ( Parser ):

    grammarFileName = "main.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'='", "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Plus", "MINUS", 
                      "MUL", "DIVIDE", "ASSIGN", "Id", "Number", "Newline", 
                      "Whitespace" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_fact = 3

    ruleNames =  [ "start", "expr", "term", "fact" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Plus=3
    MINUS=4
    MUL=5
    DIVIDE=6
    ASSIGN=7
    Id=8
    Number=9
    Newline=10
    Whitespace=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(mainParser.Id, 0)

        def ASSIGN(self):
            return self.getToken(mainParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def EOF(self):
            return self.getToken(mainParser.EOF, 0)

        def getRuleIndex(self):
            return mainParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = mainParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(mainParser.Id)
            self.state = 9
            self.match(mainParser.ASSIGN)
            self.state = 10
            self.expr(0)
            self.state = 11
            self.match(mainParser.EOF)
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


        def getRuleIndex(self):
            return mainParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Rule_minusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)

        def MINUS(self):
            return self.getToken(mainParser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(mainParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_minus" ):
                listener.enterRule_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_minus" ):
                listener.exitRule_minus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_minus" ):
                return visitor.visitRule_minus(self)
            else:
                return visitor.visitChildren(self)


    class Rule_plusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)

        def Plus(self):
            return self.getToken(mainParser.Plus, 0)
        def term(self):
            return self.getTypedRuleContext(mainParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_plus" ):
                listener.enterRule_plus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_plus" ):
                listener.exitRule_plus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_plus" ):
                return visitor.visitRule_plus(self)
            else:
                return visitor.visitChildren(self)


    class Rule3Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(mainParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule3" ):
                listener.enterRule3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule3" ):
                listener.exitRule3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule3" ):
                return visitor.visitRule3(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mainParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = mainParser.Rule3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 14
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 22
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = mainParser.Rule_plusContext(self, mainParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 17
                        self.match(mainParser.Plus)
                        self.state = 18
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = mainParser.Rule_minusContext(self, mainParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 20
                        self.match(mainParser.MINUS)
                        self.state = 21
                        self.term(0)
                        pass

             
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact(self):
            return self.getTypedRuleContext(mainParser.FactContext,0)


        def term(self):
            return self.getTypedRuleContext(mainParser.TermContext,0)


        def MUL(self):
            return self.getToken(mainParser.MUL, 0)

        def DIVIDE(self):
            return self.getToken(mainParser.DIVIDE, 0)

        def getRuleIndex(self):
            return mainParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mainParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 36
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = mainParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 30
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 31
                        self.match(mainParser.MUL)
                        self.state = 32
                        self.fact()
                        pass

                    elif la_ == 2:
                        localctx = mainParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 33
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 34
                        self.match(mainParser.DIVIDE)
                        self.state = 35
                        self.fact()
                        pass

             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(mainParser.Id, 0)

        def Number(self):
            return self.getToken(mainParser.Number, 0)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_fact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact" ):
                listener.enterFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact" ):
                listener.exitFact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact" ):
                return visitor.visitFact(self)
            else:
                return visitor.visitChildren(self)




    def fact(self):

        localctx = mainParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fact)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(mainParser.Id)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(mainParser.Number)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(mainParser.T__0)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(mainParser.T__1)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         





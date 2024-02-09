# Generated from HW4/Password.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\4")
        buf.write("\r\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\2\2\4\2")
        buf.write("\4\2\2\2\n\2\6\3\2\2\2\4\t\3\2\2\2\6\7\5\4\3\2\7\b\7\2")
        buf.write("\2\3\b\3\3\2\2\2\t\n\7\3\2\2\n\13\b\3\1\2\13\5\3\2\2\2")
        buf.write("\2")
        return buf.getvalue()


class PasswordParser ( Parser ):

    grammarFileName = "Password.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "STRING", "WS" ]

    RULE_start = 0
    RULE_checkLengthRule = 1

    ruleNames =  [ "start", "checkLengthRule" ]

    EOF = Token.EOF
    STRING=1
    WS=2

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def checkLengthRule(self):
            return self.getTypedRuleContext(PasswordParser.CheckLengthRuleContext,0)


        def EOF(self):
            return self.getToken(PasswordParser.EOF, 0)

        def getRuleIndex(self):
            return PasswordParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = PasswordParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.checkLengthRule()
            self.state = 5
            self.match(PasswordParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CheckLengthRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._STRING = None # Token

        def STRING(self):
            return self.getToken(PasswordParser.STRING, 0)

        def getRuleIndex(self):
            return PasswordParser.RULE_checkLengthRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCheckLengthRule" ):
                listener.enterCheckLengthRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCheckLengthRule" ):
                listener.exitCheckLengthRule(self)




    def checkLengthRule(self):

        localctx = PasswordParser.CheckLengthRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_checkLengthRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            localctx._STRING = self.match(PasswordParser.STRING)
            if ((None if localctx._STRING is None else localctx._STRING.text).length() >= 8) {System.out.println("True");} else {System.out.println("False");}
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






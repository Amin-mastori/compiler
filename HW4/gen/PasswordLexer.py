# Generated from HW4/Password.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\4")
        buf.write("\27\b\1\4\2\t\2\4\3\t\3\3\2\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\2\3\2\3\3\6\3\22\n\3\r\3\16\3\23\3\3\3\3\2\2\4\3")
        buf.write("\3\5\4\3\2\4\3\2$$\5\2\13\f\17\17\"\"\2\30\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\3\7\3\2\2\2\5\21\3\2\2\2\7\13\7$\2\2\b\n")
        buf.write("\n\2\2\2\t\b\3\2\2\2\n\r\3\2\2\2\13\t\3\2\2\2\13\f\3\2")
        buf.write("\2\2\f\16\3\2\2\2\r\13\3\2\2\2\16\17\7$\2\2\17\4\3\2\2")
        buf.write("\2\20\22\t\3\2\2\21\20\3\2\2\2\22\23\3\2\2\2\23\21\3\2")
        buf.write("\2\2\23\24\3\2\2\2\24\25\3\2\2\2\25\26\b\3\2\2\26\6\3")
        buf.write("\2\2\2\5\2\13\23\3\b\2\2")
        return buf.getvalue()


class PasswordLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRING = 1
    WS = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "STRING", "WS" ]

    ruleNames = [ "STRING", "WS" ]

    grammarFileName = "Password.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



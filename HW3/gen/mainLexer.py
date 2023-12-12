# Generated from C:/Users/silver/Desktop/comp/compiler/HW2/gen/main.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,68,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,
        1,8,1,9,1,9,5,9,48,8,9,10,9,12,9,51,9,9,1,10,4,10,54,8,10,11,10,
        12,10,55,1,11,1,11,1,11,1,11,1,12,4,12,63,8,12,11,12,12,12,64,1,
        12,1,12,0,0,13,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,0,21,0,
        23,10,25,11,1,0,3,2,0,65,90,97,122,1,0,48,57,3,0,9,9,13,13,32,32,
        68,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,
        11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,23,1,0,0,0,0,
        25,1,0,0,0,1,27,1,0,0,0,3,29,1,0,0,0,5,31,1,0,0,0,7,33,1,0,0,0,9,
        35,1,0,0,0,11,37,1,0,0,0,13,39,1,0,0,0,15,41,1,0,0,0,17,43,1,0,0,
        0,19,45,1,0,0,0,21,53,1,0,0,0,23,57,1,0,0,0,25,62,1,0,0,0,27,28,
        5,40,0,0,28,2,1,0,0,0,29,30,5,41,0,0,30,4,1,0,0,0,31,32,5,43,0,0,
        32,6,1,0,0,0,33,34,5,45,0,0,34,8,1,0,0,0,35,36,5,42,0,0,36,10,1,
        0,0,0,37,38,5,47,0,0,38,12,1,0,0,0,39,40,5,61,0,0,40,14,1,0,0,0,
        41,42,3,19,9,0,42,16,1,0,0,0,43,44,3,21,10,0,44,18,1,0,0,0,45,49,
        7,0,0,0,46,48,7,0,0,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,
        49,50,1,0,0,0,50,20,1,0,0,0,51,49,1,0,0,0,52,54,7,1,0,0,53,52,1,
        0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,22,1,0,0,0,57,
        58,5,10,0,0,58,59,1,0,0,0,59,60,6,11,0,0,60,24,1,0,0,0,61,63,7,2,
        0,0,62,61,1,0,0,0,63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,66,
        1,0,0,0,66,67,6,12,1,0,67,26,1,0,0,0,4,0,49,55,64,2,6,0,0,0,1,0
    ]

class mainLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    Plus = 3
    MINUS = 4
    MUL = 5
    DIVIDE = 6
    ASSIGN = 7
    Id = 8
    Number = 9
    Newline = 10
    Whitespace = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'='", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "Plus", "MINUS", "MUL", "DIVIDE", "ASSIGN", "Id", "Number", 
            "Newline", "Whitespace" ]

    ruleNames = [ "T__0", "T__1", "Plus", "MINUS", "MUL", "DIVIDE", "ASSIGN", 
                  "Id", "Number", "IDENTIFIER", "NUMBER", "Newline", "Whitespace" ]

    grammarFileName = "main2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



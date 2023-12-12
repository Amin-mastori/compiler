# Generated from C:/Users/silver/Desktop/comp/compiler/HW2/gen/main.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .mainParser import mainParser
else:
    from mainParser import mainParser

# This class defines a complete listener for a parse tree produced by mainParser.
class mainListener(ParseTreeListener):

    # Enter a parse tree produced by mainParser#start.
    def enterStart(self, ctx:mainParser.StartContext):
        pass

    # Exit a parse tree produced by mainParser#start.
    def exitStart(self, ctx:mainParser.StartContext):
        pass


    # Enter a parse tree produced by mainParser#rule_minus.
    def enterRule_minus(self, ctx:mainParser.Rule_minusContext):
        pass

    # Exit a parse tree produced by mainParser#rule_minus.
    def exitRule_minus(self, ctx:mainParser.Rule_minusContext):
        pass


    # Enter a parse tree produced by mainParser#rule_plus.
    def enterRule_plus(self, ctx:mainParser.Rule_plusContext):
        pass

    # Exit a parse tree produced by mainParser#rule_plus.
    def exitRule_plus(self, ctx:mainParser.Rule_plusContext):
        pass


    # Enter a parse tree produced by mainParser#rule3.
    def enterRule3(self, ctx:mainParser.Rule3Context):
        pass

    # Exit a parse tree produced by mainParser#rule3.
    def exitRule3(self, ctx:mainParser.Rule3Context):
        pass


    # Enter a parse tree produced by mainParser#term.
    def enterTerm(self, ctx:mainParser.TermContext):
        pass

    # Exit a parse tree produced by mainParser#term.
    def exitTerm(self, ctx:mainParser.TermContext):
        pass


    # Enter a parse tree produced by mainParser#fact.
    def enterFact(self, ctx:mainParser.FactContext):
        pass

    # Exit a parse tree produced by mainParser#fact.
    def exitFact(self, ctx:mainParser.FactContext):
        pass



del mainParser
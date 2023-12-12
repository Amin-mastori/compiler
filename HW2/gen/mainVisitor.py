# Generated from C:/Users/silver/Desktop/comp/compiler/HW2/gen/main.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .mainParser import mainParser
else:
    from mainParser import mainParser

# This class defines a complete generic visitor for a parse tree produced by mainParser.

class mainVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mainParser#start.
    def visitStart(self, ctx:mainParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#rule_minus.
    def visitRule_minus(self, ctx:mainParser.Rule_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#rule_plus.
    def visitRule_plus(self, ctx:mainParser.Rule_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#rule3.
    def visitRule3(self, ctx:mainParser.Rule3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#term.
    def visitTerm(self, ctx:mainParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#fact.
    def visitFact(self, ctx:mainParser.FactContext):
        return self.visitChildren(ctx)



del mainParser
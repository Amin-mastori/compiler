from antlr4 import *
from mainLexer import mainLexer
from mainParser import mainParser


def check_palindrome(input_string):

    input_stream = InputStream(input_string)


    lexer = mainLexer(input_stream)


    token_stream = CommonTokenStream(lexer)


    parser = mainParser(token_stream)


    tree = parser.palindrome()


    return parser.getNumberOfSyntaxErrors() == 0


# Example usage:
input_string = "12321"
is_palindrome = check_palindrome(input_string)
print(f"Is '{input_string}' a palindrome? {is_palindrome}")
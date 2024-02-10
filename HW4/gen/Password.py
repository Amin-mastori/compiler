from antlr4 import *
from PasswordLexer import PasswordLexer
from PasswordParser import PasswordParser
class PasswordListener(PasswordLexer):
    def exitPassword(self, ctx):
        password = ctx.getText()
        if isValidPassword(password):
            print("Valid password:", password)
        else:
            print("Invalid password:", password)

def isValidPassword(password):
    return (
        len(password) >= 8
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in '!@#$%^&*()_+{}|:"<>?`-=[]\';,./' for c in password)
    )

def process_input(input_string, lexer, parser):
    input_stream = input_string(input_string)
    lexer.inputStream = mainLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser= mainLexer(stream)
    tree = parser.password()

    listener = PasswordListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    input_string = "Password!"  # Replace with your input
    lexer = PasswordLexer(None)  # Instantiate your lexer
    parser = PasswordParser(None)  # Instantiate your parser

    process_input(input_string, lexer, parser)

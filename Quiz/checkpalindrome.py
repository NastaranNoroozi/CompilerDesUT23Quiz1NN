from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from palindromeLexer import palindromeLexer
from palindromeParser import palindromeParser

class PalindromeNumbersListener(palindromeParser):
    def __init__(self, tokens):
        super().__init__(tokens)
        self.tokens = tokens

    def enterPALINDROME(self, ctx):
        # Palindrome number found, display it
        print("Numeric Palindrome:", ctx.getText())

def find_palindrome_numbers(input_text):
    input_stream = InputStream(input_text)
    lexer = palindromeLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = palindromeParser(tokens)

    # Add the listener to the parser
    listener = palindromeLexer(tokens)
    walker = ParseTreeWalker()
    walker.walk(listener, parser.start())

# Example usage:
input_text = "123 121 456 787 1001 45654"
find_palindrome_numbers(input_text)

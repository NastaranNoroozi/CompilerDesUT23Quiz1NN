antlr4-python3-runtime==4.13.1
# PalindromeTest.py

from antlr4 import CommonTokenStream, InputStream
from PalindromeLexer import PalindromeLexer
from PalindromeParser import PalindromeParser

def is_palindrome(input_str):
    input_stream = InputStream(input_str)
    lexer = PalindromeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PalindromeParser(stream)

    tree = parser.start()

    return not parser.getNumberOfSyntaxErrors() > 0

# Example usage
input_number = "12321"
if is_palindrome(input_number):
    print(f"{input_number} is a palindrome number.")
else:
    print(f"{input_number} is not a palindrome number.")

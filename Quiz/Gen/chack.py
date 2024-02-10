from antlr4 import FileStream, CommonTokenStream
from quizLexer import quizLexer as PalindromeLexer
from quizParser import quizParser as PalindromeParser

input_stream = FileStream("input.txt")  # replace with your input file
lexer = PalindromeLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = PalindromeParser(token_stream)

parser.start()

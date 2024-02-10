# Generated from quiz1/quiz.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write(" \b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\6\3\24\n\3\r\3\16\3\25\3\4\3\4\3\5\6")
        buf.write("\5\33\n\5\r\5\16\5\34\3\5\3\5\2\2\6\3\3\5\4\7\5\t\6\3")
        buf.write("\2\4\3\2\62;\5\2\13\f\17\17\"\"\2!\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\13\3\2\2\2\5\23\3\2\2\2")
        buf.write("\7\27\3\2\2\2\t\32\3\2\2\2\13\f\5\7\4\2\f\r\5\7\4\2\r")
        buf.write("\16\5\7\4\2\16\17\5\7\4\2\17\20\5\7\4\2\20\21\b\2\2\2")
        buf.write("\21\4\3\2\2\2\22\24\5\7\4\2\23\22\3\2\2\2\24\25\3\2\2")
        buf.write("\2\25\23\3\2\2\2\25\26\3\2\2\2\26\6\3\2\2\2\27\30\t\2")
        buf.write("\2\2\30\b\3\2\2\2\31\33\t\3\2\2\32\31\3\2\2\2\33\34\3")
        buf.write("\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\36\3\2\2\2\36\37")
        buf.write("\b\5\3\2\37\n\3\2\2\2\5\2\25\34\4\3\2\2\b\2\2")
        return buf.getvalue()


class quizLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PalindromeNumber = 1
    NonPalindromeNumber = 2
    Digit = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "PalindromeNumber", "NonPalindromeNumber", "Digit", "WS" ]

    ruleNames = [ "PalindromeNumber", "NonPalindromeNumber", "Digit", "WS" ]

    grammarFileName = "quiz.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.PalindromeNumber_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def PalindromeNumber_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                        number = str(self.text)
                        reverse_number = number[::-1]
                        if number == reverse_number:
                            print(f"Found palindrome: {number}")
                    
     



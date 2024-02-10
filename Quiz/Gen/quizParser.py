# Generated from quiz1/quiz.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\30\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\7\3\21\n\3\f\3\16\3\24\13\3\3\4\3\4\3\4\2\3\4\5")
        buf.write("\2\4\6\2\3\3\2\3\4\2\25\2\b\3\2\2\2\4\13\3\2\2\2\6\25")
        buf.write("\3\2\2\2\b\t\5\4\3\2\t\n\7\2\2\3\n\3\3\2\2\2\13\f\b\3")
        buf.write("\1\2\f\r\5\6\4\2\r\22\3\2\2\2\16\17\f\4\2\2\17\21\5\6")
        buf.write("\4\2\20\16\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3")
        buf.write("\2\2\2\23\5\3\2\2\2\24\22\3\2\2\2\25\26\t\2\2\2\26\7\3")
        buf.write("\2\2\2\3\22")
        return buf.getvalue()


class quizParser ( Parser ):

    grammarFileName = "quiz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "PalindromeNumber", "NonPalindromeNumber", 
                      "Digit", "WS" ]

    RULE_start = 0
    RULE_sequence = 1
    RULE_element = 2

    ruleNames =  [ "start", "sequence", "element" ]

    EOF = Token.EOF
    PalindromeNumber=1
    NonPalindromeNumber=2
    Digit=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sequence(self):
            return self.getTypedRuleContext(quizParser.SequenceContext,0)


        def EOF(self):
            return self.getToken(quizParser.EOF, 0)

        def getRuleIndex(self):
            return quizParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = quizParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.sequence(0)
            self.state = 7
            self.match(quizParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(quizParser.ElementContext,0)


        def sequence(self):
            return self.getTypedRuleContext(quizParser.SequenceContext,0)


        def getRuleIndex(self):
            return quizParser.RULE_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)



    def sequence(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = quizParser.SequenceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_sequence, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.element()
            self._ctx.stop = self._input.LT(-1)
            self.state = 16
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = quizParser.SequenceContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_sequence)
                    self.state = 12
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 13
                    self.element() 
                self.state = 18
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PalindromeNumber(self):
            return self.getToken(quizParser.PalindromeNumber, 0)

        def NonPalindromeNumber(self):
            return self.getToken(quizParser.NonPalindromeNumber, 0)

        def getRuleIndex(self):
            return quizParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = quizParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            _la = self._input.LA(1)
            if not(_la==quizParser.PalindromeNumber or _la==quizParser.NonPalindromeNumber):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.sequence_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def sequence_sempred(self, localctx:SequenceContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         





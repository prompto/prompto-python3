# Generated from ArgsParser.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\36\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\7\2\f\n\2\f\2")
        buf.write("\16\2\17\13\2\3\3\5\3\22\n\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\5\5\34\n\5\3\5\2\2\6\2\4\6\b\2\2\2\34\2\r\3\2\2")
        buf.write("\2\4\21\3\2\2\2\6\27\3\2\2\2\b\33\3\2\2\2\n\f\5\4\3\2")
        buf.write("\13\n\3\2\2\2\f\17\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16")
        buf.write("\3\3\2\2\2\17\r\3\2\2\2\20\22\7\5\2\2\21\20\3\2\2\2\21")
        buf.write("\22\3\2\2\2\22\23\3\2\2\2\23\24\5\6\4\2\24\25\7\4\2\2")
        buf.write("\25\26\5\b\5\2\26\5\3\2\2\2\27\30\7\7\2\2\30\7\3\2\2\2")
        buf.write("\31\34\7\7\2\2\32\34\7\3\2\2\33\31\3\2\2\2\33\32\3\2\2")
        buf.write("\2\34\t\3\2\2\2\5\r\21\33")
        return buf.getvalue()


class ArgsParser ( Parser ):

    grammarFileName = "ArgsParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'='", "'-'", "' '" ]

    symbolicNames = [ "<INVALID>", "STRING", "EQUALS", "DASH", "WS", "ELEMENT" ]

    RULE_parse = 0
    RULE_entry = 1
    RULE_key = 2
    RULE_value = 3

    ruleNames =  [ "parse", "entry", "key", "value" ]

    EOF = Token.EOF
    STRING=1
    EQUALS=2
    DASH=3
    WS=4
    ELEMENT=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e = None # EntryContext

        def entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArgsParser.EntryContext)
            else:
                return self.getTypedRuleContext(ArgsParser.EntryContext,i)


        def getRuleIndex(self):
            return ArgsParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)




    def parse(self):

        localctx = ArgsParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ArgsParser.DASH or _la==ArgsParser.ELEMENT:
                self.state = 8
                localctx.e = self.entry()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.k = None # KeyContext
            self.v = None # ValueContext

        def EQUALS(self):
            return self.getToken(ArgsParser.EQUALS, 0)

        def key(self):
            return self.getTypedRuleContext(ArgsParser.KeyContext,0)


        def value(self):
            return self.getTypedRuleContext(ArgsParser.ValueContext,0)


        def DASH(self):
            return self.getToken(ArgsParser.DASH, 0)

        def getRuleIndex(self):
            return ArgsParser.RULE_entry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntry" ):
                listener.enterEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntry" ):
                listener.exitEntry(self)




    def entry(self):

        localctx = ArgsParser.EntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entry)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ArgsParser.DASH:
                self.state = 14
                self.match(ArgsParser.DASH)


            self.state = 17
            localctx.k = self.key()
            self.state = 18
            self.match(ArgsParser.EQUALS)
            self.state = 19
            localctx.v = self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELEMENT(self):
            return self.getToken(ArgsParser.ELEMENT, 0)

        def getRuleIndex(self):
            return ArgsParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = ArgsParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(ArgsParser.ELEMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArgsParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ELEMENTContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArgsParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ELEMENT(self):
            return self.getToken(ArgsParser.ELEMENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterELEMENT" ):
                listener.enterELEMENT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitELEMENT" ):
                listener.exitELEMENT(self)


    class STRINGContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArgsParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ArgsParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSTRING" ):
                listener.enterSTRING(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSTRING" ):
                listener.exitSTRING(self)



    def value(self):

        localctx = ArgsParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ArgsParser.ELEMENT]:
                localctx = ArgsParser.ELEMENTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(ArgsParser.ELEMENT)
                pass
            elif token in [ArgsParser.STRING]:
                localctx = ArgsParser.STRINGContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(ArgsParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






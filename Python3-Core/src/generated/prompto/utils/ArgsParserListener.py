# Generated from ArgsParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArgsParser import ArgsParser
else:
    from ArgsParser import ArgsParser

# This class defines a complete listener for a parse tree produced by ArgsParser.
class ArgsParserListener(ParseTreeListener):

    # Enter a parse tree produced by ArgsParser#parse.
    def enterParse(self, ctx:ArgsParser.ParseContext):
        pass

    # Exit a parse tree produced by ArgsParser#parse.
    def exitParse(self, ctx:ArgsParser.ParseContext):
        pass


    # Enter a parse tree produced by ArgsParser#entry.
    def enterEntry(self, ctx:ArgsParser.EntryContext):
        pass

    # Exit a parse tree produced by ArgsParser#entry.
    def exitEntry(self, ctx:ArgsParser.EntryContext):
        pass


    # Enter a parse tree produced by ArgsParser#key.
    def enterKey(self, ctx:ArgsParser.KeyContext):
        pass

    # Exit a parse tree produced by ArgsParser#key.
    def exitKey(self, ctx:ArgsParser.KeyContext):
        pass


    # Enter a parse tree produced by ArgsParser#ELEMENT.
    def enterELEMENT(self, ctx:ArgsParser.ELEMENTContext):
        pass

    # Exit a parse tree produced by ArgsParser#ELEMENT.
    def exitELEMENT(self, ctx:ArgsParser.ELEMENTContext):
        pass


    # Enter a parse tree produced by ArgsParser#STRING.
    def enterSTRING(self, ctx:ArgsParser.STRINGContext):
        pass

    # Exit a parse tree produced by ArgsParser#STRING.
    def exitSTRING(self, ctx:ArgsParser.STRINGContext):
        pass



del ArgsParser
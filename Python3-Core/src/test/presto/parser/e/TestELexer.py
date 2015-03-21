import unittest

from presto.parser.e.BaseELexerTest import BaseELexerTest
from presto.parser.ELexer import ELexer

class TestELexer(unittest.TestCase, BaseELexerTest):

    def testIntegerAttribute(self):
        actual = self.parseTokenNamesFromString("define id as: Integer attribute")
        expected = self.tokenNamesAsString([ELexer.DEFINE, ELexer.VARIABLE_IDENTIFIER,
                ELexer.AS, ELexer.COLON, ELexer.INTEGER,
                ELexer.ATTRIBUTE, ELexer.LF ])
        self.assertEquals(expected,actual)

    def testStringAttribute(self):
        actual = self.parseTokenNamesFromString("define name as: Text attribute")
        expected = self.tokenNamesAsString([ELexer.DEFINE, ELexer.VARIABLE_IDENTIFIER,
                ELexer.AS, ELexer.COLON, ELexer.TEXT,
                ELexer.ATTRIBUTE, ELexer.LF ])
        self.assertEquals(expected,actual)

    def testPersonCategory(self):
        actual = self.parseTokenNamesFromString("define Person as: category with attributes: id, name")
        expected = self.tokenNamesAsString([ ELexer.DEFINE, ELexer.TYPE_IDENTIFIER,
                ELexer.AS, ELexer.COLON, ELexer.CATEGORY,
                ELexer.WITH, ELexer.ATTRIBUTES, ELexer.COLON,
                ELexer.VARIABLE_IDENTIFIER, ELexer.COMMA, ELexer.VARIABLE_IDENTIFIER, ELexer.LF ])
        self.assertEquals(expected,actual)

    def testEmployeeCategoryExtendsPerson(self):
        actual = self.parseTokenNamesFromString("define Employee as: Person with attribute: company")
        expected = self.tokenNamesAsString([ ELexer.DEFINE, ELexer.TYPE_IDENTIFIER,
                ELexer.AS, ELexer.COLON, ELexer.TYPE_IDENTIFIER,
                ELexer.WITH, ELexer.ATTRIBUTE, ELexer.COLON,
                ELexer.VARIABLE_IDENTIFIER, ELexer.LF ])
        self.assertEquals(expected,actual)

    def testEmptyLine(self):
        actual = self.parseTokenNamesFromString("a\n\t\nb")
        expected = self.tokenNamesAsString([ ELexer.VARIABLE_IDENTIFIER, ELexer.LF, ELexer.LF, ELexer.VARIABLE_IDENTIFIER, ELexer.LF ])
        self.assertEquals(expected,actual)

    def test1Indent(self):
        actual = self.parseTokenNamesFromString("a\n\tb")
        expected = self.tokenNamesAsString([ ELexer.VARIABLE_IDENTIFIER, ELexer.LF,
                ELexer.INDENT, ELexer.VARIABLE_IDENTIFIER, ELexer.DEDENT, ELexer.LF ])
        self.assertEquals(expected,actual)

    def test2Indents(self):
        actual = self.parseTokenNamesFromString("aaa\n\tbbb\n\t\tccc\n\tddd")
        expected = self.tokenNamesAsString([ ELexer.VARIABLE_IDENTIFIER, ELexer.LF,
                ELexer.INDENT, ELexer.VARIABLE_IDENTIFIER, ELexer.LF,
                ELexer.INDENT, ELexer.VARIABLE_IDENTIFIER, ELexer.DEDENT, ELexer.LF,
                ELexer.VARIABLE_IDENTIFIER, ELexer.DEDENT, ELexer.LF ])
        self.assertEquals(expected,actual)

    def testCharLiteral(self):
        actual = self.parseTokenNamesFromString("'a'")
        expected = self.tokenNamesAsString([ ELexer.CHAR_LITERAL, ELexer.LF ])
        self.assertEquals(expected,actual)

    def testDateLiteral(self):
        actual = self.parseTokenNamesFromString("'2012-10-10'")
        expected = self.tokenNamesAsString([ ELexer.DATE_LITERAL, ELexer.LF ])
        self.assertEquals(expected,actual)


    def testTimeLiteral(self):
        actual = self.parseTokenNamesFromString("'10:10:10'")
        expected = self.tokenNamesAsString([ ELexer.TIME_LITERAL, ELexer.LF ])
        self.assertEquals(expected,actual)

    def testDateTimeLiteral(self):
        actual = self.parseTokenNamesFromString("'2012-10-10T10:10:10'")
        expected = self.tokenNamesAsString([ ELexer.DATETIME_LITERAL, ELexer.LF ])
        self.assertEquals(expected,actual)

    def testPeriodLiteral(self):
        actual = self.parseTokenNamesFromString("'P122Y'")
        expected = self.tokenNamesAsString([ ELexer.PERIOD_LITERAL, ELexer.LF ])
        self.assertEquals(expected,actual)

    def testRangeLiteral(self):
        actual = self.parseTokenNamesFromString("1..3")
        expected = self.tokenNamesAsString([ ELexer.INTEGER_LITERAL, ELexer.RANGE,
                ELexer.INTEGER_LITERAL, ELexer.LF ])
        self.assertEquals(expected,actual)

    def testEnumIdentifier(self):
        actual = self.parseTokenNamesFromString("ENTITY_1")
        expected = self.tokenNamesAsString([ ELexer.SYMBOL_IDENTIFIER, ELexer.LF ])
        self.assertEquals(expected,actual)

    def testMethodCallWith(self):
        actual = self.parseTokenNamesFromString("print with \"person\" + p.name as value")
        expected = self.tokenNamesAsString([ ELexer.VARIABLE_IDENTIFIER, ELexer.WITH,
                ELexer.TEXT_LITERAL, ELexer.PLUS, ELexer.VARIABLE_IDENTIFIER, ELexer.DOT,
                ELexer.VARIABLE_IDENTIFIER, ELexer.AS, ELexer.VARIABLE_IDENTIFIER, ELexer.LF ])
        self.assertEquals(expected,actual)

    def testTryStatement(self):
        # String actual = parseTokenNamesFromResource("exceptions/divideByZero.presto")
        # System.out.println(actual)
        pass

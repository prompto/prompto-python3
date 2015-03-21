import unittest
from antlr4 import ParseTreeWalker

from presto.parser.ECleverParser import ECleverParser
from presto.parser.EPrestoBuilder import EPrestoBuilder


class TestJavaParser(unittest.TestCase):

    def testReturn(self):
        statement = "return value;"
        stmt = self.parse_java_statement(statement)
        self.assertIsNotNone(stmt)
        self.assertEquals(statement,str(stmt))

    def testExpression(self):
        statement = "System.out;"
        stmt = self.parse_java_statement(statement)
        self.assertIsNotNone(stmt)
        self.assertEquals(statement,str(stmt))

    def testArray(self):
        statement = "value[15];"
        stmt = self.parse_java_statement(statement)
        self.assertIsNotNone(stmt)
        self.assertEquals(statement,str(stmt))

    def testFunction(self):
        statement = "System.out.print(value);"
        stmt = self.parse_java_statement(statement)
        self.assertIsNotNone(stmt)
        self.assertEquals(statement,str(stmt))

    def parse_java_statement(self, statement):
        parser = ECleverParser(text=statement)
        tree = parser.java_statement()
        builder = EPrestoBuilder(parser)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)

import unittest
from antlr4 import ParseTreeWalker

from prompto.parser.ECleverParser import ECleverParser
from prompto.parser.EPromptoBuilder import EPromptoBuilder


class TestJavaParser(unittest.TestCase):

    def testReturn(self):
        statement = "return value;"
        stmt = self.parse_java_statement(statement)
        self.assertIsNotNone(stmt)
        self.assertEqual(statement,str(stmt))

    def testExpression(self):
        statement = "System.out;"
        stmt = self.parse_java_statement(statement)
        self.assertIsNotNone(stmt)
        self.assertEqual(statement,str(stmt))

    def testArray(self):
        statement = "value[15];"
        stmt = self.parse_java_statement(statement)
        self.assertIsNotNone(stmt)
        self.assertEqual(statement,str(stmt))

    def testFunction(self):
        statement = "System.out.print(value);"
        stmt = self.parse_java_statement(statement)
        self.assertIsNotNone(stmt)
        self.assertEqual(statement,str(stmt))

    def parse_java_statement(self, statement):
        parser = ECleverParser(text=statement)
        tree = parser.java_statement()
        builder = EPromptoBuilder(parser)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)

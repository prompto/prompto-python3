import unittest

from prompto.argument.ExtendedArgument import ExtendedArgument
from prompto.declaration.NativeMethodDeclaration import *
from prompto.expression.AddExpression import *
from prompto.expression.InstanceExpression import InstanceExpression
from prompto.expression.MemberSelector import MemberSelector
from prompto.expression.NativeSymbol import *
from prompto.grammar.IdentifierList import *
from prompto.literal.BooleanLiteral import *
from prompto.literal.DateLiteral import *
from prompto.literal.DateTimeLiteral import *
from prompto.literal.DecimalLiteral import *
from prompto.literal.DictLiteral import *
from prompto.literal.HexaLiteral import *
from prompto.literal.IntegerLiteral import *
from prompto.literal.ListLiteral import *
from prompto.literal.PeriodLiteral import *
from prompto.literal.TextLiteral import *
from prompto.literal.TimeLiteral import *
from prompto.parser.OCleverParser import *
from prompto.runtime.Context import Context
from prompto.statement.NativeCall import NativeCall
from prompto.statement.UnresolvedCall import UnresolvedCall
from prompto.type.CategoryType import *
from prompto.type.ListType import *
from prompto.utils.CodeWriter import CodeWriter


class TestParserAtoms(unittest.TestCase):

    def testTuple(self):
        statement = "(1,\"John\",'12:12:12')"
        tl = self.parse(statement, OParser.tuple_literal)
        self.assertIsNotNone(tl)
        self.assertEquals("1", str(tl.expressions[0]))
        self.assertEquals("\"John\"", str(tl.expressions[1]))
        self.assertEquals("'12:12:12'", str(tl.expressions[2]))
        self.assertEquals("(1, \"John\", '12:12:12')", str(tl))

    def testRange(self):
        statement = "[1..100]"
        rl = self.parse(statement, OParser.range_literal)
        self.assertIsNotNone(rl)
        self.assertEquals("1", str(rl.getFirst()))
        self.assertEquals("100", str(rl.getLast()))
        writer = CodeWriter(Dialect.O, Context.newGlobalContext())
        rl.toDialect(writer)
        self.assertEquals(statement, str(writer))

    def testAttribute(self):
        statement = "attribute id : Integer;"
        ad = self.parse(statement, OParser.attribute_declaration)
        self.assertIsNotNone(ad)
        self.assertEquals("id", ad.getName())
        self.assertEquals("Integer", ad.getType().typeName)

    def testArrayAttribute(self):
        statement = "attribute id : Integer[];"
        ad = self.parse(statement, OParser.attribute_declaration)
        self.assertIsNotNone(ad)
        self.assertEquals("id", ad.getName())
        self.assertEquals("Integer[]", ad.getType().typeName)

    def testCategory1Attribute(self):
        statement = "category Person ( id );"
        cd = self.parse(statement, OParser.category_declaration)
        self.assertIsNotNone(cd)
        self.assertEquals("Person", cd.getName())
        self.assertIsNone(cd.getDerivedFrom())
        self.assertIsNotNone(cd.getAttributes())
        self.assertTrue("id" in cd.getAttributes())

    def testCategory2Attributes(self):
        statement = "category Person ( id, name );"
        cd = self.parse(statement, OParser.category_declaration)
        self.assertIsNotNone(cd)
        self.assertEquals("Person", cd.getName())
        self.assertIsNone(cd.getDerivedFrom())
        self.assertIsNotNone(cd.getAttributes())
        self.assertTrue("id" in cd.getAttributes())
        self.assertTrue("name" in cd.getAttributes())

    def testCategory1Derived1Attribute(self):
        statement = "category Employee( company ) extends Person;"
        cd = self.parse(statement, OParser.category_declaration)
        self.assertIsNotNone(cd)
        self.assertEquals("Employee", cd.getName())
        self.assertIsNotNone(cd.getDerivedFrom())
        self.assertTrue("Person" in cd.getDerivedFrom())
        self.assertIsNotNone(cd.getAttributes())
        self.assertTrue("company" in cd.getAttributes())

    def testCategory2DerivedNoAttribute(self):
        statement = "category Entrepreneur extends Person, Company;"
        cd = self.parse(statement, OParser.category_declaration)
        self.assertIsNotNone(cd)
        self.assertEquals("Entrepreneur", cd.getName())
        self.assertIsNotNone(cd.getDerivedFrom())
        self.assertTrue("Person" in cd.getDerivedFrom())
        self.assertTrue("Company" in cd.getDerivedFrom())
        self.assertIsNone(cd.getAttributes())

    def testMemberExpression(self):
        statement = "p.name"
        me = self.parse(statement, OParser.instance_expression)
        self.assertIsInstance(me, MemberSelector)
        self.assertEquals("name", me.getName())
        self.assertIsInstance(me.getParent(), InstanceExpression)
        uie = me.getParent()
        self.assertEquals("p", uie.getName())

    def testArgument(self):
        statement = "Person p"
        a = self.parse(statement, OParser.typed_argument)
        self.assertIsNotNone(a)
        self.assertEquals("Person", a.getType().typeName)
        self.assertEquals("p", a.getName())

    def testList1Argument(self):
        statement = "Person p"
        l = self.parse(statement, OParser.argument_list)
        self.assertIsNotNone(l)
        self.assertEquals(1, len(l))

    def testList2ArgumentsComma(self):
        statement = "Person p, Employee e"
        l = self.parse(statement, OParser.argument_list)
        self.assertIsNotNone(l)
        self.assertEquals(2, len(l))

    def testMethodCallExpression(self):
        statement = "print (\"person\" + p.name );"
        ac = self.parse(statement, OParser.method_call)
        self.assertIsNotNone(ac)

    def testMethodCallWith(self):
        statement = "print(value = \"person\" + p.name)"
        mc = self.parse(statement, OParser.method_call)
        self.assertIsNotNone(mc)
        self.assertEquals("print", mc.caller.name)
        self.assertIsNotNone(mc.getAssignments())
        ass = mc.getAssignments()[0]
        self.assertEquals("value", ass.getName())
        exp = ass.getExpression()
        self.assertIsInstance(exp, AddExpression)
        writer = CodeWriter(Dialect.O, Context.newGlobalContext())
        mc.toDialect(writer)
        self.assertEquals(statement, str(writer))

    def testMethod1Parameter1Statement(self):
        statement = "method printName ( Person p ) { print ( value = \"person\" + p.name); }"
        ad = self.parse(statement, OParser.concrete_method_declaration)
        self.assertIsNotNone(ad)
        self.assertEquals("printName", ad.getName())
        self.assertIsNotNone(ad.getArguments())
        expected = CategoryArgument(CategoryType("Person"), "p")
        self.assertTrue(expected in ad.getArguments())
        self.assertIsNotNone(ad.getStatements())
        writer = CodeWriter(Dialect.O, Context.newGlobalContext())
        ad.getStatements()[0].toDialect(writer)
        self.assertEquals("print(value = \"person\" + p.name)", str(writer))

    def testMethod1Extended1Statement(self):
        statement = "method printName ( Object(name) o ) { print ( value = \"object\" + o.name ); }"
        ad = self.parse(statement, OParser.concrete_method_declaration)
        self.assertIsNotNone(ad)
        self.assertEquals("printName", ad.getName())
        self.assertIsNotNone(ad.getArguments())
        expected = ExtendedArgument(CategoryType("Object"), "o", IdentifierList("name"))
        self.assertTrue(expected in ad.getArguments())
        self.assertIsNotNone(ad.getStatements())
        writer = CodeWriter(Dialect.O, Context.newGlobalContext())
        ad.getStatements()[0].toDialect(writer)
        self.assertEquals("print(value = \"object\" + o.name)", str(writer))

    def testMethod1Array1Statement(self):
        statement = "method printName ( Option[] options ) { print ( value = \"array\" + options ); }"
        ad = self.parse(statement, OParser.concrete_method_declaration)
        self.assertIsNotNone(ad)
        self.assertEquals("printName", ad.getName())
        self.assertIsNotNone(ad.getArguments())
        expected = CategoryArgument(ListType(CategoryType("Option")), "options")
        self.assertTrue(expected in ad.getArguments())
        self.assertIsNotNone(ad.getStatements())
        writer = CodeWriter(Dialect.O, Context.newGlobalContext())
        ad.getStatements()[0].toDialect(writer)
        self.assertEquals("print(value = \"array\" + options)", str(writer))

    def testConstructor1Attribute(self):
        statement = "Company(id=1)"
        c = self.parse(statement, OParser.constructor_expression)
        self.assertIsNotNone(c)

    def testConstructorFrom1Attribute(self):
        statement = "Company(entity,id=1)"
        c = self.parse(statement, OParser.constructor_expression)
        self.assertIsNotNone(c)

    def testConstructor2AttributesComma(self):
        statement = "Company(id=1, name=\"IBM\")"
        c = self.parse(statement, OParser.constructor_expression)
        self.assertIsNotNone(c)
        l = c.getAssignments()
        self.assertIsNotNone(l)
        self.assertEquals(2, len(l))
        a = l[0]
        self.assertIsNotNone(a)
        self.assertEquals("id", a.getName())
        e = a.getExpression()
        self.assertIsNotNone(e)
        self.assertIsInstance(e, IntegerLiteral)
        a = l[1]
        self.assertIsNotNone(a)
        self.assertEquals("name", a.getName())
        e = a.getExpression()
        self.assertIsNotNone(e)
        self.assertIsInstance(e, TextLiteral)

    def testAssignmentConstructor(self):
        statement = "c = Company ( id = 1, name = \"IBM\" );"
        a = self.parse(statement, OParser.assign_instance_statement)
        self.assertIsNotNone(a)
        self.assertIsInstance(a.getExpression(), UnresolvedCall)

    def testNativeJava(self):
        statement = "Java: System.out.println(value);"
        call = self.parse(statement, OParser.native_statement)
        self.assertIsNotNone(call)
        self.assertIsInstance(call, NativeCall)

    def testNativeCSharp(self):
        statement = "C#: Console.println(value);"
        call = self.parse(statement, OParser.native_statement)
        self.assertIsNotNone(call)
        self.assertIsInstance(call, NativeCall)

    def testNativeMethod(self):
        statement = "native method print (String value) { \r\n" \
                    + "\tJava: System.out.println(value); \r\n" \
                    + "\tC#: Console.println(value); }"
        method = self.parse(statement, OParser.native_method_declaration)
        self.assertIsNotNone(method)
        self.assertIsInstance(method, NativeMethodDeclaration)

    def testBooleanLiteral(self):
        statement = "true"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, BooleanLiteral)
        self.assertEquals("true", str(literal))
        self.assertEquals(True, literal.getValue().getValue())
        statement = "false"
        parser = OCleverParser(text=statement)
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, BooleanLiteral)
        self.assertEquals("false", str(literal))
        self.assertEquals(False, literal.getValue().getValue())

    def testStringLiteral(self):
        statement = "\"hello\""
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, TextLiteral)
        self.assertEquals("\"hello\"", literal.text)
        self.assertEquals("hello", literal.getValue().getValue())

    def testIntegerLiteral(self):
        statement = "1234"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, IntegerLiteral)
        self.assertEquals("1234", str(literal))
        self.assertEquals(1234, literal.getValue().IntegerValue())

    def testParseHexa(self):
        self.assertEquals(0x0A11, HexaLiteral.parseHexa("0x0A11").IntegerValue())

    def testHexaLiteral(self):
        statement = "0x0A11"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, HexaLiteral)
        self.assertEquals("0x0A11", literal.text)
        self.assertEquals(0x0A11, literal.getValue().IntegerValue())

    def testDecimalLiteral(self):
        statement = "1234.13"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DecimalLiteral)
        self.assertEquals("1234.13", str(literal))
        self.assertEquals(1234.13, literal.getValue().DecimalValue(), 0.0000001)

    def testEmptyListLiteral(self):
        statement = "[]"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, ListLiteral)
        self.assertEquals("[]", str(literal))
        self.assertEquals(0, literal.getValue().size())

    def testSimpleListLiteral(self):
        statement = "[john, 123]"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertEquals("[john, 123]", literal.text)
        self.assertIsInstance(literal, ListLiteral)
        self.assertEquals(2, len(literal.expressions))
        self.assertIsInstance(literal.expressions[0], InstanceExpression)
        self.assertIsInstance(literal.expressions[1], IntegerLiteral)

    def testEmptyDictLiteral(self):
        statement = "{}"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DictLiteral)
        self.assertEquals("{}", str(literal))

    def testSimpleDictLiteral(self):
        statement = "{ \"john\" : 1234, eric : 5678 }"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DictLiteral)
        writer = CodeWriter(Dialect.O, Context.newGlobalContext())
        literal.toDialect(writer)
        self.assertEquals('{"john":1234, eric:5678}', str(writer))

    def testSimpleDate(self):
        statement = "'2012-10-09'"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DateLiteral)
        self.assertEquals("'2012-10-09'", literal.text)
        self.assertEquals(date(2012, 10, 9), literal.getValue().getValue())

    def testSimpleTime(self):
        statement = "'15:03:10'"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, TimeLiteral)
        self.assertEquals("'15:03:10'", literal.text)
        self.assertEquals(time(15, 3, 10), literal.getValue().getValue())

    def testDateTime(self):
        statement = "'2012-10-09T15:18:17'"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DateTimeLiteral)
        self.assertEquals("'2012-10-09T15:18:17'", literal.text)
        self.assertEquals(datetime(2012, 10, 9, 15, 18, 17), literal.getValue().getValue())

    def testDateTimeWithMillis(self):
        statement = "'2012-10-09T15:18:17.487'"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DateTimeLiteral)
        self.assertEquals("'2012-10-09T15:18:17.487'", literal.text)
        self.assertEquals(datetime(2012, 10, 9, 15, 18, 17, 487000), literal.getValue().getValue())

    def testDateTimeWithTZ(self):
        statement = "'2012-10-09T15:18:17+02:00'"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DateTimeLiteral)
        self.assertEquals("'2012-10-09T15:18:17+02:00'", literal.text)
        #ZoneInfoProvider provider = new ZoneInfoProvider("org/joda/time/tz/data")
        #DateTimeZone tz = provider.getZone("Etc/GMT-2")
        #expected = datetime(2012, 10, 9, 15, 18, 17, tz)
        actual = literal.getValue().getValue()
        #self.assertTrue(expected.isEqual(actual))

    def testPeriod(self):
        statement = "'P3Y'"
        literal = self.parse(statement, OParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, PeriodLiteral)
        self.assertEquals("'P3Y'", literal.text)
        self.assertEquals(3, literal.getValue().years)

    def testNativeSymbol(self):
        statement = 'ENTITY_1 = "1";'
        symbol = self.parse(statement, OParser.native_symbol)
        self.assertIsNotNone(symbol)
        self.assertIsInstance(symbol, NativeSymbol)
        writer = CodeWriter(Dialect.O, Context.newGlobalContext())
        symbol.toDialect(writer)
        self.assertEquals(statement, str(writer) + ";")

    def testExpressionWith(self):
        statement = "x = print(value = \"1\");"
        stmt = self.parse(statement, OParser.statement)
        self.assertIsNotNone(stmt)
        writer = CodeWriter(Dialect.O, Context.newGlobalContext())
        stmt.toDialect(writer)
        self.assertEquals(statement, str(writer) + ";")

    def testMethodWith(self):
        statement = "print(\"a\", value = \"1\");"
        stmt = self.parse(statement, OParser.statement)
        self.assertIsNotNone(stmt)
        writer = CodeWriter(Dialect.O, Context.newGlobalContext())
        stmt.toDialect(writer)
        self.assertEquals(statement, str(writer) + ";")

    def testInstanceExpression(self):
        statement = "prefix"
        exp = self.parse(statement, OParser.expression)
        self.assertIsInstance(exp, InstanceExpression)

    def parse(self, statement, method):
        parser = OCleverParser(text=statement)
        tree = method(parser)
        builder = OPromptoBuilder(parser)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)

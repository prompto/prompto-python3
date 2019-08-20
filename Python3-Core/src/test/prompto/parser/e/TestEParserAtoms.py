import unittest
from datetime import datetime

from prompto.param.ExtendedParameter import ExtendedParameter
from prompto.expression.MemberSelector import MemberSelector
from prompto.declaration.NativeMethodDeclaration import *
from prompto.expression.PlusExpression import *
from prompto.expression.NativeSymbol import *
from prompto.expression.UnresolvedSelector import UnresolvedSelector
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
from prompto.parser.ECleverParser import *
from prompto.statement.NativeCall import NativeCall
from prompto.statement.UnresolvedCall import UnresolvedCall
from prompto.type.CategoryType import *
from prompto.type.ListType import *
from prompto.utils.CodeWriter import CodeWriter
from prompto.runtime.Context import Context


class TestParserAtoms(unittest.TestCase):


    def testTuple(self):
        statement = "(1,\"John\",'12:12:12')"
        tl = self.parse(statement,ECleverParser.tuple_literal)
        self.assertIsNotNone(tl)
        self.assertEqual("1",str(tl.expressions[0]))
        self.assertEqual("\"John\"",str(tl.expressions[1]))
        self.assertEqual("'12:12:12'",str(tl.expressions[2]))
        self.assertEqual("(1, \"John\", '12:12:12')", str(tl))


    def testRange(self):
        statement = "[1..100]"
        rl = self.parse(statement,ECleverParser.range_literal)
        self.assertIsNotNone(rl)
        self.assertEqual("1",str(rl.getFirst()))
        self.assertEqual("100",str(rl.getLast()))
        self.assertEqual("[1..100]",str(rl))


    def testAttribute(self):
        statement = "define id as Integer attribute"
        ad = self.parse(statement,ECleverParser.attribute_declaration)
        self.assertIsNotNone(ad)
        self.assertEqual("id",ad.getName())
        self.assertEqual("Integer",ad.getType().typeName)


    def testArrayAttribute(self):
        statement = "define id as Integer[] attribute"
        ad = self.parse(statement,ECleverParser.attribute_declaration)
        self.assertIsNotNone(ad)
        self.assertEqual("id",ad.getName())
        self.assertEqual("Integer[]",ad.getType().typeName)


    def testCategory1Attribute(self):
        statement = "define Person as category with attribute id "
        cd = self.parse(statement,ECleverParser.category_declaration)
        self.assertIsNotNone(cd)
        self.assertEqual("Person",cd.getName())
        self.assertIsNone(cd.getDerivedFrom())
        self.assertIsNotNone(cd.getAttributes())
        self.assertTrue("id" in cd.getAttributes())


    def testCategory2Attributes(self):
        statement = "define Person as category with attributes id, name"
        cd = self.parse(statement,ECleverParser.category_declaration)
        self.assertIsNotNone(cd)
        self.assertEqual("Person",cd.getName())
        self.assertIsNone(cd.getDerivedFrom())
        self.assertIsNotNone(cd.getAttributes())
        self.assertTrue("id" in cd.getAttributes())
        self.assertTrue("name" in cd.getAttributes())


    def testCategory1Derived1Attribute(self):
        statement = "define Employee as Person with attribute company"
        cd = self.parse(statement,ECleverParser.category_declaration)
        self.assertIsNotNone(cd)
        self.assertEqual("Employee",cd.getName())
        self.assertIsNotNone(cd.getDerivedFrom())
        self.assertTrue("Person" in cd.getDerivedFrom())
        self.assertIsNotNone(cd.getAttributes())
        self.assertTrue("company" in cd.getAttributes())



    def testCategory2DerivedNoAttribute(self):
        statement = "define Entrepreneur as Person and Company"
        cd = self.parse(statement, ECleverParser.category_declaration)
        self.assertIsNotNone(cd)
        self.assertEqual("Entrepreneur",cd.getName())
        self.assertIsNotNone(cd.getDerivedFrom())
        self.assertTrue("Person" in cd.getDerivedFrom())
        self.assertTrue("Company" in cd.getDerivedFrom())
        self.assertIsNone(cd.getAttributes())



    def testMemberExpression(self):
        statement = "p.name"
        me = self.parse(statement,ECleverParser.instance_expression)
        self.assertIsInstance(me, UnresolvedSelector)
        self.assertEqual("name",me.name)
        self.assertIsInstance(me.getParent(), UnresolvedIdentifier)
        uie = me.getParent()
        self.assertEqual("p",uie.getName())



    def testArgument(self):
        statement = "Person p"
        a = self.parse(statement, ECleverParser.typed_argument)
        self.assertIsNotNone(a)
        self.assertEqual("Person",a.getType().typeName)
        self.assertEqual("p",a.getName())



    def testList1Argument(self):
        statement = "Person p"
        l = self.parse(statement,ECleverParser.argument_list)
        self.assertIsNotNone(l)
        self.assertEqual(1,len(l))



    def testList2ArgumentsComma(self):
        statement = "Person p, Employee e"
        l = self.parse(statement,ECleverParser.argument_list)
        self.assertIsNotNone(l)
        self.assertEqual(2,len(l))



    def testList2ArgumentsAnd(self):
        statement = "Person p and Employee e"
        l = self.parse(statement,ECleverParser.full_argument_list)
        self.assertIsNotNone(l)
        self.assertEqual(2,len(l))



    def testMethodCallExpression(self):
        statement = "print \"person\" + p.name"
        ac = self.parse(statement,ECleverParser.method_call_statement)
        self.assertIsNotNone(ac)



    def testSimpleArgumentAssignment(self):
        statement = "p.name as value"
        as_ = self.parse(statement,ECleverParser.argument_assignment)
        self.assertEqual("value",as_.getName())
        exp = as_.getExpression()
        self.assertIsNotNone(exp)
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        as_.toDialect(writer)
        self.assertEqual("p.name as value",str(writer))



    def testComplexArgumentAssignment(self):
        statement = "\"person\" + p.name as value"
        as_ = self.parse(statement,ECleverParser.argument_assignment)
        self.assertEqual("value",as_.getName())
        exp = as_.getExpression()
        self.assertIsInstance(exp, PlusExpression)
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        as_.toDialect(writer)
        self.assertEqual(statement, str(writer))



    def testArgumentAssignmentList1Arg(self):
        statement = "with \"person\" + p.name as value"
        ls = self.parse(statement, ECleverParser.argument_assignment_list)
        as_ = ls[0]
        self.assertEqual("value",as_.getName())
        exp = as_.getExpression()
        self.assertIsInstance(exp, PlusExpression)
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        as_.toDialect(writer)
        self.assertEqual("\"person\" + p.name as value",str(writer))




    def testMethodCallWith(self):
        statement = "print with \"person\" + p.name as value"
        mc = self.parse(statement,ECleverParser.method_call_statement)
        self.assertIsNotNone(mc)
        self.assertEqual("print",mc.caller.getName())
        self.assertIsNotNone(mc.arguments)
        argument = mc.arguments[0]
        self.assertEqual("value",argument.getName())
        exp = argument.getExpression()
        self.assertIsInstance(exp, PlusExpression)
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        mc.toDialect(writer)
        self.assertEqual("print with \"person\" + p.name as value",str(writer))




    def testMethod1Parameter1Statement(self):
        statement = "define printName as method receiving Person p doing:\r\n" \
                + "\tprint with \"person\" + p.name as value"
        ad = self.parse(statement,ECleverParser.concrete_method_declaration)
        self.assertIsNotNone(ad)
        self.assertEqual("printName",ad.getName())
        self.assertIsNotNone(ad.getArguments())
        expected = CategoryParameter(CategoryType("Person"), "p")
        self.assertTrue(expected in ad.getArguments())
        self.assertIsNotNone(ad.getStatements())
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        ad.getStatements()[0].toDialect(writer)
        self.assertEqual("print with \"person\" + p.name as value",str(writer))




    def testMethod1Extended1Statement(self):
        statement = "define printName as method receiving Object o with attribute name doing:\r\n" \
                + "\tprint with \"object\" + o.name as value"
        ad = self.parse(statement,ECleverParser.concrete_method_declaration)
        self.assertIsNotNone(ad)
        self.assertEqual("printName",ad.getName())
        self.assertIsNotNone(ad.getArguments())
        expected = ExtendedParameter(CategoryType("Object"), "o", IdentifierList("name"))
        self.assertTrue(expected in ad.getArguments())
        self.assertIsNotNone(ad.getStatements())
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        ad.getStatements()[0].toDialect(writer)
        self.assertEqual("print with \"object\" + o.name as value",str(writer))




    def testMethod1Array1Statement(self):
        statement = "define printName as method receiving Option[] options doing:\r\n" \
                + "\tprint with \"array\" + args as value"
        ad = self.parse(statement,ECleverParser.concrete_method_declaration)
        self.assertIsNotNone(ad)
        self.assertEqual("printName",ad.getName())
        self.assertIsNotNone(ad.getArguments())
        expected = CategoryParameter(ListType(CategoryType("Option")), "options")
        self.assertTrue(expected in ad.getArguments())
        self.assertIsNotNone(ad.getStatements())
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        ad.getStatements()[0].toDialect(writer)
        self.assertEqual("print with \"array\" + args as value",str(writer))


    def testConstructor1Attribute(self):
        statement = "Company with 1 as id"
        c = self.parse(statement,ECleverParser.constructor_expression)
        self.assertIsNotNone(c)


    def testConstructorFrom1Attribute(self):
        statement = "Company from entity with 1 as_ id"
        c = self.parse(statement,ECleverParser.constructor_expression)
        self.assertIsNotNone(c)

    def testConstructor2AttributesComma(self):
        statement = "Company with 1 as id, \"IBM\" as name"
        c = self.parse(statement,ECleverParser.constructor_expression)
        self.assertIsNotNone(c)
        l = c.getArguments()
        self.assertIsNotNone(l)
        self.assertEqual(2, len(l))
        a = l[0]
        self.assertIsNotNone(a)
        self.assertEqual("id",a.getName())
        e = a.getExpression()
        self.assertIsNotNone(e)
        self.assertIsInstance(e, IntegerLiteral)
        a = l[1]
        self.assertIsNotNone(a)
        self.assertEqual("name",a.getName())
        e = a.getExpression()
        self.assertIsNotNone(e)
        self.assertIsInstance(e, TextLiteral)


    def testConstructor2AttributesAnd(self):
        statement = "Company with 1 as id and \"IBM\" as name"
        c = self.parse(statement,ECleverParser.constructor_expression)
        self.assertIsNotNone(c)
        l = c.getArguments()
        self.assertIsNotNone(l)
        self.assertEqual(2, len(l))
        a = l[0]
        self.assertIsNotNone(a)
        self.assertEqual("id",a.getName())
        e = a.getExpression()
        self.assertIsNotNone(e)
        self.assertIsInstance(e, IntegerLiteral)
        a = l[1]
        self.assertIsNotNone(a)
        self.assertEqual("name",a.getName())
        e = a.getExpression()
        self.assertIsNotNone(e)
        self.assertIsInstance(e, TextLiteral)


    def testAssignmentConstructor(self):
        statement = "c = Company with 1 as id and \"IBM\" as name"
        a = self.parse(statement,ECleverParser.assign_instance_statement)
        self.assertIsNotNone(a)
        self.assertIsInstance(a.getExpression(), UnresolvedCall)

    def testNativeJava(self):
        statement = "Java: System.out.println(value);"
        call = self.parse(statement,ECleverParser.native_statement)
        self.assertIsNotNone(call)
        self.assertIsInstance(call, NativeCall)

    def testNativeCSharp(self):
        statement = "C#: Console.println(value);"
        call = self.parse(statement,ECleverParser.native_statement)
        self.assertIsNotNone(call)
        self.assertIsInstance(call, NativeCall)

    def testNativeMethod(self):
        statement = "define print as native method receiving String value doing:\r\n" \
                + "\tJava: System.out.println(value); \r\n" \
                + "\tC#: Console.println(value); "
        method = self.parse(statement,ECleverParser.native_method_declaration)
        self.assertIsNotNone(method)
        self.assertIsInstance(method, NativeMethodDeclaration)

    def testBooleanLiteral(self):
        statement = "true"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, BooleanLiteral)
        self.assertEqual("true", str(literal))
        self.assertEqual(True, literal.getValue().getValue())
        statement = "false"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, BooleanLiteral)
        self.assertEqual("false", str(literal))
        self.assertEqual(False, literal.getValue().getValue())



    def testTextLiteral(self):
        statement = "\"hello\""
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, TextLiteral)
        self.assertEqual("\"hello\"", literal.text)
        self.assertEqual("hello", literal.getValue().getValue())



    def testIntegerLiteral(self):
        statement = "1234"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, IntegerLiteral)
        self.assertEqual("1234", str(literal))
        self.assertEqual(1234, literal.getValue().IntegerValue())



    def testParseHexa(self):
        self.assertEqual(0x0A11, HexaLiteral.parseHexa("0x0A11").IntegerValue())



    def testHexaLiteral(self):
        statement = "0x0A11"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, HexaLiteral)
        self.assertEqual("0x0A11", literal.text)
        self.assertEqual(0x0A11, literal.getValue().IntegerValue())



    def testDecimalLiteral(self):
        statement = "1234.13"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DecimalLiteral)
        self.assertEqual("1234.13", str(literal))
        self.assertEqual(1234.13, literal.getValue().DecimalValue(),0.0000001)



    def testEmptyListLiteral(self):
        statement = "[]"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, ListLiteral)
        self.assertEqual("[]", str(literal))
        self.assertEqual(0, literal.getValue().size())



    def testSimpleListLiteral(self):
        statement = "[ john, 123 ]"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertEqual("[john, 123]", str(literal))
        self.assertIsInstance(literal, ListLiteral)
        self.assertEqual(2, len(literal.expressions))
        self.assertIsInstance(literal.expressions[0], UnresolvedIdentifier)
        self.assertIsInstance(literal.expressions[1], IntegerLiteral)



    def testEmptyDictLiteral(self):
        statement = "<:>"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DictLiteral)
        self.assertEqual("<:>", str(literal))



    def testSimpleDictLiteral(self):
        statement = "< \"john\" : 1234, eric : 5678 >"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DictLiteral)
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        literal.toDialect(writer)
        self.assertEqual('<"john":1234, eric:5678>', str(writer))



    def testSimpleDate(self):
        statement = "'2012-10-09'"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DateLiteral)
        self.assertEqual("'2012-10-09'", literal.text)
        self.assertEqual(date(2012, 10, 9), literal.getValue().getValue())



    def testSimpleTime(self):
        statement = "'15:03:10'"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, TimeLiteral)
        self.assertEqual("'15:03:10'", literal.text)
        self.assertEqual(time(15, 3, 10), literal.getValue().getValue())



    def testDateTime(self):
        statement = "'2012-10-09T15:18:17'"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DateTimeLiteral)
        self.assertEqual("'2012-10-09T15:18:17'", literal.text)
        self.assertEqual(datetime(2012, 10, 9, 15, 18, 17), literal.getValue().getValue())



    def testDateTimeWithMillis(self):
        statement = "'2012-10-09T15:18:17.487'"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DateTimeLiteral)
        self.assertEqual("'2012-10-09T15:18:17.487'", literal.text)
        self.assertEqual(datetime(2012, 10, 9, 15, 18, 17, 487000), literal.getValue().getValue())



    def testDateTimeWithTZ(self):
        statement = "'2012-10-09T15:18:17+02:00'"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, DateTimeLiteral)
        self.assertEqual("'2012-10-09T15:18:17+02:00'", literal.text)
        #ZoneInfoProvider provider = new ZoneInfoProvider("org/joda/time/tz/data")
        #DateTimeZone tz = provider.getZone("Etc/GMT-2")
        #DateTime expected = new DateTime(2012, 10, 9, 15, 18, 17, tz)
        #DateTime actual = ((DateTimeLiteral)literal).getValue().getValue()
        #self.assertEqual(expected, actual)

    def testPeriod(self):
        statement = "'P3Y'"
        literal = self.parse(statement, ECleverParser.literal_expression)
        self.assertIsNotNone(literal)
        self.assertIsInstance(literal, PeriodLiteral)
        self.assertEqual("'P3Y'", literal.text)
        self.assertEqual(3,literal.getValue().years)



    def testNativeSymbol(self):
        statement = "ENTITY_1 with \"1\" as value"
        symbol = self.parse(statement, ECleverParser.native_symbol)
        self.assertIsNotNone(symbol)
        self.assertIsInstance(symbol, NativeSymbol)
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        symbol.toDialect(writer)
        self.assertEqual(statement, str(writer))



    def testExpressionWith(self):
        statement = "x = print with \"1\" as value"
        stmt = self.parse(statement, ECleverParser.statement)
        self.assertIsNotNone(stmt)
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        stmt.toDialect(writer)
        self.assertEqual(statement, str(writer))


    def testMethodWith(self):
        statement = "print \"a\" with \"1\" as value"
        stmt = self.parse(statement, ECleverParser.statement)
        self.assertIsNotNone(stmt)
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        stmt.toDialect(writer)
        self.assertEqual(statement, str(writer))

    def parse(self, statement, method):
        parser = ECleverParser(text=statement)
        parser._input.tokenSource.addLF = False
        tree = method(parser)
        builder = EPromptoBuilder(parser)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)

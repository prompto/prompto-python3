from prompto.param.CategoryParameter import CategoryParameter
from prompto.param.ExtendedParameter import ExtendedParameter
from prompto.grammar.IdentifierList import IdentifierList
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.type.AnyType import AnyType
from prompto.type.BooleanType import BooleanType
from prompto.type.CategoryType import CategoryType
from prompto.type.DateTimeType import DateTimeType
from prompto.type.DateType import DateType
from prompto.type.DecimalType import DecimalType
from prompto.type.IntegerType import IntegerType
from prompto.type.MissingType import MissingType
from prompto.type.TextType import TextType


class TestAnonymousTypes(BaseEParserTest):

    def setUp(self):
        super(TestAnonymousTypes, self).setUp()
        stmts = self.parseString("define id as Integer attribute\r\n" +
                             "define name as String attribute\r\n" +
                             "define other as String attribute\r\n" +
                             "define Simple as category with attribute name\r\n" +
                             "define Root as category with attribute id\r\n" +
                             "define DerivedWithOther as Root with attribute other\r\n" +
                             "define DerivedWithName as Root with attribute name\r\n")
        stmts.register(self.context)


    def testAnonymousAnyType(self):
        # any x
        argument = CategoryParameter(AnyType.instance, "x")
        argument.register(self.context)
        st = argument.getType(self.context)
        self.assertIsInstance(st, AnyType)
        self.assertTrue(st.isAssignableFrom(self.context, BooleanType.instance))
        self.assertTrue(st.isAssignableFrom(self.context, IntegerType.instance))
        self.assertTrue(st.isAssignableFrom(self.context, DecimalType.instance))
        self.assertTrue(st.isAssignableFrom(self.context, TextType.instance))
        self.assertTrue(st.isAssignableFrom(self.context, DateType.instance))
        self.assertTrue(st.isAssignableFrom(self.context, DateTimeType.instance))
        self.assertTrue(st.isAssignableFrom(self.context, MissingType.instance))  # missing type always compatible
        self.assertTrue(st.isAssignableFrom(self.context, AnyType.instance))
        self.assertTrue(st.isAssignableFrom(self.context, CategoryType("Simple")))
        self.assertTrue(st.isAssignableFrom(self.context, CategoryType("Root")))
        self.assertTrue(st.isAssignableFrom(self.context, CategoryType("DerivedWithOther")))
        self.assertTrue(st.isAssignableFrom(self.context, CategoryType("DerivedWithName")))


    def testAnonymousAnyTypeWithAttribute(self):
        # any x with attribute: name
        list = IdentifierList("name")
        argument = ExtendedParameter(AnyType.instance, "x", list)
        argument.register(self.context)
        st = argument.getType(self.context)
        self.assertIsInstance(st, CategoryType)
        self.assertFalse(st.isAssignableFrom(self.context, BooleanType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, IntegerType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, DecimalType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, TextType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, DateType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, DateTimeType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, MissingType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, AnyType.instance))  # any type never compatible
        self.assertTrue(st.isAssignableFrom(self.context, CategoryType("Simple")))  # since Simple has a name
        self.assertFalse(st.isAssignableFrom(self.context, CategoryType("Root")))  # since Root has no name
        self.assertFalse(
            st.isAssignableFrom(self.context, CategoryType("DerivedWithOther")))  # since DerivedWithOther has no name
        self.assertTrue(
            st.isAssignableFrom(self.context, CategoryType("DerivedWithName")))  # since DerivedWithName has a name


    def testAnonymousCategoryType(self):
        # Root x
        argument = CategoryParameter(CategoryType("Root"), "x")
        argument.register(self.context)
        st = argument.getType(self.context)
        self.assertIsInstance(st, CategoryType)
        self.assertFalse(st.isAssignableFrom(self.context, BooleanType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, IntegerType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, DecimalType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, TextType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, DateType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, DateTimeType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, MissingType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, AnyType.instance))  # any type never compatible
        self.assertFalse(st.isAssignableFrom(self.context, CategoryType("Simple")))  # since Simple does not extend Root
        self.assertTrue(st.isAssignableFrom(self.context, CategoryType("Root")))  # since Root is Root
        self.assertTrue(
            st.isAssignableFrom(self.context, CategoryType("DerivedWithOther")))  # since DerivedWithOther extends Root
        self.assertTrue(
            st.isAssignableFrom(self.context, CategoryType("DerivedWithName")))  # since DerivedWithName extends Root


    def testAnonymousCategoryTypeWithAttribute(self):
        # Root x with attribute: name
        list = IdentifierList("name")
        argument = ExtendedParameter(CategoryType("Root"), "test", list)
        argument.register(self.context)
        st = argument.getType(self.context)
        self.assertIsInstance(st, CategoryType)
        self.assertFalse(st.isAssignableFrom(self.context, BooleanType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, IntegerType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, DecimalType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, TextType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, DateType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, DateTimeType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, MissingType.instance))
        self.assertFalse(st.isAssignableFrom(self.context, AnyType.instance))  # any type never compatible
        self.assertFalse(st.isAssignableFrom(self.context, CategoryType("Simple")))  # since Simple does not extend Root
        self.assertFalse(st.isAssignableFrom(self.context, CategoryType("Root")))  # since Root has no name
        self.assertFalse(
            st.isAssignableFrom(self.context, CategoryType("DerivedWithOther")))  # since DerivedWithOther has no name
        self.assertTrue(
            st.isAssignableFrom(self.context, CategoryType("DerivedWithName")))  # since DerivedWithName has a name

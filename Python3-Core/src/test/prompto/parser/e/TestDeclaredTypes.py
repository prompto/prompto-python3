from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.type.IntegerType import IntegerType
from prompto.type.DecimalType import DecimalType
from prompto.type.TextType import TextType
from prompto.type.DateType import DateType
from prompto.type.DateTimeType import DateTimeType
from prompto.type.MissingType import MissingType
from prompto.type.CategoryType import CategoryType
from prompto.type.AnyType import AnyType
from prompto.type.BooleanType import BooleanType


class TestDeclaredTypes(BaseEParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        self.registerCategoryTypes()

    def registerCategoryTypes(self):
        stmts = self.parseString("define id as: Integer attribute\r\n" +
                                 "define name as: String attribute\r\n" +
                                 "define Root as: category with attribute: id\r\n" +
                                 "define Derived as: Root with attribute: name\r\n" +
                                 "define Unrelated as: category with attributes: id and name\r\n")
        stmts.register(self.context)

    def testBooleanType(self):
        st = BooleanType.instance
        self.assertEquals(st, BooleanType.instance)
        self.assertTrue(st.isAssignableTo(self.context, BooleanType.instance))
        self.assertFalse(st.isAssignableTo(self.context, IntegerType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DecimalType.instance))
        self.assertFalse(st.isAssignableTo(self.context, TextType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateTimeType.instance))
        self.assertFalse(st.isAssignableTo(self.context, MissingType.instance))
        self.assertTrue(st.isAssignableTo(self.context, AnyType.instance))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Root")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Derived")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Unrelated")))

    def testIntegerType(self):
        st = IntegerType.instance
        self.assertEquals(st, IntegerType.instance)
        self.assertFalse(st.isAssignableTo(self.context, BooleanType.instance))
        self.assertTrue(st.isAssignableTo(self.context, IntegerType.instance))
        self.assertTrue(st.isAssignableTo(self.context, DecimalType.instance))
        self.assertFalse(st.isAssignableTo(self.context, TextType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateTimeType.instance))
        self.assertFalse(st.isAssignableTo(self.context, MissingType.instance))
        self.assertTrue(st.isAssignableTo(self.context, AnyType.instance))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Root")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Derived")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Unrelated")))

    def testDecimalType(self):
        st = DecimalType.instance
        self.assertEquals(st, DecimalType.instance)
        self.assertFalse(st.isAssignableTo(self.context, BooleanType.instance))
        self.assertTrue(st.isAssignableTo(self.context, IntegerType.instance))
        self.assertTrue(st.isAssignableTo(self.context, DecimalType.instance))
        self.assertFalse(st.isAssignableTo(self.context, TextType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateTimeType.instance))
        self.assertFalse(st.isAssignableTo(self.context, MissingType.instance))
        self.assertTrue(st.isAssignableTo(self.context, AnyType.instance))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Root")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Derived")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Unrelated")))

    def testStringType(self):
        st = TextType.instance
        self.assertEquals(st, TextType.instance)
        self.assertFalse(st.isAssignableTo(self.context, BooleanType.instance))
        self.assertFalse(st.isAssignableTo(self.context, IntegerType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DecimalType.instance))
        self.assertTrue(st.isAssignableTo(self.context, TextType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateTimeType.instance))
        self.assertFalse(st.isAssignableTo(self.context, MissingType.instance))
        self.assertTrue(st.isAssignableTo(self.context, AnyType.instance))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Root")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Derived")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Unrelated")))

    def testDateType(self):
        st = DateType.instance
        self.assertEquals(st, DateType.instance)
        self.assertFalse(st.isAssignableTo(self.context, BooleanType.instance))
        self.assertFalse(st.isAssignableTo(self.context, IntegerType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DecimalType.instance))
        self.assertFalse(st.isAssignableTo(self.context, TextType.instance))
        self.assertTrue(st.isAssignableTo(self.context, DateType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateTimeType.instance))
        self.assertFalse(st.isAssignableTo(self.context, MissingType.instance))
        self.assertTrue(st.isAssignableTo(self.context, AnyType.instance))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Root")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Derived")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Unrelated")))

    def testDateTimeType(self):
        st = DateTimeType.instance
        self.assertEquals(st, DateTimeType.instance)
        self.assertFalse(st.isAssignableTo(self.context, BooleanType.instance))
        self.assertFalse(st.isAssignableTo(self.context, IntegerType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DecimalType.instance))
        self.assertFalse(st.isAssignableTo(self.context, TextType.instance))
        self.assertTrue(st.isAssignableTo(self.context, DateType.instance))
        self.assertTrue(st.isAssignableTo(self.context, DateTimeType.instance))
        self.assertFalse(st.isAssignableTo(self.context, MissingType.instance))
        self.assertTrue(st.isAssignableTo(self.context, AnyType.instance))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Root")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Derived")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Unrelated")))

    def testMissingType(self):
        st = MissingType.instance
        self.assertEquals(st, MissingType.instance)
        self.assertTrue(st.isAssignableTo(self.context, BooleanType.instance))
        self.assertTrue(st.isAssignableTo(self.context, IntegerType.instance))
        self.assertTrue(st.isAssignableTo(self.context, DecimalType.instance))
        self.assertTrue(st.isAssignableTo(self.context, TextType.instance))
        self.assertTrue(st.isAssignableTo(self.context, DateType.instance))
        self.assertTrue(st.isAssignableTo(self.context, DateTimeType.instance))
        self.assertTrue(st.isAssignableTo(self.context, MissingType.instance))
        self.assertTrue(st.isAssignableTo(self.context, AnyType.instance))
        self.assertTrue(st.isAssignableTo(self.context, CategoryType("Root")))
        self.assertTrue(st.isAssignableTo(self.context, CategoryType("Derived")))
        self.assertTrue(st.isAssignableTo(self.context, CategoryType("Unrelated")))

    def testRootCategoryType(self):
        st = CategoryType("Root")
        self.assertEquals(st, CategoryType("Root"))
        self.assertFalse(st.isAssignableTo(self.context, BooleanType.instance))
        self.assertFalse(st.isAssignableTo(self.context, IntegerType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DecimalType.instance))
        self.assertFalse(st.isAssignableTo(self.context, TextType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateTimeType.instance))
        self.assertFalse(st.isAssignableTo(self.context, MissingType.instance))
        self.assertTrue(st.isAssignableTo(self.context, AnyType.instance))
        self.assertTrue(st.isAssignableTo(self.context, CategoryType("Root")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Derived")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Unrelated")))

    def testDerivedCategoryType(self):
        st = CategoryType("Derived")
        self.assertEquals(st, CategoryType("Derived"))
        self.assertFalse(st.isAssignableTo(self.context, BooleanType.instance))
        self.assertFalse(st.isAssignableTo(self.context, IntegerType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DecimalType.instance))
        self.assertFalse(st.isAssignableTo(self.context, TextType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateTimeType.instance))
        self.assertFalse(st.isAssignableTo(self.context, MissingType.instance))
        self.assertTrue(st.isAssignableTo(self.context, AnyType.instance))
        self.assertTrue(st.isAssignableTo(self.context, CategoryType("Root")))
        self.assertTrue(st.isAssignableTo(self.context, CategoryType("Derived")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Unrelated")))

    def testUnrelatedCategoryType(self):
        st = CategoryType("Unrelated")
        self.assertEquals(st, CategoryType("Unrelated"))
        self.assertFalse(st.isAssignableTo(self.context, BooleanType.instance))
        self.assertFalse(st.isAssignableTo(self.context, IntegerType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DecimalType.instance))
        self.assertFalse(st.isAssignableTo(self.context, TextType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateType.instance))
        self.assertFalse(st.isAssignableTo(self.context, DateTimeType.instance))
        self.assertFalse(st.isAssignableTo(self.context, MissingType.instance))
        self.assertTrue(st.isAssignableTo(self.context, AnyType.instance))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Root")))
        self.assertFalse(st.isAssignableTo(self.context, CategoryType("Derived")))
        self.assertTrue(st.isAssignableTo(self.context, CategoryType("Unrelated")))

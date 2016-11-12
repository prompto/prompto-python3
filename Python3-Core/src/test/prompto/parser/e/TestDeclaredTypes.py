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

def isAssignableTo(context, t1, t2):
    return t2.isAssignableFrom(context, t1)


class TestDeclaredTypes(BaseEParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        self.registerCategoryTypes()

    def registerCategoryTypes(self):
        stmts = self.parseString("define id as Integer attribute\r\n" +
                                 "define name as String attribute\r\n" +
                                 "define Root as category with attribute id\r\n" +
                                 "define Derived as Root with attribute name\r\n" +
                                 "define Unrelated as category with attributes id and name\r\n")
        stmts.register(self.context)

    def testBooleanType(self):
        st = BooleanType.instance
        self.assertEquals(st, BooleanType.instance)
        self.assertTrue(isAssignableTo(self.context, st, BooleanType.instance))
        self.assertFalse(isAssignableTo(self.context, st, IntegerType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DecimalType.instance))
        self.assertFalse(isAssignableTo(self.context, st, TextType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateTimeType.instance))
        self.assertTrue(isAssignableTo(self.context, st, MissingType.instance))
        self.assertTrue(isAssignableTo(self.context, st, AnyType.instance))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Root")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Derived")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Unrelated")))

    def testIntegerType(self):
        st = IntegerType.instance
        self.assertEquals(st, IntegerType.instance)
        self.assertFalse(isAssignableTo(self.context, st, BooleanType.instance))
        self.assertTrue(isAssignableTo(self.context, st, IntegerType.instance))
        self.assertTrue(isAssignableTo(self.context, st, DecimalType.instance))
        self.assertFalse(isAssignableTo(self.context, st, TextType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateTimeType.instance))
        self.assertTrue(isAssignableTo(self.context, st, MissingType.instance))
        self.assertTrue(isAssignableTo(self.context, st, AnyType.instance))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Root")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Derived")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Unrelated")))

    def testDecimalType(self):
        st = DecimalType.instance
        self.assertEquals(st, DecimalType.instance)
        self.assertFalse(isAssignableTo(self.context, st, BooleanType.instance))
        self.assertTrue(isAssignableTo(self.context, st, IntegerType.instance))
        self.assertTrue(isAssignableTo(self.context, st, DecimalType.instance))
        self.assertFalse(isAssignableTo(self.context, st, TextType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateTimeType.instance))
        self.assertTrue(isAssignableTo(self.context, st, MissingType.instance))
        self.assertTrue(isAssignableTo(self.context, st, AnyType.instance))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Root")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Derived")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Unrelated")))

    def testTestType(self):
        st = TextType.instance
        self.assertEquals(st, TextType.instance)
        self.assertFalse(isAssignableTo(self.context, st, BooleanType.instance))
        self.assertFalse(isAssignableTo(self.context, st, IntegerType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DecimalType.instance))
        self.assertTrue(isAssignableTo(self.context, st, TextType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateTimeType.instance))
        self.assertTrue(isAssignableTo(self.context, st, MissingType.instance))
        self.assertTrue(isAssignableTo(self.context, st, AnyType.instance))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Root")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Derived")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Unrelated")))

    def testDateType(self):
        st = DateType.instance
        self.assertEquals(st, DateType.instance)
        self.assertFalse(isAssignableTo(self.context, st, BooleanType.instance))
        self.assertFalse(isAssignableTo(self.context, st, IntegerType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DecimalType.instance))
        self.assertFalse(isAssignableTo(self.context, st, TextType.instance))
        self.assertTrue(isAssignableTo(self.context, st, DateType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateTimeType.instance))
        self.assertTrue(isAssignableTo(self.context, st, MissingType.instance))
        self.assertTrue(isAssignableTo(self.context, st, AnyType.instance))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Root")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Derived")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Unrelated")))

    def testDateTimeType(self):
        st = DateTimeType.instance
        self.assertEquals(st, DateTimeType.instance)
        self.assertFalse(isAssignableTo(self.context, st, BooleanType.instance))
        self.assertFalse(isAssignableTo(self.context, st, IntegerType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DecimalType.instance))
        self.assertFalse(isAssignableTo(self.context, st, TextType.instance))
        self.assertTrue(isAssignableTo(self.context, st, DateType.instance))
        self.assertTrue(isAssignableTo(self.context, st, DateTimeType.instance))
        self.assertTrue(isAssignableTo(self.context, st, MissingType.instance))
        self.assertTrue(isAssignableTo(self.context, st, AnyType.instance))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Root")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Derived")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Unrelated")))

    def testMissingType(self):
        st = MissingType.instance
        self.assertEquals(st, MissingType.instance)
        self.assertFalse(isAssignableTo(self.context, st, BooleanType.instance))
        self.assertFalse(isAssignableTo(self.context, st, IntegerType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DecimalType.instance))
        self.assertFalse(isAssignableTo(self.context, st, TextType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateTimeType.instance))
        self.assertTrue(isAssignableTo(self.context, st, MissingType.instance))
        self.assertTrue(isAssignableTo(self.context, st, AnyType.instance))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Root")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Derived")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Unrelated")))

    def testRootCategoryType(self):
        st = CategoryType("Root")
        self.assertEquals(st, CategoryType("Root"))
        self.assertFalse(isAssignableTo(self.context, st, BooleanType.instance))
        self.assertFalse(isAssignableTo(self.context, st, IntegerType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DecimalType.instance))
        self.assertFalse(isAssignableTo(self.context, st, TextType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateTimeType.instance))
        self.assertTrue(isAssignableTo(self.context, st, MissingType.instance))
        self.assertTrue(isAssignableTo(self.context, st, AnyType.instance))
        self.assertTrue(isAssignableTo(self.context, st, CategoryType("Root")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Derived")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Unrelated")))

    def testDerivedCategoryType(self):
        st = CategoryType("Derived")
        self.assertEquals(st, CategoryType("Derived"))
        self.assertFalse(isAssignableTo(self.context, st, BooleanType.instance))
        self.assertFalse(isAssignableTo(self.context, st, IntegerType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DecimalType.instance))
        self.assertFalse(isAssignableTo(self.context, st, TextType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateTimeType.instance))
        self.assertTrue(isAssignableTo(self.context, st, MissingType.instance))
        self.assertTrue(isAssignableTo(self.context, st, AnyType.instance))
        self.assertTrue(isAssignableTo(self.context, st, CategoryType("Root")))
        self.assertTrue(isAssignableTo(self.context, st, CategoryType("Derived")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Unrelated")))

    def testUnrelatedCategoryType(self):
        st = CategoryType("Unrelated")
        self.assertEquals(st, CategoryType("Unrelated"))
        self.assertFalse(isAssignableTo(self.context, st, BooleanType.instance))
        self.assertFalse(isAssignableTo(self.context, st, IntegerType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DecimalType.instance))
        self.assertFalse(isAssignableTo(self.context, st, TextType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateType.instance))
        self.assertFalse(isAssignableTo(self.context, st, DateTimeType.instance))
        self.assertTrue(isAssignableTo(self.context, st, MissingType.instance))
        self.assertTrue(isAssignableTo(self.context, st, AnyType.instance))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Root")))
        self.assertFalse(isAssignableTo(self.context, st, CategoryType("Derived")))
        self.assertTrue(isAssignableTo(self.context, st, CategoryType("Unrelated")))

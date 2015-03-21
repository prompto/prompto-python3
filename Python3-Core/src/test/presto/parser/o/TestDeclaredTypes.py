from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out
from presto.type.IntegerType import IntegerType
from presto.type.DecimalType import DecimalType
from presto.type.TextType import TextType
from presto.type.DateType import DateType
from presto.type.DateTimeType import DateTimeType
from presto.type.MissingType import MissingType
from presto.type.CategoryType import CategoryType
from presto.type.AnyType import AnyType
from presto.type.BooleanType import BooleanType


class TestDeclaredTypes(BaseOParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        self.registerCategoryTypes()

    def registerCategoryTypes(self):
        stmts = self.parseString("attribute id: Integer;" +
                                 "attribute name: String;" +
                                 "category Root(id);" +
                                 "category Derived(name) extends Root;" +
                                 "category Unrelated(id, name);")
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


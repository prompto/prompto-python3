from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.type.BooleanType import BooleanType
from presto.type.IntegerType import IntegerType
from presto.type.DecimalType import DecimalType
from presto.type.TextType import TextType
from presto.type.DateType import DateType
from presto.type.DateTimeType import DateTimeType
from presto.type.AnyType import AnyType
from presto.type.CategoryType import CategoryType
from presto.type.MissingType import MissingType
from presto.grammar.CategoryArgument import CategoryArgument
from presto.grammar.IdentifierList import IdentifierList


class TestAnonymousTypes(BaseEParserTest):

    def setUp(self):
        super(TestAnonymousTypes, self).setUp()
        stmts = self.parseString("define id as: Integer attribute\r\n" +
                             "define name as: String attribute\r\n" +
                             "define other as: String attribute\r\n" +
                             "define Simple as: category with attribute: name\r\n" +
                             "define Root as: category with attribute: id\r\n" +
                             "define DerivedWithOther as: Root with attribute: other\r\n" +
                             "define DerivedWithName as: Root with attribute: name\r\n")
        stmts.register(self.context)


    def testAnonymousAnyType(self):
        # any x
        argument = CategoryArgument(AnyType.instance, "x", None)
        argument.register(self.context)
        st = argument.getType(self.context)
        self.assertIsInstance(st, AnyType)
        self.assertTrue(BooleanType.instance.isAssignableTo(self.context, st))
        self.assertTrue(IntegerType.instance.isAssignableTo(self.context, st))
        self.assertTrue(DecimalType.instance.isAssignableTo(self.context, st))
        self.assertTrue(TextType.instance.isAssignableTo(self.context, st))
        self.assertTrue(DateType.instance.isAssignableTo(self.context, st))
        self.assertTrue(DateTimeType.instance.isAssignableTo(self.context, st))
        self.assertTrue(MissingType.instance.isAssignableTo(self.context, st))  # missing type always compatible
        self.assertTrue(AnyType.instance.isAssignableTo(self.context, st))
        self.assertTrue(CategoryType("Simple").isAssignableTo(self.context, st))
        self.assertTrue(CategoryType("Root").isAssignableTo(self.context, st))
        self.assertTrue(CategoryType("DerivedWithOther").isAssignableTo(self.context, st))
        self.assertTrue(CategoryType("DerivedWithName").isAssignableTo(self.context, st))


    def testAnonymousAnyTypeWithAttribute(self):
        # any x with attribute: name
        list = IdentifierList("name")
        argument = CategoryArgument(AnyType.instance, "x", list)
        argument.register(self.context)
        st = argument.getType(self.context)
        self.assertIsInstance(st, CategoryType)
        self.assertFalse(BooleanType.instance.isAssignableTo(self.context, st))
        self.assertFalse(IntegerType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DecimalType.instance.isAssignableTo(self.context, st))
        self.assertFalse(TextType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DateType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DateTimeType.instance.isAssignableTo(self.context, st))
        self.assertTrue(MissingType.instance.isAssignableTo(self.context, st))  # missing type always compatible
        self.assertFalse(AnyType.instance.isAssignableTo(self.context, st))  # any type never compatible
        self.assertTrue(CategoryType("Simple").isAssignableTo(self.context, st))  # since Simple has a name
        self.assertFalse(CategoryType("Root").isAssignableTo(self.context, st))  # since Root has no name
        self.assertFalse(
            CategoryType("DerivedWithOther").isAssignableTo(self.context, st))  # since DerivedWithOther has no name
        self.assertTrue(
            CategoryType("DerivedWithName").isAssignableTo(self.context, st))  # since DerivedWithName has a name


    def testAnonymousCategoryType(self):
        # Root x
        argument = CategoryArgument(CategoryType("Root"), "x", None)
        argument.register(self.context)
        st = argument.getType(self.context)
        self.assertIsInstance(st, CategoryType)
        self.assertFalse(BooleanType.instance.isAssignableTo(self.context, st))
        self.assertFalse(IntegerType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DecimalType.instance.isAssignableTo(self.context, st))
        self.assertFalse(TextType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DateType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DateTimeType.instance.isAssignableTo(self.context, st))
        self.assertTrue(MissingType.instance.isAssignableTo(self.context, st))  # missing type always compatible
        self.assertFalse(AnyType.instance.isAssignableTo(self.context, st))  # any type never compatible
        self.assertFalse(CategoryType("Simple").isAssignableTo(self.context, st))  # since Simple does not extend Root
        self.assertTrue(CategoryType("Root").isAssignableTo(self.context, st))  # since Root is Root
        self.assertTrue(
            CategoryType("DerivedWithOther").isAssignableTo(self.context, st))  # since DerivedWithOther extends Root
        self.assertTrue(
            CategoryType("DerivedWithName").isAssignableTo(self.context, st))  # since DerivedWithName extends Root


    def testAnonymousCategoryTypeWithAttribute(self):
        # Root x with attribute: name
        list = IdentifierList("name")
        argument = CategoryArgument(CategoryType("Root"), "test", list)
        argument.register(self.context)
        st = argument.getType(self.context)
        self.assertIsInstance(st, CategoryType)
        self.assertFalse(BooleanType.instance.isAssignableTo(self.context, st))
        self.assertFalse(IntegerType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DecimalType.instance.isAssignableTo(self.context, st))
        self.assertFalse(TextType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DateType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DateTimeType.instance.isAssignableTo(self.context, st))
        self.assertTrue(MissingType.instance.isAssignableTo(self.context, st))  # missing type always compatible
        self.assertFalse(AnyType.instance.isAssignableTo(self.context, st))  # any type never compatible
        self.assertFalse(CategoryType("Simple").isAssignableTo(self.context, st))  # since Simple does not extend Root
        self.assertFalse(CategoryType("Root").isAssignableTo(self.context, st))  # since Root has no name
        self.assertFalse(
            CategoryType("DerivedWithOther").isAssignableTo(self.context, st))  # since DerivedWithOther has no name
        self.assertTrue(
            CategoryType("DerivedWithName").isAssignableTo(self.context, st))  # since DerivedWithName has a name

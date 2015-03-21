from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestEnums(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceOPO("enums/categoryEnum.o")

    def testIntegerEnum(self):
        self.compareResourceOPO("enums/integerEnum.o")

    def testTextEnum(self):
        self.compareResourceOPO("enums/textEnum.o")



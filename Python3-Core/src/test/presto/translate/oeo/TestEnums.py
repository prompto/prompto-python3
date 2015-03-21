from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestEnums(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceOEO("enums/categoryEnum.o")

    def testIntegerEnum(self):
        self.compareResourceOEO("enums/integerEnum.o")

    def testTextEnum(self):
        self.compareResourceOEO("enums/textEnum.o")



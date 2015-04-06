from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestEnums(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceOEO("enums/categoryEnum.poc")

    def testIntegerEnum(self):
        self.compareResourceOEO("enums/integerEnum.poc")

    def testTextEnum(self):
        self.compareResourceOEO("enums/textEnum.poc")



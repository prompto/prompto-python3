from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestEnums(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceOSO("enums/categoryEnum.poc")

    def testIntegerEnum(self):
        self.compareResourceOSO("enums/integerEnum.poc")

    def testTextEnum(self):
        self.compareResourceOSO("enums/textEnum.poc")



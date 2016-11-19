from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestEnums(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceOMO("enums/categoryEnum.poc")

    def testIntegerEnum(self):
        self.compareResourceOMO("enums/integerEnum.poc")

    def testTextEnum(self):
        self.compareResourceOMO("enums/textEnum.poc")



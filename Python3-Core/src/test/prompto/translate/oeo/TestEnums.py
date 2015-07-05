# generated: 2015-07-05T23:01:01.785
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestEnums(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceOEO("enums/categoryEnum.poc")

    def testIntegerEnum(self):
        self.compareResourceOEO("enums/integerEnum.poc")

    def testTextEnum(self):
        self.compareResourceOEO("enums/textEnum.poc")



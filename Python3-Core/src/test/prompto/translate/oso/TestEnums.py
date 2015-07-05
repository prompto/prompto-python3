# generated: 2015-07-05T23:01:01.786
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestEnums(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceOSO("enums/categoryEnum.poc")

    def testIntegerEnum(self):
        self.compareResourceOSO("enums/integerEnum.poc")

    def testTextEnum(self):
        self.compareResourceOSO("enums/textEnum.poc")



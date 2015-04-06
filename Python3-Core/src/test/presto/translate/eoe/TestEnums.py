from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestEnums(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceEOE("enums/categoryEnum.pec")

    def testIntegerEnum(self):
        self.compareResourceEOE("enums/integerEnum.pec")

    def testTextEnum(self):
        self.compareResourceEOE("enums/textEnum.pec")



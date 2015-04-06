from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestEnums(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceESE("enums/categoryEnum.pec")

    def testIntegerEnum(self):
        self.compareResourceESE("enums/integerEnum.pec")

    def testTextEnum(self):
        self.compareResourceESE("enums/textEnum.pec")



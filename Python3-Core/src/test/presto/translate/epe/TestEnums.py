from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestEnums(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceEPE("enums/categoryEnum.e")

    def testIntegerEnum(self):
        self.compareResourceEPE("enums/integerEnum.e")

    def testTextEnum(self):
        self.compareResourceEPE("enums/textEnum.e")



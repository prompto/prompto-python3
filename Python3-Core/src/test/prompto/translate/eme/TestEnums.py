from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestEnums(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceEME("enums/categoryEnum.pec")

    def testIntegerEnum(self):
        self.compareResourceEME("enums/integerEnum.pec")

    def testTextEnum(self):
        self.compareResourceEME("enums/textEnum.pec")



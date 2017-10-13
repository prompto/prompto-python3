from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestEnums(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceEOE("enums/categoryEnum.pec")

    def testIntegerEnum(self):
        self.compareResourceEOE("enums/integerEnum.pec")

    def testTextEnum(self):
        self.compareResourceEOE("enums/textEnum.pec")

    def testTextEnumArg(self):
        self.compareResourceEOE("enums/textEnumArg.pec")

    def testTextEnumVar(self):
        self.compareResourceEOE("enums/textEnumVar.pec")



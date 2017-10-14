from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestEnums(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceEME("enums/categoryEnum.pec")

    def testIntegerEnum(self):
        self.compareResourceEME("enums/integerEnum.pec")

    def testStoreCategoryEnum(self):
        self.compareResourceEME("enums/storeCategoryEnum.pec")

    def testStoreIntegerEnum(self):
        self.compareResourceEME("enums/storeIntegerEnum.pec")

    def testStoreTextEnum(self):
        self.compareResourceEME("enums/storeTextEnum.pec")

    def testTextEnum(self):
        self.compareResourceEME("enums/textEnum.pec")

    def testTextEnumArg(self):
        self.compareResourceEME("enums/textEnumArg.pec")

    def testTextEnumVar(self):
        self.compareResourceEME("enums/textEnumVar.pec")



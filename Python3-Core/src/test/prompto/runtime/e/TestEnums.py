from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestEnums(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCategoryEnum(self):
        self.checkOutput("enums/categoryEnum.pec")

    def testIntegerEnum(self):
        self.checkOutput("enums/integerEnum.pec")

    def testTextEnum(self):
        self.checkOutput("enums/textEnum.pec")



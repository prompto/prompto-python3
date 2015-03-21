from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestEnums(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCategoryEnum(self):
        self.checkOutput("enums/categoryEnum.e")

    def testIntegerEnum(self):
        self.checkOutput("enums/integerEnum.e")

    def testTextEnum(self):
        self.checkOutput("enums/textEnum.e")



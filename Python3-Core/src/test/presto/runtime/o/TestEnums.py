from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestEnums(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCategoryEnum(self):
        self.checkOutput("enums/categoryEnum.o")

    def testIntegerEnum(self):
        self.checkOutput("enums/integerEnum.o")

    def testTextEnum(self):
        self.checkOutput("enums/textEnum.o")



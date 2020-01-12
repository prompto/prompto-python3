from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestEnums(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCategoryEnum(self):
        self.checkOutput("enums/categoryEnum.poc")

    def testIntegerEnum(self):
        self.checkOutput("enums/integerEnum.poc")

    def testSwitchEnum(self):
        self.checkOutput("enums/switchEnum.poc")

    def testTextEnum(self):
        self.checkOutput("enums/textEnum.poc")

    def testTextEnumArg(self):
        self.checkOutput("enums/textEnumArg.poc")

    def testTextEnumVar(self):
        self.checkOutput("enums/textEnumVar.poc")



from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestArrow(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testFilterFromList(self):
        self.checkOutput("arrow/filterFromList.poc")

    def testFilterFromSet(self):
        self.checkOutput("arrow/filterFromSet.poc")

    def testSortCategory1Arg(self):
        self.checkOutput("arrow/sortCategory1Arg.poc")

    def testSortCategory2Args(self):
        self.checkOutput("arrow/sortCategory2Args.poc")

    def testSortText1Arg(self):
        self.checkOutput("arrow/sortText1Arg.poc")

    def testSortText1ArgDesc(self):
        self.checkOutput("arrow/sortText1ArgDesc.poc")

    def testSortText2Args(self):
        self.checkOutput("arrow/sortText2Args.poc")

    def testSortText2ArgsDesc(self):
        self.checkOutput("arrow/sortText2ArgsDesc.poc")



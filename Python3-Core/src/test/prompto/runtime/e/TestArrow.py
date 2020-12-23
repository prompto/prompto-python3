from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestArrow(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testHasAllFromList(self):
        self.checkOutput("arrow/hasAllFromList.pec")

    def testHasAllFromSet(self):
        self.checkOutput("arrow/hasAllFromSet.pec")

    def testHasAnyFromList(self):
        self.checkOutput("arrow/hasAnyFromList.pec")

    def testHasAnyFromSet(self):
        self.checkOutput("arrow/hasAnyFromSet.pec")



from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestExit(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAssignedReturn(self):
        self.checkOutput("exit/assignedReturn.pec")

    def testAssignedReturnInDoWhile(self):
        self.checkOutput("exit/assignedReturnInDoWhile.pec")

    def testAssignedReturnInForEach(self):
        self.checkOutput("exit/assignedReturnInForEach.pec")

    def testAssignedReturnInIf(self):
        self.checkOutput("exit/assignedReturnInIf.pec")

    def testAssignedReturnInWhile(self):
        self.checkOutput("exit/assignedReturnInWhile.pec")

    def testUnassignedReturn(self):
        self.checkOutput("exit/unassignedReturn.pec")

    def testUnassignedReturnInDoWhile(self):
        self.checkOutput("exit/unassignedReturnInDoWhile.pec")

    def testUnassignedReturnInForEach(self):
        self.checkOutput("exit/unassignedReturnInForEach.pec")

    def testUnassignedReturnInIf(self):
        self.checkOutput("exit/unassignedReturnInIf.pec")

    def testUnassignedReturnInWhile(self):
        self.checkOutput("exit/unassignedReturnInWhile.pec")



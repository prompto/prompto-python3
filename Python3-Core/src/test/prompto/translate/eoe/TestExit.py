from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestExit(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAssignedReturn(self):
        self.compareResourceEOE("exit/assignedReturn.pec")

    def testAssignedReturnInDoWhile(self):
        self.compareResourceEOE("exit/assignedReturnInDoWhile.pec")

    def testAssignedReturnInForEach(self):
        self.compareResourceEOE("exit/assignedReturnInForEach.pec")

    def testAssignedReturnInIf(self):
        self.compareResourceEOE("exit/assignedReturnInIf.pec")

    def testAssignedReturnInWhile(self):
        self.compareResourceEOE("exit/assignedReturnInWhile.pec")

    def testUnassignedReturn(self):
        self.compareResourceEOE("exit/unassignedReturn.pec")

    def testUnassignedReturnInDoWhile(self):
        self.compareResourceEOE("exit/unassignedReturnInDoWhile.pec")

    def testUnassignedReturnInForEach(self):
        self.compareResourceEOE("exit/unassignedReturnInForEach.pec")

    def testUnassignedReturnInIf(self):
        self.compareResourceEOE("exit/unassignedReturnInIf.pec")

    def testUnassignedReturnInWhile(self):
        self.compareResourceEOE("exit/unassignedReturnInWhile.pec")



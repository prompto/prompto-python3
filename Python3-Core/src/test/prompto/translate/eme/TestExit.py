from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestExit(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAssignedReturn(self):
        self.compareResourceEME("exit/assignedReturn.pec")

    def testAssignedReturnInDoWhile(self):
        self.compareResourceEME("exit/assignedReturnInDoWhile.pec")

    def testAssignedReturnInForEach(self):
        self.compareResourceEME("exit/assignedReturnInForEach.pec")

    def testAssignedReturnInIf(self):
        self.compareResourceEME("exit/assignedReturnInIf.pec")

    def testAssignedReturnInWhile(self):
        self.compareResourceEME("exit/assignedReturnInWhile.pec")

    def testUnassignedReturn(self):
        self.compareResourceEME("exit/unassignedReturn.pec")

    def testUnassignedReturnInDoWhile(self):
        self.compareResourceEME("exit/unassignedReturnInDoWhile.pec")

    def testUnassignedReturnInForEach(self):
        self.compareResourceEME("exit/unassignedReturnInForEach.pec")

    def testUnassignedReturnInIf(self):
        self.compareResourceEME("exit/unassignedReturnInIf.pec")

    def testUnassignedReturnInWhile(self):
        self.compareResourceEME("exit/unassignedReturnInWhile.pec")



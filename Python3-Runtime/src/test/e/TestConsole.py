# generated: 2015-10-05T22:40:45.473
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestConsole(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        self.coreContext = None
        self.loadDependency("console")
        self.loadDependency("core")
    
    def tearDown(self):
        Out.restore()

    def testPrint(self):
        self.runTests("console/print.pec")



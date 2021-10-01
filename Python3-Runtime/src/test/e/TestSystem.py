from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestSystem(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        self.coreContext = None
        self.loadDependency("system")
    
    def tearDown(self):
        Out.restore()

    def testSystem(self):
        self.runTests("system/system.pec")



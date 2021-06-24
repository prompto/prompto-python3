from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestPath(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        self.coreContext = None
        self.loadDependency("path")
        self.loadDependency("core")
    
    def tearDown(self):
        Out.restore()

    def testPath(self):
        self.runTests("path/path.pec")



from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestInternet(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        self.coreContext = None
        self.loadDependency("internet")
        self.loadDependency("console")
        self.loadDependency("core")
    
    def tearDown(self):
        Out.restore()

    def testUrl(self):
        self.runTests("internet/url.pec")



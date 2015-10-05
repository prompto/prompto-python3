# generated: 2015-10-05T22:40:45.477
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestCore(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        self.coreContext = None
        self.loadDependency("core")
    
    def tearDown(self):
        Out.restore()

    def testAny(self):
        self.runTests("core/any.pec")

    def testAttribute(self):
        self.runTests("core/attribute.pec")

    def testError(self):
        self.runTests("core/error.pec")



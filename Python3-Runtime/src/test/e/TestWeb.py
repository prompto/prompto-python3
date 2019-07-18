from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestWeb(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        self.coreContext = None
        self.loadDependency("web")
        self.loadDependency("core")
    
    def tearDown(self):
        Out.restore()

    def testEvents(self):
        self.runTests("web/events.pec")

    def testReact(self):
        self.runTests("web/react.pec")

    def testUtils(self):
        self.runTests("web/utils.pec")



from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out
from prompto.runtime.ApplicationContext import ApplicationContext

class TestScheduler(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        self.loadDependency("core")
        self.savedContext = ApplicationContext.set(self.coreContext)
    
    def tearDown(self):
        Out.restore()
        ApplicationContext.set(self.savedContext)
        self.savedContext = None

    def testScheduler(self):
        self.runTests("manual/scheduler.pec", True)


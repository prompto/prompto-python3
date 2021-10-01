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

    def testAbstract(self):
        self.runTests("core/abstract.pec")

    def testAny(self):
        self.runTests("core/any.pec")

    def testAttribute(self):
        self.runTests("core/attribute.pec")

    def testAttributes(self):
        self.runTests("core/attributes.pec")

    def testAudit(self):
        self.runTests("core/audit.pec")

    def testCategory(self):
        self.runTests("core/category.pec")

    def testCloud(self):
        self.runTests("core/cloud.pec")

    def testConfig(self):
        self.runTests("core/config.pec")

    def testError(self):
        self.runTests("core/error.pec")

    def testMath(self):
        self.runTests("core/math.pec")

    def testParse(self):
        self.runTests("core/parse.pec")

    def testTime(self):
        self.runTests("core/time.pec")

    def testUtils(self):
        self.runTests("core/utils.pec")



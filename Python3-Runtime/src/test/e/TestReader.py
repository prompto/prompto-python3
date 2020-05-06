from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestReader(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        self.coreContext = None
        self.loadDependency("reader")
        self.loadDependency("core")
    
    def tearDown(self):
        Out.restore()

    def testCsv(self):
        self.runTests("reader/csv.pec")

    def testJson(self):
        self.runTests("reader/json.pec")

    def testYaml(self):
        self.runTests("reader/yaml.pec")



from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestMethods(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAnonymous(self):
        self.checkOutput("methods/anonymous.poc")

    def testAttribute(self):
        self.checkOutput("methods/attribute.poc")

    def testDefault(self):
        self.checkOutput("methods/default.poc")

    def testE_as_e_bug(self):
        self.checkOutput("methods/e_as_e_bug.poc")

    def testExplicit(self):
        self.checkOutput("methods/explicit.poc")

    def testExpressionWith(self):
        self.checkOutput("methods/expressionWith.poc")

    def testExtended(self):
        self.checkOutput("methods/extended.poc")

    def testImplicit(self):
        self.checkOutput("methods/implicit.poc")

    def testMember(self):
        self.checkOutput("methods/member.poc")

    def testPolymorphic_abstract(self):
        self.checkOutput("methods/polymorphic_abstract.poc")

    def testPolymorphic_implicit(self):
        self.checkOutput("methods/polymorphic_implicit.poc")

    def testPolymorphic_named(self):
        self.checkOutput("methods/polymorphic_named.poc")

    def testPolymorphic_runtime(self):
        self.checkOutput("methods/polymorphic_runtime.poc")

    def testSpecified(self):
        self.checkOutput("methods/specified.poc")


